from portParaSet import *
from dataStreamWindow import *

import platform

__messageHeader__ = "\xaa\x55\xaa"

__calibarationNum__ = 0
__statisticsNum__ =1
__othersNum__ =2

__isCollectingData__ = 0
__isCotrolledModeWaiting__ = 1
__isWorkingMode__ = 2
__isNotSure__ =3

class WindowActionContainer():

    @staticmethod
    def isOtherActionFinished(windowObj, showMessage=True):
        if not windowObj.serialCommand.isCommandFinished():
            if showMessage:
                windowObj.logWindow.warningLog('Last action not finished yet, please wait')
            return False
        else:
            return True
            

    @staticmethod
    def connectPortAction(windowObj):
        if not WindowActionContainer.isOtherActionFinished(windowObj):
            return
        
        if not windowObj.controlCenter.applyConnectPort(windowObj.portBaudrate, windowObj.portNum):
            windowObj.logWindow.errorLog("connection Failed at Port %d" %(windowObj.portNum+1))
            windowObj.portSetAction()
            
    @staticmethod        
    def disconnectPortAction(windowObj):
        if not WindowActionContainer.isOtherActionFinished(windowObj):
            return
        
        windowObj.controlCenter.applyDisconnectPort()
        #windowObj.logWindow.infoLog('disconnect port %d' %(windowObj.portNum+1))
 

    @staticmethod
    def showPortWindowAction(windowObj):
        if not WindowActionContainer.isOtherActionFinished(windowObj):
            return
        
        windowObj.ShowPortWindowItem.setEnabled(False)
        windowObj.controlCenter.forcedLock(windowObj.portWindow)
        windowObj.portWindow.show()

    @staticmethod
    def portSetAction(windowObj):
        if not WindowActionContainer.isOtherActionFinished(windowObj):
            return
        
        windowObj.portSetObj = PortSet(windowObj, windowObj.portNum, windowObj.portBaudrate)
        windowObj.portSetObj.show()
        if windowObj.portSetObj.exec_():
            windowObj.portNum, windowObj.portBaudrate = windowObj.portSetObj.result()
            windowObj.logWindow.infoLog("Set ok: num[ %d ], baudrate[ %d ]" %(windowObj.portNum+1, windowObj.portBaudrate))
        windowObj.portSetObj = None


    @staticmethod
    def helpAbout(windowObj):
        QMessageBox.about(windowObj, "About %s" %windowObj.__softwareName__,
                    """<b>%s</b> v %s
                    <p>Copyright &copy; 2015 *********.
                    All rights reserved.
                    <p>This application can be used to *****************************.
                    <p>Python %s - Qt %s - PyQt %s on %s""" % (windowObj.__softwareName__,
                    windowObj.__version__, platform.python_version(),
                    QT_VERSION_STR, PYQT_VERSION_STR, platform.system()))


    @staticmethod
    def debugModeAction(windowObj):
        if not WindowActionContainer.isOtherActionFinished(windowObj):
            return
        
        def sendError():
            recordStatus = False
            windowObj.logWindow.errorLog("the device does not answer, check your device status")
            
        def sendFinishFirst():
            windowObj.serialCommand.setCommand(windowObj.debugModeItem, '\x55',
                                               'enter controlled mode',sendFinish,sendError, 2, 'end')


        def sendFinish():
            windowObj.logWindow.infoLog("enter Control mode ok")
            windowObj.emit(SIGNAL("deviceStatus(int)"),__isCotrolledModeWaiting__)
                
        windowObj.serialCommand.setCommand(windowObj.debugModeItem, '\xAA',
                                           'try controlled mode', sendFinishFirst,sendError, 20, 'start')
 
        

            
    @staticmethod
    def workingModeAction(windowObj):
        if not WindowActionContainer.isOtherActionFinished(windowObj):
            return
        
        def sendError():
            windowObj.logWindow.errorLog("the device does not answer, check your device status")
            
        def sendFinish():
            windowObj.logWindow.infoLog("enter working mode ok")
            windowObj.emit(SIGNAL("deviceStatus(int)"),__isWorkingMode__)

                
        windowObj.serialCommand.setCommand(windowObj.workingModeItem, '\xAA',
                                           'Copyright (C) 2014 IBM Corp. All Rights Reserved', sendFinish, sendError, 20)  



    @staticmethod
    def startCollectDataAction(windowObj, theSource=__othersNum__):
        if not WindowActionContainer.isOtherActionFinished(windowObj):
            return
        
        #windowObj.StartCollectDataItem.setEnabled(False)
        def sendError():
            windowObj.logWindow.errorLog("the device does not answer, make sure it is in control mode")
            #windowObj.dataStreamWindow.close()
            
        def sendFinish():
            windowObj.logWindow.infoLog("Start collect data now")
            windowObj.emit(SIGNAL("collectFinished(int)"),theSource)
            #windowObj._signal_2.emit(theSource)
            

        windowObj.serialCommand.setCommand(windowObj.StartCollectDataItem, 'getRawData\n\r', 'getRawData started',
                                             sendFinish, sendError, 1)


    @staticmethod
    def stopCollectDataAction(windowObj):
        if not WindowActionContainer.isOtherActionFinished(windowObj):
            return
        
        def sendError():
            windowObj.logWindow.errorLog("the device does not answer, make sure it is collecting data")
            
        def sendFinish():
            windowObj.logWindow.infoLog("Stop collect data OK")


        windowObj.serialCommand.setCommand(windowObj.StopCollectDataItem, '\x5A',
                                           'getRawData stopped', sendFinish, sendError, 1)
 


    @staticmethod
    def statisticsAction(windowObj):
        if not WindowActionContainer.isOtherActionFinished(windowObj):
            return

        windowObj.logWindow.infoLog("Prepare to show the statistics window")
        
        def showStatisticsWin():
            windowObj.StatisticsItem.setEnabled(False)
            windowObj.realtimeWindow.show()
            windowObj.realtimeWindow.dataStreamGraph.show()

        def sendError():
            windowObj.emit(SIGNAL("doAutoCollect(int)"),__statisticsNum__)
            #windowObj._signal_1.emit(__statisticsNum__)
            
        def sendFinish():
            #WindowActionContainer.showStatisticsWin(windowObj)
            windowObj.emit(SIGNAL("collectFinished(int)"),__statisticsNum__)
            
        windowObj.serialCommand.setCommand(windowObj.StatisticsItem, '', __messageHeader__,
                                             sendFinish, sendError, 1)
         

    @staticmethod
    def calibrationAction(windowObj):
        if not WindowActionContainer.isOtherActionFinished(windowObj):
            return
        
        windowObj.logWindow.infoLog("Prepare to show the calibration window")
        
        def showCalibrationWin():
            windowObj.CalibrationItem.setEnabled(False)
            windowObj.dataStreamWindow.show()
            windowObj.dataStreamWindow.dataStreamGraph.show()
            windowObj.dataStreamWindow.dataProbabilityGraph.show()        

        def sendError():
            windowObj.emit(SIGNAL("doAutoCollect(int)"),__calibarationNum__)
            #windowObj._signal_1.emit(__calibarationNum__)
            
        def sendFinish():
            #WindowActionContainer.showCalibrationWin(windowObj)
            windowObj.emit(SIGNAL("collectFinished(int)"),__calibarationNum__)
            
        windowObj.serialCommand.setCommand(windowObj.CalibrationItem, '', __messageHeader__,
                                             sendFinish, sendError, 1)


    @staticmethod
    def showCalibrationWin(windowObj):
        windowObj.CalibrationItem.setEnabled(False)
        windowObj.dataStreamWindow.show()
        windowObj.dataStreamWindow.dataStreamGraph.show()
        windowObj.dataStreamWindow.dataProbabilityGraph.show()

    @staticmethod
    def showStatisticsWin(windowObj):
        windowObj.StatisticsItem.setEnabled(False)
        windowObj.realtimeWindow.show()
        windowObj.realtimeWindow.dataStreamGraph.show()

    @staticmethod
    def collectSchedule(windowObj, theSource):
        while not WindowActionContainer.isOtherActionFinished(windowObj, False):
            pass

        WindowActionContainer.startCollectDataAction(windowObj, theSource)

    @staticmethod
    def collectActionFinished(windowObj, theSource):
       # while not WindowActionContainer.isOtherActionFinished(windowObj):
       #     print 'Not OVer'

        if __calibarationNum__ == theSource:
            WindowActionContainer.showCalibrationWin(windowObj)
        elif __statisticsNum__ == theSource:
            WindowActionContainer.showStatisticsWin(windowObj)



    @staticmethod
    def queryCollecting(windowObj):
        if not WindowActionContainer.isOtherActionFinished(windowObj):
            return
        
        def sendError():
            windowObj.emit(SIGNAL("deviceStatus(int)"),__isNotSure__)
            
        def sendFinish():
            windowObj.emit(SIGNAL("deviceStatus(int)"),__isCollectingData__)
                
        windowObj.serialCommand.setCommand(None, "queryState\n\r", __messageHeader__,
                                             sendFinish, sendError, 1)
    @staticmethod
    def queryControlledWaiting(windowObj):
        while not WindowActionContainer.isOtherActionFinished(windowObj, False):
            pass
        
        def sendError():
            windowObj.emit(SIGNAL("deviceStatus(int)"),__isWorkingMode__)
            
        def sendFinish():
            windowObj.emit(SIGNAL("deviceStatus(int)"),__isCotrolledModeWaiting__) 
                
        windowObj.serialCommand.setCommand(None, "queryState\n\r", "controlled",
                                             sendFinish, sendError, 1)

    @staticmethod
    def decodeTheStatus(theCoding):
        if __isNotSure__ == theCoding:
            return False, "Device Status: Not Sure"
        elif __isCollectingData__ == theCoding:
            return True, "Device Status: is Collecting Data"
        elif __isWorkingMode__ == theCoding:
            return True, "Device Status: is in Working Mode if the serial port has connected to it"
        elif __isCotrolledModeWaiting__ == theCoding:
            return True, "Device Status: is in Control Mode and waiting command"
    
        
    @staticmethod
    def setServer(windowObj, ipstr, portNum):
        if not WindowActionContainer.isOtherActionFinished(windowObj):
            return       

        def sendError():
            windowObj.logWindow.errorLog("server set failed")
            
        def sendFinish():
            windowObj.logWindow.infoLog("server set OK: "+ipstr+" "+str(portNum))
            
        windowObj.serialCommand.setCommand(None, 'serverParaSet'+' ' + ipstr +' '+str(portNum)+"\n\r", "Server Para",
                                             sendFinish, sendError, 1)        


    @staticmethod
    def showServer(windowObj):
        if not WindowActionContainer.isOtherActionFinished(windowObj):
            return       

        def sendError():
            windowObj.logWindow.errorLog("Server info query failed, make sure it is in control mode")
            windowObj.emit(SIGNAL("SERVER INFO"))
            
        def sendFinish():
            #windowObj.logWindow.errorLog("server set OK")
            windowObj.emit(SIGNAL("SERVER INFO"))
            #print windowObj.serialCommand.getRecaivedMessage()
            
        windowObj.serialCommand.setCommand(None, 'serverParaShow\n\r', "!!", sendFinish, sendError, 1) 



