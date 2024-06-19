class PriorityQueue:
    def __init__(self):
        self.binary_heap = [0]
        self.size = 0
        self.number_of_swaps = 0

    def __str__(self):
        return str(self.binary_heap)

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size
    
    def add_all_ignore_order(self, a_list):
        for values in a_list:
            self.binary_heap.append(values)
            self.size += 1
    
    def percolate_up(self, index):
        while index // 2 > 0:
            if self.binary_heap[index] < self.binary_heap[index // 2]:
                self.binary_heap[index], self.binary_heap[index // 2] = self.binary_heap[index // 2], self.binary_heap[index]
                self.number_of_swaps += 1
            index = index // 2

    def insert(self, element):
        self.binary_heap.append(element)
        self.size += 1
        self.percolate_up(self.size)

priority_queue3 = PriorityQueue()
priority_queue3.insert(6)
priority_queue3.insert(9)
priority_queue3.insert(8)
priority_queue3.insert(5)
print(priority_queue3)
print(len(priority_queue3))
print(priority_queue3.number_of_swaps)