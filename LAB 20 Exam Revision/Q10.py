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
        self.count = 0
    
    def size(self):
        return self.count
    
    def add(self, item): 
        self.head = Node(item, self.head)
        self.count += 1
    
    def clear(self):
        self.head = None
        self.count = 0
        
    def is_empty(self):
        return self.count == 0
    
    def __str__(self):
        if self.count > 0:
            current = self.head
            data = []
            while current != None:
                data += [current.get_data()]
                current = current.get_next()
            return "Head: " + " --> ".join(str(d) for d in data)
        return ''

    def remove_first_odd_node(self):
        current = self.head
        previous = None

        while current is not None:
            if current.get_data() % 2 != 0:
                if previous is None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
                self.count -= 1
                return current.get_data()
            previous = current
            current = current.get_next()
        return None

                    
my_list = LinkedList()
my_list.add(5)
my_list.add(4)
my_list.add(3)
my_list.add(2)
print(my_list)
print(my_list.size())
print(my_list.remove_first_odd_node())
print(my_list)
print(my_list.size())
