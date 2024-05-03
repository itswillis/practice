def calculate_percentage_change(initial, revised):
    percentage_change = ((revised - initial) / abs(initial)) * 100
    percentage_change = round(percentage_change)
    return percentage_change

print(calculate_percentage_change(60, 71))
print(calculate_percentage_change(71, 60))
print(calculate_percentage_change(-60, -71))
print(calculate_percentage_change(-71, -60))
print(calculate_percentage_change(-7, 1))
print(calculate_percentage_change(2, -5))