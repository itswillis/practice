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


class BinarySearchTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
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
    
    def insert(self, new_data):
        if new_data == self.data:
            return 
        elif new_data < self.data: 
            if self.left == None:
                self.left = BinarySearchTree(new_data)
            else:
                self.left.insert(new_data)
        else:
            if self.right == None:
                self.right = BinarySearchTree(new_data)
            else:
                self.right.insert(new_data)

def create_a_bigger_bst():
    return BinarySearchTree(48, BinarySearchTree(26, BinarySearchTree(12), BinarySearchTree(31)), BinarySearchTree(68, BinarySearchTree(50), BinarySearchTree(71)))


def print_tree(t, level):
    print(' ' * (level*4) + str(t.get_data())) 
    if t.get_left() != None:
        print('(L)', end = '')
        print_tree(t.get_left(), level + 1) 
    if t.get_right() != None: 
        print('(R)', end = '')
        print_tree(t.get_right(), level + 1) 

def create_bst_from_sorted_list(sorted_list):
    if not sorted_list:
        return None
    mid_index = len(sorted_list) // 2
    root = BinarySearchTree(sorted_list[mid_index])
    root.left = create_bst_from_sorted_list(sorted_list[:mid_index])
    root.right = create_bst_from_sorted_list(sorted_list[mid_index+1:])

    return root

tree = create_bst_from_sorted_list([1, 3, 5, 7, 9, 11, 13])
print_tree(tree, 0)
print(type(tree))