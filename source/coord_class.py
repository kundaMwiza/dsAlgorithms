import math

class Coordinate:
    """
    Coordinate class storing euclidean coordinates
    input: x, y floats
    """
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return '<x_coord: '+str(self.x)+" y_coord: "+str(self.y)+'>'
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

center = Coordinate(1,5)
side = Coordinate(2,3)
print(center)
print(center.distance(side))
print(type(Coordinate))
