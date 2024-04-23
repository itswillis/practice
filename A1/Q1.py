class Arrival: 
    def __init__(self, month = 'JAN', number_of_arrivals = 0):
        self.month = month 
        self.number_of_arrivals = number_of_arrivals

    def get_number_of_arrivals(self): 
        return self.number_of_arrivals
    
    def __str__(self): 
        return (f"{self.month}: {self.number_of_arrivals:>6}")

data1 = Arrival("NOV", 317760)
data2 = Arrival("FEB", 6180)
data3 = Arrival()
print(data1)
print(data2)
print(data3)
print(type(data1))
print(data1.get_number_of_arrivals())