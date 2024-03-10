def append_double_to(element, values=None):
    if values is None:
        values = []
    values.append(element*2)
    return values

my_list = append_double_to(100)
print(my_list)
my_list = append_double_to(200)
print(my_list)