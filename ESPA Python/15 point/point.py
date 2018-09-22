import math
import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def dist(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    def __str__(self):
        return str("(%.2f,%.2f)" % (self.x, self.y))

inp = sys.stdin.readlines()
inp = [list(map(float, x.split())) for x in inp]
print (inp)

maxDist = 0
maxPoint = Point(0,0)
for x in inp:
    point = Point(x[0], x[1])
    if (maxDist < point.dist()) :
        maxDist = point.dist()
        maxPoint = point
    elif maxDist == point.dist() and point.x > maxPoint.x:
        maxDist = point.dist()
        maxPoint = point

print (maxPoint)
