# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serialPort.ui'
#
# Created: Fri Mar 27 19:55:58 2015
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

class Ui_serialPortDlg(object):
    def setupUi(self, serialPortDlg):
        serialPortDlg.setObjectName(_fromUtf8("serialPortDlg"))
        serialPortDlg.resize(775, 338)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(serialPortDlg.sizePolicy().hasHeightForWidth())
        serialPortDlg.setSizePolicy(sizePolicy)
        serialPortDlg.setMinimumSize(QtCore.QSize(775, 338))
        serialPortDlg.setMaximumSize(QtCore.QSize(775, 338))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        serialPortDlg.setFont(font)
        self.widget = QtGui.QWidget(serialPortDlg)
        self.widget.setGeometry(QtCore.QRect(12, 11, 641, 314))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.portInfoDisplay = QtGui.QTextBrowser(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portInfoDisplay.sizePolicy().hasHeightForWidth())
        self.portInfoDisplay.setSizePolicy(sizePolicy)
        self.portInfoDisplay.setMinimumSize(QtCore.QSize(639, 262))
        self.portInfoDisplay.setMaximumSize(QtCore.QSize(640, 263))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.portInfoDisplay.setFont(font)
        self.portInfoDisplay.setObjectName(_fromUtf8("portInfoDisplay"))
        self.verticalLayout.addWidget(self.portInfoDisplay)
        self.label = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(100, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        #self.portCommandBox = QtGui.QComboBox(self.widget)
        self.portCommandBox = ComboBoxCustom(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portCommandBox.sizePolicy().hasHeightForWidth())
        self.portCommandBox.setSizePolicy(sizePolicy)
        self.portCommandBox.setMinimumSize(QtCore.QSize(639, 23))
        self.portCommandBox.setMaximumSize(QtCore.QSize(639, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.portCommandBox.setFont(font)
        self.portCommandBox.setEditable(True)
        self.portCommandBox.setObjectName(_fromUtf8("portCommandBox"))
        self.verticalLayout.addWidget(self.portCommandBox)
        self.recordScreenButton = QtGui.QPushButton(serialPortDlg)
        self.recordScreenButton.setGeometry(QtCore.QRect(660, 41, 80, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recordScreenButton.sizePolicy().hasHeightForWidth())
        self.recordScreenButton.setSizePolicy(sizePolicy)
        self.recordScreenButton.setMinimumSize(QtCore.QSize(80, 23))
        self.recordScreenButton.setMaximumSize(QtCore.QSize(80, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.recordScreenButton.setFont(font)
        self.recordScreenButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.recordScreenButton.setObjectName(_fromUtf8("recordScreenButton"))
        self.portFormatBox = QtGui.QComboBox(serialPortDlg)
        self.portFormatBox.setGeometry(QtCore.QRect(660, 300, 80, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portFormatBox.sizePolicy().hasHeightForWidth())
        self.portFormatBox.setSizePolicy(sizePolicy)
        self.portFormatBox.setMinimumSize(QtCore.QSize(80, 23))
        self.portFormatBox.setMaximumSize(QtCore.QSize(80, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.portFormatBox.setFont(font)
        self.portFormatBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.portFormatBox.setObjectName(_fromUtf8("portFormatBox"))
        self.clearScreenButton = QtGui.QPushButton(serialPortDlg)
        self.clearScreenButton.setEnabled(True)
        self.clearScreenButton.setGeometry(QtCore.QRect(660, 12, 80, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearScreenButton.sizePolicy().hasHeightForWidth())
        self.clearScreenButton.setSizePolicy(sizePolicy)
        self.clearScreenButton.setMinimumSize(QtCore.QSize(80, 23))
        self.clearScreenButton.setMaximumSize(QtCore.QSize(80, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.clearScreenButton.setFont(font)
        self.clearScreenButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.clearScreenButton.setObjectName(_fromUtf8("clearScreenButton"))
        self.label.setBuddy(self.portCommandBox)

        self.retranslateUi(serialPortDlg)
        QtCore.QMetaObject.connectSlotsByName(serialPortDlg)
        serialPortDlg.setTabOrder(self.clearScreenButton, self.recordScreenButton)
        serialPortDlg.setTabOrder(self.recordScreenButton, self.portFormatBox)
        serialPortDlg.setTabOrder(self.portFormatBox, self.portCommandBox)
        serialPortDlg.setTabOrder(self.portCommandBox, self.portInfoDisplay)

    def retranslateUi(self, serialPortDlg):
        serialPortDlg.setWindowTitle(_translate("serialPortDlg", "Serial Commuication", None))
        self.label.setText(_translate("serialPortDlg", "Command Line", None))
        self.recordScreenButton.setText(_translate("serialPortDlg", "Start Record", None))
        self.clearScreenButton.setText(_translate("serialPortDlg", "Clear Screen", None))

#####################add by zyy########################################
from PyQt4.QtCore import *
from PyQt4.QtGui import *

enterSignalfromCommand='EnterPressed'

class ComboBoxCustom(QtGui.QComboBox):

    def keyPressEvent(self, event):
        if event.key()==Qt.Key_Enter or event.key()==Qt.Key_Return:
            self.emit(SIGNAL(enterSignalfromCommand))
        else:
            QtGui.QComboBox.keyPressEvent(self, event) 
