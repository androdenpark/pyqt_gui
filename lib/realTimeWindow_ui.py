# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'realTimeWindow_ui.ui'
#
# Created: Wed May 06 10:36:51 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from dataStreamWindow_plot import DataStreamMatplot

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

class Ui_realTimeGraph(object):
    def setupUi(self, realTimeGraph):
        realTimeGraph.setObjectName(_fromUtf8("realTimeGraph"))
        realTimeGraph.resize(772, 320)
        realTimeGraph.setMinimumSize(QtCore.QSize(772, 320))
        realTimeGraph.setMaximumSize(QtCore.QSize(772, 320))
        self.layoutWidget = QtGui.QWidget(realTimeGraph)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 11, 752, 307))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_9.setMargin(0)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.dataStreamGraph = DataStreamMatplot(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataStreamGraph.sizePolicy().hasHeightForWidth())
        self.dataStreamGraph.setSizePolicy(sizePolicy)
        self.dataStreamGraph.setMinimumSize(QtCore.QSize(750, 205))
        self.dataStreamGraph.setMaximumSize(QtCore.QSize(750, 500))
        self.dataStreamGraph.setObjectName(_fromUtf8("dataStreamGraph"))
        self.verticalLayout_9.addWidget(self.dataStreamGraph)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.Dcoffset_U_spinBox = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.Dcoffset_U_spinBox.setMinimumSize(QtCore.QSize(70, 0))
        self.Dcoffset_U_spinBox.setMaximum(9999.0)
        self.Dcoffset_U_spinBox.setObjectName(_fromUtf8("Dcoffset_U_spinBox"))
        self.horizontalLayout.addWidget(self.Dcoffset_U_spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(100, 0))
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.Dcoffset_L_pinBox = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.Dcoffset_L_pinBox.setMaximum(9999.0)
        self.Dcoffset_L_pinBox.setObjectName(_fromUtf8("Dcoffset_L_pinBox"))
        self.horizontalLayout_4.addWidget(self.Dcoffset_L_pinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(100, 0))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_6.addWidget(self.label_5)
        self.DcoffsetCurrent_label = QtGui.QLabel(self.layoutWidget)
        self.DcoffsetCurrent_label.setObjectName(_fromUtf8("DcoffsetCurrent_label"))
        self.horizontalLayout_6.addWidget(self.DcoffsetCurrent_label)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        self.label_9.setMinimumSize(QtCore.QSize(100, 0))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_7.addWidget(self.label_9)
        self.DcoffsetTotol_label = QtGui.QLabel(self.layoutWidget)
        self.DcoffsetTotol_label.setObjectName(_fromUtf8("DcoffsetTotol_label"))
        self.horizontalLayout_7.addWidget(self.DcoffsetTotol_label)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_10.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.line = QtGui.QFrame(self.layoutWidget)
        self.line.setMinimumSize(QtCore.QSize(20, 60))
        self.line.setMaximumSize(QtCore.QSize(60, 16777215))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_4.addWidget(self.line)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_10.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.variance_U_spinBox = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.variance_U_spinBox.setMinimumSize(QtCore.QSize(70, 0))
        self.variance_U_spinBox.setMaximum(9999.0)
        self.variance_U_spinBox.setObjectName(_fromUtf8("variance_U_spinBox"))
        self.horizontalLayout_2.addWidget(self.variance_U_spinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.varianceRange_label = QtGui.QLabel(self.layoutWidget)
        self.varianceRange_label.setMinimumSize(QtCore.QSize(100, 0))
        self.varianceRange_label.setObjectName(_fromUtf8("varianceRange_label"))
        self.horizontalLayout_5.addWidget(self.varianceRange_label)
        self.variance_L_SpinBox = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.variance_L_SpinBox.setMaximum(9999.0)
        self.variance_L_SpinBox.setObjectName(_fromUtf8("variance_L_SpinBox"))
        self.horizontalLayout_5.addWidget(self.variance_L_SpinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        self.label_8.setMinimumSize(QtCore.QSize(100, 0))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_8.addWidget(self.label_8)
        self.varianceCurrent_label = QtGui.QLabel(self.layoutWidget)
        self.varianceCurrent_label.setObjectName(_fromUtf8("varianceCurrent_label"))
        self.horizontalLayout_8.addWidget(self.varianceCurrent_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_10 = QtGui.QLabel(self.layoutWidget)
        self.label_10.setMinimumSize(QtCore.QSize(100, 0))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_9.addWidget(self.label_10)
        self.varianceTotol_label = QtGui.QLabel(self.layoutWidget)
        self.varianceTotol_label.setObjectName(_fromUtf8("varianceTotol_label"))
        self.horizontalLayout_9.addWidget(self.varianceTotol_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10.addLayout(self.verticalLayout_2)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.line_2 = QtGui.QFrame(self.layoutWidget)
        self.line_2.setMinimumSize(QtCore.QSize(20, 60))
        self.line_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_5.addWidget(self.line_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_10.addLayout(self.verticalLayout_5)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_13 = QtGui.QLabel(self.layoutWidget)
        self.label_13.setEnabled(False)
        self.label_13.setMinimumSize(QtCore.QSize(100, 0))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_3.addWidget(self.label_13)
        self.quantity_spinBox = QtGui.QSpinBox(self.layoutWidget)
        self.quantity_spinBox.setEnabled(False)
        self.quantity_spinBox.setMinimumSize(QtCore.QSize(70, 0))
        self.quantity_spinBox.setMaximum(999999)
        self.quantity_spinBox.setObjectName(_fromUtf8("quantity_spinBox"))
        self.horizontalLayout_3.addWidget(self.quantity_spinBox)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem2)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label_21 = QtGui.QLabel(self.layoutWidget)
        self.label_21.setMinimumSize(QtCore.QSize(100, 20))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_15.addWidget(self.label_21)
        self.quantityTotol_label = QtGui.QLabel(self.layoutWidget)
        self.quantityTotol_label.setObjectName(_fromUtf8("quantityTotol_label"))
        self.horizontalLayout_15.addWidget(self.quantityTotol_label)
        self.verticalLayout_7.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_10.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.line_3 = QtGui.QFrame(self.layoutWidget)
        self.line_3.setMinimumSize(QtCore.QSize(20, 60))
        self.line_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_6.addWidget(self.line_3)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.horizontalLayout_10.addLayout(self.verticalLayout_6)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.setButton = QtGui.QPushButton(self.layoutWidget)
        self.setButton.setObjectName(_fromUtf8("setButton"))
        self.verticalLayout_3.addWidget(self.setButton)
        self.startButton = QtGui.QPushButton(self.layoutWidget)
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.verticalLayout_3.addWidget(self.startButton)
        self.verticalLayout_8.addLayout(self.verticalLayout_3)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem4)
        self.horizontalLayout_10.addLayout(self.verticalLayout_8)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.retranslateUi(realTimeGraph)
        QtCore.QMetaObject.connectSlotsByName(realTimeGraph)

    def retranslateUi(self, realTimeGraph):
        realTimeGraph.setWindowTitle(_translate("realTimeGraph", "RealTime Raw Data Graph", None))
        self.label.setText(_translate("realTimeGraph", "DC Offset Upper:", None))
        self.label_3.setText(_translate("realTimeGraph", "DC Offset Lower:", None))
        self.label_5.setText(_translate("realTimeGraph", "Current:", None))
        self.DcoffsetCurrent_label.setText(_translate("realTimeGraph", "0", None))
        self.label_9.setText(_translate("realTimeGraph", "Totol:", None))
        self.DcoffsetTotol_label.setText(_translate("realTimeGraph", "0", None))
        self.label_2.setText(_translate("realTimeGraph", "Variance Upper:", None))
        self.varianceRange_label.setText(_translate("realTimeGraph", "Variance Lower:", None))
        self.label_8.setText(_translate("realTimeGraph", "Current:", None))
        self.varianceCurrent_label.setText(_translate("realTimeGraph", "0", None))
        self.label_10.setText(_translate("realTimeGraph", "Totol:", None))
        self.varianceTotol_label.setText(_translate("realTimeGraph", "0", None))
        self.label_13.setText(_translate("realTimeGraph", "Test Quantity:", None))
        self.label_21.setText(_translate("realTimeGraph", "Totol:", None))
        self.quantityTotol_label.setText(_translate("realTimeGraph", "0", None))
        self.setButton.setText(_translate("realTimeGraph", "Set", None))
        self.startButton.setText(_translate("realTimeGraph", "Start", None))

