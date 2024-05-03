class Point: 
    def __init__(self, x = 1, y = 1):
        self.x = x 
        self.y = y
    
    def get_score(self):
        return self.x + self.y
    
    def __str__(self):
        return (f"({self.x}, {self.y})")

    def get_middle_point(self, other):
        middle_x = (self.x + other.x) // 2
        middle_y = (self.y + other.y) // 2

        return Point(middle_x, middle_y)
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

points = [Point(), Point(10, 20), Point(20, 30)]
for point in points:
    print(point.get_score(), point)
print(type(points[0]))
temp = points[0].get_middle_point(points[1])
print(type(temp))
print(temp)
point4 = Point(10, 20)
print(points[1] == point4)
print(points[0] == point4)
print(point4 == 2)