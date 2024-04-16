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
    


point1 = Point(10,20)
point2 = Point(30,40)
print(point1, point2)
print("The distance between two points is {:.2f}.".format(point1.get_distance(point2)))
print(type(point1))
print(type(point2))
