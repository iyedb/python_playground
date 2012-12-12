import sys

from PySide.QtCore import *
from PySide.QtGui import *
"""
# Create a Qt application
app = QApplication(sys.argv)
# 
# Enter Qt application main loop
app.exec_()
sys.exit()
"""


def quit():
  sys.exit()
	
app = QApplication(sys.argv)
systrayico = QSystemTrayIcon(QIcon("icon18.gif"))
systrayico.show()
#systrayico.showMessage('hello', 'hello', msecs=2000)

menu = QMenu()
quitAction = menu.addAction('Quit')
quitAction.triggered.connect(quit)
systrayico.setContextMenu(menu)
app.exec_()
sys.exit()
