def recursive(x, y):
    if x == y:
        return 0
    else:
        return recursive(x-1, y) + 1
    


print("Result =", recursive(2, 3))