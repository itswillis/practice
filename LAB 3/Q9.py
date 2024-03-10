# the function returns a tuple containing the value at the given index from the parameter list
def get_tuple_at(names, index):
    return (names[index], )


my_tuple = get_tuple_at(['May', 'Amy', 'Alan'], 1)
print(my_tuple)
print(type(my_tuple))
print(get_tuple_at(['May', 'Amy', 'Alan'], 0))