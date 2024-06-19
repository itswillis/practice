def get_lucas_term(n):
    if n == 1:
        return 2
    if n == 2:
        return 1
    else:
        return get_lucas_term(n-1) + get_lucas_term(n-2)



print(get_lucas_term(6))
