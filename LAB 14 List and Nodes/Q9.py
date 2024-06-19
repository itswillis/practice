class Node:
    def __init__(self, data, next = None):
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
        new_node = Node(value, self.next)
        self.next = new_node

    def has_next(self):
        if self.next is not None:
            return True
        return False
    
    def square_data(self):
        self.data = self.data**2

    def __str__(self):
        return str(self.data)
    

node1 = Node(5)
node2 = Node(3, node1)
node3 = Node(4, node2)
node4 = Node(6, node3)
node1.square_data()
node2.square_data()
node4.square_data()
print(node1)
print(node2)
print(node3)
print(node4)