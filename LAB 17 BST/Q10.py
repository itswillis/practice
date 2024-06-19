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

def create_bst_from_list(values):
    if not values:
        return None
    root = BinarySearchTree(values[0])
    for value in values:
        root.insert(value)
    return root

def is_bst(my_tree):
    

tree = create_bst_from_list([7, 12, 4, 9, 20])
print_tree(tree, 0)