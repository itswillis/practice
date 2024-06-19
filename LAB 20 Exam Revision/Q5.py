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

def delete_mid(a_stack):
    stack_size = a_stack.size()

    if stack_size % 2 == 0:
        middle_index = (stack_size // 2) - 1
    else:
        middle_index = stack_size // 2
        
    temp_stack = Stack()

    for i in range(stack_size):
        item = a_stack.pop()
        if i != middle_index: # skips middle index
            temp_stack.push(item)

    while not temp_stack.is_empty():
        a_stack.push(temp_stack.pop())

my_stack = Stack()
print(my_stack)
delete_mid(my_stack)
print(my_stack)
    
