from controlCenter_portOperation import * 

class ControlCenter():
    def __init__(self, Mainwindow, logWindow):
        self.serialLock = False
        self.currentUploadObj = None
        Mainwindow.addSysbroadcastSignalObj(self)
        self.serialPort = SerialPortOperation(Mainwindow, self)
        self.logWindow = logWindow
        self.mainWindow = Mainwindow


    def lockSerialPort(self, uploadObj):
        if not self.serialLock:
            self.currentUploadObj = uploadObj
            self.currentUploadObj.setPortPara(self.serialPort)
            self.serialLock = True
            if self.currentUploadObj is not self.mainWindow.serialCommand :
                #self.logWindow.infoLog('%s is connect to the port' %self.currentUploadObj.className())
                pass
        return self.serialLock


    def getCurrentLockObj(self):
        return self.currentUploadObj


    def forcedLock(self, uploadObj):
        self.currentUploadObj = uploadObj
        self.currentUploadObj.setPortPara(self.serialPort)
        self.serialLock = True
        #if self.currentUploadObj is not self.mainWindow.serialCommand :
        #    self.logWindow.infoLog('%s is connect to the port' %self.currentUploadObj.className())

    def unlockSerialPort(self, uploadObj):
        if self.serialLock and uploadObj is self.currentUploadObj :
            self.currentUploadObj = None
            self.serialLock = False
        return not self.serialLock

    def dealPortSignal(self, signalstr, portNum):
        if self.currentUploadObj is None :
            return
        if 'disconn' in signalstr:
            self.serialPort.stop_thread()
        else:
            self.serialPort.start_thread()

    def getData(self, data):
        if self.currentUploadObj is not None:
            self.currentUploadObj.getData(data)
        else:
            return

    def writeData(self, uploadObj, data):
        if uploadObj is self.currentUploadObj:
            return self.serialPort.writeData(data)
        else:
            raise Exception, "access denied"

    def clearPort(self, bufferName):
        if 'in' in bufferName:
            self.serialPort.clear_recaiveBuff()
        else:
            self.serialPort.clear_writeBuff()            

    def applyConnectPort(self, baudRate, port):
        return self.serialPort.connect(baudRate, port)

    def applyDisconnectPort(self):
        self.serialPort.disconnect()

    def className(self):
        return 'ControlCenter'

    def delayTime(self):
        i = 0xffff
        while i > 0xff :
            i -= 1
            a =3*4/2


    

            
        
            
            
        
