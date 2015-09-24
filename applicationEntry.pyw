'''
import sys
import os


def getCurrentPath():
    path= str(sys.path[0])
    if os.path.isdir(path):
        sys.path.append(path+'\\lib')
        sys.path.append(path+'\\lib\\source')
        return path
    else:
        return None
        sys.path.append(os.path.dirname(path)+'\\lib')
        sys.path.append(os.path.dirname(path)+'\\lib\\source')
        return os.path.dirname(path)

print getCurrentPath()

#sys.path.append(thePath+'\\lib')
#sys.path.append(thePath+'\\lib\\source')
'''
import sys



sys.path.append(str(sys.path[0])+'\\lib')
sys.path.append(str(sys.path[0])+'\\lib\\source')

from mainWindow import *

app = QApplication(sys.argv)
app.setOrganizationName("***********")
app.setOrganizationDomain("*********")
app.setApplicationName("****************")
form = MainWindow("1.0.0", "****************")
app.exec_()
