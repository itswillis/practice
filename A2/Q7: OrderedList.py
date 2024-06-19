class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next
    
class OrderedList:

    '''
    Define an OrderedList class to represent an ordered linked list.

    Authour: William Tang
    '''

    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length
    
    def is_empty(self):
        if not self.length:
            return True
        return False
    
    def add(self, value):
        new_node = Node(value)
        # special case - adding to empty linked list
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
        
        # special case - for head at end
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node

        else:
            # locate the node before the point of insertion
            current = self.head
            while (current.next is not None and current.next.data < new_node.data):
                current = current.next
            
            new_node.next = current.next
            current.next = new_node
        
        self.length += 1

    def search(self, value):
        current = self.head
        while current != None:
            if current.get_data() == value:
                return True
            else:
                current = current.get_next()
        return False # return False if not found

    def remove(self, value):
        found = False
        current = self.head
        previous = None
        while current != None and not found:
            if current.get_data() == value:
                found = True
            else:
                previous = current
                current = current.get_next()
        if found:
            if previous == None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())
            self.length -= 1
            return value # return the value if found
        return None # return None if not found
    
    def __str__(self): 
        result = ''
        current = self.head
        if self.length != 0: 
            while current: 
                result = result + str(current.data) + ' --> '
                current = current.next
            return (f"Head: {result[:-5]}")
        else: 
            return ("")
        
	
o_list = OrderedList()
o_list.add("hello")
o_list.add("world")
o_list.add("class")
o_list.add("ahoy")
print("Ordered List:", o_list, "Length of list:", len(o_list))
print("Removing:", o_list.remove("absent"))
print("Removing:", o_list.remove("hello"))
print("Removing:", o_list.remove("class"))
print("Ordered List:", o_list, "Length of list:", len(o_list))