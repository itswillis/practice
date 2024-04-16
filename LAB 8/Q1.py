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




cone1 = Cone()
print(cone1.get_radius())
cone2 = Cone(6, 12)
print(cone2.get_radius())
cone1.set_radius(-1)
print(cone1.get_radius())
cone1.set_radius(12)
print(cone1.get_radius())
cone3 = Cone(1, 1)
print(cone1 == cone3)
print(cone1.get_height())
cone1.set_height(-10)
print(cone1.get_height())