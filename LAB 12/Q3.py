class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)                
    def dequeue(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)
    

a_queue = Queue()
a_queue.enqueue(3)
a_queue.enqueue(4)
a_queue.enqueue(5)
temp = a_queue.dequeue()
a_queue.enqueue(a_queue.peek())
a_queue.enqueue(temp)
a_queue.enqueue(a_queue.dequeue())
print(a_queue.items) 