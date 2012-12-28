from PySide.QtCore import Qt, QUrl, QSize
from PySide.QtGui import QMainWindow, QGraphicsScene, QGraphicsView, QApplication, QFont, QFontMetrics, QFontInfo
from PySide.QtWebKit import QWebView, QWebPage
from lxml import etree
import urllib2
import codecs
import StringIO
from mako.template import Template


class MainWindow(QMainWindow):
	def __init__(self, x_pox, y_pos, width, height):
		super(MainWindow, self).__init__()

		self.setGeometry(x_pox, y_pos, width, height)
		self.setMaximumSize(width, height)
		self.setMinimumSize(width, height)
		self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
		self.setWindowFlags(self.windowFlags() | Qt.Tool)
		self.setWindowFlags(self.windowFlags() | Qt.CustomizeWindowHint)
		self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
		self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint)
		self.view = QWebView(self)
		self.view.page().setViewportSize(QSize(width, height))
		super(MainWindow, self).setCentralWidget(self.view)
	
	def showEvent(self, event):
		self.view.setHtml( self.generate_html() )

	def generate_html(self):
		doc = urllib2.urlopen('http://news.ycombinator.com/')
		unicode_string = doc.read().decode('utf-8')
		e = etree.fromstring(unicode_string, etree.HTMLParser())

		urls = []
		for i in e.xpath('//td/a'):
			if len(i.getparent().keys()) == 1 and i.getparent().values()[0] == 'title':
				if isinstance(i.text, str):
					u_s = i.text.decode('utf-8')
				else:
					u_s = i.text
				if u_s == u'More':
					continue
				subtext = i.getparent().getparent().getnext()
				urls.append(u_s)

		template_file = QUrl.fromLocalFile('template.html')	
		template = Template( filename=template_file.path() )	
		return template.render_unicode(rows=urls)




