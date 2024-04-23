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

def check_xml_well_formedness(string):

    stack = Stack()
    
    tag = ""
    is_opening_tag = True
    in_tag = False

    for char in string:
        if char == '<':
            in_tag = True
            tag = ""
            is_opening_tag = True
        elif char == '>':
            if is_opening_tag:
                stack.push(tag)
            else:
                if stack.is_empty() or stack.pop() != tag:
                    return False
            in_tag = False
        elif in_tag:
            if char == '/':
                is_opening_tag = False
                tag = ""
            else:
                tag += char

    return stack.is_empty()
            
            
print(check_xml_well_formedness("<tag1><tag2></tag2></tag1>"))         
print(check_xml_well_formedness("<tag1><tag2></tag1></tag2>"))
