# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ADCdataParaSet.ui'
#
# Created: Wed May 06 17:06:43 2015
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

class Ui_ADCdataPara(object):
    def setupUi(self, ADCdataPara):
        ADCdataPara.setObjectName(_fromUtf8("ADCdataPara"))
        ADCdataPara.resize(635, 470)
        ADCdataPara.setMinimumSize(QtCore.QSize(635, 470))
        ADCdataPara.setMaximumSize(QtCore.QSize(635, 470))
        self.layoutWidget = QtGui.QWidget(ADCdataPara)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 614, 446))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.line_3 = QtGui.QFrame(self.layoutWidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout.addWidget(self.line_3)
        self.label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_21 = QtGui.QLabel(self.layoutWidget)
        self.label_21.setMinimumSize(QtCore.QSize(150, 0))
        self.label_21.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_3.addWidget(self.label_21)
        self.data_Y_start_spinBox = QtGui.QSpinBox(self.layoutWidget)
        self.data_Y_start_spinBox.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.data_Y_start_spinBox.setFont(font)
        self.data_Y_start_spinBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.data_Y_start_spinBox.setMinimum(0)
        self.data_Y_start_spinBox.setMaximum(9999)
        self.data_Y_start_spinBox.setProperty("value", 0)
        self.data_Y_start_spinBox.setObjectName(_fromUtf8("data_Y_start_spinBox"))
        self.horizontalLayout_3.addWidget(self.data_Y_start_spinBox)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_23 = QtGui.QLabel(self.layoutWidget)
        self.label_23.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.horizontalLayout_4.addWidget(self.label_23)
        self.data_Y_end_spinBox = QtGui.QSpinBox(self.layoutWidget)
        self.data_Y_end_spinBox.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.data_Y_end_spinBox.setFont(font)
        self.data_Y_end_spinBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.data_Y_end_spinBox.setMinimum(1)
        self.data_Y_end_spinBox.setMaximum(9999)
        self.data_Y_end_spinBox.setProperty("value", 4096)
        self.data_Y_end_spinBox.setObjectName(_fromUtf8("data_Y_end_spinBox"))
        self.horizontalLayout_4.addWidget(self.data_Y_end_spinBox)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.line_2 = QtGui.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout.addWidget(self.label_8)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_15 = QtGui.QLabel(self.layoutWidget)
        self.label_15.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_5.addWidget(self.label_15)
        self.peak_X_start_spinBox = QtGui.QSpinBox(self.layoutWidget)
        self.peak_X_start_spinBox.setEnabled(False)
        self.peak_X_start_spinBox.setMinimumSize(QtCore.QSize(120, 0))
        self.peak_X_start_spinBox.setMaximumSize(QtCore.QSize(1111, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.peak_X_start_spinBox.setFont(font)
        self.peak_X_start_spinBox.setMaximum(9999)
        self.peak_X_start_spinBox.setObjectName(_fromUtf8("peak_X_start_spinBox"))
        self.horizontalLayout_5.addWidget(self.peak_X_start_spinBox)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_18 = QtGui.QLabel(self.layoutWidget)
        self.label_18.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_6.addWidget(self.label_18)
        self.peak_Y_start_doubleSpinBox = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.peak_Y_start_doubleSpinBox.setEnabled(False)
        self.peak_Y_start_doubleSpinBox.setMinimumSize(QtCore.QSize(120, 0))
        self.peak_Y_start_doubleSpinBox.setMaximumSize(QtCore.QSize(1111, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.peak_Y_start_doubleSpinBox.setFont(font)
        self.peak_Y_start_doubleSpinBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.peak_Y_start_doubleSpinBox.setMaximum(1.0)
        self.peak_Y_start_doubleSpinBox.setSingleStep(0.1)
        self.peak_Y_start_doubleSpinBox.setObjectName(_fromUtf8("peak_Y_start_doubleSpinBox"))
        self.horizontalLayout_6.addWidget(self.peak_Y_start_doubleSpinBox)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_17 = QtGui.QLabel(self.layoutWidget)
        self.label_17.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_7.addWidget(self.label_17)
        self.peak_X_end_spinBox = QtGui.QSpinBox(self.layoutWidget)
        self.peak_X_end_spinBox.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.peak_X_end_spinBox.setFont(font)
        self.peak_X_end_spinBox.setMaximum(9999)
        self.peak_X_end_spinBox.setProperty("value", 4096)
        self.peak_X_end_spinBox.setObjectName(_fromUtf8("peak_X_end_spinBox"))
        self.horizontalLayout_7.addWidget(self.peak_X_end_spinBox)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_19 = QtGui.QLabel(self.layoutWidget)
        self.label_19.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_8.addWidget(self.label_19)
        self.peak_Y_end_doubleSpinBox = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.peak_Y_end_doubleSpinBox.setEnabled(False)
        self.peak_Y_end_doubleSpinBox.setMaximumSize(QtCore.QSize(1111, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.peak_Y_end_doubleSpinBox.setFont(font)
        self.peak_Y_end_doubleSpinBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.peak_Y_end_doubleSpinBox.setMinimum(0.1)
        self.peak_Y_end_doubleSpinBox.setMaximum(1.0)
        self.peak_Y_end_doubleSpinBox.setSingleStep(0.1)
        self.peak_Y_end_doubleSpinBox.setProperty("value", 1.0)
        self.peak_Y_end_doubleSpinBox.setObjectName(_fromUtf8("peak_Y_end_doubleSpinBox"))
        self.horizontalLayout_8.addWidget(self.peak_Y_end_doubleSpinBox)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.line = QtGui.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout.addWidget(self.label_9)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_16 = QtGui.QLabel(self.layoutWidget)
        self.label_16.setMinimumSize(QtCore.QSize(150, 0))
        self.label_16.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_13.addWidget(self.label_16)
        self.collectPoints_spinBox = QtGui.QSpinBox(self.layoutWidget)
        self.collectPoints_spinBox.setMinimumSize(QtCore.QSize(120, 0))
        self.collectPoints_spinBox.setMaximumSize(QtCore.QSize(1111, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.collectPoints_spinBox.setFont(font)
        self.collectPoints_spinBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.collectPoints_spinBox.setMinimum(4)
        self.collectPoints_spinBox.setMaximum(999999)
        self.collectPoints_spinBox.setSingleStep(4)
        self.collectPoints_spinBox.setProperty("value", 4)
        self.collectPoints_spinBox.setObjectName(_fromUtf8("collectPoints_spinBox"))
        self.horizontalLayout_13.addWidget(self.collectPoints_spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_10 = QtGui.QLabel(self.layoutWidget)
        self.label_10.setMinimumSize(QtCore.QSize(150, 0))
        self.label_10.setMaximumSize(QtCore.QSize(131, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_14.addWidget(self.label_10)
        self.peakInterval_spinBox = QtGui.QSpinBox(self.layoutWidget)
        self.peakInterval_spinBox.setMinimumSize(QtCore.QSize(450, 0))
        self.peakInterval_spinBox.setMaximumSize(QtCore.QSize(1000, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.peakInterval_spinBox.setFont(font)
        self.peakInterval_spinBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.peakInterval_spinBox.setMaximum(9999)
        self.peakInterval_spinBox.setProperty("value", 60)
        self.peakInterval_spinBox.setObjectName(_fromUtf8("peakInterval_spinBox"))
        self.horizontalLayout_14.addWidget(self.peakInterval_spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label_11 = QtGui.QLabel(self.layoutWidget)
        self.label_11.setMinimumSize(QtCore.QSize(150, 0))
        self.label_11.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_15.addWidget(self.label_11)
        self.peakGroup_spinBox = QtGui.QSpinBox(self.layoutWidget)
        self.peakGroup_spinBox.setMinimumSize(QtCore.QSize(450, 0))
        self.peakGroup_spinBox.setMaximumSize(QtCore.QSize(1000, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.peakGroup_spinBox.setFont(font)
        self.peakGroup_spinBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.peakGroup_spinBox.setMaximum(9999)
        self.peakGroup_spinBox.setProperty("value", 5)
        self.peakGroup_spinBox.setObjectName(_fromUtf8("peakGroup_spinBox"))
        self.horizontalLayout_15.addWidget(self.peakGroup_spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.label_12 = QtGui.QLabel(self.layoutWidget)
        self.label_12.setMinimumSize(QtCore.QSize(150, 0))
        self.label_12.setMaximumSize(QtCore.QSize(131, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_16.addWidget(self.label_12)
        self.slopeThreshold_spinBox = QtGui.QSpinBox(self.layoutWidget)
        self.slopeThreshold_spinBox.setMinimumSize(QtCore.QSize(450, 0))
        self.slopeThreshold_spinBox.setMaximumSize(QtCore.QSize(1000, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.slopeThreshold_spinBox.setFont(font)
        self.slopeThreshold_spinBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.slopeThreshold_spinBox.setMaximum(9999)
        self.slopeThreshold_spinBox.setProperty("value", 0)
        self.slopeThreshold_spinBox.setObjectName(_fromUtf8("slopeThreshold_spinBox"))
        self.horizontalLayout_16.addWidget(self.slopeThreshold_spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.label_13 = QtGui.QLabel(self.layoutWidget)
        self.label_13.setMinimumSize(QtCore.QSize(150, 0))
        self.label_13.setMaximumSize(QtCore.QSize(131, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_17.addWidget(self.label_13)
        self.apmThreshold_spinBox = QtGui.QSpinBox(self.layoutWidget)
        self.apmThreshold_spinBox.setMinimumSize(QtCore.QSize(450, 0))
        self.apmThreshold_spinBox.setMaximumSize(QtCore.QSize(1000, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.apmThreshold_spinBox.setFont(font)
        self.apmThreshold_spinBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.apmThreshold_spinBox.setMaximum(9999)
        self.apmThreshold_spinBox.setProperty("value", 850)
        self.apmThreshold_spinBox.setObjectName(_fromUtf8("apmThreshold_spinBox"))
        self.horizontalLayout_17.addWidget(self.apmThreshold_spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_17)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_37 = QtGui.QHBoxLayout()
        self.horizontalLayout_37.setObjectName(_fromUtf8("horizontalLayout_37"))
        self.label_38 = QtGui.QLabel(self.layoutWidget)
        self.label_38.setMinimumSize(QtCore.QSize(150, 0))
        self.label_38.setMaximumSize(QtCore.QSize(131, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_38.setFont(font)
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.horizontalLayout_37.addWidget(self.label_38)
        self.smoothWidth_spinBox = QtGui.QSpinBox(self.layoutWidget)
        self.smoothWidth_spinBox.setMinimumSize(QtCore.QSize(450, 0))
        self.smoothWidth_spinBox.setMaximumSize(QtCore.QSize(1000, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.smoothWidth_spinBox.setFont(font)
        self.smoothWidth_spinBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.smoothWidth_spinBox.setMaximum(9999)
        self.smoothWidth_spinBox.setProperty("value", 5)
        self.smoothWidth_spinBox.setObjectName(_fromUtf8("smoothWidth_spinBox"))
        self.horizontalLayout_37.addWidget(self.smoothWidth_spinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_37)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.label_25 = QtGui.QLabel(self.layoutWidget)
        self.label_25.setMinimumSize(QtCore.QSize(150, 0))
        self.label_25.setMaximumSize(QtCore.QSize(131, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.horizontalLayout_21.addWidget(self.label_25)
        self.integralInterval_SpinBox = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.integralInterval_SpinBox.setMinimumSize(QtCore.QSize(450, 0))
        self.integralInterval_SpinBox.setMaximumSize(QtCore.QSize(1000, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.integralInterval_SpinBox.setFont(font)
        self.integralInterval_SpinBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.integralInterval_SpinBox.setMaximum(9999.0)
        self.integralInterval_SpinBox.setProperty("value", 3.0)
        self.integralInterval_SpinBox.setObjectName(_fromUtf8("integralInterval_SpinBox"))
        self.horizontalLayout_21.addWidget(self.integralInterval_SpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        self.label_39 = QtGui.QLabel(self.layoutWidget)
        self.label_39.setMinimumSize(QtCore.QSize(150, 0))
        self.label_39.setMaximumSize(QtCore.QSize(131, 40))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_39.setFont(font)
        self.label_39.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.horizontalLayout_23.addWidget(self.label_39)
        self.filterArray_textEdit = QtGui.QTextEdit(self.layoutWidget)
        self.filterArray_textEdit.setEnabled(False)
        self.filterArray_textEdit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.filterArray_textEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.filterArray_textEdit.setObjectName(_fromUtf8("filterArray_textEdit"))
        self.horizontalLayout_23.addWidget(self.filterArray_textEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem)
        self.ok_Button = QtGui.QPushButton(self.layoutWidget)
        self.ok_Button.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.ok_Button.setObjectName(_fromUtf8("ok_Button"))
        self.horizontalLayout_22.addWidget(self.ok_Button)
        self.cancel_Button = QtGui.QPushButton(self.layoutWidget)
        self.cancel_Button.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.cancel_Button.setObjectName(_fromUtf8("cancel_Button"))
        self.horizontalLayout_22.addWidget(self.cancel_Button)
        self.setDefault_Button = QtGui.QPushButton(self.layoutWidget)
        self.setDefault_Button.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.setDefault_Button.setObjectName(_fromUtf8("setDefault_Button"))
        self.horizontalLayout_22.addWidget(self.setDefault_Button)
        self.help_Button = QtGui.QPushButton(self.layoutWidget)
        self.help_Button.setEnabled(True)
        self.help_Button.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.help_Button.setObjectName(_fromUtf8("help_Button"))
        self.horizontalLayout_22.addWidget(self.help_Button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_22)

        self.retranslateUi(ADCdataPara)
        QtCore.QObject.connect(self.cancel_Button, QtCore.SIGNAL(_fromUtf8("clicked()")), ADCdataPara.reject)
        QtCore.QMetaObject.connectSlotsByName(ADCdataPara)
        ADCdataPara.setTabOrder(self.data_Y_start_spinBox, self.data_Y_end_spinBox)
        ADCdataPara.setTabOrder(self.data_Y_end_spinBox, self.peak_X_start_spinBox)
        ADCdataPara.setTabOrder(self.peak_X_start_spinBox, self.peak_X_end_spinBox)
        ADCdataPara.setTabOrder(self.peak_X_end_spinBox, self.peak_Y_start_doubleSpinBox)
        ADCdataPara.setTabOrder(self.peak_Y_start_doubleSpinBox, self.peak_Y_end_doubleSpinBox)
        ADCdataPara.setTabOrder(self.peak_Y_end_doubleSpinBox, self.collectPoints_spinBox)
        ADCdataPara.setTabOrder(self.collectPoints_spinBox, self.peakInterval_spinBox)
        ADCdataPara.setTabOrder(self.peakInterval_spinBox, self.peakGroup_spinBox)
        ADCdataPara.setTabOrder(self.peakGroup_spinBox, self.slopeThreshold_spinBox)
        ADCdataPara.setTabOrder(self.slopeThreshold_spinBox, self.apmThreshold_spinBox)
        ADCdataPara.setTabOrder(self.apmThreshold_spinBox, self.integralInterval_SpinBox)

    def retranslateUi(self, ADCdataPara):
        ADCdataPara.setWindowTitle(_translate("ADCdataPara", "Graph Setting", None))
        self.label.setText(_translate("ADCdataPara", "Filtered Data Graph  Axis Range <1000 points at X asix>", None))
        self.label_21.setText(_translate("ADCdataPara", "Y Start:", None))
        self.label_23.setText(_translate("ADCdataPara", "Y End:", None))
        self.label_8.setText(_translate("ADCdataPara", "Peak Probability Graph Axis Range", None))
        self.label_15.setText(_translate("ADCdataPara", "X Start:", None))
        self.label_18.setText(_translate("ADCdataPara", "Y Start:", None))
        self.label_17.setText(_translate("ADCdataPara", "X End:", None))
        self.label_19.setText(_translate("ADCdataPara", "Y End:", None))
        self.label_9.setText(_translate("ADCdataPara", "Peak Probability Graph Peak Find Para", None))
        self.label_16.setText(_translate("ADCdataPara", "Collect Points(*1000): ", None))
        self.label_10.setText(_translate("ADCdataPara", "Min Peak Interval:", None))
        self.label_11.setText(_translate("ADCdataPara", "Peak Group:", None))
        self.label_12.setText(_translate("ADCdataPara", "Slope Threshold:", None))
        self.label_13.setText(_translate("ADCdataPara", "Amplitude Threshold:", None))
        self.label_38.setText(_translate("ADCdataPara", "Smooth Width:", None))
        self.label_25.setText(_translate("ADCdataPara", "Integral Interval:", None))
        self.label_39.setText(_translate("ADCdataPara", "Filter Array: ", None))
        self.filterArray_textEdit.setHtml(_translate("ADCdataPara", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-18, -510, -271, 823, 2356, 3088, 2356, 823, -271, -510, -18</p></body></html>", None))
        self.ok_Button.setText(_translate("ADCdataPara", "OK", None))
        self.cancel_Button.setText(_translate("ADCdataPara", "Cancel", None))
        self.setDefault_Button.setText(_translate("ADCdataPara", "Set Default", None))
        self.help_Button.setText(_translate("ADCdataPara", "Help", None))
