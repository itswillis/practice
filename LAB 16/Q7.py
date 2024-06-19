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

    def square_data(self):
        return self.set_data(self.data ** 2)
    
    def is_leaf(self):
        if self.left is None and self.right is None:
            return True
        return False
    
    def sum_values(self):
        total = self.data

        if self.left is not None:
            total += self.left.sum_values()

        if self.right is not None:
            total += self.right.sum_values() 

        return total


tree1 = BinaryTree(7, BinaryTree(2, BinaryTree(1), BinaryTree(5)), BinaryTree(9, None, BinaryTree(14)))
print(tree1.sum_values())
print(tree1.get_left().sum_values())
print(tree1.get_right().sum_values())