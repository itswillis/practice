class Student: 
    def __init__(self, name = "UNKNOWN", age = 1, student_id = 1):
        self.name = name
        self.age = age 
        self.student_id = student_id
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_student_id(self):
        return self.student_id
    
    def __str__(self):
        return (f"{self.name}({self.age}),{self.student_id}")
    
    def __eq__(self, other):
        if self.student_id == other.student_id:
            return True
        return False
    
    def __lt__(self, other): 
        if self.age < other.age:
            return True
        return False
    
    def __le__(self, other):
        if self.age <= other.age:
            return True
        return False
    
    def __gt__(self, other):
        if self.age > other.age:
            return True
        return False
    
    def __ge__(self, other):
        if self.age >= other.age:
            return True
        return False


student1 = Student()
student2 = Student("Dick Smith", 56, 234567)
print(student1, student2, student1 == student2)
print(student1 < student2)
print(student1 >= student2)
student3 = Student("Peter Smith", 28, 234567)
print(student1, student3, student1 == student3)
print(student1 < student3)
print(student1 >= student3)