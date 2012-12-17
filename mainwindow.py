from PySide.QtCore import Qt
from PySide.QtGui import QMainWindow,QGraphicsScene,QGraphicsView,QApplication


class MainWindow(QMainWindow):
	def __init__(self, x_pox, y_pos):
		super(MainWindow, self).__init__()
		self.scene = QGraphicsScene()
		self.scene.addText("Hello, world!")
		self.view = QGraphicsView(self.scene)
		self.setGeometry(x_pox, 23, 300, 400)

		self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
		self.setWindowFlags(self.windowFlags() | Qt.Tool)
		self.setWindowFlags(self.windowFlags() | Qt.CustomizeWindowHint)
		self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
		self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint)
		
		super(MainWindow, self).setCentralWidget(self.view)
		
	def closeEvent(self, event):
		event.ignore()
		self.hide()


