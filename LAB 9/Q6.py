from math import sqrt

class Point: 
    def __init__(self, x = 1, y = 1):
        self.x = x 
        self.y = y
    def __str__(self):
        return(f"({self.x}, {self.y})")
    
    def get_distance(self, other):
        d = (sqrt(((other.x - self.x)**2) + ((other.y - self.y) ** 2)))
        return d 

class PolyLine: 
    def __init__(self):
        self.points = []
    
    def get_point(self, index):
        return self.points[index]
    
    def add_point(self, x, y):
        new_point = Point(x, y)
        self.points.append(new_point)
    
line1 = PolyLine()
line1.add_point(10, 20)
line1.add_point(20, 30)
point1 = line1.get_point(1)
print(type(line1))
print(type(point1))
print(point1)

line1 = PolyLine();
line1.add_point(10, 20)
line1.add_point(20, 30)
line1.add_point(30, 40)
print(line1.get_point(0))
print(line1.get_point(1))
print(line1.get_point(2))