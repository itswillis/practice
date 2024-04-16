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

    def get_total_length(self):
        total = 0 
        for i in range(len(self.points) - 1):
            total += self.points[i].get_distance(self.points[i+1])
        return total


    def __str__(self):
        return "->".join(str(p) for p in self.points)

class Grid:
    def __init__(self, x1 = 1, y1 = 1, x2 = 1, y2 = 1):
        self.top_left = Point(x1, y1)
        self.bottom_right = Point(x2, y2)
        self.point = []

    def add_point(self, point):
        if (self.top_left.x <= point.x <= self.bottom_right.x) and (self.top_left.y <= point.y <= self.bottom_right.y):
            self.point.append(point)
            return True
        else:
            return False
        
    def get_point(self, index): 
        return self.point[index]
        
points = [Point(2, 2), Point(7, 6), Point(24, 36), Point(53, 85), Point(3, 24)]
grid1 = Grid(1, 1, 10, 10)
for element in points:
    print(grid1.add_point(element))
print(grid1.get_point(0))
point1 = grid1.get_point(1)
print(type(point1))
print(point1)



