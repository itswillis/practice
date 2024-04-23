class Point:
    def __init__(self, x = 1, y = 1):
        self.x = x
        self.y = y

    def get_score(self):
        return (self.x + self.y)

    def get_middle_point(self, other):
        middle_x = (self.x + other.x) // 2
        middle_y = (self.y + other.y) // 2

        return Point(middle_x, middle_y)
        

    def __str__(self):
        return (f"({self.x}, {self.y})")

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

class ConnectedLine:
    def __init__(self):
        self.points = [Point(0,0)]

    def add_point(self, point):
        self.points.append(point)

    def get_total_score(self):
        total = 0
        for point in self.points:
            total += point.get_score()
        return total

    def get_middle_points(self):
        middle_points = []
        for i in range(len(self.points) - 1):
            middle = self.points[i].get_middle_point(self.points[i + 1])
            middle_points.append((middle.x, middle.y))
        return middle_points
    
    def __str__(self):
        if len(self.points) == 1:
            return ""
        joined = ' -> '.join(str(p) for p in self.points)
        return joined

    

points = [Point(), Point(10, 20), Point(20, 30)]
line = ConnectedLine()
for point in points:
    line.add_point(point)
print(line, type(line))
print(line.get_total_score())
result = line.get_middle_points()
print(type(result))
print('\n'.join(str(point) for point in result))
line2 = ConnectedLine() 
print(line2)
print(line)
    

        
