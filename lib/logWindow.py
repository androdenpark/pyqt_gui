from PyQt4.QtCore import *
from PyQt4.QtGui import *


class LogWindow():
    def __init__(self, logWidget):
        self.logWidget = logWidget

    def warningLog(self, message):
        fontColor = QColor(0, 255, 0)
        self.logWidget.setTextColor(fontColor)
        self.logWidget.append('<%s>Warning:' %unicode(QDateTime().currentDateTime().toString(Qt.ISODate)) + message)

    def infoLog(self, message):
        fontColor = QColor(0,0,0)
        self.logWidget.setTextColor(fontColor)
        self.logWidget.append('<%s>Info:' %unicode(QDateTime().currentDateTime().toString(Qt.ISODate)) + message)
                                                                    
    def errorLog(self, message):
        fontColor = QColor(255, 0, 0)
        self.logWidget.setTextColor(fontColor)
        self.logWidget.append('<%s>Error:' %unicode(QDateTime().currentDateTime().toString(Qt.ISODate)) + message)





    
                            
