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
    
try:
    stack1 = Stack()
    print (stack1.pop())
    print("OK")
except IndexError as err:
    print("ERROR:")
    print (err)

try:
    stack1 = Stack()
    print (stack1.peek())
except IndexError as err:
    print (err)

	
try:
    stack1 = Stack()
    stack1.push(2)
    print (stack1.peek())
    print (stack1.pop())
    print (stack1.pop())
except IndexError as err:
    print (err)