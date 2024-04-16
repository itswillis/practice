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

cone1 = Cone()
print("{:.2f}".format(cone1.get_circle_base_area()))
print("{:.2f}".format(cone1.get_volume()))
cone2 = Cone(4, 6)
print("{:.2f}".format(cone2.get_circle_base_area()))
print("{:.2f}".format(cone2.get_volume()))
print(type(cone1))