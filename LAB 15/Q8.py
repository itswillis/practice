class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def add_after(self, value):
        new_node = Node(value,self.next )
        self.next = new_node

    def remove_after(self):
        self.next = self.next.get_next()

    def __str__(self):
        return str(self.data)

class LinkedList:   
    def __init__(self):
        self.head = None
        self.count= 0

    def __len__(self):
        return self.count

    def get_head(self):
        return self.head
    
    def add(self, value):
        new_node = Node(value)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1
        
    def search(self, value):
        current = self.head
        while current != None:
            if current.data == value:
                return True
            current = current.get_next()
        return False
        
    def remove(self, value):
        found = False
        previous = None
        current = self.head
        while current != None and not found:
            if current.data == value:
                found = True
            else:
                previous = current
                current = current.get_next()
        if found:
            if previous == None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())
            self.count -= 1
    
    def clear(self):
        self.head = None 
        self.count = 0
    
    def is_empty(self): 
        if self.count == 0: 
            return True
        return False
    
    def size(self):
        return self.count
    
    def __str__(self): 
        result = ''
        current = self.head
        if self.count != 0: 
            while current: 
                result = result + str(current.data) + ' --> '
                current = current.next
            return (f"Head: {result[:-4]}")
        else: 
            return ("")
        
    def remove_first(self):
        current = self.head
        if self.head is not None:
            self.head = self.head.get_next()
            self.count -= 1
        return current
    
    def square(self):
        current = self.head
        while current:
            current.set_data(current.get_data() ** 2)
            current = current.get_next()

    def move_last_to_front(self):
        last = self.head
        second_to_last = None

        while last.get_next() is not None:
            second_to_last = last
            last = last.get_next()
        
        if second_to_last is not None:
            second_to_last.set_next(None)
            last.set_next(self.head)
            self.head = last

my_list = LinkedList()
my_list.add('dog')
my_list.move_last_to_front()
print(my_list)