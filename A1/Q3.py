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
        self.process(months_list) # call the process method directly 

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
    
    def process_data_per_month(self, month_name):
        filename = f'{self.region_code}_{month_name}.txt'
        input_file = open(filename, 'r')
        arrival_data = input_file.read().split()
        input_file.close()

        total_arrivals = sum(int(arrival) for arrival in arrival_data)
        arrival_object = Arrival(month_name, total_arrivals)
        self.arrivals_list.append(arrival_object)

    def process(self, months_list):
        for month in months_list:
            self.process_data_per_month(month) # process each month one by one to read in the months_list

    def __str__(self): 
        region_information =  '\t'.join(str(arrival) for arrival in self.arrivals_list) # detailed statistics for each month
        return (f"{self.region_code}({self.get_total_number_of_arrivals()})\t{region_information}")
    
months_list = ['NOV', 'DEC']
au = Region("Australia", "AU", months_list)
print(au)