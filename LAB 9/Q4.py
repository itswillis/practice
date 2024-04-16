class Triangle: 
    def __init__(self, base = 1, height = 1):
        self.base = base
        self.height = height
    def get_base(self):
        return (self.base)
    def get_height(self):
        return (self.height)
    def get_area(self):
        return (0.5*self.base*self.height)
    
    def __str__(self):
        return (f"Triangle with base: {self.base}, height: {self.height}, and area: {self.get_area():.2f}")
    
class Block: 
    def __init__(self, base = 1, height = 1): 
        self.triangle = [Triangle(base, height)]

    def add_triangle(self, base, height):
        new_triangle = Triangle(base, height)
        self.triangle.append(new_triangle)

    def get_triangle(self, index):
        return (self.triangle[index])
    
    def __str__(self):
        return '\n'.join([str(item) for item in self.triangle])


block1 = Block(10.5, 25.1)
block1.add_triangle(22, 43)
block1.add_triangle(15.5, 14)
print(block1)
print(type(block1))
triangle1 = block1.get_triangle(2)
print(type(triangle1))
print(triangle1)
print(block1.get_triangle(1))