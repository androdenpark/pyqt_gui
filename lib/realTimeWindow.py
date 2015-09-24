from PyQt4.QtCore import *
from PyQt4.QtGui import *
from realTimeWindow_ui import *
from ADCDataProcess import *
#from ADCdataParaSetDlg import *
from realTimeWindow_setPara import *
import numpy as np



__GraphTitle__=''


class RealTimeDisplayWindow(QDialog, Ui_realTimeGraph):
    def __init__(self, associatedBar, MainWindow, controlCenter, logWindow):
        super(RealTimeDisplayWindow, self).__init__(MainWindow)
        self.setupUi(self)
        self.startButton.clicked.connect(self.actionSchechdul)
        self.setButton.clicked.connect(self.applySetPara)

        self.dataBuff = ''
        self.rightData=[]
        self.controlCenter = controlCenter
        self.logWindow = logWindow
        self.associatedBar = associatedBar
        self.dataThread = DataProcess()
        self.dataCalculateObj = StatisticDataCaculate()
        self.showLoadedSetValue()
        
        MainWindow.addSysbroadcastSignalObj(self)
        
        self.setAutoFillBackground(False)
        palette=QPalette()
        palette.setBrush(QPalette.Background, QColor(191,0,191))
        self.setPalette(palette)

        self.connect(self, SIGNAL("dataReady"), self.dealDataReadySignal)

        self.dataStreamGraph_Xlen = 1000

        self.dataStreamGraph.initAxisValue(0, 0, 1000, 4096)
        
        self.settingActionHappened =False


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

        #print len(self.dataBuff),'uu'
 
        if len(self.dataBuff) >= self.dataThread.blockLen*self.dataThread.blockNum :
            if self.isApplyedSetting():
                self.setPara()

            #when reach the setCounts ,stop the statistics running
            if self.dataCalculateObj.isQuantityReached():
                #self.pauseShow()
                pass
            
            try:
                processedData = self.processCollectedData()
                if processedData is not None and self.dataCalculateObj.needShowGraph():
                    self.saveProcessedData(processedData)
                    #print 'ww'
                    self.emit(SIGNAL("dataReady"))
                elif processedData is None:
                    self.controlCenter.clearPort('in')
                    #return (self.refreshSeconds*1000) #sleep self.refreshSeconds
            except Exception, e:
                print e
                self.controlCenter.clearPort('in')
            finally:
                self.dataBuff =''

        return None
        

    def processCollectedData(self):
        try:
            processedData = self.dataThread.processData(self.dataBuff)

            if processedData is not None:
                meanValue = self.dataThread.getMean(processedData)
                varVaule = self.dataThread.getVar(processedData)
                self.dataCalculateObj.processIncomeData(meanValue, varVaule)
                self.refreshStatisticsData()
                                  
                #self.rightData = processedData
                #self.rightData.append(processedData)
                #self.rightData.append(meanValue)
                #self.rightData.append(varVaule)
                return processedData
            else:
                return None
        except Exception, e:
            print e 
            return None

    def saveProcessedData(self, theData):
        while( self.rightData != []):
            self.controlCenter.delayTime()
            
        self.rightData = theData
        

    def refreshStatisticsData(self):
        displayList=self.dataCalculateObj.getDisplayData()

        self.DcoffsetCurrent_label.setText('%.2f' %displayList[0])
        self.DcoffsetTotol_label.setText(('%.2f' %(100*displayList[1]))+"%")

        self.varianceCurrent_label.setText('%.2f' %displayList[2])
        self.varianceTotol_label.setText(('%.2f' %(100*displayList[3]))+"%")

        self.quantityTotol_label.setText('%d' %displayList[4])       

    def setPortPara(self, portObj):
        portObj.set_readDataLen(self.dataThread.blockLen)


    def dealDataReadySignal(self):
        self.disPlayData()
        self.rightData=[]

    def disPlayData(self):              
        # only show the first self.dataStreamGraph_Xlen points
        #displayXdata = range(1,len(self.rightData[0])+1)
        self.dataStreamGraph.addAxes(__GraphTitle__)
        displayXdata = range(1, self.dataStreamGraph_Xlen+1)
        displayYdata = self.rightData[:self.dataStreamGraph_Xlen] 
        self.dataStreamGraph.plot(displayXdata, displayYdata, 'red')        
        self.dataStreamGraph.showNewGraph()

        
    def className(self):
        return 'Statistics Window'

    def dealPortSignal(self, signalstr, portNum):
        if 'disconn' in signalstr :
            self.setWindowTitle('Disconnected!!!')
        else:
            self.setWindowTitle('Connected at port %d' %portNum)

    def continueShow(self):
        self.dataBuff =''
        self.dataCalculateObj.resetInternalAttributes()
        self.startButton.setText("Stop")
        #self.startButton.setEnabled(False)
        self.controlCenter.forcedLock(self)
        self.controlCenter.clearPort('in')
        


    def pauseShow(self):
        self.controlCenter.unlockSerialPort(self)
        #self.startButton.setEnabled(True)
        self.startButton.setText("Start")
        

    def actionSchechdul(self):
        if 'Start' in self.startButton.text():            
            self.continueShow()
        else:           
            self.pauseShow()


    def applySetPara(self):
        self.settingActionHappened=True

    def isApplyedSetting(self):
        if self.settingActionHappened:
            self.settingActionHappened = False
            return True
        else:
            return False
    
    def setPara(self):       
        paraList=[]
        paraList.append(self.Dcoffset_U_spinBox.value())
        paraList.append(self.Dcoffset_L_pinBox.value())
        paraList.append(self.variance_U_spinBox.value())
        paraList.append(self.variance_L_SpinBox.value())
        paraList.append(self.quantity_spinBox.value())      
        self.dataCalculateObj.setAttributes(paraList)

    def showLoadedSetValue(self):
        theList = self.dataCalculateObj.getAtrributes()
        self.Dcoffset_U_spinBox.setValue(theList[0])
        self.Dcoffset_L_pinBox.setValue(theList[1])
        self.variance_U_spinBox.setValue(theList[2])
        self.variance_L_SpinBox.setValue(theList[3])
        self.quantity_spinBox.setValue(theList[4])
        
        

    def closeEvent(self, event):
        self.associatedBar.setEnabled(True)
        #Ui_statisticsDialog.closeEvent(self, event)
        self.pauseShow()
        self.dataStreamGraph.axisParaWin.close()
        QDialog.closeEvent(self, event)


    def saveSetPara(self,theSettings):
        self.dataCalculateObj.saveAttributes(theSettings)




        
        
        

    
