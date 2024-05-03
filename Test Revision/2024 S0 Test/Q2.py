def create_dictionary(data):
    a_dict = {}
    for sublist in data:
        sum_sublist = sum(sublist)

        if sum_sublist not in a_dict:
            a_dict[sum_sublist] = [sublist]
        else:
            a_dict[sum_sublist].append(sublist)
    
    return a_dict


data = [[1, 3, 1], [3, 6, 9], [2, 5, 1], [1, 1, 2, 1]]
dict1 = create_dictionary(data)
print(type(dict1))
for key in sorted(dict1):
    print(key, dict1[key])