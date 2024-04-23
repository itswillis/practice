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

def create_stack(numbers): 
    stack = Stack() 
    for number in numbers:
        stack.push(number + 1)
    return stack

def zip_list_stack(a_list, a_stack):
    # alterate returns a new STACK object
    stack = Stack() 

    # list = [1, 3] 
    # stack is [10, 20]
    # function returns [1, 20, 3, 10]

    # can we turn the stack into a list first? 
    stack_list = []
    while not a_stack.is_empty():
        stack_list.append(a_stack.pop())
    stack_list.reverse()
    
    for i in range(len(a_list)):
        stack.push(a_list[i])
        stack.push(stack_list.pop())

    return stack


stack1 = Stack()
for number in range(1, 5):
    stack1.push(number)
list1 = [10, 20, 30, 40]
data = zip_list_stack(list1, stack1)
print(data)
print(type(data))
print(stack1.size())