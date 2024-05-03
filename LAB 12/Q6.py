class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty!")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty!")
        return self.items[len(self.items)-1]
    
    def clear(self):
        self.items = []

    def __str__(self):
        joined = ', '.join(f"'{item}'" if isinstance(item, str) else str(item) for item in self.items)
        return (f"-> |{joined}| ->")


class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.is_empty(): 
            raise IndexError("ERROR: The stack is empty!")
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("ERROR: The stack is empty!")
        return self.items[-1]
    def size(self):
        return len(self.items)
    def clear(self):
        self.items = []
    def __str__(self):
        joined = ', '.join(f"'{item}'" if isinstance(item, str) else str(item) for item in self.items)
        return (f"[{joined} <-")

def zip_queue_stack(a_queue, a_stack):
    queue_result = []
    stack_result = []
    queue = Queue()

    for _ in range(a_queue.size()):
        queue_result.append(a_queue.dequeue())

    for _ in range(a_stack.size()):
        stack_result.append(a_stack.pop())

    for i in range(len(queue_result)):
        queue.enqueue(queue_result[i])
        queue.enqueue(stack_result[i])
    
    return queue

queue1 = Queue()
for i in range(1, 6):
    queue1.enqueue(i)
stack1 = Stack()
for letter in ['h', 'e', 'l', 'l', 'o']:
    stack1.push(letter)
print(zip_queue_stack(queue1, stack1))