from PyQt4.QtCore import *
from PyQt4.QtGui import *

from serialDisplay_ui import *


class SerialPortWindow(QDialog, Ui_serialPortDlg):
    def __init__(self, Mainwindow, controlCenter, associatedBar, infoObj, commandHistory=None,commandFormat='ASCII'):
        super(SerialPortWindow, self).__init__(Mainwindow)
        self.setupUi(self)# this must be called before acess any attrubutes of Ui_serialPortDlg, because they are definded in it
        self.commandHistory = commandHistory
        self.commandFormat = commandFormat
        self.infoObj = infoObj
        self.associatedBar = associatedBar
        self.recaiveData = ''
        Mainwindow.addSysbroadcastSignalObj(self)
        self.controlCenter = controlCenter
        self.sendLine = 0

        def background():
            self.setAutoFillBackground(False)                                  
            palette=QPalette()
            #palette.setBrush(QPalette.Background, QBrush(QPixmap(':/subBackground.png')))
            palette.setBrush(QPalette.Background, QColor(191,0,191))
            self.setPalette(palette)
            
        background()                                    
       
        super(SerialPortWindow, self).connect(self.portCommandBox, SIGNAL(enterSignalfromCommand), self.commandInputFinish)
        
        if 'HEX' in self.commandFormat:
            formatList = ['HEX','ASCII']
        else:
            formatList = ['ASCII','HEX']
            
        self.portFormatBox.addItems(formatList)
        


            
    def closeEvent(self, event):
        self.controlCenter.unlockSerialPort(self)       
        self.associatedBar.setEnabled(True)
        self.portInfoDisplay.clear()
        QDialog.closeEvent(self, event)
        

    @pyqtSignature("")
    def on_clearScreenButton_clicked(self):
        self.portInfoDisplay.clear()

    @pyqtSignature("")
    def on_recordScreenButton_clicked(self):
        pass
                
        
    def refreshHistory(self):
        if self.commandHistory is not None:
            #showHistory = self.commandHistory       ## showHistory is referring to self.commandHistory 
            self.commandHistory.append('Clear History...')  ## and operation to showHistory is also acturally operation to self.commandHistory 
            self.portCommandBox.clear()
            self.portCommandBox.addItems(self.commandHistory)
            del self.commandHistory[-1]
    
    def commandInputFinish(self):
        self.portCommandBox.setEnabled(False)
        try:
            commandContent=unicode(self.portCommandBox.currentText())
            commandContent=str(commandContent)

            if  'Clear History' in commandContent:
                self.commandHistory = None
                self.portCommandBox.clear()
                self.portCommandBox.setEditText('')
                return
            
            self.commandFormat = self.portFormatBox.currentText()

            if 'HEX' in self.commandFormat:
                def transformToHex(data):
                    if len(data)%2 != 0:
                        data.append('0')
                    try:
                        data = data.decode('hex')
                    except:
                        self.infoObj.warningLog('Imput [ %s ] contains illlegal character' %commandContent)
                        return None

                if transformToHex(commandContent)  is not None:
                    self.writeData(commandContent)
                else:
                    return
                    
            else:
                if self.writeData(commandContent+'\r\n'):
                    self.infoObj.infoLog('data [ %s ] send out ok' %commandContent)
                else:
                    self.infoObj.infoLog('data [ %s ] send out failed' %commandContent)
                    return
                
            self.commandHistory = QStringList() \
                                  if self.commandHistory is None else self.commandHistory

            if not self.commandHistory.contains(commandContent) :   
                #if self.commandHistory.isEmpty():
                self.commandHistory.prepend(QString(commandContent))
                if self.commandHistory.count() > 15:       #max history to remember is 5
                    del self.commandHistory[-1]
                self.refreshHistory()
        except Exception, e:
                print e

        finally:
            self.portCommandBox.setEnabled(True)
                
            
        




    def isAntoClear(self):
        if self.sendLine > 1000:
            self.portInfoDisplay.clear()
            self.sendLine = 0
            self.portInfoDisplay.append('the infomation is anto cleared to release storge!')


    ############the following func is needed when create a window to connect to port##############################

    def className(self):
        return 'Console Window'



    def displayText(self, theText):
        self.portInfoDisplay.append(QString(theText))
        scrollBar = self.portInfoDisplay.verticalScrollBar()
        scrollBar.setValue(0xffff)
        self.sendLine += 1           
        self.controlCenter.delayTime()    
        self.isAntoClear()

    def getData(self, dataRecaive):            

        self.recaiveData += dataRecaive

        if self.recaiveData.endswith('\n\r') or self.recaiveData.endswith('\r\n'):
            self.displayText(self.recaiveData[0:-2])
            self.recaiveData = ''
   
        if len(self.recaiveData) > 2000 :
            self.displayText('recaive data 2000 bytes')
            self.recaiveData = ''

        return None
        
        

    def writeData(self, data):
        try:
            if self.controlCenter.writeData(self, data):
                return True
            else:
                return False
        except Exception, e:
            if "access denied" in e:
                QMessageBox.about(self, 'WORNING!!!',
                                  "The port is occupyed by others!!!" )
            else:
                self.displayText("write error occures during sending data to port")
            return False
                
        

    def dealPortSignal(self, signalstr, portNum):
        if 'disconn' in signalstr :
            self.setWindowTitle('Disconnected!!!')
        else:
            self.setWindowTitle('Connected at port %d' %portNum)

    def setPortPara(self, portObj):
        portObj.set_readDataLen(1)

            

    

        
            
                

                    




