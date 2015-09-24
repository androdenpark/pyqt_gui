from __future__ import division

from PyQt4.QtCore import *

__graphRefreshFrequency__=12

class StatisticDataCaculate():
    def __init__(self):
        #self.dcOffsetUpperLimit=0
        #self.dcOffsetLowerLimit=0        
        #self.varianceUpperLimit=0
        #self.varianceLowerLimit=0        
        #self.quantity=0
        self.loadAttributes()
        self.resetInternalAttributes()
        

    def resetInternalAttributes(self):
        self.dcOffsetCurrent=0
        self.dcOffsetError=0
        self.varianceCurrent=0
        self.varianceError=0
        self.quantityCurrent=0
        
    #paraList=[dcOffsetUpperLimit, dcOffsetLowerLimit, varianceUpperLimit,
    #    varianceLowerLimit, quantity]     
    def setAttributes(self, paraList):
        self.dcOffsetUpperLimit=paraList[0]
        self.dcOffsetLowerLimit=paraList[1]        
        self.varianceUpperLimit=paraList[2]
        self.varianceLowerLimit=paraList[3]        
        self.quantity=paraList[4]
        self.resetInternalAttributes()

    def getAtrributes(self):
        theList=[self.dcOffsetUpperLimit,self.dcOffsetLowerLimit,
                 self.varianceUpperLimit,self.varianceLowerLimit, self.quantity]
        return theList

    def saveAttributes(self, theSettings):
        theSettings.setValue("dcOffsetUpperLimit", QVariant(self.dcOffsetUpperLimit))
        theSettings.setValue("dcOffsetLowerLimit", QVariant(self.dcOffsetLowerLimit))
        theSettings.setValue("varianceUpperLimit", QVariant(self.varianceUpperLimit))
        theSettings.setValue("varianceLowerLimit", QVariant(self.varianceLowerLimit))
        theSettings.setValue("statisticQuantity", QVariant(self.quantity))
        

    def loadAttributes(self):
        settings = QSettings()
        self.dcOffsetUpperLimit=(settings.value("dcOffsetUpperLimit").toDouble())[0]
        self.dcOffsetLowerLimit=(settings.value("dcOffsetLowerLimit").toDouble())[0]       
        self.varianceUpperLimit=(settings.value("varianceUpperLimit").toDouble())[0]
        self.varianceLowerLimit=(settings.value("varianceLowerLimit").toDouble())[0]       
        self.quantity=(settings.value("statisticQuantity").toInt())[0]
        #self.isNotFirstTimeUse=(settings.value("dcOffsetUpperLimit").toDouble())[1]

        
        

    def processIncomeData(self, meanValue, varValue):        
        self.quantityCurrent += 1
        self.dcOffsetCurrent = meanValue
        self.varianceCurrent = varValue

        if(self.dcOffsetCurrent< self.dcOffsetLowerLimit or self.dcOffsetCurrent>self.dcOffsetUpperLimit):
            self.dcOffsetError += 1
        if(self.varianceCurrent< self.varianceLowerLimit or self.varianceCurrent>self.varianceUpperLimit):
            self.varianceError += 1

    def getDisplayData(self):
        displayList=[self.dcOffsetCurrent, self.dcOffsetError/self.quantityCurrent,
                     self.varianceCurrent, self.varianceError/self.quantityCurrent,
                     self.quantityCurrent]
        return displayList

    def isQuantityReached(self):
        return self.quantityCurrent >= self.quantity

    def needShowGraph(self):
        return 0 == self.quantityCurrent%__graphRefreshFrequency__
        
            
            
        

        


    
