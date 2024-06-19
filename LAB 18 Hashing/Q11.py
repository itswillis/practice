class SimpleHashTable:
    def __init__(self, size=7):
        self.size = size
        self.slots = [None] * self.size

    def __str__(self):
        return str(self.slots)

    def get_hash_index(self, key):
        return key % self.size

    def put(self, key):
        if self.is_full():
            raise IndexError("ERROR: The hash table is full.")
        index = self.get_hash_index(key)
        while self.slots[index] is not None:
            index = (index + 1) % self.size
        self.slots[index] = key

    def is_empty(self):
        return all(slot is None for slot in self.slots)

    def is_full(self):
        return all(slot is not None for slot in self.slots)

    def clear(self):
        self.slots = [None] * self.size

    def __len__(self):
        return sum(1 for slot in self.slots if slot is not None)