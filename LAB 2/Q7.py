def print_table(continents_data_dict, number_of_rows):
    sorted_continents = sorted(continents_data_dict.keys())
    
    print("".join(f"{continent:>10}|" for continent in sorted_continents))
    
    for i in range(number_of_rows):
        print("".join(f"{continents_data_dict[continent][i]:>10}|" for continent in sorted_continents))


# Example usage:
data_dict = {'Europe': [6270, 4830, 13160], 'America': [11810, 11200, 17110], 'Oceania': [116490, 109200, 127980]}
print_table(data_dict, 3)
