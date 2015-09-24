from PyQt4.QtCore import *
from PyQt4.QtGui import *
from dataStreamWindow_ui import *
from ADCDataProcess import *
from ADCdataParaSetDlg import *
from dataStreamWindowStatistics import *
import numpy as np


__ProbabilityTitle__='Peak Probability Graph'
__StreamTitle__='Filtered Data Graph'


class AdcDataStream(QDialog, Ui_statisticsDialog):
    def __init__(self, associatedBar, MainWindow, controlCenter, logWindow):
        super(AdcDataStream, self).__init__(MainWindow)
        self.setupUi(self)
        self.continueButton.clicked.connect(self.continueShow)
        self.pauseButton.clicked.connect(self.applyPauseShow)
        self.setButton.clicked.connect(self.setPara)
        self.statisticsButton.clicked.connect(self.statisticsShow)
        #self.graphButton.clicked.connect(self.graphShow)

        self.dataBuff = ''
        self.rightData=[]
        self.controlCenter = controlCenter
        self.logWindow = logWindow
        self.associatedBar = associatedBar
        self.dataThread = DataProcess()
        #self.collectCounts = 0
        self.dacDataParaSetDlg = ADCdataParaSetDlg(self)
               
        #self.dataThread = ShowThread(self.dataStreamGraph)       
        MainWindow.addSysbroadcastSignalObj(self)
        
        self.setAutoFillBackground(False)
        palette=QPalette()
        #palette.setBrush(QPalette.Background, QBrush(QPixmap(':/subBackground.png')))
        palette.setBrush(QPalette.Background, QColor(191,0,191))
        self.setPalette(palette)

        self.connect(self, SIGNAL("dataReady"), self.dealDataReadySignal)
        self.connect(self, SIGNAL("VALUE SETTED"), self.dealSettingSignal)
        self.connect(self, SIGNAL("refresh Statistics"), self.refreshStatisticsData)
        #self.isDislayedOver = True
        self.dataStreamGraph_Xlen = 1000
                     
        self.showPauseApplyed = False

        self.dataStreamGraph.initAxisValue(0, 0, 1000, 4096)
        self.dataProbabilityGraph.initAxisValue(0, 0, 4096, 1)
        self.refreshAtrributes()

        self.graphStatistics=DataStreamGraphStatistics(self)

        self.continueButton.setText("Start")
        self.setButton.setText("Settings")
        self.pauseButton.setText("Stop")


    def getData(self, data):            
        if self.dataBuff == '' :
            index = data.find(self.dataThread.blockHeader )
            if index == 0 :
                self.dataBuff = data
            elif index == -1 :
                self.controlCenter.delayTime()
                self.controlCenter.clearPort('in')
            else:
                self.dataBuff = data[index:]           
        else:
            self.dataBuff += data

        #print len(self.dataBuff)
 
        if len(self.dataBuff) >= self.dataThread.blockLen*self.dataThread.blockNum :

            if self.isApplyedPauseShow() or self.dataThread.isReachedCount():
                self.pauseShow()
                return None                
            #self.collectCounts = self.collectCounts + 1 if self.collectCounts < 0xffff else 1
            #self.autoPauseCollectData() # stop recaive data ,the process needed time may longer than this function be called again
            try:
                theProcessedDataList =[]            
                if self.processCollectedData(theProcessedDataList) is not None :
                    self.saveProcessedData(theProcessedDataList)
                    if self.dataThread.needRefreshGraph():
                        #self.saveProcessedData(theProcessedDataList)
                        self.emit(SIGNAL("dataReady"))
                        #return (self.refreshSeconds*1000) #sleep self.refreshSeconds
                    else:
                        self.emit(SIGNAL("refresh Statistics"))
                else:
                    #self.autoContinueCollectData()
                    self.controlCenter.clearPort('in')
            except Exception, e:
                print e
                self.controlCenter.clearPort('in')
            finally:
                self.dataBuff =''
                
        return None
        

        
    def saveProcessedData(self, theList):
        while self.rightData != []:
            self.controlCenter.delayTime()          
        self.rightData = theList

    def refreshStatisticsData(self):
        if len(self.rightData[2])> 0:
            probalilityList = [data[1] for data in self.rightData[2]]
            maxProbalility = max(probalilityList)
            theMaxProbalility = self.rightData[2][probalilityList.index(maxProbalility)]
            #print   theMaxProbalility       
            maxShowLine = 15
            self.rightData[2] = self.rightData[2] if len(self.rightData[2])<maxShowLine else (self.rightData[2])[:maxShowLine]
            attributeList=[np.mean(self.rightData[0]), max(self.rightData[0]), min(self.rightData[0]),
                                   (self.rightData[2])[0][0],(self.rightData[2])[-1][0], theMaxProbalility,
                           (self.rightData[2])]
        else:
            attributeList=[np.mean(self.rightData[0]), max(self.rightData[0]), min(self.rightData[0]),
                                   0, 0, None , None]
            
        self.graphStatistics.setAttributes(attributeList)
        self.collectPoints_label.setText("%d" %self.dataThread.getCurrentCounts())
        self.rightData = []
        
    def processCollectedData(self, theList):
        try:
            processedData, probabilityDataValue, probabilityData = self.dataThread.generateDisplayData(self.dataBuff)
            if processedData is not None:
                theList.append(processedData)
                theList.append(probabilityDataValue)
                theList.append(probabilityData)
                return theList
            else:
                return None
        except Exception, e:
            print e 
            return None

                
    def setPortPara(self, portObj):
        portObj.set_readDataLen(self.dataThread.blockLen)


    def dealDataReadySignal(self):
        self.disPlayData()
        self.rightData=[]
        #self.autoContinueCollectData()
        

    def dealSettingSignal(self):
        self.refreshAtrributes()       
        #self.autoContinueCollectData()

        if not self.continueButton.isEnabled(): #restore previous status
            self.autoContinueCollectData()
       

    def disPlayData(self):
        #self.collectPoints_label.setText("%d" %self.dataThread.getCurrentCounts())
        #get new Figure
        self.dataStreamGraph.addAxes(__StreamTitle__)       
        displayXdata = range(1, self.dataStreamGraph_Xlen+1)
        #self.dataStreamGraph.getAxDot(displayXdata,[0]*self.dataStreamGraph_Xlen, 'red')
               
        # only show the first self.dataStreamGraph_Xlen points
        #displayXdata = range(1,len(self.rightData[0])+1)
        displayYdata = (self.rightData[0])[:self.dataStreamGraph_Xlen]
        self.dataStreamGraph.plot(displayXdata, displayYdata, 'red')


        if len(self.rightData[1]) > 0:
            displayXdata = []
            displayYdata = []
            for data in self.rightData[1]:
                displayXdata.append(data[1])
                displayYdata.append(data[0])       
            self.dataStreamGraph.scatter(displayXdata, displayYdata, 'blue',60)
 
        

        if len(self.rightData[2] )>0:
            displayXdata = []
            displayYdata = []
            #print self.rightData[2]
            for data in self.rightData[2]:
                displayXdata.append(data[0])
                displayYdata.append(data[1])
            self.dataProbabilityGraph.addAxes(__ProbabilityTitle__)
            #self.dataProbabilityGraph.scatter(displayXdata, displayYdata, 'yellow', 15)
            self.dataProbabilityGraph.bar(displayXdata, displayYdata)

        self.dataStreamGraph.showNewGraph()
        self.dataProbabilityGraph.showNewGraph()
        print 'oo'
        #release the buffer to start recaive data again
        #self.rightData = []
        #self.dataBuff =''
        
    def className(self):
        return 'Calibration Window'

    def dealPortSignal(self, signalstr, portNum):
        if 'disconn' in signalstr :
            self.setWindowTitle('Disconnected!!!')
        else:
            self.setWindowTitle('Connected at port %d' %portNum)

    def continueShow(self):
        self.dataThread.restartCalculateProbablility()
        self.dataBuff =''
        self.continueButton.setEnabled(False)
        self.controlCenter.forcedLock(self)
        self.controlCenter.clearPort('in')

    def applyPauseShow(self):
        self.showPauseApplyed = True

    def isApplyedPauseShow(self):
        if self.showPauseApplyed:
            self.showPauseApplyed = False
            return True
        else:
            return False
        
    def pauseShow(self):
        self.controlCenter.unlockSerialPort(self)
        self.continueButton.setEnabled(True)
        

    def autoPauseCollectData(self):
        self.controlCenter.unlockSerialPort(self)

    def autoContinueCollectData(self):
        self.dataThread.restartCalculateProbablility()
        self.dataBuff =''
        self.controlCenter.forcedLock(self)
        self.controlCenter.clearPort('in')
    
    def setPara(self):
        #self.controlCenter.unlockSerialPort(self) # pause collecting data for setting
        self.autoPauseCollectData()
        self.setButton.setEnabled(False)
        self.dacDataParaSetDlg.show()
        pass


    def statisticsShow(self):
        self.graphStatistics.show()



    def closeEvent(self, event):
        self.associatedBar.setEnabled(True)
        #Ui_statisticsDialog.closeEvent(self, event)
        self.pauseShow()
        self.dataStreamGraph.axisParaWin.close()
        self.dataProbabilityGraph.axisParaWin.close()
        self.graphStatistics.close()
        QDialog.closeEvent(self, event)



    def refreshAtrributes(self):

        peaksParaList=[self.dacDataParaSetDlg.minPeakInterval,
                                     self.dacDataParaSetDlg.smoothWidth, self.dacDataParaSetDlg.peakGroup,
                                     self.dacDataParaSetDlg.slopeThread, self.dacDataParaSetDlg.ampThreshold,
                                     None, self.dacDataParaSetDlg.integralInteval, self.dataProbabilityGraph.axisParaWin.getYstart(),
                       self.dataProbabilityGraph.axisParaWin.getYend()]
        
        self.dataThread.setAttribute(self.dacDataParaSetDlg.collectPoints, peaksParaList)


    def saveSetPara(self, theSetting):
        self.dacDataParaSetDlg.saveAttributes(theSetting)
        
        
        

    
