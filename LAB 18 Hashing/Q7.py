def get_simple_numeric_hash(key, table_size):
    square = str(key ** 2)
    square_remove = square[1:-1]
    square_remove = int(square_remove)
    return (square_remove%table_size)


print(get_simple_numeric_hash(655, 13))
print(get_simple_numeric_hash(654, 13))
print(get_simple_numeric_hash(653, 13))