class CircularQueue: 
    def __init__(self, capacity = 8):
        self.items = [None] * capacity
        self.max_queue = capacity
        self.front = 0 
        self.back = self.max_queue - 1
        self.count = 0 
    
    def is_empty(self):
        return self.count == 0 
    
    def show_contents(self):
        return (f"{self.items}, front:{self.front}, back:{self.back}, count:{self.count}")
    
    def is_full(self):
        return self.count == self.max_queue
    
    def enqueue(self, item):
        if self.is_full():
            raise IndexError("ERROR: The queue is full.")
        self.back = (self.back + 1) % self.max_queue
        self.items[self.back] = item
        self.count += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty.")
        item = self.items[self.front]
        self.front = (self.front + 1) % self.max_queue
        self.count -= 1 
        return item
    
    def peek(self):
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty.")
        return self.items[self.front]

    def size(self): 
        return self.count

    def __str__(self):
        joined = ', '.join(str(self.items[(self.front + i) % self.max_queue]) for i in range(self.count -1, -1, -1))
        return (f"-> |{joined}| ->")

try:
    queue1 = CircularQueue(4)
    for i in range(5):
        queue1.enqueue(i)
    print(queue1.size())
except IndexError as err:
    print(err) 