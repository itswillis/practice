def create_odd_even_dictionary(numbers):
    a_dict = {}
    for num in numbers:
        key = num % 2 
        if key not in a_dict: 
            a_dict[key] = []
        a_dict[key].append(num)
    
    return a_dict
        
        

numbers =  [3, 25, 23, 13, 19, 34, 56, 44, 21, 46]
a_dict = create_odd_even_dictionary(numbers)
for key in sorted(a_dict.keys()):
    print(key, a_dict[key])