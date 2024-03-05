def read_file(filename):
    input_file = open(filename, 'r')
    contents = input_file.read().split("\n")
    input_file.close()

    a_list = []
    for words in contents:
        a_list.append(words)
    return a_list

def create_data_dictionary(regions, data_list):
    a_dict = {}
    
    for region in regions:
        a_dict[region] = 0  
    
    for string in data_list:
        numbers = string.split()
        for i, region in enumerate(regions):
            a_dict[region] += int(numbers[i]) if i < len(numbers) else 0  

    return a_dict

def create_continent_regions_dictionary(contents):
    a_dict = {}
    for letters in contents:
        x = letters.split(":")
        if len(x) == 2:  # Ensure there are two parts after splitting
            continent = x[0]
            regions = x[1].split(",")
            if continent not in a_dict:
                a_dict[continent] = []
            a_dict[continent] = regions
    return a_dict


def create_continents_data_dictionary(a_dict):
    for key, _ in a_dict.items():
        a_dict[key] = []
    return a_dict

def create_data_dictionary(regions, data_list):
    a_dict = {}
    # add the regions as keys in dictionary first
    
    column_sum = [0] * len(data_list[0].split())

    for region in regions:
        a_dict[region] = None

    for string in data_list: 
        numbers = string.split() # split by whitespace
        for i in range(len(numbers)):
            column_sum[i] += int(numbers[i])

    for i, key in enumerate(a_dict.keys()):
        a_dict[key] = column_sum[i]
    return a_dict

def process_data(continents_data_dict, continent_regions_dict, data_dict):
    for continent, regions in continent_regions_dict.items():
        total_arrivals = sum(data_dict.get(region, 0) for region in regions)
        if continent in continents_data_dict:
            continents_data_dict[continent].append(total_arrivals)


def print_title():
    print("Monthly NZ-resident traveller arrivals (Nov23 - Jan24)")
    print("======================================================")

def print_table(continents_data_dict, number_of_rows):
    sorted_continents = sorted(continents_data_dict.keys())
    
    print("".join(f"{continent:>10}|" for continent in sorted_continents))
    
    for i in range(number_of_rows):
        print("".join(f"{continents_data_dict[continent][i]:>10}|" for continent in sorted_continents))

def main():
    regions_file = input("Enter a filename for reading regions: ")
    continents_file = input("Enter a filename for reading continents: ")

    print()  # Add an empty line for spacing

    regions = read_file(regions_file)
    continent_regions_dict = create_continent_regions_dictionary(read_file(continents_file))  # Use continents_file directly
    create_continents_data_dictionary(continent_regions_dict)
    
    print("Entering loop...")  # Debug print
    for _ in range(3):  # Repeat for 3 months
        arrivals_file = input("Enter a filename for reading arrivals data: ")
        print()  # Add an empty line for spacing
        arrivals_data = read_file(arrivals_file)
        data_dict = create_data_dictionary(regions, arrivals_data)
        process_data(continent_regions_dict, continent_regions_dict, data_dict)  # Pass correct arguments
    print("Exiting loop...")  # Debug print
    
    print_title()
    print_table(continent_regions_dict, 3)



main()