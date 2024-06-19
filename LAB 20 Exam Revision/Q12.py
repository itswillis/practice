class PriorityQueue:
    def __init__(self):
        self.binary_heap = [0]  # Heap with a placeholder for easier child/parent calculations
        self.size = 0

    def percolate_up(self, i):
        while i // 2 > 0 and self.binary_heap[i] > self.binary_heap[i // 2]:
            self.binary_heap[i], self.binary_heap[i // 2] = self.binary_heap[i // 2], self.binary_heap[i]
            i = i // 2

    def insert(self, item):
        self.binary_heap.append(item)
        self.size += 1
        self.percolate_up(self.size)

    def get_larger_child_index(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.binary_heap[i * 2] > self.binary_heap[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def percolate_down(self, i):
        while i * 2 <= self.size:
            mc = self.get_larger_child_index(i)
            if self.binary_heap[i] < self.binary_heap[mc]:
                self.binary_heap[mc], self.binary_heap[i] = self.binary_heap[i], self.binary_heap[mc]
            i = mc

    def delete_maximum(self):
        if self.size == 0:
            return None
        maximum_value = self.binary_heap[1]
        self.binary_heap[1] = self.binary_heap[self.size]
        self.binary_heap.pop()
        self.size -= 1
        if self.size > 0:
            self.percolate_down(1)
        return maximum_value

def max_product_of_k(numbers, k):
    if k > len(numbers):
        return None
    max_heap = PriorityQueue()
    for number in numbers:
        max_heap.insert(number)
    max_product = 1
    for _ in range(k):
        max_product *= max_heap.delete_maximum()
    return max_product

# Example usage
arr_nums = [12, 74, 9, 50, 61, 41]
k = 2
print(f"Original list elements: {arr_nums}")
max_product = max_product_of_k(arr_nums, k)
print(f"Maximum product of {k} number(s) of the said list: {max_product}")
