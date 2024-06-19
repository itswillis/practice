class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def enqueue(self, item):
        print("New node in the queue.")
        self.items.insert(0, item)
    def dequeue(self):
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty!")
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty!")
        return self.items[len(self.items)-1]
    def __str__(self):
        queue_str = "| ->"
        for i in range(len(self.items) - 1, -1, -1):
            if i == len(self.items) - 1:
                queue_str = str(self.items[i]) + queue_str
            else:
                queue_str = str(self.items[i]) + ", " + queue_str
        queue_str = "-> |" + queue_str
        return queue_str	

class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert_left(self, new_data):
        if self.left == None:
            self.left = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data, left=self.left)
            self.left = t

    def insert_right(self, new_data):
        if self.right == None:
            self.right = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data, right=self.right)
            self.right = t

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def __iter__(self):
        return BTLevelorderIterator(self)

class BTLevelorderIterator:
    def __init__(self, binary_tree):
        self.queue = Queue()
        if binary_tree:
            self.queue.enqueue(binary_tree)

    def __next__(self):
        if self.queue.is_empty():
            raise StopIteration
        
        current_node = self.queue.dequeue()
        if current_node.left:
            self.queue.enqueue(current_node.left)
        if current_node.right:
            self.queue.enqueue(current_node.right)
        
        return current_node


tree1 = BinaryTree('noon', BinaryTree('rotator', BinaryTree('funny', None, None), None), BinaryTree('deed', None, None))
myIt=iter(tree1)
print(next(myIt).get_data())
