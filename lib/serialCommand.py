from PyQt4.QtCore import *
from PyQt4.QtGui import *


class  SerialCommand(QThread):
    def __init__(self, MainWindow, logWindow, controlCenter):
        super(SerialCommand, self).__init__(MainWindow)
        self.MainWindow = MainWindow
        self.logWindow = logWindow
        self.controlCenter = controlCenter
        self.dataBuff=''
        self.isRunning = False

        self.forcedUnlockObj = None
        self.recaivedBytes=''

    def isCommandFinished(self):
        return not self.isRunning
        
        

    def getRecaivedMessage(self):
        return self.recaivedBytes
    
    def setCommand(self, toolBar, sendString, responseString=None, responseFunc=None,
                                            errorFunc=None, commandTime=5, commandType="single"):
        if self.isRunning and ("single" in commandType or 'start' in commandType):
            self.logWindow.warningLog("the last Command has not finished yet")
            return
        
        self.sendString = sendString
        self.responseString = responseString
        self.responseFunc = responseFunc
        self.errorFunc = errorFunc
        self.toolBar = toolBar
        self.commandTime = commandTime
        self.commandType = commandType

        self.controlCenter.forcedLock(self)
        self.startTime = QDateTime().currentDateTime()

        if self.toolBar is not None:
            self.toolBar.setEnabled(False)
        self.forcedUnlockObj = self.controlCenter.getCurrentLockObj()
        if "single" in self.commandType or 'start' in self.commandType  :
            self.isRunning = True
            self.start()            


    def commandFinish(self, status):
        if 'Finished' in status:
            if 'start' in self.commandType or 'middle' in self.commandType:
                self.responseFunc() # the func may set 'self.commandType'
                return
            else:
                self.responseFunc()
        else :
            self.errorFunc()
            
        self.recaivedBytes=self.dataBuff
        self.dataBuff =''
        if self.toolBar is not None:
            self.toolBar.setEnabled(True)
        self.controlCenter.forcedLock(self.forcedUnlockObj)
        self.isRunning = False
        

    def isContinue(self):
        if self.startTime.secsTo(QDateTime().currentDateTime()) >  self.commandTime :
            return False
        else:
            self.msleep(10)
            return True
   
    
    def run(self):       
        while self.isRunning :
            status = ''
            try:
                self.controlCenter.clearPort('in')
                self.dataBuff = ''
                self.writeData(self.sendString)        
                while self.isContinue():
                    if self.responseString in self.dataBuff:
                        status = 'Finished'
                        break
            except Exception, e:
                print e
            finally:
                self.commandFinish(status)
            
                
                                  

    ############the following func is needed when create a window to connect to port##############################
    def className(self):
        return 'serialCommand'

    def getData(self, dataRecaive):
        self.dataBuff += dataRecaive
        return None

    def writeData(self, data):
        if len(data) > 0 :
            try:
                self.controlCenter.writeData(self, data)
            except Exception, e:
                if "access denied" in e:
                    QMessageBox.about(self, 'WORNING!!!',
                                      "The port is occupyed by others!!!" )
                else:
                    self.logWindow.errorLog("write error occures during sending data to port")         

    def setPortPara(self, portObj):
        portObj.set_readDataLen(1)

    

                    
                
            
            
            
        
        

            
 
            
