# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serverPortSet.ui'
#
# Created: Wed May 06 19:04:23 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_severSetDialog(object):
    def setupUi(self, severSetDialog):
        severSetDialog.setObjectName(_fromUtf8("severSetDialog"))
        severSetDialog.resize(327, 130)
        severSetDialog.setMinimumSize(QtCore.QSize(327, 130))
        severSetDialog.setMaximumSize(QtCore.QSize(327, 130))
        self.widget = QtGui.QWidget(severSetDialog)
        self.widget.setGeometry(QtCore.QRect(10, 11, 301, 111))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(80, 0))
        self.label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.ip_lineEdit_1 = QtGui.QLineEdit(self.widget)
        self.ip_lineEdit_1.setMinimumSize(QtCore.QSize(40, 0))
        self.ip_lineEdit_1.setMaximumSize(QtCore.QSize(40, 16777215))
        self.ip_lineEdit_1.setObjectName(_fromUtf8("ip_lineEdit_1"))
        self.horizontalLayout.addWidget(self.ip_lineEdit_1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(5, 0))
        self.label_2.setMaximumSize(QtCore.QSize(5, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.ip_lineEdit_2 = QtGui.QLineEdit(self.widget)
        self.ip_lineEdit_2.setMinimumSize(QtCore.QSize(40, 0))
        self.ip_lineEdit_2.setMaximumSize(QtCore.QSize(40, 16777215))
        self.ip_lineEdit_2.setObjectName(_fromUtf8("ip_lineEdit_2"))
        self.horizontalLayout.addWidget(self.ip_lineEdit_2)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(5, 0))
        self.label_3.setMaximumSize(QtCore.QSize(5, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.ip_lineEdit_3 = QtGui.QLineEdit(self.widget)
        self.ip_lineEdit_3.setMinimumSize(QtCore.QSize(40, 0))
        self.ip_lineEdit_3.setMaximumSize(QtCore.QSize(40, 16777215))
        self.ip_lineEdit_3.setObjectName(_fromUtf8("ip_lineEdit_3"))
        self.horizontalLayout.addWidget(self.ip_lineEdit_3)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(5, 0))
        self.label_4.setMaximumSize(QtCore.QSize(5, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.ip_lineEdit_4 = QtGui.QLineEdit(self.widget)
        self.ip_lineEdit_4.setMinimumSize(QtCore.QSize(40, 0))
        self.ip_lineEdit_4.setMaximumSize(QtCore.QSize(40, 16777215))
        self.ip_lineEdit_4.setObjectName(_fromUtf8("ip_lineEdit_4"))
        self.horizontalLayout.addWidget(self.ip_lineEdit_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setMinimumSize(QtCore.QSize(80, 0))
        self.label_5.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        self.port_spinBox = QtGui.QSpinBox(self.widget)
        self.port_spinBox.setMinimumSize(QtCore.QSize(80, 0))
        self.port_spinBox.setMaximum(99999)
        self.port_spinBox.setObjectName(_fromUtf8("port_spinBox"))
        self.horizontalLayout_2.addWidget(self.port_spinBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.okButton = QtGui.QPushButton(self.widget)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.horizontalLayout_3.addWidget(self.okButton)
        self.cancelButton = QtGui.QPushButton(self.widget)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout_3.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(severSetDialog)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), severSetDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(severSetDialog)
        severSetDialog.setTabOrder(self.ip_lineEdit_1, self.ip_lineEdit_2)
        severSetDialog.setTabOrder(self.ip_lineEdit_2, self.ip_lineEdit_3)
        severSetDialog.setTabOrder(self.ip_lineEdit_3, self.ip_lineEdit_4)
        severSetDialog.setTabOrder(self.ip_lineEdit_4, self.port_spinBox)
        severSetDialog.setTabOrder(self.port_spinBox, self.okButton)
        severSetDialog.setTabOrder(self.okButton, self.cancelButton)

    def retranslateUi(self, severSetDialog):
        severSetDialog.setWindowTitle(_translate("severSetDialog", "Server Setting", None))
        self.label.setText(_translate("severSetDialog", "Server IP:", None))
        self.label_2.setText(_translate("severSetDialog", ".", None))
        self.label_3.setText(_translate("severSetDialog", ".", None))
        self.label_4.setText(_translate("severSetDialog", ".", None))
        self.label_5.setText(_translate("severSetDialog", "Server Port:", None))
        self.okButton.setText(_translate("severSetDialog", "OK", None))
        self.cancelButton.setText(_translate("severSetDialog", "Cancel", None))






from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ServerSettingWin(QDialog, Ui_severSetDialog):
    def __init__(self,logWin, parentWin):
        super(ServerSettingWin, self).__init__(parentWin)
        self.setupUi(self)
        self.okButton.clicked.connect(self.okButtionclicked)
        #self.parentWin.connect(self.parentWin)
        self.setAttributes("192.168.1.1",8080)
        self.loWin=logWin
        self.mainWin = parentWin
        

    def setAttributes(self, ipStr, portNum):
        self.serverIP = ipStr
        self.portNum = portNum

    def getAttributes(self):
        return self.serverIP, self.portNum


    def okButtionclicked(self):
        getServerIP = str(self.ip_lineEdit_1.text())+ "."+str(self.ip_lineEdit_2.text())\
                 +"."+str(self.ip_lineEdit_3.text())+"."+str(self.ip_lineEdit_4.text())

        getServerIP.replace(" ", "")
        ipCheckList = getServerIP.split(".")
        for value in ipCheckList:
            if not value.isdigit():
                self.loWin.errorLog("the imput IP format is illegal")
                self.close()
                return
        self.serverIP = getServerIP
        self.portNum = self.port_spinBox.value()
        self.close()
        self.mainWin.emit(SIGNAL("SERVER SET"))


    def setShowText(self):
        ipStrList=self.serverIP.split(".")
        self.ip_lineEdit_1.setText(ipStrList[0])
        self.ip_lineEdit_2.setText(ipStrList[1])
        self.ip_lineEdit_3.setText(ipStrList[2])
        self.ip_lineEdit_4.setText(ipStrList[3])
        self.port_spinBox.setValue(self.portNum)
        
        
        
        
        
        


