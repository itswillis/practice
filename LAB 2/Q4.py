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

regions = ['AU', 'US', 'FJ']
contents = ['24730 3430 3650', '23610 3320 3290', '22470 2600 3910', '23920 2460 3470']
a_dict = create_data_dictionary(regions, contents)
for key in sorted(a_dict):
    print(key, a_dict[key])