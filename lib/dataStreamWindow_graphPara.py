# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'axisSettingWindow.ui'
#
# Created: Tue Apr 28 11:07:25 2015
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

class Ui_axisSetting(object):
    def setupUi(self, axisSetting):
        axisSetting.setObjectName(_fromUtf8("axisSetting"))
        axisSetting.resize(400, 150)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(axisSetting.sizePolicy().hasHeightForWidth())
        axisSetting.setSizePolicy(sizePolicy)
        axisSetting.setMinimumSize(QtCore.QSize(400, 150))
        axisSetting.setMaximumSize(QtCore.QSize(400, 150))
        self.widget = QtGui.QWidget(axisSetting)
        self.widget.setGeometry(QtCore.QRect(20, 20, 361, 111))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.X_start_doubleSpinBox = QtGui.QDoubleSpinBox(self.widget)
        self.X_start_doubleSpinBox.setMaximum(9999.0)
        self.X_start_doubleSpinBox.setObjectName(_fromUtf8("X_start_doubleSpinBox"))
        self.horizontalLayout.addWidget(self.X_start_doubleSpinBox)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.X_end_doubleSpinBox = QtGui.QDoubleSpinBox(self.widget)
        self.X_end_doubleSpinBox.setMaximum(9999.0)
        self.X_end_doubleSpinBox.setObjectName(_fromUtf8("X_end_doubleSpinBox"))
        self.horizontalLayout.addWidget(self.X_end_doubleSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.Y_start_doubleSpinBox = QtGui.QDoubleSpinBox(self.widget)
        self.Y_start_doubleSpinBox.setMaximum(9999.0)
        self.Y_start_doubleSpinBox.setObjectName(_fromUtf8("Y_start_doubleSpinBox"))
        self.horizontalLayout_2.addWidget(self.Y_start_doubleSpinBox)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.Y_end_doubleSpinBox = QtGui.QDoubleSpinBox(self.widget)
        self.Y_end_doubleSpinBox.setMaximum(9999.0)
        self.Y_end_doubleSpinBox.setObjectName(_fromUtf8("Y_end_doubleSpinBox"))
        self.horizontalLayout_2.addWidget(self.Y_end_doubleSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.position_label = QtGui.QLabel(self.widget)
        self.position_label.setObjectName(_fromUtf8("position_label"))
        self.horizontalLayout_3.addWidget(self.position_label)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.okButton = QtGui.QPushButton(self.widget)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.horizontalLayout_4.addWidget(self.okButton)
        self.cancelButton = QtGui.QPushButton(self.widget)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout_4.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.label.setBuddy(self.X_start_doubleSpinBox)
        self.label_3.setBuddy(self.X_end_doubleSpinBox)
        self.label_2.setBuddy(self.Y_start_doubleSpinBox)
        self.label_4.setBuddy(self.Y_end_doubleSpinBox)

        self.retranslateUi(axisSetting)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), axisSetting.reject)
        QtCore.QMetaObject.connectSlotsByName(axisSetting)

    def retranslateUi(self, axisSetting):
        axisSetting.setWindowTitle(_translate("axisSetting", "Axis Setting", None))
        self.label.setText(_translate("axisSetting", "X Axis Start:", None))
        self.label_3.setText(_translate("axisSetting", "X Axis End:", None))
        self.label_2.setText(_translate("axisSetting", "Y Axis Start:", None))
        self.label_4.setText(_translate("axisSetting", "Y Axis End:", None))
        self.label_5.setText(_translate("axisSetting", "Click Position:", None))
        self.position_label.setText(_translate("axisSetting", "X:00,Y:01", None))
        self.okButton.setText(_translate("axisSetting", "OK", None))
        self.cancelButton.setText(_translate("axisSetting", "Cancel", None))



from PyQt4.QtCore import *
from PyQt4.QtGui import *

class AxisSettingWin(QDialog, Ui_axisSetting):
    def __init__(self,parentWin):
        super(AxisSettingWin, self).__init__(parentWin)
        self.setupUi(self)
        self.okButton.clicked.connect(self.okButtionclicked)
        #self.parentWin.connect(self.parentWin)

    def setAttributes(self, xstart, ystart, xend, yend):
        self.xstart =xstart
        self.ystart=ystart
        self.xend = xend
        self.yend = yend
        self.setAxisShowData()

    def getYstart(self):
        return self.ystart

    def getYend(self):
        return self.yend

    def okButtionclicked(self):
        xstart = self.X_start_doubleSpinBox.value()
        ystart = self.Y_start_doubleSpinBox.value()
        xend = self.X_end_doubleSpinBox.value()
        yend = self.Y_end_doubleSpinBox.value()

        if xend > xstart :
            self.xstart = self.X_start_doubleSpinBox.value()
            self.xend = self.X_end_doubleSpinBox.value()
        if yend > ystart :    
            self.ystart=self.Y_start_doubleSpinBox.value()
            self.yend = self.Y_end_doubleSpinBox.value()
        
        self.close()

    def setClickPosition(self, theStr):
        self.position_label.setText(theStr)

    def setAxisShowData(self):
        self.X_start_doubleSpinBox.setValue(self.xstart)
        self.Y_start_doubleSpinBox.setValue(self.ystart)
        self.X_end_doubleSpinBox.setValue(self.xend)
        self.Y_end_doubleSpinBox.setValue(self.yend)
        
        

