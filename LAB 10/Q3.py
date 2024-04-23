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


print(create_stack([5, 7, 18, -2, 9, 4]))
print(create_stack([1, 2, 3, 4, 5]))