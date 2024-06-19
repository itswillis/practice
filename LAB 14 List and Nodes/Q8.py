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

    def __str__(self):
        return str(self.data)
    

node1 = Node('Peter')
node2 = Node('David', node1)
node3 = Node('Bob', node2)
node4 = Node('Frank', node3)
print(node1.has_next())
print(node4.has_next())