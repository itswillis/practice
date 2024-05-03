def calculate_percentage_change(initial, revised):
    percentage_change = ((revised - initial) / abs(initial)) * 100
    percentage_change = round(percentage_change)
    return percentage_change

def calculate_changes(numbers): 
    changes_list = []
    for i in range(len(numbers) - 1):
        current = numbers[i] 
        next = numbers[i+1]
        changed = calculate_percentage_change(current, next)

        changes_list.append(changed)
    return changes_list

print(calculate_changes([60, 71, 60]))