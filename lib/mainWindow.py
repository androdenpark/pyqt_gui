from PyQt4.QtCore import *
from PyQt4.QtGui import *

from actionDefination import *
from controlCenter import *
from serialDisplay import *
from logWindow import *
from serialCommand import *
from realTimeWindow import *
from serverSetWin import *

import resources




class MainWindow(QMainWindow):
    def __init__(self,version='0.0', name='PM25', parent=None):
        super(MainWindow, self).__init__(parent)
        self.__version__= version
        self.__softwareName__ = name
        

        
        def setMenu():
            PortSetItem = self.createAction("Set Serial Port", self.portSetAction,"Ctrl+S", "portSet")
            self.WirelessSetItem = self.createAction("Set Remote Server", self.wirelessSetAction,"Ctrl+R", "wirelessSet")
            
            self.debugModeItem = self.createAction("Control Mode", self.debugModeAction,"Ctrl+U", "debug")
            self.workingModeItem = self.createAction("Working Mode", self.workingModeAction,"Ctrl+W", "working")
        
            self.CalibrationItem = self.createAction("Calibration", self.calibrationAction, "Ctrl+F", "calibration")
            self.StatisticsItem = self.createAction("Statistics", self.statisticsAction, "Ctrl+T", "statistics")
            
            self.StartCollectDataItem = self.createAction("Start Collect Data", self.startCollectDataAction, "Ctrl+L", "collectData")
            self.StopCollectDataItem = self.createAction("Stop Collect Data", self.stopCollectDataAction, "Ctrl+D", "disCollectData")

            helpAction=self.createAction("About", self.helpAbout,)

            self.ConnectPortItem = self.createAction("Connect Serial Port", self.connectPortAction,"Ctrl+H","connect")
            self.DisconnectPortItem = self.createAction("Disconnect Serial Port", self.disconnectPortAction,"Ctrl+I", "disconnect")
            self.ShowPortWindowItem = self.createAction("Console Window", self.showPortWindowAction,"Ctrl+O", "showPortWindow")
                       
        
            # 'set' Menu 
            setMenu = self.menuBar().addMenu("&Set")
            self.addActions(setMenu, (PortSetItem, self.WirelessSetItem, None))


            # 'Control' Menu
            controlMenu = self.menuBar().addMenu("&Control")
            self.addActions(controlMenu,(self.ConnectPortItem, self.DisconnectPortItem, self.ShowPortWindowItem))

            modeMenu = controlMenu.addMenu("&Set Mode")
            self.addActions(modeMenu, (self.debugModeItem, self.workingModeItem))

            #'data analysis' menu
            analysisMenu = self.menuBar().addMenu("&Data Analysis")
            self.addActions(analysisMenu, (self.CalibrationItem, self.StatisticsItem , self.StartCollectDataItem, self.StopCollectDataItem))
            
        
            #'help' Menu
            helpMenu = self.menuBar().addMenu("&Help")
            self.addActions(helpMenu,(helpAction, None))


            #Toolbar
            Toolbar = self.addToolBar("Edit")
            Toolbar.setObjectName("ToolBar")
            toolTupleItem=(PortSetItem, self.WirelessSetItem, None, self.ConnectPortItem,  self.DisconnectPortItem,
                           self.ShowPortWindowItem, None,
                           self.debugModeItem,   self.workingModeItem, None, self.CalibrationItem, self.StatisticsItem, None,
                           )
            self.addActions(Toolbar,toolTupleItem)


        def loadInitValue():

            settings = QSettings()
            
            self.portNum = (settings.value("serialPortNum").toInt())[0]
            self.portBaudrate = (settings.value("serialPortBaudrate").toInt())[0]

            if not (settings.value("serialPortBaudrate").toInt())[1] :                
                self.portNum = 0xffff #first time to use this app, show set serialPara window

        def setMianWindow():
            
            #background color
            palette=QPalette()
            palette.setColor(QPalette.Background, QColor(204, 204, 204))
            #palette.setBrush(QPalette.Background, QBrush(QPixmap(':/mainBackground.png')))
            
            self.setPalette(palette)

            #window size
            self.windowWidth=836
            height=542
            self.setFixedSize(self.windowWidth, height)      
            self.setWindowTitle(self.__softwareName__)



                
            #self._signal_1=QtCore.pyqtSignal(int)
            #self._signal_2=QtCore.pyqtSignal(int)
            
            self.connect(self, SIGNAL("portConnected"), self.broadcastConnected)
            self.connect(self, SIGNAL("portDisonnected"), self.broadcastDisconnected)
            self.connect(self, SIGNAL("doAutoCollect(int)"), self.collectSchedule)
            self.connect(self, SIGNAL("collectFinished(int)"), self.collectActionFinished)
            #self.connect(self, QtCore.SIGNAL("self._signal_1(int)"), collectSchedule)
            #self.connect(self, QtCore.SIGNAL("self._signal_2(int)"), collectActionFinished)
            #self._signal_1.connect(collectSchedule)
            #self._signal_2.connect(collectActionFinished)

            self.connect(self, SIGNAL("deviceStatus(int)"), self.decideDeviceStatus)
            #self.connect(self, SIGNAL("IN CONTROL"), self.dealControlSignal)

            self.connect(self, SIGNAL("SERVER SET"), self.setServer)
            self.connect(self, SIGNAL("SERVER INFO"), self.serverInfoCome)
            
            

        def setLogWindow():
            self.imageLabel = QLabel()
            self.setCentralWidget(self.imageLabel)
            
            #log window
            logDockWidget = QDockWidget("", self)
            height=500
            logDockWidget.setFixedSize(self.windowWidth, height)
            palette=QPalette()
            #palette.setColor(QPalette.Background, QColor(192, 253, 123))
            palette.setColor(QPalette.Background, QColor(0, 253, 0, 0))
            logDockWidget.setPalette(palette)
            logDockWidget.setFeatures(QDockWidget.AllDockWidgetFeatures)
        
            self.logDisplayText = QTextEdit()
            palette.setColor(QPalette.Base, QColor(0, 253, 0, 0))
            self.logDisplayText.setPalette(palette)
            '''
            fontColor = QColor(255, 255, 0)
            self.logDisplayText.setTextColor(fontColor)
            self.logDisplayText.setText("log start here")
            '''
            
            
            logDockWidget.setWidget(self.logDisplayText)
            logDockWidget.setAllowedAreas(Qt.BottomDockWidgetArea)
            self.addDockWidget(Qt.BottomDockWidgetArea, logDockWidget)




        
       
        setMenu()
        loadInitValue()        
        setMianWindow()
        setLogWindow()
        self.broRegisteredObjList = []
        self.logWindow = LogWindow(self.logDisplayText)
        
        self.serverSetWin=ServerSettingWin(self.logWindow, self)
        
        self.controlCenter = ControlCenter(self, self.logWindow)
        self.serialCommand = SerialCommand(self, self.logWindow, self.controlCenter)
        self.portWindow = SerialPortWindow(self, self.controlCenter, self.ShowPortWindowItem, self.logWindow)     
        self.controlCenter.lockSerialPort(self.portWindow)     
        
        self.dataStreamWindow=AdcDataStream(self.CalibrationItem, self, self.controlCenter, self.logWindow)
        self.realtimeWindow = RealTimeDisplayWindow(self.StatisticsItem, self, self.controlCenter, self.logWindow)

        self.disableItems()
        self.startupItems(False)
        self.show()
        self.connectPortAction()
          

    def enableItems(self):                   
        self.CalibrationItem.setEnabled(True)
        self.StatisticsItem.setEnabled(True)
        self.WirelessSetItem.setEnabled(True)    
        self.StartCollectDataItem.setEnabled(True)
        self.StopCollectDataItem.setEnabled(True)

    def disableItems(self):
        self.CalibrationItem.setEnabled(False)
        self.StatisticsItem.setEnabled(False)
        self.WirelessSetItem.setEnabled(False)    
        self.StartCollectDataItem.setEnabled(False)
        self.StopCollectDataItem.setEnabled(False)

    def startupItems(self, status):
        #self.WirelessSetItem.setEnabled(status)
        self.debugModeItem.setEnabled(status)
        self.workingModeItem.setEnabled(status)        

        
    def broadcastConnected(self):
        
        self.logWindow.infoLog("connected at Port %d" %(self.portNum+1))
        self.ConnectPortItem.setEnabled(False)
        
        if self.broRegisteredObjList is not None:
            for i, obj in enumerate(self.broRegisteredObjList):
                #print obj.className()
                try:
                    obj.dealPortSignal('connected',(self.portNum+1))
                except Exception,e:
                    del self.broRegisteredObjList[i]
                    print e
                
        self.DisconnectPortItem.setEnabled(True)
        self.queryCurrentDeviceStatus()

    def broadcastDisconnected(self):
        self.logWindow.infoLog( "disconnected at Port %d" %(self.portNum+1))
        self.DisconnectPortItem.setEnabled(False)
       
        if self.broRegisteredObjList is not None:
            for i, obj in enumerate(self.broRegisteredObjList):
                
                try:
                    obj.dealPortSignal('disconnected', (self.portNum+1))
                except Exception,e:
                    del self.broRegisteredObjList[i]
                    print e

        self.ConnectPortItem.setEnabled(True)

    def addSysbroadcastSignalObj(self, obj):
        self.broRegisteredObjList.append(obj)
        

    def createAction(self, text, slot=None, shortcut=None, icon=None,
                     tip=None, checkable=False, signal="triggered()"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon(":/%s.png" %icon))           
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            #action.setToolTip(tip)
            #action.setStatusTip(tip)
            pass
        if slot is not None:
            self.connect(action, SIGNAL(signal), slot)
        if checkable:
            action.setCheckable(True)
        return action

    def addActions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)



    def showPortWindowAction(self):
        WindowActionContainer.showPortWindowAction(self)
                     
    def connectPortAction(self):
        WindowActionContainer.connectPortAction(self)
            
    def disconnectPortAction(self):
        WindowActionContainer.disconnectPortAction(self)

    def portSetAction(self):        
        WindowActionContainer.portSetAction(self)

    def debugModeAction(self):
        WindowActionContainer.debugModeAction(self)

    def workingModeAction(self):
        WindowActionContainer.workingModeAction(self)
        
    def startCollectDataAction(self):
        WindowActionContainer.startCollectDataAction(self)

    def stopCollectDataAction(self):
        WindowActionContainer.stopCollectDataAction(self)

    def helpAbout(self):
        WindowActionContainer.helpAbout(self)


    def calibrationAction(self):        
        WindowActionContainer.calibrationAction(self)
    
    def statisticsAction(self):
        WindowActionContainer.statisticsAction(self)

    def wirelessSetAction(self):
        #self.queryCurrentDeviceStatus()
        WindowActionContainer.showServer(self)
        
    def serverInfoCome(self):
        incomeMessage = self.serialCommand.getRecaivedMessage()
        print incomeMessage
        ipStr="0.0.0.0"
        portNum=0
        
        if "Server Para" in incomeMessage:
            incomeMessage = incomeMessage.split(" ")
            for index, value in enumerate(incomeMessage):
                if "!!" in value:
                    ipStr=incomeMessage[index-2]
                    portNum= int(incomeMessage[index-1])
        
        self.serverSetWin.setAttributes(ipStr, portNum)        
        self.serverSetWin.setShowText()
        self.serverSetWin.show()
        
    
    def collectSchedule(self, theStr):
        WindowActionContainer.collectSchedule(self, theStr)

    def collectActionFinished(self, theStr):
        WindowActionContainer.collectActionFinished(self, theStr)

    def queryCurrentDeviceStatus(self):
        self.logWindow.infoLog("now get the device status")
        WindowActionContainer.queryCollecting(self)
        
    def decideDeviceStatus(self, theCoding):
        theResult, theStr = WindowActionContainer.decodeTheStatus(theCoding)
        if theResult:
            self.logWindow.infoLog(theStr)
            if "Working" in theStr :
                self.disableItems()
            else:
                self.enableItems()
            self.startupItems(True)
        else:
            WindowActionContainer.queryControlledWaiting(self)



    def setServer(self):
        ipstr, portNum=self.serverSetWin.getAttributes()
        WindowActionContainer.setServer(self, ipstr, portNum)
                

    def closeEvent(self, event):
        
        self.stopCollectDataAction()

        #save setted para
        settings = QSettings()
        settings.setValue("serialPortNum", QVariant(self.portNum))
        settings.setValue("serialPortBaudrate", QVariant(self.portBaudrate))

        self.realtimeWindow.saveSetPara(settings)
        self.dataStreamWindow.saveSetPara(settings)
        
        
        #self.stopCollectDataAction()
        try:
            self.realtimeWindow.close()
        except:
            pass
        
        try:
            self.portSetObj.close()
        except:
            pass
        
        try:
            self.portWindow.close()
        except:
            pass

        try:
            self.dataStreamWindow.close()
        except:
            pass
        
        try:
            self.controlCenter.applyDisconnectPort()
        except:             #the self.portSetObj may not be defined before reference
            pass

        try:
            self.serverSetWin.close()
        except:
            pass

                             


        QMainWindow.closeEvent(self, event)




