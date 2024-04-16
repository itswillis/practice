from math import pi
class Cone:
    def __init__ (self, radius = 1, height = 1):
        self.radius = radius 
        self.height = height 
    def get_radius(self):
        return self.radius
    def set_radius(self, base_length):
        if base_length > 0:
            self.radius = base_length
    def get_height(self):
        return self.height
    def set_height(self, height):
        if height > 0: 
            self.height = height
    def get_circle_base_area(self): 
        return (pi*(self.radius**2))
    def get_volume(self):
        return ((pi*(self.radius**2)*self.height)/3)
    def __repr__(self):
        return (f"Cone({self.radius}, {self.height})")
    def __str__(self):
        return (f"A cone with a circle base area of {self.get_circle_base_area():.2f} and a volume of {self.get_volume():.2f}.")
    

cone1 = Cone(2, 4)
print(cone1)
print(type(cone1))
print(repr(cone1))
cone2 = Cone()
print(cone2)
print(repr(cone2))