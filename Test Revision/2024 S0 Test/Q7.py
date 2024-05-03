def get_valid_fruit_names(fruit_list, number_required):
    valid_list = []

    while len(valid_list) != number_required:
        fruit_name = input("Enter a fruit name: ")
        if fruit_name in fruit_list:
            if fruit_name not in valid_list:
                valid_list.append(fruit_name)
    
    return valid_list
            




fruit_list = ['orange', 'apple', 'pear', 'lemon', 'kiwifruit']
print(get_valid_fruit_names(fruit_list, 3))