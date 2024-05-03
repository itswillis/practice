class Course: 
    def __init__(self, name = "UNKNOWN", number_of_students = 0): 
        self.name = name 
        self.number_of_students = number_of_students

    def __str__(self): 
        return f"{self.name}({self.number_of_students})"
    
    def register(self):
        self.number_of_students += 1
    
    def un_register(self):
        if self.number_of_students > 0: 
            self.number_of_students -= 1

    
course1 = Course()
course2 = Course('Python101')
print(course1)
print(course2)
print(type(course1))
print(type(course1.name)) #check the type
course1.register()
course1.register()
print(course1)
course1.un_register()
print(course1)


course1 = Course('Python101')
course1.un_register()
print(course1)
course1.un_register()
print(course1)