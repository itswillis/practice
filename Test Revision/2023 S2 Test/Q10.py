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

def linear_search_by_nhi(patients_list, target):
    for i, patient in enumerate(patients_list):
        if target in patient.nhi_number:
            return (True, i+1)

    return (False, i+1)



data = [Patient("Raymond Ng", "aga2962"), Patient("Alice Kim", "akm2564"), Patient("John Zhang", "ara3443"),  Patient("Albert Mak", "bet9542"), Patient("David Chan", "bro2123")]
print(linear_search_by_nhi(data, 'akm2564'))
print(linear_search_by_nhi(data, 'bro2546'))

data = [Patient("Raymond Ng", "aga2962"), Patient("Alice Kim", "akm2564"), Patient("John Zhang", "ara3443"),  Patient("Albert Mak", "bet9542"), Patient("David Chan", "bro2123")]
print(linear_search_by_nhi(data, 'ara3443'))
print(linear_search_by_nhi(data, 'wah5645'))