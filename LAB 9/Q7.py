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

line1 = PolyLine()
line1.add_point(10, 20)
line1.add_point(20, 30)
line2 = PolyLine();
line2.add_point(10, 20)
line2.add_point(20, 30)
line2.add_point(30, 40)
print(line1)
print(line2)
print("The total length is {:.2f}".format(line1.get_total_length()))
print("The total length is {:.2f}".format(line2.get_total_length()))