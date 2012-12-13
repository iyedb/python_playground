#!/usr/bin/env python

import sys
from PySide.QtCore import *
from PySide.QtGui import QMainWindow,QGraphicsScene,QGraphicsView,QApplication,QSystemTrayIcon,QMenu, QIcon

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
		self.scene = QGraphicsScene()
		self.scene.addText("Hello, world!")
		self.view = QGraphicsView(self.scene)
		super(MainWindow, self).setCentralWidget(self.view)
		
	def closeEvent(self, event):
		event.ignore()
		self.hide()
		
		
#refactor 		
def _quit():
	app.quit()
	qDebug('bye!')
	
def show_window(thereason):
	print thereason
	if thereason == QSystemTrayIcon.ActivationReason.Trigger:
		main_window.showMaximized()


#create the QApplication instance before any other widget
app = QApplication(sys.argv)		
main_window = MainWindow()		
	
	
systrayico = QSystemTrayIcon(QIcon("icon18.gif"))
menu = QMenu()
quitAction = menu.addAction('Quit')
quitAction.triggered.connect(_quit)
systrayico.activated.connect(show_window)
systrayico.setContextMenu(menu)
systrayico.show()

print app.desktop().screenGeometry(app.desktop().primaryScreen()).topLeft()
print app.desktop().screenGeometry(app.desktop().primaryScreen()).bottomRight()

print app.desktop().availableGeometry(app.desktop().primaryScreen()).topLeft()
print app.desktop().availableGeometry(app.desktop().primaryScreen()).bottomRight()

sys.exit(app.exec_())



	
