from ctypes import *
import numpy as np
import pandas as pd
import time, sys
import edk
import os

# Don't forget to "python setup.py build install" after modifying this file

class PyemotivException(Exception):
    pass

class Epoc(object):
    def initializeInternalVariables(self):
        self.eEvent = edk.EE_EmoEngineEventCreate()
        self.eState = edk.EE_EmoStateCreate()
        
        self.userId = 0
        
        # The channels, as returned when querying the raw data
        self.channels = [ 'ED_COUNTER','ED_INTERPOLATED','ED_RAW_CQ', #0-2
                          'ED_AF3','ED_F7','ED_F3','ED_FC5','ED_T7',  #3-7
                          'ED_P7','ED_O1','ED_O2','ED_P8','ED_T8',    #8-12
                          'ED_FC6','ED_F4','ED_F8','ED_AF4',          #13-17
                          'ED_GYROX', 'ED_GYROY','ED_TIMESTAMP','ED_ES_TIMESTAMP', #18-20
                          'ED_FUNC_ID','ED_FUNC_VALUE','ED_MARKER',   #21-23
                          'ED_SYNC_SIGNAL']                           #24
        
        # The logical channels, as returned when querying the conact quality. This involves the reference channels plus two duplicates
        # Signal quality and input data for some sensors will be identical: CMS = DRL, FP1 = AF3, F2 = AF4
        self.logicalChannels = ['CMS', 'DRL', 'FP1', 'AF3', 'F7', 
                                'F3', 'FC5', 'T7', 'P7', 'O1',
                                'O2', 'P8', 'T8', 'FC6', 'F4',
                                'F8', 'AF4', 'FP2']
        self.raw_channels_idx = range(3,17)
        self.rawChannels = self.channels[3:17]
        self.gyro_idx = [self.channels.index("ED_GYROX"), self.channels.index("ED_GYROY")]
        self.m = len(self.channels)
        self.sr = 1/127.94
        
        self.composerPort = 1726

        (self.lastRaw, self.lastProcessed, self.lastContact) = (None, None, None)

    """
    Class that connects to Emotiv Epoc by wrapping the 
    research SDK dynamic link libraries
    """
    def __init__(self, connectionType = "local", connectionTimeout = 2):
        self.initializeInternalVariables()
        self.reset()
        
        self.connected = False
        self.connectionTimeout = connectionTimeout
        self.debug = True
        
        # either "local" or "remote"
        self.connectionType = connectionType
        
        # sets whether the previous data should be dropped on the next read. 
        # this is used after writing the data arrays to a file to save memory but always have at least one valid data
        self.clearDataArraysOnNextRead = False
        
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
            currentTime = time.time()
            if getRawData:
                raw = self._acquireRawDataSensorBySensor(rawDataChannels, currentTime = currentTime)
                if not isinstance(raw, bool):
                    self.lastUpdateTime = raw[-1,0]
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
                            processedData = self._acquireProcessedData(True, currentTime = currentTime)
                        else:
                            processedData = np.vstack((processedData, self._acquireProcessedData(True, currentTime = currentTime)))
                    
                    if getContactQuality:
                        if contactQuality is False:
                            contactQuality = self._acquireContactQuality(currentTime = currentTime)
                        else:
                            contactQuality = np.vstack((contactQuality, self._acquireContactQuality(currentTime = currentTime)))
                    
                    if not getRawData and getProcessedData:
                        self.lastUpdateTime = processedData[-1,0]
                    if not getRawData and not getProcessedData and getContactQuality:
                        self.lastUpdateTime = contactQuality[-1,0]
            
            if not waitForResults:
                break
            
            if timeout is not None and time.time() - t0 > timeout:
                errorMessage = 'Timeout while reading data.'
                if not isinstance(rawData, bool) or not isinstance(processedData, bool):
                    errorMessage = errorMessage + 'Some data frames were dropped because of this exception.'
                raise PyemotivException(errorMessage)

        return (rawData, processedData, contactQuality)
            

    def _acquireRawDataBatch(self, idx, currentTime = None):
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

    def _acquireRawDataSensorBySensor(self, idx, currentTime = None):
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
        
        if currentTime is None:
            currentTime = time.time()

        container = np.empty((n, len(idx) + 1))
        
        k = 1
        for i in idx:
            data = np.empty((1,n))
            data_ctype = np.ctypeslib.as_ctypes(data)
            edk.EE_DataGet(self.data_handler, i, byref(data_ctype), n)
            data_read = np.ctypeslib.as_array(data_ctype)
            container[:,k] = data_read[0]
            k+=1

        self.times = np.linspace(self.times[-1]+self.sr, 
                                 self.times[-1]+ n*self.sr, n)

        lastEmotivTimestamp = container[-1, 20]
        for i in range(n):
            #container[i, 0] = currentTime - (lastEmotivTimestamp - container[i, 20])
            #container[i, 0] = currentTime
            container[:,0] = np.ones((1,n)) * currentTime
            pass

        return container
    
    def _acquireProcessedData(self, includeUnscaledValues = False, currentTime = None):
        """
        Gets the processed data values.
        
        If includeUnscaledValues is True then the unscaled values are also reported, making the resulting array larget.
        Only available in SDK v2+
        """
        edk.EE_EmoEngineEventGetEmoState(self.eEvent, self.eState)

        return self.getEmoStates(includeUnscaledValues)
    
    def _acquireContactQuality(self, currentTime = None):
        edk.EE_EmoEngineEventGetUserId(self.eEvent, self.userId)
        edk.EE_EmoEngineEventGetEmoState(self.eEvent, self.eState)

        numChannels = edk.ES_GetNumContactQualityChannels(self.eEvent)
        contactQualityArr = (c_long*numChannels)()
        edk.ES_GetContactQualityFromAllChannels(self.eState, contactQualityArr, numChannels)
        
        if currentTime is None:
            currentTime = time.time()

        contactQuality = np.zeros((1, 24))
        contactQuality[0][0] = currentTime
        contactQuality[0][1] = edk.ES_GetTimeFromStart(self.eState)
        contactQuality[0][2] = self.userId
        contactQuality[0][3] = edk.ES_GetWirelessSignalStatus(self.eState)
        
        batteryChargeLevel = c_int()
        batteryMaxChargeLevel = c_int()
        edk.ES_GetBatteryChargeLevel(self.eState, byref(batteryChargeLevel), byref(batteryMaxChargeLevel))
        contactQuality[0][4] = batteryChargeLevel.value
        contactQuality[0][5] = batteryMaxChargeLevel.value
        
        for i in range(numChannels):
            contactQuality[0][i+6] = contactQualityArr[i]

        return contactQuality

    def getEmoStates(self, includeUnscaledValues = False, currentTime = None):
        if currentTime is None:
            currentTime = time.time()

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
            container = np.zeros((1, 38))
        else:
            container = np.zeros((1, 26))
        
        # General data
        containerIndex = 0
        container[0][0] = currentTime
        containerIndex += 1
        container[0][containerIndex] = edk.ES_GetTimeFromStart(self.eState)
        containerIndex += 1
        container[0][containerIndex] = self.userId
        containerIndex += 1
        
        #Expressive Suite
        container[0][containerIndex] = edk.ES_ExpressivIsBlink(self.eState)
        containerIndex += 1
        container[0][containerIndex] = edk.ES_ExpressivIsLeftWink(self.eState)
        containerIndex += 1
        container[0][containerIndex] = edk.ES_ExpressivIsRightWink(self.eState)
        containerIndex += 1
        container[0][containerIndex] = edk.ES_ExpressivIsLookingLeft(self.eState)
        containerIndex += 1
        container[0][containerIndex] = edk.ES_ExpressivIsLookingRight(self.eState)
        containerIndex += 1
        container[0][containerIndex] = expressivStates[ edk.EXP_EYEBROW ]
        containerIndex += 1
        container[0][containerIndex] = expressivStates[ edk.EXP_FURROW ]
        containerIndex += 1
        container[0][containerIndex] = expressivStates[ edk.EXP_SMILE ]
        containerIndex += 1
        container[0][containerIndex] = expressivStates[ edk.EXP_CLENCH ]
        containerIndex += 1
        container[0][containerIndex] = expressivStates[ edk.EXP_SMIRK_LEFT ]
        containerIndex += 1
        container[0][containerIndex] = expressivStates[ edk.EXP_SMIRK_RIGHT ]
        containerIndex += 1
        container[0][containerIndex] = expressivStates[ edk.EXP_LAUGH ]
        containerIndex += 1
        
        # Affectiv Suite
        container[0][containerIndex] = edk.ES_AffectivGetExcitementShortTermScore(self.eState)
        containerIndex += 1
        container[0][containerIndex] = edk.ES_AffectivGetExcitementLongTermScore(self.eState)
        containerIndex += 1
        container[0][containerIndex] = edk.ES_AffectivGetMeditationScore(self.eState)
        containerIndex += 1
        container[0][containerIndex] = edk.ES_AffectivGetFrustrationScore(self.eState)
        containerIndex += 1
        container[0][containerIndex] = edk.ES_AffectivGetEngagementBoredomScore(self.eState)
        containerIndex += 1
        
        # Affectiv is active?
        container[0][containerIndex] = edk.ES_AffectivIsActive(self.eState, edk.AFF_EXCITEMENT)
        containerIndex += 1
        container[0][containerIndex] = edk.ES_AffectivIsActive(self.eState, edk.AFF_MEDITATION)
        containerIndex += 1
        container[0][containerIndex] = edk.ES_AffectivIsActive(self.eState, edk.AFF_FRUSTRATION)
        containerIndex += 1
        container[0][containerIndex] = edk.ES_AffectivIsActive(self.eState, edk.AFF_ENGAGEMENT_BOREDOM)
        containerIndex += 1

        #Cognitive Suite
        container[0][containerIndex] = edk.ES_CognitivGetCurrentAction(self.eState)
        containerIndex += 1
        container[0][containerIndex] = edk.ES_CognitivGetCurrentActionPower(self.eState)
        containerIndex += 1

        # Affective unscaled model parameters
        if includeUnscaledValues:
            functionNames = ['ES_AffectivGetExcitementShortTermModelParams',
                             'ES_AffectivGetMeditationModelParams', 
                             'ES_AffectivGetFrustrationModelParams', 
                             'ES_AffectivGetEngagementBoredomModelParams']

            for functionName in functionNames:
                rawScore = c_double()
                minScale = c_double()
                maxScale = c_double()
                function = getattr(edk, functionName)
                function(self.eState, byref(rawScore), byref(minScale), byref(maxScale))
                container[0][containerIndex] = rawScore.value
                containerIndex += 1
                container[0][containerIndex] = minScale.value
                containerIndex += 1
                container[0][containerIndex] = maxScale.value
                containerIndex += 1

        return container
    
    def addMarker(self, marker):
        edk.EE_DataSetMarker(self.userId, marker)

    def getProcessedDataFileHeader(self, includeUnscaledValues = False, joinAsString = True):
        header = ['Local timestamp', 'Time From Start', 'User ID',
                  'Blink','Wink Left','Wink Right','Look Left','Look Right','Eyebrow','Furrow','Smile','Clench','Smirk Left','Smirk Right','Laugh',
                  'Short Term Excitement','Long Term Excitement','Meditation','Frustration','Engagement/Boredom',
                  'Excitement is active','Meditation is active','Frustration is active','Engagement/Boredom is active',
                  'Cognitiv Action','Cognitiv Power']
        
        if includeUnscaledValues:
            for name in ['Short Term Excitement','Meditation','Frustration','Engagement/Boredom',]: #there is no long term exc for some reason
                for score in ['raw', 'min', 'max']:
                    header.append(name + " " + score)
        
        if joinAsString:
            return ','.join(header)
        else:
            return header

    def getRawDataFileHeader(self, joinAsString = True):
        header = ['Local timestamp']
        header.extend(self.channels)
        # Learning point of the day: extend returns None, so writing ['Local time'].extend(..) doesn't do what you mean..

        if joinAsString:
            return ','.join(header)
        else:
            return header

    def getContactQualityFileHeader(self, joinAsString = True):
        header = ['Local timestamp', 'Time From Start','User ID','Wireless Signal Status', 'Battery Charge Level', 'Battery Max Charge Level']
        
        for channel in self.logicalChannels:
            header.append(channel)
        
        if joinAsString:
            return ','.join(header)
        else:
            return header
    
    def close(self):
        edk.EE_EngineDisconnect()
        edk.EE_EmoStateFree(self.eState)
        edk.EE_EmoEngineEventFree(self.eEvent)
        self.rawFile.close()
        self.processedFile.close()
        self.qualityFile.close()
        
    def readData(self):
        if self.connectionType == "local":
            (raw, processed, contact) = \
                self.getData(getRawData = True, getProcessedData = True, getContactQuality = True, waitForResults = True)    
            
            if self.clearDataArraysOnNextRead or (self.rawData is None and self.processedData is None and self.contactQuality is None):
                if len(raw.shape) > 1:
                    self.rawData = raw
                else:
                    self.rawData = np.empty((1, 25))
                    self.rawData[0] = raw

                if len(processed.shape) > 1:
                    self.processedData = processed
                else:
                    self.processedData = np.empty((1, 33))
                    self.processedData[0] = processed
                
                if len(contact.shape) > 1:
                    self.contactQuality = contact
                else:
                    self.contactQuality = np.empty((1, 23))
                    self.contactQuality[0] = contact
                    
                self.clearDataArraysOnNextRead = False
            else:
                # FIXME no vstack
                self.rawData = np.vstack((self.rawData, raw))
                self.processedData = np.vstack((self.processedData, processed))
                self.contactQuality = np.vstack((self.contactQuality, contact))

        else: # remote
            (raw, processed, contact) = \
                self.getData(getRawData = False, getProcessedData = True, getContactQuality = False, waitForResults = True)    
            
            if self.clearDataArraysOnNextRead or self.processedData is None:
                (self.rawData, self.processedData, self.contactQuality) = (raw, processed, contact)
                self.clearDataArraysOnNextRead = False
            else:
                self.processedData = np.vstack((self.processedData, processed))

        return True
    
    def openHDFStore(self, directory = ""):
        pd.set_option('io.hdf.default_format','table')

        self.rawHDFStore = pd.HDFStore(os.path.join(directory, "raw.h5"))
        self.processedHDFStore = pd.HDFStore(os.path.join(directory, "processed.h5"))
        self.contactHDFStore = pd.HDFStore(os.path.join(directory, "contact.h5"))

    def readDataToHDF(self):
        if self.connectionType == "local":
            (self.lastRaw, self.lastProcessed, self.lastContact) = \
                self.getData(getRawData = True, getProcessedData = True, getContactQuality = True, waitForResults = True)    
            
            if self.rawHDFStore is None:
                self.openHDFStore()

            self.rawHDFStore.append(        'raw',       pd.DataFrame(self.lastRaw, columns = self.getRawDataFileHeader(joinAsString = False)).set_index(['Local timestamp']))
            self.processedHDFStore.append(  'processed', pd.DataFrame(self.lastProcessed, columns = self.getProcessedDataFileHeader(includeUnscaledValues = True, joinAsString = False)).set_index(['Local timestamp']))
            self.contactHDFStore.append(    'contact',   pd.DataFrame(self.lastContact, columns = self.getContactQualityFileHeader(joinAsString = False)).set_index(['Local timestamp']))

        else: # remote, fixme
            (raw, processed, contact) = \
                self.getData(getRawData = False, getProcessedData = True, getContactQuality = False, waitForResults = True)    
            
            if self.clearDataArraysOnNextRead or self.processedData is None:
                (self.rawData, self.processedData, self.contactQuality) = (raw, processed, contact)
                self.clearDataArraysOnNextRead = False
            else:
                self.processedData = np.vstack((self.processedData, processed))

        return True

    def flushHDFStore(self):
        self.rawHDFStore.flush(fsync=True)
        self.processedHDFStore.flush(fsync=True)
        self.contactHDFStore.flush(fsync=True)
        
    def exportHDFToCSV(self, directory = ""):
        self.rawHDFStore['raw'].to_csv(os.path.join(directory, "raw.csv"))
        self.processedHDFStore['processed'].to_csv(os.path.join(directory, "processed.csv"))
        self.contactHDFStore['contact'].to_csv(os.path.join(directory, "contact.csv"))

    def save(self, directory = None, useHDF = False):
        if directory is not None:
            originalDir = os.getcwd()

            os.chdir(directory)

        if useHDF:
            self.rawHDFStore.close()
            self.processedHDFStore.close()
            self.contactHDFStore.close()
        else:
            if self.rawFile is None or self.processedFile is None or self.qualityFile is None:
                self.rawFile = file('raw.txt', 'a')
                self.processedFile = file('processed.txt', 'a')
                self.qualityFile = file('quality.txt', 'a') 
                np.savetxt(self.rawFile, self.rawData, delimiter=',', header=self.getRawDataFileHeader())
                np.savetxt(self.processedFile, self.processedData, delimiter=',', header=self.getProcessedDataFileHeader(True))
                np.savetxt(self.qualityFile, self.contactQuality, delimiter=',', header=self.getContactQualityFileHeader())
            else:
                self.rawFile = file('raw.txt', 'a')
                self.processedFile = file('processed.txt', 'a')
                self.qualityFile = file('quality.txt', 'a')
                # no headers if the files are already open and we are just appending
                np.savetxt(self.rawFile, self.rawData, delimiter=',')
                np.savetxt(self.processedFile, self.processedData, delimiter=',')
                np.savetxt(self.qualityFile, self.contactQuality, delimiter=',')
                
            self.clearDataArraysOnNextRead = True
            #(self.rawData, self.processedData, self.contactQuality) = (None, None, None)
            #instead of clearing the data arrays right away, we will do it when the next data comes in, so that they're never empty during the recording
                
            self.rawFile.flush()
            self.processedFile.flush()
            self.qualityFile.flush()
        
        if directory is not None:
            os.chdir(originalDir)

    def reset(self):
        self.times = [0.]

        (self.rawData, self.processedData, self.contactQuality) = (None, None, None)
        (self.rawFile, self.processedFile, self.qualityFile) = (None, None, None)
        (self.rawHDFStore, self.processedHDFStore, self.contactHDFStore) = (None, None, None)
        self.lastUpdateTime = None

if __name__ == "__main__":
    e = Epoc("local")
    i = 0
    
    directory = "J:/home/eperfa/Synetiq/Mindr/"
    
    inspect = False
    save = True
    
    import serial
    ser = serial.Serial(1, 19200, timeout=0.01)

    startTime = time.time()

    print "Saving EEG data"
    while save:
        i += 1
        time.sleep(0.01)
        ok = e.readDataToHDF()
        
        if ser.inWaiting():
            res = ser.read(ser.inWaiting()) #in case there is a newline at the end of the transmission
            print "res: " + res
            intres = int(res)
            print "intres: " + str(intres)
            e.addMarker(intres)
        
#         if i % 100 == 0:
#             e.save(directory)
#             print "flushed"
#         if not ok:
#             save = False
#             inspect = False
#             print "Stop marker detected, stopping EEG data saving"
        if time.time() - startTime > 36:
            print "Timeout"
            save = False

#    e.close()
    e.HDFStore.close()
    e.save(directory)

    #print data