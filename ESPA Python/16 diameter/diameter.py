import sys
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def dist(self, other):
        d = (self.x - other.x) ** 2 + (self.y - other.y) ** 2
        return math.sqrt(d)
    def __str__(self):
        return ("(%.2f,%.2f)" % (self.x, self.y))

inp = sys.stdin.readlines()
inp = [list(map(float, x.split())) for x in inp]

points = [Point(x[0], x[1]) for x in inp]

maxDist = 0
for i in range(len(points)):
    for j in range(i+1, len(points)):
        dist =  points[i].dist(points[j])
        if maxDist < dist:
            maxDist = dist
        print (points[i], points[j], points[i].dist(points[j]))

print ("%.2f" % maxDist)
