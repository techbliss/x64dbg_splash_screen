from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QApplication, QFont, QPixmap, QSplashScreen
import os
import sys
import time
dn = os.getcwd()
sys.path.insert(0, dn)
print dn
version = "Branch"+" 1564632"
build_date = "Build Date"+" 12.12.2112"

def X64dbgSplash(self):
    splash = QtGui.QSplashScreen(QtGui.QPixmap("22.png"))
    splash.showMessage("X64Dbg\n"+version+'\n'+build_date+"\nLoading debugger... 0%", QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.white )
    splash.show()
    for i in range(1, 6):
        time.sleep(4)
        splash.showMessage("X64Dbg\n"+version+'\n'+build_date+"\nLoading debugger...{0}%".format(i * 25), QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.white)
        QtGui.QApplication.processEvents()
        splash.show()
    splash.finish(splash)

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    X64dbgSplash(([0]))
    app.quit()