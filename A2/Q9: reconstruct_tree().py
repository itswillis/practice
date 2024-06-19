class ListBinaryTree:
	"""A binary tree class with nodes as lists."""
	DATA = 0    # just some constants for readability
	LEFT = 1
	RIGHT = 2   

	def __init__(self, root_value, left=None, right=None):
		"""Create a binary tree with a given root value
		left, right the left, right subtrees		
		"""	
		self.node = [root_value, left, right]
		
	def create_tree(self, a_list):
		return ListBinaryTree(a_list[0], a_list[1], a_list[2])

	def insert_left(self, value):
		"""Inserts value to the left of this node.
		Pushes any existing left subtree down as the left child of the new node.
		"""
		self.node[self.LEFT] = ListBinaryTree(value, self.node[self.LEFT], None)

	def insert_right(self, value):
		"""Inserts value to the right of this node.
		Pushes any existing left subtree down as the left child of the new node.
		"""      
		self.node[self.RIGHT] = ListBinaryTree(value, None, self.node[self.RIGHT])

	def insert_tree_left(self, tree):
		"""Inserts new left subtree of current node"""
		self.node[self.LEFT] = tree

	def insert_tree_right(self, tree):
		"""Inserts new left subtree of current node"""
		self.node[self.RIGHT] = tree

	def set_value(self, new_value):
		"""Sets the value of the node."""
		self.node[self.DATA] = new_value

	def get_value(self):
		"""Gets the value of the node."""
		return self.node[self.DATA]

	def get_left_subtree(self):
		"""Gets the left subtree of the node."""
		return self.node[self.LEFT]

	def get_right_subtree(self):
		"""Gets the right subtree of the node."""
		return self.node[self.RIGHT]

	def __str__(self):
		return '['+str(self.node[self.DATA])+', '+str(self.node[self.LEFT])+', '+\
	 str(self.node[self.RIGHT])+']'

def reconstruct_tree(inorder_sequence, postorder_sequence):
	
    '''
	This is a recursive function that takes: 
        - inorder_sequence: a list of items obtained by traversing a tree using inorder traversal
		- postorder_sequence: a list of items obtained by traversing a tree using postorder traversal

	This function returns:
        - a reconstructed binary tree as a nested list
	
	Authour: William Tang
	'''
	
	# base case
    if not postorder_sequence:
        return None
	
    root_value = postorder_sequence[-1] # identify the root - using post order as L,R,N
    root = ListBinaryTree(root_value)
    root_index_in_inorder = inorder_sequence.index(root_value)

    # divide in order sequences
    left_inorder_sequence = inorder_sequence[:root_index_in_inorder]
    right_inorder_sequence = inorder_sequence[root_index_in_inorder + 1:]

    # divide post order sequences
    left_postorder_sequence = postorder_sequence[:root_index_in_inorder]
    right_postorder_sequence = postorder_sequence[root_index_in_inorder:-1]

    # recursive construction
    root.insert_tree_left(reconstruct_tree(left_inorder_sequence, left_postorder_sequence))
    root.insert_tree_right(reconstruct_tree(right_inorder_sequence, right_postorder_sequence))

    return root

inorder_seq = [2, 5, 7, 10, 999, 15]
postorder_seq = [2, 7, 5, 15, 999, 10]
print(reconstruct_tree(inorder_seq, postorder_seq))