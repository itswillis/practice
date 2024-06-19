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

def print_tree(t, level):
    print(' ' * (level*4) + str(t.get_data())) 
    if t.get_left() != None:
        print('(L)', end = '')
        print_tree(t.get_left(), level + 1) 
    if t.get_right() != None: 
        print('(R)', end = '')
        print_tree(t.get_right(), level + 1) 

def create_a_bigger_tree():
    return BinaryTree(14, BinaryTree(44, BinaryTree(11), BinaryTree(85)), BinaryTree(82, BinaryTree(41), BinaryTree(21)))

def convert_tree_to_list(tree):
    if tree == None:
        return None
    else:
        result = []
        result.append((tree.get_data()))
        result.append(convert_tree_to_list(tree.get_left()))
        result.append(convert_tree_to_list(tree.get_right()))
        return result

def create_tree_from_nested_list(node_list):
    if node_list == None:
        return None
    
    root = BinaryTree(node_list[0])

    root.left = create_tree_from_nested_list(node_list[1])
    root.right = create_tree_from_nested_list(node_list[2])

    return root


tree = create_tree_from_nested_list([10, [5, None, None], [15, [11, None, None], [22, None, None]]])
print_tree(tree, 0)