def get_lucas_list(n):
    if n == 1:
        return [2] # first lucas
    if n == 2:
        return [2, 1] # first two lucas
    else:
        lucas_list = get_lucas_list(n-1)
        lucas_list.append(lucas_list[-1] + lucas_list[-2])
        return lucas_list
    
data = get_lucas_list(100)
print(data)
