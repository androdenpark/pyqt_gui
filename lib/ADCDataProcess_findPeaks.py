from __future__ import division #get the dot of division
import numpy as np


__probalilityFielt__ = 0.05
__refreshTime__ = 12

class FindPeaks():
    def __init__(self):
        self.peakInterval = 6
        self.smoothWidth = 5
        self.peakGroup =5
        self.slopeThreshold = 0
        self.ampThreshold = 850
        self.filterPara = [-18, -510, -271, 823, 2356, 3088, 2356, 823, -271, -510, -18]
        self.integralInteval =3
        self.filterCoefBitWidth = 13
        self.probabilityLowerLimit = 0
        self.probabilityUpperLimit = 1
        self.peakValueContainer=[]
        self.collectCounts = 0

    #peaksParaList = [peakInterval, smoothWidth, peakGroup, slopeThreshold, ampThreshold,
    #                 filterPara, integralInteval, probabilityLowerLimit, probabilityUpperLimit]
    
    def resetPeakValueContainer(self):
        self.peakValueContainer=[]
        self.collectCounts = 0

    def getCurrentCounts(self):
        return self.collectCounts

    def calculateFinalProbability(self, currentProbabilityList):

        if len(self.peakValueContainer) == 0:
            if len(currentProbabilityList) == 0:
                return []
            else:
                self.peakValueContainer += currentProbabilityList
        else:
            theValueExistLits = [theValue[0] for theValue in self.peakValueContainer]

            for value in currentProbabilityList:
                try:
                    index = theValueExistLits.index(value[0])
                    (self.peakValueContainer[index])[1] += value[1]                    
                except ValueError:
                    self.peakValueContainer.append([value[0], value[1]])

                    
        totolNums = sum([theValue[1] for theValue in self.peakValueContainer])
        
        def calculateProbability(theData):                          
            probability=[]
            for data in theData:
                theProbability = data[1]/totolNums
                if theProbability >= self.probabilityLowerLimit and theProbability >= __probalilityFielt__ :
                    probability.append([data[0], data[1]/totolNums])      
            probability.sort()
            return probability

        currentTotolProbability=calculateProbability(self.peakValueContainer)


        def prepareDisplayData(theData):
            if len(theData) < 2:
                return theData
            
            #theValueExistLits = [theValue[0] for theValue in theData]
            dataMin = int(theData[0][0]//self.integralInteval)
            dataMax = int(theData[-1][0]//self.integralInteval)
            theShowList = [[a*self.integralInteval,0] for a in range(dataMin, dataMax+1)]
            theShowListValue=[a[0] for a in theShowList]
            for value in theData:
                try:
                    index = theShowListValue.index(value[0])
                    theShowList[index][1]=value[1]
                except Exception,e:
                    print e
            return theShowList          

        return prepareDisplayData(currentTotolProbability)
        
        
    def setAttribute(self, peaksParaList):
        self.peakInterval =  peaksParaList[0]#peakInterval
        self.smoothWidth = peaksParaList[1]#smoothWidth
        self.peakGroup = peaksParaList[2]#peakGroup
        self.slopeThreshold = peaksParaList[3]#slopeThreshold
        self.ampThreshold = peaksParaList[4]#ampThreshold
        self.integralInteval = peaksParaList[6]#integralInteval
        self.probabilityLowerLimit = peaksParaList[7]#probabilityLowerLimit
        self.probabilityUpperLimit = peaksParaList[8]#probabilityUpperLimit
        if peaksParaList[5] is not None:
            self.filterPara = peaksParaList[5]#filterPara

        self.resetPeakValueContainer()
        

    def deriv(self, processData):
        derivedData=[]
        derivedData.append(processData[1]-processData[0])
        index = 1
        dataLength = len(processData)
        while index < (dataLength-1):
            derivedData.append((processData[index+1] - processData[index-1])/2)
            index += 1
                
        derivedData.append(processData[-1] - processData[-2])
        return derivedData


    def fastsmooth(self, smoothData):           
        halfBW = (self.smoothWidth+1)//2            #get the integer rusult
        sumPoints = sum(smoothData[:self.smoothWidth])

        totolLen = len(smoothData)
        data = [0]*totolLen

        for index, value in enumerate(smoothData):
            if index < totolLen - self.smoothWidth:
                data[index+halfBW-1]= sumPoints
                sumPoints = sumPoints - value + smoothData[index+self.smoothWidth]

        return data


    def peakFind(self, smoothedData, convolvedData):
        
        def sign(x):
            if x > 0:
                return 1
            if x < 0:
                return -1
            else :
                return 0
            
        PeakSearchBackPoints = self.peakGroup//2          #get the integer rusult
        PeakSearchForwardPoints = self.peakGroup - PeakSearchBackPoints - 1

        PeakList=[]
        for index, value in enumerate(smoothedData):
            if index < self.smoothWidth:
                continue
            if index < len(smoothedData)-self.smoothWidth :
                conditionOne = (value - smoothedData[index+1]) > self.slopeThreshold*convolvedData[index] and convolvedData[index] > self.ampThreshold
                if sign(value)> sign(smoothedData[index+1]) and  conditionOne :
                    if PeakSearchBackPoints >  index :
                        PeakSearchBackPoints = index
                    if (PeakSearchForwardPoints + index)>=len(smoothedData) :
                        PeakSearchForwardPoints = len(smoothedData) - index -1

                    referenceData = convolvedData[index-PeakSearchBackPoints: index+PeakSearchForwardPoints+1]
                    MaxValue = max(referenceData)
                    MaxIndex = index-PeakSearchBackPoints + referenceData.index(MaxValue)

                    PeakList.append([MaxValue, MaxIndex])

        return PeakList



    def filterPeaks(self, peaksData):
        peaksCount = len(peaksData)
        
        if peaksCount<1:
            return []
        
        prePeakMaxValue = (peaksData[0])[0]
        prePeakMaxIndex = (peaksData[0])[1]
        prePeakLastIndex = prePeakMaxIndex

            
        filteredPeaks = []

        for index, value in enumerate(peaksData):
            if value[1]- prePeakLastIndex >= self.peakInterval:
                filteredPeaks.append([prePeakMaxValue, prePeakMaxIndex])
                prePeakMaxIndex = value[1]
                prePeakMaxValue = value[0]
            else:
                if value[0] > prePeakMaxValue:
                    prePeakMaxIndex = value[1]
                    prePeakMaxValue = value[0]
            
            prePeakLastIndex = value[1]

        return filteredPeaks

    def getPeaksProbability(self, peaksValue):
        sortPeaks = []
        for data in peaksValue:
            sortPeaks.append(data[0])
        sortPeaks.sort()
        #totolNums = len(sortPeaks)
        probabilityList =[]
        if len(sortPeaks)> 0 :
            sortPeaks.append(sortPeaks[-1]+ self.integralInteval) # as the endFlag of index
            currentEndValue = (sortPeaks[0]//self.integralInteval +1)*self.integralInteval
            currentCount = 0
            for data in sortPeaks:
                #print currentEndValue
                if data <= currentEndValue:                    
                    currentCount += 1
                else:
                    probabilityList.append([currentEndValue, currentCount])
                    currentCount = 1
                    currentEndValue = (data//self.integralInteval +1)*self.integralInteval
                
        return self.calculateFinalProbability(probabilityList)
                    
                
    def needRefreshGraph(self):
        return 0 == self.collectCounts%__refreshTime__
    

    def findPeaks(self, theData):
        self.collectCounts = self.collectCounts + 1 if self.collectCounts < 0xffff else 1
        
        try:
            #convolvedData = np.ndarray.tolist(np.convolve(theData, self.filterPara))[0:len(theData)]
            convolvedData = np.convolve(theData, self.filterPara)[0:len(theData)]
            convolvedData = convolvedData/(sum(self.filterPara))
            convolvedData = np.ndarray.tolist(convolvedData)
            #print convolvedData
            #convolvedDatadd=np.round(convolvedData)
            #convolvedData =np.ndarray.tolist(convolvedDatadd
            
            derivedData = self.deriv(convolvedData)
            #print 'derivedData'
            smoothedData = self.fastsmooth(derivedData)
            #print 'smoothedData'
            peakList = self.peakFind(smoothedData, convolvedData)
            #print 'peakList'
            peakResult = self.filterPeaks(peakList)
            #print 'peakResult'
            peakProbability = self.getPeaksProbability(peakResult)
            #print peakProbability
            return (convolvedData, peakResult , peakProbability)
        except Exception, e:
            print 'findPeaks error: ' ,e
            return (None, [], [])



