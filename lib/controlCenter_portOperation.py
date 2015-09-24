from PyQt4.QtCore import *
from PyQt4.QtGui import *
import serial


#############this class is only accessable by control center##################


#  after the appliction starts, the following steps must be done:
#    1.register log window to get port infomation shown, use <register_logWindow(infoObj)>
#    2.try to connect the port saved in rom, use <connect(self, baudRate, port)>


#  before recaive the data, the instance must do:
#    1. register the upload obj to handle the racaived data, use <register_upload(self, upLayerobj)>
#    2. set read bytes one time, use <set_readDataLen(self, readLen)>
#    3. clear read buff if needed, use <clear_recaiveBuff(self)>


#  if the instance is no longer need to recaive data,:
#    1. unregister the upload obj to release the thread


#  if  the appliction is going to terminate:
#    1. disconnect the port
#    2. stop the thread



class SerialPortOperation(QThread):
    def __init__(self, MainWindow, controlCentor):
        super(SerialPortOperation, self).__init__(MainWindow)
        self.isContinueRun=True
        self.serialObj = None
        self.mainWindow = MainWindow
        self.controlCentor = controlCentor
    
    def set_readDataLen(self, readLen):
        self.readLen = readLen
    
    def clear_recaiveBuff(self):
        if self.serialObj is not None:
            self.serialObj.flushInput()

    def clear_writeBuff(self):
        if self.serialObj is not None:
            self.serialObj.flushOutput()

    def stop_thread(self):
        self.isContinueRun = False

    def start_thread(self):
        self.isContinueRun = True
        self.start()        

    def isConnect(self):
        if self.serialObj is not None:
            return self.serialObj.isOpen()
        else:
            return False
                   
    def run(self):
        while self.isContinueRun:
            if self.controlCentor.currentUploadObj is None:
                self.clear_recaiveBuff()
                continue
                    
            try:
                if not self.isConnect():
                    self.mainWindow.emit(SIGNAL("portDisonnected"))
                    return
            
                dataRecaived = self.serialObj.read(self.readLen)
                if dataRecaived is '': # the read is non-blocking
                    continue
                else:
                    sleepTime = self.controlCentor.getData(dataRecaived)
                    if sleepTime is not None :
                        self.msleep(sleepTime)
                        self.clear_recaiveBuff()
            except:
                pass
            

    def writeData(self, writeData):
        sendLen=len(writeData)           
        if sendLen != self.serialObj.write(str(writeData)):# it should be type of 'str', not include type of 'unicode' 
            return False
        else:
            return True
            
                    
    def connect(self, baudRate, port):        
        try:
            self.serialObj = serial.Serial(port, baudRate, serial.EIGHTBITS, serial.PARITY_NONE,
                                    serial.STOPBITS_ONE, 3, False, False, 3)#timeout 1 seconds
            if not self.isConnect():
                self.serialObj.open()
            self.mainWindow.emit(SIGNAL("portConnected"))
            return True
        except :
            self.serialObj = None           
            return False


    def disconnect(self):
        try:
            self.serialObj.close()           
        except :
            pass
        finally:
            self.stop_thread()
            self.serialObj = None
            self.mainWindow.emit(SIGNAL("portDisonnected"))
