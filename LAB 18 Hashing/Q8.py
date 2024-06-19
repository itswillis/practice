def get_weighted_hash(key, table_size):
    hash_value = 0
    
    for index, char in enumerate(key):
        weight = index + 1
        weighted_ascii = ord(char) * weight
        hash_value += weighted_ascii
    return hash_value % table_size


print(get_weighted_hash('cat', 13))
print(get_weighted_hash('dog', 13))