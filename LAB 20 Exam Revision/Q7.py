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

def print_node_chain(first_node):
    current = first_node
    while current:
        print(f"Node({current})", end=" -> ")
        current = current.get_next()
    print("None")   


def create_chain_nodes_from_list(a_list):
    head = None
    previous_node = None

    for item in a_list:
        new_node = Node(item)

        if head is None:
            head = new_node
        else:
            previous_node.set_next(new_node)

        previous_node = new_node

    return head


chain_nodes = create_chain_nodes_from_list(["hello"])
print_node_chain(chain_nodes)
print(type(chain_nodes))
