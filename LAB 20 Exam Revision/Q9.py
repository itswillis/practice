class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)                
    def pop(self):
        if self.is_empty():
            raise IndexError('ERROR: The stack is empty!')
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError('ERROR: The stack is empty!')
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)        
    def __str__(self):
        return str(self.items)[:-1] + ' <-'

class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        if self.is_empty():
            raise IndexError('ERROR: The queue is empty!')
        return self.items.pop() 
    def size(self):
        return len(self.items)
    def peek(self):
        if self.is_empty():
            raise IndexError('ERROR: The queue is empty!')
        return self.items[len(self.items)-1]
    def __str__(self):
        return '-> |' + str(self.items)[1:-1] + '| ->'
    def clear(self):
        self.items = []

def reverse_queue_region(a_queue, start, end):
    # dequeue elements from the original queue
    # use stack to reverse order for elements between start and end indicies
    # re-enqueue elements back into the queue

    stack = Stack()
    result_queue = Queue()
    
    size = a_queue.size()

    for _ in range(1, start):
        result_queue.enqueue(a_queue.dequeue())

    for _ in range(start, end + 1):
        stack.push(a_queue.dequeue())

    while not stack.is_empty():
        result_queue.enqueue(stack.pop())

    while not a_queue.is_empty():
        result_queue.enqueue(a_queue.dequeue())

    return result_queue

    

my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
print(my_queue)
new_queue = reverse_queue_region(my_queue, 1, 4)
print(new_queue)
