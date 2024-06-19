class SimpleHashTable:
    def __init__(self, size=7):
        self.size = size  
        self.slots = [None] * self.size  

    def get_hash_index(self, key):
        return key % self.size

    def __str__(self):
        return str(self.slots)

    def put(self, key):
        original_index = self.get_hash_index(key)
        index = original_index
        while self.slots[index] is not None:
            index = (index + 1) % self.size
        self.slots[index] = key



my_hash_table = SimpleHashTable(13)
my_hash_table.put(13)
my_hash_table.put(26)
my_hash_table.put(14)
my_hash_table.put(15)
my_hash_table.put(16)
my_hash_table.put(17)
print(my_hash_table)