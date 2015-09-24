import numpy as np
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ADCDataProcess_findPeaks import *

class DataProcess():
    def __init__(self, parent=None):
        self.blockHeader = '\xaa\x55\xaa'
        self.blockLen = 507
        self.blockNum = 4
        self.collectedCounts = 0
        self.findPeaksObj = FindPeaks()

    def setAttribute(self, blockMulti, peaksParaList):
        self.collectedCounts = blockMulti
        self.findPeaksObj.setAttribute(peaksParaList)
        
    def dataCheck(self, dataBlock, expectedSequence):
        getData = list(dataBlock)
        if expectedSequence != self.getSequence(dataBlock):
            raise Exception, 'ExpectedSequence: %d, but it is %d' %(expectedSequence, self.getSequence(dataBlock))
            return None

        #print '%d' %expectedSequence
        
        dataToInt = []
        getData = getData[2:]
        for data in getData:
            dataToInt.append(ord(data))
                
        dataLen = len(dataToInt)
        i=0
        checkHighByte = 0
        checkLowByte = 0
        dataStream=[]

        while i < (dataLen-1-2):
            dataStream.append( dataToInt[i]*256 + dataToInt[i+1] )
            checkHighByte ^= dataToInt[i]
            checkLowByte ^= dataToInt[i+1]
            i += 2

        if checkHighByte != dataToInt[-2] or checkLowByte != dataToInt[-1] :
            raise Exception, "CheckSum error"
            return None
        else:
            return dataStream

    def getSequence(self, data):
        return ord(data[0])*256 + ord(data[1])



    def processData(self, data):
        rightdataBuff=[]
        if data.count(self.blockHeader) != self.blockNum :
            raise Exception, 'header num error'
            return None

        checkCount = 0
        startSequence = self.getSequence(data[len(self.blockHeader):self.blockLen])
        
        while checkCount < self.blockNum :
            blockStart = len(self.blockHeader) + checkCount*self.blockLen
            blockEnd = checkCount*self.blockLen + self.blockLen
            
            ExpectSequence =  startSequence + checkCount
            result = self.dataCheck(data[blockStart:blockEnd], ExpectSequence)
            if result == None:
                return None
            else:
                rightdataBuff += result
                checkCount += 1

        return rightdataBuff

    def getMean(self, data):
        return np.mean(data)


    def getVar(self, data):
        return np.var(data)

    

    def generateDisplayData(self, rawdata):
        theData = self.processData(rawdata)
        if theData is not None:
            return self.findPeaksObj.findPeaks(theData)
        else:
            return (None, [], [])

    def needRefreshGraph(self):
        return self.findPeaksObj.needRefreshGraph()

    def restartCalculateProbablility(self):
        self.findPeaksObj.resetPeakValueContainer()
        
    def getCurrentCounts(self):
        return self.findPeaksObj.getCurrentCounts()

    def isReachedCount(self):
        return self.getCurrentCounts() >= self.collectedCounts

'''
class ShowThread(DataProcess, QThread):
    def __init__(self, WidgetShow, parent=None):
        DataProcess.__init__(self, parent) # when use classname to  init super, para(self) must be put in
        QThread.__init__(self, WidgetShow)
        self.widget = WidgetShow
        self.isContinue = True
        self.startShow = False
        
    def setPara(self, showdata):
        self.showdata = showdata
        self.startShow = True

    def stop_stread(self):
        self.isContinue = False

    def __del__(self):
        self.isContinue = False

    def run(self):
        while self.isContinue:
            if self.startShow :
                
                print 'hhhhhhhh'
                if processedData is not None:  
                    self.widget.plot(processedData, noteList)
                    self.startShow = False
                    print 'aaaaaaa'
            self.msleep(10)
'''                 
           
        
        

    
