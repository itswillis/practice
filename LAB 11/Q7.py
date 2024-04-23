def get_valid_fruit_names(fruit_list, number_required):

    resultant = []

    while (len(resultant)) != number_required:
        fruit = input("Enter a fruit name: ")
        if fruit in fruit_list:
            if fruit not in resultant: 
                resultant.append(fruit)

    return resultant

fruit_list = ['orange', 'apple', 'pear', 'lemon', 'kiwifruit']
print(get_valid_fruit_names(fruit_list, 3))
    
