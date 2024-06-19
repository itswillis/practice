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

def count_nodes_len_greater_than(binary_tree, length):
    if not binary_tree:
        return 0

    if len(binary_tree.data) > length:
        current_count = 1
    else:
        current_count = 0

    left_count = count_nodes_len_greater_than(binary_tree.left, length)
    right_count = count_nodes_len_greater_than(binary_tree.right, length)

    return current_count + left_count + right_count


tree1 = BinaryTree('noon', BinaryTree('rotator', BinaryTree('funny', None, None), None), BinaryTree('deed', None, None))
print(count_nodes_len_greater_than(tree1, 0))
