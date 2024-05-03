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
    
def selection_sort(patients): 
    for position in range(len(patients) -1, 0, -1):
        position_largest = 0 
        for i in range(1, position):
            if patients[i].nhi_number > patients[position_largest].nhi_number:
                position_largest = i
        if patients[position_largest].nhi_number > patients[position].nhi_number: 
            patients[position_largest], patients[position] = patients[position], patients[position_largest]

data = [Patient("David Chan", "bch5654"), Patient("Alan Mak", "bet5642"), Patient("Alice Wong", "aet2564")]
selection_sort(data)
for person in data:
    print(person)