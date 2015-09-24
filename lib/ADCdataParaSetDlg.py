from  ADCdataParaSet_ui import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class ADCdataParaSetDlg(QDialog, Ui_ADCdataPara):
    def __init__(self, parentWindow):
        super(ADCdataParaSetDlg, self).__init__(parentWindow)
        self.setupUi(self)
        self.ok_Button.clicked.connect(self.okButtonClicked)
        self.help_Button.clicked.connect(self.helpMessage)
        self.setDefault_Button.clicked.connect(self.setDefaultValue)
        if self.isValueSaved():
            self.loadAttributes()
        else:
            self.setDefaultValue()       
        self.parentWindow = parentWindow

    def okButtonClicked(self):
        self.getValue()
        self.close()
        self.parentWindow.emit(SIGNAL("VALUE SETTED"))
        

    def getValue(self):
  
        #self.dataGraph_Ystart = self.data_Y_start_spinBox.value()

        #self.dataGraph_Yend = self.data_Y_end_spinBox.value()

        #self.peakGraph_Xstart = self.peak_X_start_spinBox.value()
        #self.peakGraph_Xend = self.peak_X_end_spinBox.value()
        #self.peakGraph_Ystart = self.peak_Y_start_doubleSpinBox.value()
        #self.peakGraph_Yend = self.peak_Y_end_doubleSpinBox.value()
           
        self.collectPoints = self.collectPoints_spinBox.value()
        
        self.minPeakInterval = self.peakInterval_spinBox.value()
        self.peakGroup = self.peakGroup_spinBox.value()
        self.slopeThread = self.slopeThreshold_spinBox.value()
        self.ampThreshold = self.apmThreshold_spinBox.value()
        self.smoothWidth = self.smoothWidth_spinBox.value()
        self.integralInteval = self.integralInterval_SpinBox.value()
        #self.filterArray = self.filterArray_textInput.text()
        

    def setValue(self):

        #self.data_Y_start_spinBox.setValue(self.dataGraph_Ystart)
        #self.data_Y_end_spinBox.setValue(self.dataGraph_Yend)

        #self.peak_X_start_spinBox.setValue(self.peakGraph_Xstart)
        #self.peak_X_end_spinBox.setValue(self.peakGraph_Xend)
        #self.peak_Y_start_doubleSpinBox.setValue(self.peakGraph_Ystart)
        #self.peak_Y_end_doubleSpinBox.setValue(self.peakGraph_Yend)
                   
        self.collectPoints_spinBox.setValue(self.collectPoints)
                
        self.peakInterval_spinBox.setValue(self.minPeakInterval)
        self.peakGroup_spinBox.setValue(self.peakGroup)
        self.slopeThreshold_spinBox.setValue(self.slopeThread)
        self.apmThreshold_spinBox.setValue(self.ampThreshold)
        self.smoothWidth_spinBox.setValue(self.smoothWidth)
        self.integralInterval_SpinBox.setValue(self.integralInteval)
        #self.filterArray_textInput.text(self.filterArray)


    def saveAttributes(self, theSettings):
        theSettings.setValue("collectPoints", QVariant(self.collectPoints))
        theSettings.setValue("minPeakInterval", QVariant(self.minPeakInterval))
        theSettings.setValue("peakGroup", QVariant(self.peakGroup))
        theSettings.setValue("slopeThread", QVariant(self.slopeThread))
        theSettings.setValue("ampThreshold", QVariant(self.ampThreshold))
        theSettings.setValue("smoothWidth", QVariant(self.smoothWidth))
        theSettings.setValue("integralInteval", QVariant(self.integralInteval))
        

    def loadAttributes(self):
        settings = QSettings()
        self.collectPoints=(settings.value("collectPoints").toInt())[0]
        self.minPeakInterval=(settings.value("minPeakInterval").toInt())[0]     
        self.peakGroup=(settings.value("peakGroup").toInt())[0]
        self.slopeThread=(settings.value("slopeThread").toInt())[0]
        self.ampThreshold=(settings.value("ampThreshold").toInt())[0]
        self.smoothWidth=(settings.value("smoothWidth").toInt())[0]
        self.integralInteval=(settings.value("integralInteval").toDouble())[0]    
        #self.isNotFirstTimeUse=(settings.value("dcOffsetUpperLimit").toDouble())[1]
        self.setValue()


    def isValueSaved(self):
        settings = QSettings()
        return (settings.value("collectPoints").toInt())[1]
    
    def setDefaultValue(self):
       
        #self.dataGraph_Ystart = 0
        #self.dataGraph_Yend = 4096

        #self.peakGraph_Xstart = 0
        #self.peakGraph_Xend = 4096
        #self.peakGraph_Ystart = 0
        #self.peakGraph_Yend = 1
        self.collectPoints = 4        
        self.minPeakInterval = 60
        self.peakGroup = 5
        self.slopeThread = 0
        self.ampThreshold = 850
        self.smoothWidth = 5
        self.integralInteval =3

        self.setValue()
        

    def helpMessage(self):
        print 'help button is not used in current version'


    def closeEvent(self, event):
        self.parentWindow.setButton.setEnabled(True)
        #Ui_ADCdataPara.closeEvent(self, event)
        QDialog.closeEvent(self, event)
        self.parentWindow.emit(SIGNAL("VALUE SETTED"))

    
        
        
