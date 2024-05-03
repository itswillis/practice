def get_pair_sum(numbers): 
    sum_list = []
    for i in range(len(numbers) - 1):
        current = numbers[i]
        next = numbers[i+1]
        null = 0

        try: 
            current = float(numbers[i])
            next = float(numbers[i+1])
            sum_list.append(current + next)
        except: 
            sum_list.append(null)

    return sum_list


	
print(get_pair_sum([2, '8', 9, 1, 6, 5]))