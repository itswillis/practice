class Arrival: 
    def __init__(self, month = 'JAN', number_of_arrivals = 0):
        self.month = month 
        self.number_of_arrivals = number_of_arrivals

    def get_number_of_arrivals(self): 
        return self.number_of_arrivals
    
    def __str__(self): 
        return (f"{self.month}: {self.number_of_arrivals:>6}")

class Region:
    def __init__(self, region_name, region_code, months_list = []): 
        self.region_name = region_name
        self.region_code = region_code
        self.months_list = months_list
        self.arrivals_list = []

    def get_arrivals_list(self): 
        return (self.arrivals_list)
    
    def add_arrival(self, month, value):
        new_arrivals = Arrival(month, value)
        self.arrivals_list.append(new_arrivals)
    
    def get_total_number_of_arrivals(self): 
        total_arrivals = 0 
        for arrival in self.arrivals_list:
            total_arrivals += arrival.get_number_of_arrivals()
        return total_arrivals

    def __str__(self): 
        region_information =  '\t'.join(str(arrival) for arrival in self.arrivals_list) # detailed statistics for each month
        return (f"{self.region_code}({self.get_total_number_of_arrivals()})\t{region_information}")


months_list = ['NOV', 'DEC', 'JAN', 'FEB']
au = Region("Australia", "AU", months_list)
au.add_arrival("NOV", 317760)
au.add_arrival("DEC", 266960)
au.add_arrival("JAN", 300480)
au.add_arrival("FEB", 226180)
print(au.get_total_number_of_arrivals())  # 1111380  
print(au)   # AU(1111380)\tNOV: 317760\tDEC: 266960\tJAN: 300480\tFEB: 226180
print(type(au)) # <class '__main__.Region'>
values = au.get_arrivals_list()
print(type(values[0])) # <class '__main__.Arrival'>