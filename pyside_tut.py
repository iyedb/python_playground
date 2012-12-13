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

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
	def closeEvent(self, event):
		event.ignore()
		self.hide()
		
		

def _quit():
	app.quit()
	qDebug('bye!')
	
app = QApplication(sys.argv)
systrayico = QSystemTrayIcon(QIcon("icon18.gif"))
systrayico.show()
systrayico.showMessage('hello', 'hello', msecs=2000)

def what(thereason):
	print thereason
	if thereason == QSystemTrayIcon.ActivationReason.Trigger:
		main_window.show()
		

menu = QMenu()
quitAction = menu.addAction('Quit')
quitAction.triggered.connect(_quit)
systrayico.activated.connect(what)

systrayico.setContextMenu(menu)

scene = QGraphicsScene()
scene.addText("Hello, world!")

view = QGraphicsView(scene)


main_window = MainWindow()
main_window.setCentralWidget(view)



app.exec_()
sys.exit()
