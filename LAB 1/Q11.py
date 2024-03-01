def create_odds(max_value):
    result = [values for values in range(1,max_value) if values % 2 != 0]
    return result

print(create_odds(22))
print(create_odds(31))