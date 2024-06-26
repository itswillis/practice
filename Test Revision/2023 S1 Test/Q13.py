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
    
def combine_two_stacks(stack1, stack2):
    new_stack = Stack()
    temp_stack = Stack()

    # Reverse the stacks to access elements in the original order
    while not stack1.is_empty():
        temp_stack.push(stack1.pop())
    while not temp_stack.is_empty():
        stack1.push(stack2.pop())

    while not stack2.is_empty():
        temp_stack.push(stack2.pop())
    while not temp_stack.is_empty():
        stack2.push(temp_stack.pop())

    # Combine elements from both stacks
    while not stack1.is_empty() and not stack2.is_empty():
        element1 = stack1.pop()
        element2 = stack2.pop()
        new_stack.push(str(element1) + str(element2))

    # Handle leftover elements from stack2 first 
    while not stack2.is_empty():
        new_stack.push(str(stack2.pop()))

    # Then handle leftover elements from stack1
    while not stack1.is_empty():
        reversed_combined.append(str(reverse_stack1.pop()))

    # As elements are combined in reverse order, they need to be reversed back
    while reversed_combined:
        new_stack.push(reversed_combined.pop())

    return new_stack

stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack2 = Stack()
stack2.push('a')
stack2.push('b')
data = combine_two_stacks(stack1, stack2)
print(data)
print(data.peek())
stack3 = Stack()
stack3.push(1)
stack3.push(2)
stack4 = Stack()
stack4.push('a')
stack4.push('b')
stack4.push('c')
data2 = combine_two_stacks(stack3, stack4)
print(data2)
print(data2.peek())