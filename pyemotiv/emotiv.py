from ctypes import *
import numpy as np
import time, sys
from emotivErrorCodes import errorCodes

# http://emotiv.com/bitrix/components/bitrix/forum.interface/show_file.php?fid=4258

class Epoc(object):
    def loadDLL(self):
        #setup access to binaries
        if sys.platform=='darwin':
            edk_file='libedk.1.0.0.dylib'
        elif sys.platform=='win32':
            sys.path.append('lib')
            edk_file='edk.dll'
        self.edk=CDLL(edk_file)

    def initializeExternalFunctions(self):
        EE_EmoEngineEventCreate = self.edk.EE_EmoEngineEventCreate
        EE_EmoEngineEventCreate.restype = c_void_p
        self.eEvent      = EE_EmoEngineEventCreate()
        
        EE_EmoEngineEventGetEmoState = self.edk.EE_EmoEngineEventGetEmoState
        EE_EmoEngineEventGetEmoState.argtypes=[c_void_p,c_void_p]
        EE_EmoEngineEventGetEmoState.restype = c_int
        
        ES_GetTimeFromStart = self.edk.ES_GetTimeFromStart
        ES_GetTimeFromStart.argtypes=[c_void_p]
        ES_GetTimeFromStart.restype = c_float
        
        EE_EmoStateCreate = self.edk.EE_EmoStateCreate
        EE_EmoStateCreate.restype = c_void_p
        self.eState=EE_EmoStateCreate()
        
        ES_GetWirelessSignalStatus=self.edk.ES_GetWirelessSignalStatus
        ES_GetWirelessSignalStatus.restype = c_int
        ES_GetWirelessSignalStatus.argtypes = [c_void_p]
        
        ES_ExpressivIsBlink=self.edk.ES_ExpressivIsBlink
        ES_ExpressivIsBlink.restype = c_int
        ES_ExpressivIsBlink.argtypes= [c_void_p]
        
        ES_ExpressivIsLeftWink=self.edk.ES_ExpressivIsLeftWink
        ES_ExpressivIsLeftWink.restype = c_int
        ES_ExpressivIsLeftWink.argtypes= [c_void_p]
        
        ES_ExpressivIsRightWink=self.edk.ES_ExpressivIsRightWink
        ES_ExpressivIsRightWink.restype = c_int
        ES_ExpressivIsRightWink.argtypes= [c_void_p]
        
        ES_ExpressivIsLookingLeft=self.edk.ES_ExpressivIsLookingLeft
        ES_ExpressivIsLookingLeft.restype = c_int
        ES_ExpressivIsLookingLeft.argtypes= [c_void_p]
        
        ES_ExpressivIsLookingRight=self.edk.ES_ExpressivIsLookingRight
        ES_ExpressivIsLookingRight.restype = c_int
        ES_ExpressivIsLookingRight.argtypes= [c_void_p]
        
        ES_ExpressivGetUpperFaceAction=self.edk.ES_ExpressivGetUpperFaceAction
        ES_ExpressivGetUpperFaceAction.restype = c_int
        ES_ExpressivGetUpperFaceAction.argtypes= [c_void_p]
        
        ES_ExpressivGetUpperFaceActionPower=self.edk.ES_ExpressivGetUpperFaceActionPower
        ES_ExpressivGetUpperFaceActionPower.restype = c_float
        ES_ExpressivGetUpperFaceActionPower.argtypes= [c_void_p]
        
        ES_ExpressivGetLowerFaceAction=self.edk.ES_ExpressivGetLowerFaceAction
        ES_ExpressivGetLowerFaceAction.restype = c_int
        ES_ExpressivGetLowerFaceAction.argtypes= [c_void_p]
        
        ES_ExpressivGetLowerFaceActionPower=self.edk.ES_ExpressivGetLowerFaceActionPower
        ES_ExpressivGetLowerFaceActionPower.restype = c_float
        ES_ExpressivGetLowerFaceActionPower.argtypes= [c_void_p]
        
        ES_AffectivGetExcitementShortTermScore=self.edk.ES_AffectivGetExcitementShortTermScore
        ES_AffectivGetExcitementShortTermScore.restype = c_float
        ES_AffectivGetExcitementShortTermScore.argtypes= [c_void_p]
        
        ES_AffectivGetExcitementLongTermScore=self.edk.ES_AffectivGetExcitementLongTermScore
        ES_AffectivGetExcitementLongTermScore.restype = c_float
        ES_AffectivGetExcitementLongTermScore.argtypes= [c_void_p]
        
        
        ES_AffectivGetEngagementBoredomScore=self.edk.ES_AffectivGetEngagementBoredomScore
        ES_AffectivGetEngagementBoredomScore.restype = c_float
        ES_AffectivGetEngagementBoredomScore.argtypes= [c_void_p]
        
        ES_CognitivGetCurrentAction=self.edk.ES_CognitivGetCurrentAction
        ES_CognitivGetCurrentAction.restype = c_int
        ES_CognitivGetCurrentAction.argtypes= [c_void_p]
        
        ES_CognitivGetCurrentActionPower=self.edk.ES_CognitivGetCurrentActionPower
        ES_CognitivGetCurrentActionPower.restype = c_float
        ES_CognitivGetCurrentActionPower.argtypes= [c_void_p]


    def initializeInternalVariables(self):
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
        
        self.composerPort = c_uint(1726)

    """
    Class that connects to Emotiv Epoc by wrapping the 
    research SDK dynamic link libraries
    """
    def __init__(self):
        self.loadDLL()
        self.initializeExternalFunctions()
        self.initializeInternalVariables()
        
        self.connected = False
        # either "local" or "remote"
        self.connectionType = "remote"
        
        self.justRawData = False
        
    def connect(self, timeout = 10):   
        """
        Establishes connection to Emotiv Epoc
        """
        if self.connectionType == "local":
            if self.edk.EE_EngineConnect("Emotiv Systems-5") != 0:
                raise Exception("Emotiv Engine start up failed.")
        elif self.connectionType == "remote":
            if self.edk.EE_EngineRemoteConnect("127.0.0.1", self.composerPort) != 0:
                raise Exception("Cannot connect to EmoComposer on")
        else:
            raise Exception("Unknow connection type - please specify either 'local' or 'remote'.")
        
        self.data_handler = self.edk.EE_DataCreate()
        self.edk.EE_DataSetBufferSizeInSec(5)
        

        state = self.edk.EE_EngineGetNextEvent(self.eEvent)
        t0 = time.time()
        while not self.connected:
            state = self.edk.EE_EngineGetNextEvent(self.eEvent)
            if state == errorCodes["EDK_OK"]:
                self.connected = True
                self.edk.EE_DataAcquisitionEnable(c_uint(0),c_bool(1))
                break
            if time.time() - t0 > timeout:
                raise Exception('Timeout while connecting to Epoc!')
                
    
    def get_all(self):
        """
        Get block of raw data from the device buffer
        """
        if not self.connected:
            self.connect()
            
        container = self.aquire(xrange(self.m))
        self.raw = np.array([container[i] for i in self.raw_channels_idx])
        self.gyros = np.array([container[i] for i in self.gyro_idx])
        self.all_data = container
        return self.all_data
    
    def get_raw(self):
        if not self.connected:
            self.connect()
        container = self.aquire(self.raw_channels_idx)
        self.raw = container
        return container
    
    def get_gyros(self):
        if not self.connected:
            self.connect()
        container = self.aquire(self.gyro_idx)
        self.gyros = container
        return container
        
    def aquire(self,idx):
        state = self.edk.EE_EngineGetNextEvent(self.eEvent)
        
        nSamples = c_int()
        while True:
            if self.justRawData != True:
                if (state == errorCodes["EDK_OK"]):
                    eventType = self.edk.EE_EmoEngineEventGetType(self.eEvent)
                    self.edk.EE_EmoEngineEventGetUserId(self.eEvent, self.userId)
            
                    if (eventType == EE_EmoStateUpdated):
                        self.edk.EE_EmoEngineEventGetEmoState(self.eEvent, self.eState)
                        timestamp = ES_GetTimeFromStart(self.eState)
        
                        printf("%10.3fs : New EmoState from user %d ...\r", timestamp, userID)
                        
                        #logEmoState(ofs, userID, eState, writeHeader);
                elif (state != errorCodes["EDK_NO_EVENT"]):
                    raise Exception('Internal error of Emotiv while acquiring states')
        
            self.edk.EE_DataUpdateHandle(c_uint(0), self.data_handler)
            self.edk.EE_DataGetNumberOfSample(self.data_handler, 
                                              byref(nSamples))
            n = nSamples.value
            if not n:
                continue
            container = np.empty((len(idx) , n))
            k=0
            for i in idx:
                data = np.empty((1,n))
                data_ctype = np.ctypeslib.as_ctypes(data)
                self.edk.EE_DataGet(self.data_handler, i, byref(data_ctype),
                                    c_uint(n))
                data_read = np.ctypeslib.as_array(data_ctype)
                container[k,:] = data_read[0]
                k+=1
            self.times = np.linspace(self.times[-1]+self.sr, 
                                     self.times[-1]+ n*self.sr, n)            
            return container
        
        
if __name__ == "__main__":
    e = Epoc()
    while True:
        e.get_raw()