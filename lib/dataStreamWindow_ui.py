# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataStreamWindow_ui.ui'
#
# Created: Fri Apr 24 12:58:44 2015
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

class Ui_statisticsDialog(object):
    def setupUi(self, statisticsDialog):
        statisticsDialog.setObjectName(_fromUtf8("statisticsDialog"))
        statisticsDialog.resize(772, 478)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(statisticsDialog.sizePolicy().hasHeightForWidth())
        statisticsDialog.setSizePolicy(sizePolicy)
        statisticsDialog.setMinimumSize(QtCore.QSize(772, 478))
        statisticsDialog.setMaximumSize(QtCore.QSize(772, 478))
        self.layoutWidget = QtGui.QWidget(statisticsDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 752, 466))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.dataStreamGraph = DataStreamMatplot(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataStreamGraph.sizePolicy().hasHeightForWidth())
        self.dataStreamGraph.setSizePolicy(sizePolicy)
        self.dataStreamGraph.setMinimumSize(QtCore.QSize(750, 205))
        self.dataStreamGraph.setMaximumSize(QtCore.QSize(750, 500))
        self.dataStreamGraph.setObjectName(_fromUtf8("dataStreamGraph"))
        self.verticalLayout.addWidget(self.dataStreamGraph)
        self.dataProbabilityGraph = DataStreamMatplot(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataProbabilityGraph.sizePolicy().hasHeightForWidth())
        self.dataProbabilityGraph.setSizePolicy(sizePolicy)
        self.dataProbabilityGraph.setMinimumSize(QtCore.QSize(750, 205))
        self.dataProbabilityGraph.setMaximumSize(QtCore.QSize(750, 500))
        self.dataProbabilityGraph.setObjectName(_fromUtf8("dataProbabilityGraph"))
        self.verticalLayout.addWidget(self.dataProbabilityGraph)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.collectPoints_label = QtGui.QLabel(self.layoutWidget)
        self.collectPoints_label.setMinimumSize(QtCore.QSize(100, 0))
        self.collectPoints_label.setObjectName(_fromUtf8("collectPoints_label"))
        self.horizontalLayout_3.addWidget(self.collectPoints_label)
        self.continueButton = QtGui.QPushButton(self.layoutWidget)
        self.continueButton.setObjectName(_fromUtf8("continueButton"))
        self.horizontalLayout_3.addWidget(self.continueButton)
        self.pauseButton = QtGui.QPushButton(self.layoutWidget)
        self.pauseButton.setObjectName(_fromUtf8("pauseButton"))
        self.horizontalLayout_3.addWidget(self.pauseButton)
        self.statisticsButton = QtGui.QPushButton(self.layoutWidget)
        self.statisticsButton.setObjectName(_fromUtf8("statisticsButton"))
        self.horizontalLayout_3.addWidget(self.statisticsButton)
        self.setButton = QtGui.QPushButton(self.layoutWidget)
        self.setButton.setObjectName(_fromUtf8("setButton"))
        self.horizontalLayout_3.addWidget(self.setButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(statisticsDialog)
        QtCore.QMetaObject.connectSlotsByName(statisticsDialog)

    def retranslateUi(self, statisticsDialog):
        statisticsDialog.setWindowTitle(_translate("statisticsDialog", "Data Stream", None))
        self.label_2.setText(_translate("statisticsDialog", "Collected Points(*1000):", None))
        self.collectPoints_label.setText(_translate("statisticsDialog", "0", None))
        self.continueButton.setText(_translate("statisticsDialog", "Continue", None))
        self.pauseButton.setText(_translate("statisticsDialog", "Pause", None))
        self.statisticsButton.setText(_translate("statisticsDialog", "Statistics", None))
        self.setButton.setText(_translate("statisticsDialog", "More...", None))


