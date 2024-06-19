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

priority_queue = PriorityQueue()
priority_queue.add_all_ignore_order([6, 7, 10, 9, 22, 45, 8])
priority_queue.percolate_up(7)
print(priority_queue)
print(priority_queue.number_of_swaps)