from PyQt4.QtCore import *
from PyQt4.QtGui import *


#myLock=QReadWriteLock()

class PublicAttribute():
    def __init__(self):
        self.forWrite=0
        self.forRead=0
        
        
class LockLearningThreadOne(QThread):        
    def run(self):
        myLock=QReadWriteLock()
        self.myAttributes=PublicAttribute()
        while(True):
            

            try:
                myLock.lockForWrite()
                self.myAttributes.forRead = 2
                print "I'm Jack"
                self.sleep(10)
            finally:
                myLock.unlock()
                

class LockLearningThreadTwo(QThread):
    def run(self):
        myLock=QReadWriteLock()
        self.myAttributes=PublicAttribute()
        while(True):
            try:
                myLock.lockForRead()
                
                print "I'm Mickle"
                print self.myAttributes.forRead
                self.sleep(1)
            finally:
                myLock.unlock()






if __name__=="__main__":
    threadOne=LockLearningThreadOne()
    threadTwo=LockLearningThreadTwo()

    threadOne.start()
    threadTwo.start()    
