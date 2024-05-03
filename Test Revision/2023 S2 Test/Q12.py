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

class Student: 
    def __init__(self, name, username, max_count = 1):
        self.name = name
        self.username = username
        self.max_count = max_count
        self.courses = []

    def enrol(self, course):
        if len(self.courses) < self.max_count:
            self.courses.append(course)
            course.register()

    def un_enrol(self, course):
        if course in self.courses: 
            self.courses.remove(course)
            course.un_register()
    
    def __str__(self):
        courses = ', '.join(str(course) for course in self.courses)
        if not self.courses: 
            return (f"{self.name}: Not enrolled in any courses.")
        return (f"{self.name} enrolled: [{courses}] course(s).")


	
	
course1 = Course('Python101')
student1 = Student("Dick Smith", "dsmil123")
student2 = Student("Michael Hill", "mhil456", 2)
student1.enrol(course1)
print(student1)
student2.enrol(course1)
print(student2)
print(course1)
student1.un_enrol(course1)
print(course1)
print(student1)