from ctypes import *
import numpy as np
import time, sys
import edk
from pyemotivException import PyemotivException
import os

# Don't forget to "python setup.py build install" after modifying this file

class Epoc(object):
    def initializeInternalVariables(self):
        self.eEvent = edk.EE_EmoEngineEventCreate()
        self.eState = edk.EE_EmoStateCreate()
        
        self.userId = 0
        self.channels = [ 'ED_COUNTER','ED_INTERPOLATED','ED_RAW_CQ', #0-2
                          'ED_AF3','ED_F7','ED_F3','ED_FC5','ED_T7',  #3-7
                          'ED_P7','ED_O1','ED_O2','ED_P8','ED_T8',    #8-12
                          'ED_FC6','ED_F4','ED_F8','ED_AF4',          #13-17
                          'ED_GYROX', 'ED_GYROY','ED_TIMESTAMP','ED_ES_TIMESTAMP', #18-20
                          'ED_FUNC_ID','ED_FUNC_VALUE','ED_MARKER',   #21-23
                          'ED_SYNC_SIGNAL']                           #24
        self.raw_channels_idx = range(3,17)
        self.gyro_idx = [self.channels.index("ED_GYROX"),self.channels.index("ED_GYROY")]
        self.names = [name[3:] for name in self.channels]
        #self.name_dict = {name:i for name,i in zip(self.names, xrange(len(self.names)))} # dict comprehension is new in Python 2.7, and this line is useless anyway
        self.m = len(self.channels)
        self.sr = 1/127.94
        self.times = [0.]
        
        self.composerPort = 1726
        
        (self.rawData, self.processedData, self.contactQuality) = (None, None, None)
        (self.rawFile, self.processedFile, self.qualityFile) = (None, None, None)

    """
    Class that connects to Emotiv Epoc by wrapping the 
    research SDK dynamic link libraries
    """
    def __init__(self, connectionType = "local", connectionTimeout = 2):
        self.initializeInternalVariables()
        
        self.connected = False
        self.connectionTimeout = connectionTimeout
        self.debug = True
        
        # either "local" or "remote"
        self.connectionType = connectionType
        
    def setConnectionType(self, connectionType):
        self.connectionType = connectionType
        
    def getSoftwareVersion(self):
        a = None
        b = 1
        c = 1
        i = edk.EE_SoftwareGetVersion(a, b, c)
        return c
    
    def connect(self):   
        """
        Establishes connection to Emotiv Epoc
        """
        if self.connectionType == "local":
            if edk.EE_EngineConnect("Emotiv Systems-5") != 0:
                raise PyemotivException("Emotiv Engine start up failed.")
            self.data_handler = edk.EE_DataCreate()
            edk.EE_DataSetBufferSizeInSec(5)
        elif self.connectionType == "remote":
            if edk.EE_EngineRemoteConnect("127.0.0.1", self.composerPort, "Emotiv Systems-5") != 0:
                raise PyemotivException("Cannot connect to EmoComposer")
        else:
            raise PyemotivException("Unknow connection type - please specify either 'local' or 'remote'.")

        t0 = time.time()
        while not self.connected:
            state = edk.EE_EngineGetNextEvent(self.eEvent)
            if state == edk.EDK_OK:
                self.connected = True
                if self.connectionType == "local":
                    edk.EE_DataAcquisitionEnable(self.userId, True)
                break
            if time.time() - t0 > self.connectionTimeout:
                raise PyemotivException('Timeout while connecting to Epoc!')

    def getData(self, getRawData = False, getProcessedData = False, getContactQuality = False, waitForResults = True, timeout = None, rawDataChannels = None, processedDataChannels = None):
        """
        Get data from the device buffer
        """
        if not self.connected:
            self.connect()
        
        if getRawData and self.connectionType == "remote":
            raise PyemotivException("No raw data available when using EmoComposer - please query only the processed data")
        
        if getRawData and rawDataChannels is None:
            rawDataChannels = xrange(self.m)

        (rawContainer, processedContainer, contactQuality) = \
            self.aquire(getRawData, getProcessedData, getContactQuality, waitForResults, timeout, rawDataChannels)
            
        return (rawContainer, processedContainer, contactQuality) 

    def aquire(self, getRawData = False, getProcessedData = False, getContactQuality = False, waitForResults = True, timeout = None, rawDataChannels = None, processedDataChannels = None):
        rawData = False
        processedData = False
        contactQuality = False
        
        if timeout is not None:
            t0 = time.time()

        while (isinstance(rawData, bool) and getRawData) or (isinstance(processedData, bool) and getProcessedData):
            if getRawData:
                raw = self._acquireRawDataIndividually(rawDataChannels)
                if not isinstance(raw, bool):
                    if rawData is False:
                        rawData = raw
                    else:
                        rawData = np.vstack((rawData, raw))
            
            event = edk.EE_EngineGetNextEvent(self.eEvent)
            if event != edk.EDK_OK and event != edk.EDK_NO_EVENT:
                raise PyemotivException('Internal error of Emotiv while acquiring states')
            
            if event == edk.EDK_OK:
                edk.EE_EmoEngineEventGetUserId(self.eEvent, self.userId)
                eventType = edk.EE_EmoEngineEventGetType(self.eEvent)
                
                if eventType == edk.EE_EmoStateUpdated:
                    if getProcessedData:
                        if processedData is False:
                            processedData = self._acquireProcessedData(True)
                        else:
                            processedData = np.vstack((processedData, self._acquireProcessedData(True)))
                    
                    if getContactQuality:
                        if contactQuality is False:
                            contactQuality = self._acquireContactQuality()
                        else:
                            contactQuality = np.vstack((contactQuality, self._acquireContactQuality()))
            
            if not waitForResults:
                break
            
            if timeout is not None and time.time() - t0 > timeout:
                errorMessage = 'Timeout while reading data.'
                if not isinstance(rawData, bool) or not isinstance(processedData, bool):
                    errorMessage = errorMessage + 'Some data frames were dropped because of this exception.'
                raise PyemotivException(errorMessage)

        return (rawData, processedData, contactQuality)
            

    def _acquireRawDataBatch(self, idx):
        """
        Acquire raw data points in one batch. Requires SDK v2+
        """

        nSamples = c_int()
        edk.EE_DataUpdateHandle(0, self.data_handler)
        edk.EE_DataGetNumberOfSample(self.data_handler, byref(nSamples))
        n = nSamples.value
        if not n or n == 0:
            return False

        data = np.empty((len(idx) , n))
        data_ctype = np.ctypeslib.as_ctypes(data)
        edk.EE_DataGetMultiChannels(self.data_handler, idx, len(idx), data_ctype, n)
        data_read = np.ctypeslib.as_array(data_ctype)
        data = data_read

        self.times = np.linspace(self.times[-1]+self.sr, 
                                 self.times[-1]+ n*self.sr, n)
                            
        return data

    def _acquireRawDataIndividually(self, idx):
        """
        Acquire raw data points channel by channel and then combine them.
        It's slower but backwards-compatible
        """
        nSamples = c_int()
        edk.EE_DataUpdateHandle(0, self.data_handler)
        edk.EE_DataGetNumberOfSample(self.data_handler, byref(nSamples))
        n = nSamples.value
        if not n:
            return False

        container = np.empty((len(idx) , n))
        k=0
        for i in idx:
            data = np.empty((1,n))
            data_ctype = np.ctypeslib.as_ctypes(data)
            edk.EE_DataGet(self.data_handler, i, byref(data_ctype), n)
            data_read = np.ctypeslib.as_array(data_ctype)
            container[k,:] = data_read[0]
            k+=1
        self.times = np.linspace(self.times[-1]+self.sr, 
                                 self.times[-1]+ n*self.sr, n)

        return container.transpose()

    
    def _acquireProcessedData(self, includeUnscaledValues = False):
        """
        Gets the processed data values.
        
        If includeUnscaledValues is True then the unscaled values are also reported, making the resulting array larget.
        Only available in SDK v2+
        """
        edk.EE_EmoEngineEventGetEmoState(self.eEvent, self.eState)

        return self.getEmoStates(includeUnscaledValues)
    
    def _acquireContactQuality(self):
        edk.EE_EmoEngineEventGetUserId(self.eEvent, self.userId)
        edk.EE_EmoEngineEventGetEmoState(self.eEvent, self.eState)

        numChannels = edk.ES_GetNumContactQualityChannels(self.eEvent)
        contactQualityArr = (c_long*numChannels)()
        edk.ES_GetContactQualityFromAllChannels(self.eState, contactQualityArr, numChannels)

        contactQuality = []
        contactQuality.append(edk.ES_GetTimeFromStart(self.eState))
        contactQuality.append(self.userId)
        contactQuality.append(edk.ES_GetWirelessSignalStatus(self.eState))
        
        batteryChargeLevel = c_int()
        batteryMaxChargeLevel = c_int()
        edk.ES_GetBatteryChargeLevel(self.eState, byref(batteryChargeLevel), byref(batteryMaxChargeLevel))
        contactQuality.append(batteryChargeLevel.value)
        contactQuality.append(batteryMaxChargeLevel.value)
        
        for i in range(numChannels):
            contactQuality.append(contactQualityArr[i])

        return contactQuality

    def getEmoStates(self, includeUnscaledValues = False):
        expressivStates={}
        expressivStates[ edk.EXP_EYEBROW     ] = 0
        expressivStates[ edk.EXP_FURROW      ] = 0
        expressivStates[ edk.EXP_SMILE       ] = 0
        expressivStates[ edk.EXP_CLENCH      ] = 0
        expressivStates[ edk.EXP_SMIRK_LEFT  ] = 0
        expressivStates[ edk.EXP_SMIRK_RIGHT ] = 0
        expressivStates[ edk.EXP_LAUGH       ] = 0
        upperFaceAction = edk.ES_ExpressivGetUpperFaceAction(self.eState)
        upperFacePower  = edk.ES_ExpressivGetUpperFaceActionPower(self.eState)
        lowerFaceAction = edk.ES_ExpressivGetLowerFaceAction(self.eState)
        lowerFacePower  = edk.ES_ExpressivGetLowerFaceActionPower(self.eState)
        expressivStates[ upperFaceAction ] = upperFacePower;
        expressivStates[ lowerFaceAction ] = lowerFacePower;
        
        if includeUnscaledValues:
            container = np.zeros(33)
        else:
            container = np.zeros(21)
        
        # General data
        container[0] = edk.ES_GetTimeFromStart(self.eState)
        container[1] = self.userId
        
        #Expressive Suite
        container[2] = edk.ES_ExpressivIsBlink(self.eState)
        container[3] = edk.ES_ExpressivIsLeftWink(self.eState)
        container[4] = edk.ES_ExpressivIsRightWink(self.eState)
        container[5] = edk.ES_ExpressivIsLookingLeft(self.eState)
        container[6] = edk.ES_ExpressivIsLookingRight(self.eState)
        container[7] = expressivStates[ edk.EXP_EYEBROW ]
        container[8] = expressivStates[ edk.EXP_FURROW ]
        container[9] = expressivStates[ edk.EXP_SMILE ]
        container[10] = expressivStates[ edk.EXP_CLENCH ]
        container[11] = expressivStates[ edk.EXP_SMIRK_LEFT ]
        container[12] = expressivStates[ edk.EXP_SMIRK_RIGHT ]
        container[13] = expressivStates[ edk.EXP_LAUGH ]
        
        # Affectiv Suite
        container[14] = edk.ES_AffectivGetExcitementShortTermScore(self.eState)
        container[15] = edk.ES_AffectivGetExcitementLongTermScore(self.eState)
        container[16] = edk.ES_AffectivGetMeditationScore(self.eState)
        container[17] = edk.ES_AffectivGetFrustrationScore(self.eState)
        container[18] = edk.ES_AffectivGetEngagementBoredomScore(self.eState)

        #Cognitive Suite
        container[19] = edk.ES_CognitivGetCurrentAction(self.eState)
        container[20] = edk.ES_CognitivGetCurrentActionPower(self.eState)

        # Affective unscaled model parameters
        if includeUnscaledValues:
            functionNames = ['ES_AffectivGetExcitementShortTermModelParams',
                             'ES_AffectivGetMeditationModelParams', 
                             'ES_AffectivGetFrustrationModelParams', 
                             'ES_AffectivGetEngagementBoredomModelParams']
            containerIndex = 21

            for functionName in functionNames:
                rawScore = c_int()
                minScale = c_int()
                maxScale = c_int()
                scaledScore = c_int()
                function = getattr(edk, functionName)
                function(self.eState, byref(rawScore), byref(minScale), byref(maxScale))
                container[containerIndex] = rawScore.value
                containerIndex += 1
                container[containerIndex] = minScale.value
                containerIndex += 1
                container[containerIndex] = maxScale.value
                containerIndex += 1

        return container
    
    def addMarker(self, marker):
        edk.EE_DataSetMarker(self.userId, marker)

    def getProcessedDataFileHeader(self, includeUnscaledValues = False):
        header = ['Time From Start','User ID',
                  'Blink','Wink Left','Wink Right','Look Left','Look Right','Eyebrow','Furrow','Smile','Clench','Smirk Left','Smirk Right','Laugh',
                  'Short Term Excitement','Long Term Excitement','Meditation','Frustration','Engagement/Boredom',
                  'Cognitiv Action','Cognitiv Power']
        
        if includeUnscaledValues:
            for name in ['Short Term Excitement','Meditation','Frustration','Engagement/Boredom',]: #there is no long term exc for some reason
                for score in ['raw', 'min', 'max']:
                    header.append(name + " " + score)
        
        return ','.join(header)

    def getRawDataFileHeader(self):
        return ','.join(self.channels)

    def getContactQualityFileHeader(self):
        header = ['Time From Start','User ID','Wireless Signal Status', 'Battery Charge Level', 'Battery Max Charge Level']
        
        for channel in self.channels:
            header.append(channel)
        
        return ','.join(header)
    
    def close(self):
        edk.EE_EngineDisconnect()
        edk.EE_EmoStateFree(self.eState)
        edk.EE_EmoEngineEventFree(self.eEvent)
        self.rawFile.close()
        self.processedFile.close()
        self.qualityFile.close()
        
    def collectData(self):
        (raw, processed, contact) = \
            self.getData(getRawData = True, getProcessedData = True, getContactQuality = True, waitForResults = True)    
        
        if self.rawData is None and self.processedData is None and self.contactQuality is None:
            (self.rawData, self.processedData, self.contactQuality) = (raw, processed, contact)
        else:
            self.rawData = np.vstack((self.rawData, raw))
            self.processedData = np.vstack((self.processedData, processed))
            self.contactQuality = np.vstack((self.contactQuality, contact))
            
        if self.isMarkerReceived(raw, 254):
            return False
        
        return True
            
    def isMarkerReceived(self, rawData, marker):
        for markerItem in rawData[:, 23]:
            if markerItem != 0:
                print markerItem
            if markerItem == marker:
                return True
        
    def save(self, directory = None):
        if directory is not None:
            originalDir = os.getcwd()
            
            resultsDir = os.path.join(directory, "results")
            if not os.path.exists(resultsDir):
                os.mkdir(resultsDir)
            
            os.chdir(resultsDir)

            idFile = open("last_id.txt", "r+")
            currentId = int(idFile.readline()) + 1
        
            # Maybe the last_id.txt is out of date, so we update it if needed
            while os.path.exists("results_" + str(currentId)):
                currentId = currentId + 1
            
            currentId = str(currentId)
        
            # Overwrite the id in the file
            idFile.seek(0,0)
            idFile.write(currentId)
            idFile.close()
    
            os.mkdir("results_" + currentId)
            os.chdir("results_" + currentId)
            resultsDir = os.getcwd()
            
        if self.rawFile is None or self.processedFile is None or self.qualityFile is None:
            self.rawFile = file('raw.txt', 'a')
            self.processedFile = file('processed.txt', 'a')
            self.qualityFile = file('quality.txt', 'a') 
            np.savetxt(self.rawFile, self.rawData, delimiter=',', header=self.getRawDataFileHeader())
            np.savetxt(self.processedFile, self.processedData, delimiter=',', header=self.getProcessedDataFileHeader(True))
            np.savetxt(self.qualityFile, self.contactQuality, delimiter=',', header=self.getContactQualityFileHeader())
        else:
            # no headers if the files are already open and we are just appending
            np.savetxt(self.rawFile, self.rawData, delimiter=',')
            np.savetxt(self.processedFile, self.processedData, delimiter=',')
            np.savetxt(self.qualityFile, self.contactQuality, delimiter=',')
            
        (self.rawData, self.processedData, self.contactQuality) = (None, None, None)
            
        self.rawFile.flush()
        self.processedFile.flush()
        self.qualityFile.flush()

if __name__ == "__main__":
    e = Epoc("local")
    i = 0
    
    directory = "J:/home/eperfa/Synetiq/Mindr/"
    
    inspect = False
    save = True

    while inspect:
        time.sleep(0.01)
        save = False
        (raw, processed, contact) = \
            e.getData(getRawData = True, getProcessedData = False, getContactQuality = False, waitForResults = True)
            
        if e.isMarkerReceived(raw, 1):
            inspect = False
            save = True
            print "Start marker detected"

    startTime = time.time()

    print "Saving EEG data"
    while save:
        i += 1
        time.sleep(0.01)
        ok = e.collectData()
        if i % 100 == 0:
            e.save()
        if not ok:
            save = False
            inspect = False
            print "Stop marker detected, stopping EEG data saving"
        if time.time() - startTime > 360:
            print "Timeout"
            save = False

    e.close()
    e.save(directory)

    #print data