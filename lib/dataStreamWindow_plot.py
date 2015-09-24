from __future__ import division #get the dot of division
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as matplotWidget
from matplotlib.figure import Figure as matplotFigure
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import AutoLocator

from dataStreamWindow_graphPara import *

import numpy as np


__graphHeight__ = 205
__graphWidght__ = 750

__xAxisStart__ = 0.04*__graphWidght__
__xAxisLen__ = 0.95*__graphWidght__
__xAxisEnd__ = __xAxisLen__ + __xAxisStart__

__yAxisStart__ = (1-0.07-0.85)*__graphHeight__
__yAxisLen__ = 0.85*__graphHeight__
__yAxisEnd__ = __yAxisLen__ + __yAxisStart__




class DataStreamMatplot(matplotWidget):
                      
    def __init__(self, parent=None):
        self.figure = matplotFigure(None, None, 'm')
        self.figure.hold(False)
        #self.waveAx = self.figure.add_subplot(111)
        #fixed plot size by :[left, bottom, width, height], the value is relateive to figure size        
        super(DataStreamMatplot, self).__init__(self.figure)        
        #matplotWidget.__init__(self, self.figure)        
        self.axisParaWin = AxisSettingWin(self)
        #self.connect(self,SIGNAL("AXIS SETTING"),self.doAxisSetting)
        #self.addAxes()


    def initAxisValue(self, xstart, ystart, xend, yend):
        self.axisParaWin.setAttributes(xstart, ystart, xend, yend)
        self.addAxes('')
    
    def doAxisSetting(self):
        self.ax.set_xlim(self.axisParaWin.xstart, self.axisParaWin.xend)
        self.ax.set_ylim(self.axisParaWin.ystart, self.axisParaWin.yend)
        for tick in self.ax.xaxis.get_ticklabels() + self.ax.yaxis.get_ticklabels():
            tick.set_fontsize(8)


    def addAxes(self, theTitle="unknown"):
        self.figure.clear()            
        self.ax = self.figure.add_axes([0.04, 0.07, 0.95, 0.85])
        self.ax.grid(True)
        self.ax.set_title(theTitle, fontsize=12, fontweight='bold')
        self.doAxisSetting()


    def getAxDot(self, plotXData, plotYData, color):
        self.axDot, = self.ax.plot(plotXData, plotYData, color)

        
    def plotByDot(self, plotXData, plotYData):
        #xData=range(1,len(plotData)+1)           
        self.axDot.set_data(plotXData, plotYData)
        #self.axDot.set_data(range(1,501), [2000]*500)


    def plot(self, plotXData, plotYData, color):        
        self.ax.plot(plotXData, plotYData, color)
        #self.ax.xaxis.draw()
        #self.ax.yaxis.draw()

    def showNewGraph(self):
        self.draw()

    def scatter(self, scatterXData, scatterYData, color, scale):
        self.ax.scatter(scatterXData, scatterYData, s=scale, c=color, marker='*')
 

    def bar(self, barXData, barYData):
        self.ax.bar(barXData, barYData, facecolor='#9999ff', edgecolor='white')


    def mouseDoubleClickEvent(self, event):
        clickQpoint = event.pos()
        thePosition = 'X:%.2f, Y:%.2f' %(self.getClickAxisValue(clickQpoint.x(), clickQpoint.y()))
        self.axisParaWin.setClickPosition(thePosition)
        self.axisParaWin.show()

    def getClickAxisValue(self, theX, theY):
        if theX >= __xAxisStart__ and theX <= __xAxisEnd__:
            xValue = self.axisParaWin.xstart +\
                     ((theX - __xAxisStart__)/__xAxisLen__)*(self.axisParaWin.xend - self.axisParaWin.xstart)
        else:
            xValue = 0

        if theY >= __yAxisStart__ and theY <= __yAxisEnd__:
            yValue = self.axisParaWin.yend -  \
                     ((theY - __yAxisStart__)/__yAxisLen__)*(self.axisParaWin.yend - self.axisParaWin.ystart)
        else:
            yValue = 0

        return xValue, yValue
            
               



        
