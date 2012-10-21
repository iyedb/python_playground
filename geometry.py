from math import atan2
from math import pi


class Angle:
	def __init__(self, begin, end):
		self.begin = begin
		self.end = end
	
	def contains(self, x, y):
		rad = atan2(x,y)
		alpha = rad/pi * 180
		if alpha < 0:
			alpha = alpha + 360
		
		if alpha >= self.begin and alpha < self.end:
			return True
		return False
		
	
	def f(self, x, y):
		z = atan2(x,y)





class Circle:
	def __init__(self, sector):
		self.sector = sector
		self.sectors = []
	def looper(self):
		for i in range(self.sector):
			print str(self.sectors[i].begin) + ":" + str(self.sectors[i].end)
	def divide(self):
		start = 0
		increment = 360 / self.sector
		for i in xrange(self.sector):
			a = Angle(start, start + increment)
			self.sectors.append(a)
			start = start + increment
	
	def getContainerSector(self, x,y):
		for i in self.sectors:
			if i.contains(x,y):
				return i
			
	




c = Circle(6)
c.divide()
c.looper()

angle = c.getContainerSector(-1,1)

print "the containing sector is " + str(angle.begin) + ":" + str(angle.end)
