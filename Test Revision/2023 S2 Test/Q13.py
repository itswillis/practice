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
        return 'Stack: ' + str(self.items)

def evaluate_large_number_postfix_exp(string):
    number_str = ''

    a_stack = Stack() 
    
    for letter in string: 
        if letter.isdigit(): 
            number_str += letter

        elif letter == '(': 
            a_stack.push(letter)
        
        elif letter == ')':
            a_stack.pop()

    return number_str
    



print(evaluate_large_number_postfix_exp("(24)3+"))