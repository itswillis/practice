class Patient:
    def __init__(self, name, nhi_number):
        self.name = name
        self.nhi_number = nhi_number
    def __str__(self):
       return "{}({})".format(self.name, self.nhi_number)
    
    def __eq__(self, other):
        if isinstance(other, Patient):
            return self.nhi_number == other.nhi_number
        return False
    
    def __lt__(self, other):
        return self.nhi_number < other.nhi_number


patient1 = Patient("Alan Smith", "dsm1234")
patient2 = Patient("Michael Hill", "mhi2456")
patient3 = Patient("Vincent Smith", "vsm1234")
print(patient1 == patient2)
print(patient1 == patient3)
print(patient2 == patient3)
print(patient1 < patient2)
print(patient1 < patient3)
print(patient1 == 'mhi2456')
print(patient2 == 'mhi2456')
data = [patient1, patient2, patient3]
data.sort()
for person in data:
    print(person)