from ctypes import *
import numpy as np
import time, sys
import edk

class Epoc(object):
    def initializeInternalVariables(self):
        self.eEvent = edk.EE_EmoEngineEventCreate()
        self.eState = edk.EE_EmoStateCreate()
        
        self.userId = 0
        self.channels = [ 'ED_COUNTER','ED_INTERPOLATED','ED_RAW_CQ',
                          'ED_AF3','ED_F7','ED_F3','ED_FC5','ED_T7',
                          'ED_P7','ED_O1','ED_O2','ED_P8','ED_T8',
                          'ED_FC6','ED_F4','ED_F8','ED_AF4','ED_GYROX',
                          'ED_GYROY','ED_TIMESTAMP','ED_ES_TIMESTAMP',
                          'ED_FUNC_ID','ED_FUNC_VALUE','ED_MARKER',
                          'ED_SYNC_SIGNAL']
        self.raw_channels_idx = range(3,17)
        self.gyro_idx = [self.channels.index("ED_GYROX"),self.channels.index("ED_GYROY")]
        self.names = [name[3:] for name in self.channels]
        self.name_dict = {name:i for name,i in zip(self.names,
                                                   xrange(len(self.names)))}
        self.m = len(self.channels)
        self.all_data = np.zeros((25,2))
        self.raw = np.zeros((14,2))
        self.gyros = np.zeros((2,2))
        self.sr = 1/127.94
        self.times = [0.]
        
        self.composerPort = 1726

    """
    Class that connects to Emotiv Epoc by wrapping the 
    research SDK dynamic link libraries
    """
    def __init__(self, connectionType = "local", connectionTimeout = 10):
        self.initializeInternalVariables()
        
        self.connected = False
        # either "local" or "remote"
        self.connectionType = "remote"
        self.connectionTimeout = connectionTimeout

        self.debug = True
    
    
    def connect(self):   
        """
        Establishes connection to Emotiv Epoc
        """
        if self.debug:
            print 'Connecting..'

        if self.connectionType == "local":
            if edk.EE_EngineConnect("Emotiv Systems-5") != 0:
                raise PyemotivException("Emotiv Engine start up failed.")
        elif self.connectionType == "remote":
            if edk.EE_EngineRemoteConnect("127.0.0.1", self.composerPort, "Emotiv Systems-5") != 0:
                raise PyemotivException("Cannot connect to EmoComposer on")
        else:
            raise PyemotivException("Unknow connection type - please specify either 'local' or 'remote'.")
        
        self.data_handler = edk.EE_DataCreate()
        edk.EE_DataSetBufferSizeInSec(5)

        t0 = time.time()
        while not self.connected:
            state = edk.EE_EngineGetNextEvent(self.eEvent)
            if state == edk.EDK_OK:
                self.connected = True
                edk.EE_DataAcquisitionEnable(0, True)
                break
            if time.time() - t0 > self.connectionTimeout:
                raise PyemotivException('Timeout while connecting to Epoc!')
            
        if self.debug:
            print 'Connected'
                
    def get_all(self):
        """
        Get block of raw data from the device buffer
        """
        if not self.connected:
            self.connect()
            
        (rawContainer, processedContainer) = self.aquire(getRawData = True, getProcessedData = True, rawDataChannels = xrange(self.m))
        self.raw = np.array([rawContainer[i] for i in self.raw_channels_idx])
        self.gyros = np.array([rawContainer[i] for i in self.gyro_idx])
        self.all_data = rawContainer
        return (self.all_data, processedContainer)
    
    def get_all_raw(self):
        """
        Get block of raw data from the device buffer
        """
        if not self.connected:
            self.connect()
            
        container = self.aquire(getRawData = True, getProcessedData = False, rawDataChannels = xrange(self.m))
        self.raw = np.array([container[i] for i in self.raw_channels_idx])
        self.gyros = np.array([container[i] for i in self.gyro_idx])
        self.all_data = container
        return self.all_data
    
    def get_all_processed(self):
        """
        Get block of processed data from the device buffer
        """
        if not self.connected:
            self.connect()
            
        processedContainer = self.aquire(getRawData = False, getProcessedData = True)
        return processedContainer
    
    def get_raw(self):
        if not self.connected:
            self.connect()

        container = self.aquire(getRawData = True, getProcessedData = False, rawDataChannels = self.raw_channels_idx)
        self.raw = container
        return container
    
    def get_gyros(self):
        if not self.connected:
            self.connect()

        container = self.aquire(getRawData = True, getProcessedData = False, rawDataChannels = self.gyro_idx)
        self.gyros = container
        return container
        
    def aquire(self, getRawData = True, getProcessedData = True, rawDataChannels = None, processedDataChannels = None):
        rawData = False
        processedData = False

        # FIXME this will DROP/OVERWRITE DATA if, for example, we received some raw data, but not the processed states !
        while (isinstance(rawData, bool) and not rawData or not getRawData) and (isinstance(processedData, bool) and not processedData or not getProcessedData):
            if getProcessedData:
                processedData = self.acquireProcessedData()
        
            if getProcessedData:
                rawData = self.acquireRawData(rawDataChannels)

        if (getRawData and getProcessedData):
            return (rawData, processedData)
        elif getRawData:
            return rawData
        else:
            return processedData
            

    def acquireRawData(self, idx):
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
        return container
    
    def acquireProcessedData(self):
        state = edk.EE_EngineGetNextEvent(self.eEvent)
        if (state == edk.EDK_NO_EVENT):
            return False
        elif (state == edk.EDK_OK):
            eventType = edk.EE_EmoEngineEventGetType(self.eEvent)
            edk.EE_EmoEngineEventGetUserId(self.eEvent, self.userId)

            if (eventType == edk.EE_EmoStateUpdated):
                edk.EE_EmoEngineEventGetEmoState(self.eEvent, self.eState)
                timestamp = edk.ES_GetTimeFromStart(self.eState)

                return self.getEmoState(self.userId, self.eState)
        else:
            raise PyemotivException('Internal error of Emotiv while acquiring states')        

    def getEmoState(self, userID, eState):
        expressivStates={}
        expressivStates[ edk.EXP_EYEBROW     ] = 0
        expressivStates[ edk.EXP_FURROW      ] = 0
        expressivStates[ edk.EXP_SMILE       ] = 0
        expressivStates[ edk.EXP_CLENCH      ] = 0
        expressivStates[ edk.EXP_SMIRK_LEFT  ] = 0
        expressivStates[ edk.EXP_SMIRK_RIGHT ] = 0
        expressivStates[ edk.EXP_LAUGH       ] = 0
        upperFaceAction = edk.ES_ExpressivGetUpperFaceAction(eState)
        upperFacePower  = edk.ES_ExpressivGetUpperFaceActionPower(eState)
        lowerFaceAction = edk.ES_ExpressivGetLowerFaceAction(eState)
        lowerFacePower  = edk.ES_ExpressivGetLowerFaceActionPower(eState)
        expressivStates[ upperFaceAction ] = upperFacePower;
        expressivStates[ lowerFaceAction ] = lowerFacePower;
        
        container = np.zeros(22)
        
        # General data
        container[0] = edk.ES_GetTimeFromStart(eState)
        container[1] = userID
        container[2] = edk.ES_GetWirelessSignalStatus(eState)
        
        #Expressive Suite
        container[3] = edk.ES_ExpressivIsBlink(eState)
        container[4] = edk.ES_ExpressivIsLeftWink(eState)
        container[5] = edk.ES_ExpressivIsRightWink(eState)
        container[6] = edk.ES_ExpressivIsLookingLeft(eState)
        container[7] = edk.ES_ExpressivIsLookingRight(eState)
        container[8] = expressivStates[ edk.EXP_EYEBROW ]
        container[9] = expressivStates[ edk.EXP_FURROW ]
        container[10] = expressivStates[ edk.EXP_SMILE ]
        container[11] = expressivStates[ edk.EXP_CLENCH ]
        container[12] = expressivStates[ edk.EXP_SMIRK_LEFT ]
        container[13] = expressivStates[ edk.EXP_SMIRK_RIGHT ]
        container[14] = expressivStates[ edk.EXP_LAUGH ]
        
        # Affectiv Suite
        container[15] = edk.ES_AffectivGetExcitementShortTermScore(eState)
        container[16] = edk.ES_AffectivGetExcitementLongTermScore(eState)
        container[17] = edk.ES_AffectivGetMeditationScore(eState)
        container[18] = edk.ES_AffectivGetFrustrationScore(eState)
        container[19] = edk.ES_AffectivGetEngagementBoredomScore(eState)
        
        #Cognitive Suite
        container[20] = edk.ES_CognitivGetCurrentAction(eState)
        container[21] = edk.ES_CognitivGetCurrentActionPower(eState)
        
        return container
    
    def getProcessedDataFileHeader(self):
        header = ['Time','UserID','Wireless Signal Status','Blink','Wink Left','Wink Right','Look Left','Look Right','Eyebrow','Furrow','Smile','Clench','Smirk Left','Smirk Right','Laugh','Short Term Excitement','Long Term Excitement','Meditation','Frustration','Engagement/Boredom','Cognitiv Action','Cognitiv Power']
        return ','.join(header)

    def close(self):
        edk.EE_EngineDisconnect()
        edk.EE_EmoStateFree(self.eState)
        edk.EE_EmoEngineEventFree(self.eEvent)

if __name__ == "__main__":
    e = Epoc()
    i = 0
    data = np.zeros([22, ])
    while i < 400:
        print "Round %d starting" % i
        data2 = e.get_all_processed()
        data = np.vstack((data, data2))
        i += 1
    e.close()
    np.savetxt("processed.txt", data, delimiter=',', header=e.getProcessedDataFileHeader())
    #print data