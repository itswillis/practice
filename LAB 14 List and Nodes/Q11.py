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
    
def print_node_chain(a_node):
    if a_node is None:
        print()
        return
    print(a_node.data, end= ' ')
    if a_node.next is not None:
        print_node_chain(a_node.next)
    else:
        print()

def square_node_chain(first_node):
    current = first_node
    while current is not None:
        current_data = current.get_data()
        square_data = current_data * current_data
        current.set_data(square_data)

        current = current.get_next()
    
node1 = Node(3)
node2 = Node(6)
node2.set_next(node1)
square_node_chain(node2)
print_node_chain(node2)