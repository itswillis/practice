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
    
    def get_max(self):
        if self.right == None:
            return self.data
        else:
            return self.right.get_max()
        
    def get_min(self):
        if self.left == None:
            return self.data
        else:
            return self.left.get_min()

def create_bst_from_list(values):
    for i in range(len(values)):
        BinarySearchTree.insert(values[i])

def print_tree(t, level):
    print(' ' * (level*4) + str(t.get_data())) 
    if t.get_left() != None:
        print('(L)', end = '')
        print_tree(t.get_left(), level + 1) 
    if t.get_right() != None: 
        print('(R)', end = '')
        print_tree(t.get_right(), level + 1) 


tree8 = BinarySearchTree(7, BinarySearchTree(3, BinarySearchTree(1), BinarySearchTree(4)), BinarySearchTree(10, BinarySearchTree(8), BinarySearchTree(13)))

tree2 = BinarySearchTree(27, BinarySearchTree(14, BinarySearchTree(10), BinarySearchTree(19)), BinarySearchTree(35, BinarySearchTree(31), BinarySearchTree(42)))
tree1 = BinaryTree(7, BinaryTree(2, BinaryTree(1), BinaryTree(5)), BinaryTree(9))

	
tree = create_bst_from_list([7, 12, 4, 9, 20])
print_tree(tree, 0)