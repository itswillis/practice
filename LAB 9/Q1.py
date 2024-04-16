class Address: 
    def __init__(self, street = "", city = "", postal_code = 0, is_residental = False):
        self.street = street
        self.city = city
        self.postal_code = postal_code
        self.is_residental = is_residental
    
    def get_postal_code(self):
        return self.postal_code
    
    def calculate_postage_cost(self):
        if self.is_residental == True: 
            return ("$2")
        else: 
            return ("$4")
    
    def __str__(self): 
        return(f"Shipping to {self.street}, {self.city}({self.postal_code}) is {self.calculate_postage_cost()}.")

address1 = Address("34 Princess Street", "Auckland", 1010, False)
address3 = Address("1023 Westmoreland Street", "Auckland", 1021, True)
print(address1)
print(address3)
print(address1 == address3)
print(type(address1))
