
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import serial


#class PortSet(QDialog):
class PortSet(QDialog):
    def __init__(self, parent=None, port=0, baudRate=115200, MaxPortNum=30):
        super(PortSet, self).__init__(parent)
        self.port = port
        self.baudRate = baudRate
        self.MaxPortNum = MaxPortNum  #MaxPortNum=30

        self.serialList = self.getSerialList()
        print self.serialList
        self.serialListBox = QComboBox()
        self.serialListBox.setEditable(True)
        self.serialListBox.addItems(sorted(self.serialList.keys()))

        self.baudRateList = ['4800', '9600', '115200']         
        self.baudRateListBox = QComboBox()
        self.baudRateListBox.setEditable(True)
        self.baudRateListBox.addItems(self.baudRateList)

        portLable =QLabel('Port Num')
        portLable.setBuddy(self.serialListBox)
        rateLable =QLabel('Baud Rate')
        rateLable.setBuddy(self.baudRateListBox)
        

        okButton = QPushButton("OK", self)
        cancelButton = QPushButton("Cancel", self)
        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(okButton)
        buttonLayout.addWidget(cancelButton)


        layout = QGridLayout()
        layout.addWidget(portLable, 0, 0)
        layout.addWidget(self.serialListBox, 0, 1)
        layout.addWidget(rateLable, 1, 0)
        layout.addWidget(self.baudRateListBox, 1, 1)
        layout.addLayout(buttonLayout, 2, 0, 1, 3)
        self.setLayout(layout)

        self.connect(okButton, SIGNAL("clicked()"),
                     self, SLOT("accept()"))
               
        self.connect(cancelButton, SIGNAL("clicked()"),
                     self, SLOT("reject()"))

        self.connect(self.serialListBox,
                     SIGNAL("currentIndexChanged(int)"), self._selectPort)
        self.connect(self.baudRateListBox,
                     SIGNAL("currentIndexChanged(int)"), self._baudRate)

        self.updateList()
        self.setWindowTitle("Port Set")
        


    def findExistSerialPort(self, portNum):
        try:
            tempPortObj = None
            tempPortObj =  serial.Serial(portNum)
        except SerialException:
            pass
        finally:
            if tempPortObj is not None:
                tempPortObj.close()
                return serial.device(portNum)
            else:
                return None
                                      
    def getSerialList(self):
        serialList={}
        tryPort=0
        
        while tryPort < self.MaxPortNum :
            portStr = self.findExistSerialPort(tryPort)
            if portStr is not None:
                serialList[portStr]=tryPort
                #print serialList
                #serialList.append(unicode(portStr))
            tryPort += 1
        return serialList



    def _selectPort(self):
        key = unicode(self.serialListBox.currentText())
        if self.serialList.has_key(key):
            self.port = self.serialList[key]
            print key, self.port
            
        
        
        

    def _baudRate(self):
        text = unicode(self.baudRateListBox.currentText())
        self.baudRate = int(text)
        
        
               
    def result(self):     
        return self.port, self.baudRate


    def updateList(self):
        #self.baudRateListBox.setCurrentText(QString(str(self.baudRate)))
        self.baudRateListBox.setEditText(QString(str(self.baudRate)))
        portName = serial.device(self.port)
        if self.serialList.has_key(portName):
            self.serialListBox.setEditText(QString(portName))
        else:
            key = unicode(self.serialListBox.currentText())
            self.port = self.serialList[key]

        
            
        


        
        
        
        
        
        
        
        

        
        
        
        
