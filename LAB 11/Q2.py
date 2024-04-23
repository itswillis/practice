def create_dictionary(data):
    result_dict = {}

    for sub_list in data:

        key = sum(sub_list)

        if key in result_dict:
            result_dict[key].append(sub_list)
        else:
            result_dict[key] = [sub_list]

    return result_dict 
    


data = [[1, 3, 1], [3, 6, 9], [2, 5, 1], [1, 1, 2, 1]]
dict1 = create_dictionary(data)
print(type(dict1))
for key in sorted(dict1):
    print(key, dict1[key])
