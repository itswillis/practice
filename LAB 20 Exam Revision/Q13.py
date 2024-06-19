class LinearHashTable:
    def __init__(self, size=7):
        self.size = size
        self.slots = [None] * size
        
    def __str__(self):
        return str(self.slots)
        
    def get_hash_code(self, key):
        return key % self.size
        
    def clear(self):
        self.slots = [None] * self.size
        
    def is_empty(self):
        return self.__len__() == 0
        
    def __len__(self):
        count = 0
        for item in self.slots:
            if item != None:
                count += 1
        return count
        
    def load_factor(self):
        return self.__len__() / self.size
        
    def rehash(self):
        old_slots = self.slots
        self.size *= 2
        self.slots = [None] * self.size
        for key in old_slots:
            if key is not None:
                self._put_rehash(key)
        
    def _put_rehash(self, key):
        index = self.get_hash_code(key)
        while self.slots[index] is not None:
            index = (index + 1) % self.size
        self.slots[index] = key
        
    def put(self, key):
        if self.__len__() >= self.size:
            raise IndexError("ERROR: The hash table is full.")
        index = self.get_hash_code(key)
        while self.slots[index] is not None:
            index = (index + 1) % self.size
        self.slots[index] = key
        if self.load_factor() > 0.7:
            self.rehash()

hashtable = LinearHashTable(5)
print(f"Size data field: {hashtable.size}")
print(f"Table data field: {hashtable.slots}")
numbers = [2, 5, 7, 15]
for number in numbers:
    hashtable.put(number)
print(f"Size data field: {hashtable.size}")
print(f"Table data field: {hashtable.slots}")
