# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataStreamWindowStatistics_ui.ui'
#
# Created: Thu Apr 30 10:01:16 2015
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

class Ui_dataStreamStatistics(object):
    def setupUi(self, dataStreamStatistics):
        dataStreamStatistics.setObjectName(_fromUtf8("dataStreamStatistics"))
        dataStreamStatistics.resize(405, 300)
        dataStreamStatistics.setMinimumSize(QtCore.QSize(405, 300))
        dataStreamStatistics.setMaximumSize(QtCore.QSize(405, 300))
        self.widget = QtGui.QWidget(dataStreamStatistics)
        self.widget.setGeometry(QtCore.QRect(20, 11, 371, 281))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.currentDc_label = QtGui.QLabel(self.widget)
        self.currentDc_label.setObjectName(_fromUtf8("currentDc_label"))
        self.horizontalLayout.addWidget(self.currentDc_label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.CurrentAmpMax_label = QtGui.QLabel(self.widget)
        self.CurrentAmpMax_label.setObjectName(_fromUtf8("CurrentAmpMax_label"))
        self.horizontalLayout_2.addWidget(self.CurrentAmpMax_label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.CurrentAmpMin_label = QtGui.QLabel(self.widget)
        self.CurrentAmpMin_label.setObjectName(_fromUtf8("CurrentAmpMin_label"))
        self.horizontalLayout_3.addWidget(self.CurrentAmpMin_label)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_5 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_12 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_4.addWidget(self.label_12)
        self.peakMin_label = QtGui.QLabel(self.widget)
        self.peakMin_label.setObjectName(_fromUtf8("peakMin_label"))
        self.horizontalLayout_4.addWidget(self.peakMin_label)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_7 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_5.addWidget(self.label_7)
        self.peakMax_label = QtGui.QLabel(self.widget)
        self.peakMax_label.setObjectName(_fromUtf8("peakMax_label"))
        self.horizontalLayout_5.addWidget(self.peakMax_label)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_6 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_6.addWidget(self.label_6)
        self.maxProbability_label = QtGui.QLabel(self.widget)
        self.maxProbability_label.setObjectName(_fromUtf8("maxProbability_label"))
        self.horizontalLayout_6.addWidget(self.maxProbability_label)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.label_8 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout.addWidget(self.label_8)
        self.peakRank_textBrowser = QtGui.QTextBrowser(self.widget)
        self.peakRank_textBrowser.setObjectName(_fromUtf8("peakRank_textBrowser"))
        self.verticalLayout.addWidget(self.peakRank_textBrowser)

        self.retranslateUi(dataStreamStatistics)
        QtCore.QMetaObject.connectSlotsByName(dataStreamStatistics)

    def retranslateUi(self, dataStreamStatistics):
        dataStreamStatistics.setWindowTitle(_translate("dataStreamStatistics", "Graph Statistics", None))
        self.label.setText(_translate("dataStreamStatistics", "Filtered Data Graph", None))
        self.label_2.setText(_translate("dataStreamStatistics", "Current Dc Offset:", None))
        self.currentDc_label.setText(_translate("dataStreamStatistics", "0", None))
        self.label_3.setText(_translate("dataStreamStatistics", "Current Max Amplitude:", None))
        self.CurrentAmpMax_label.setText(_translate("dataStreamStatistics", "0", None))
        self.label_4.setText(_translate("dataStreamStatistics", "Current Min Amplitude:", None))
        self.CurrentAmpMin_label.setText(_translate("dataStreamStatistics", "0", None))
        self.label_5.setText(_translate("dataStreamStatistics", "Peak Probability Graph", None))
        self.label_12.setText(_translate("dataStreamStatistics", "Peak Min Value:", None))
        self.peakMin_label.setText(_translate("dataStreamStatistics", "0", None))
        self.label_7.setText(_translate("dataStreamStatistics", "Peak Max Value:", None))
        self.peakMax_label.setText(_translate("dataStreamStatistics", "0", None))
        self.label_6.setText(_translate("dataStreamStatistics", "Peak Max Probability:", None))
        self.maxProbability_label.setText(_translate("dataStreamStatistics", "0", None))
        self.label_8.setText(_translate("dataStreamStatistics", "Peak Probability List: ", None))
        self.peakRank_textBrowser.setHtml(_translate("dataStreamStatistics", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))

