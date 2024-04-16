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

class Person: 
    def __init__(self, name, street = "", city = "", postal_code = 0, is_residental = False):
        self.name = name 
        self.address = Address(street, city, postal_code, is_residental)

    def get_address(self):
        return(self.address)
    
    def __str__(self):
        return(f"{self.name}: {self.address}")

person1 = Person("Dick Smith", "34 Princess Street", "Auckland", 1010, False)
person2 = Person("Michael Hill", "1023 Westmoreland Street", "Auckland", 1021, True)
print(person1)
print(person2)
print(type(person1))
item = person1.get_address()
print(type(item))
print(item)