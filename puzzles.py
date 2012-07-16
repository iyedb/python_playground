v = [1,5,15,2,98,0,-1,-6,45,78]



def times2(x):
	x = x*2


def quicksort(vect, low, high):
	
	
	pivot = low
	
	if low < high:
		
		i = low
		j = high
		while i < j:
			
			while vect[i] < vect[pivot] and i < high:
				i = i + 1
			while vect[j] > vect[pivot]:
				j = j - 1
			if i < j:
				tmp = vect[j]
				vect[j] = vect[i]
				vect[i] = tmp		
			
		quicksort(vect, low, pivot)
		
		quicksort(vect,pivot + 1, high)
	

quicksort(v,0,len(v) - 1)

#print v

class Node():
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		

def add_node(node, value):
	if node is None:
		node = Node(value)
	else:
		if value <= node.value:
			node.left = add_node(node.left, value)
		else:
			node.right = add_node(node.right, value)
	return node
	
	
	
	
def traverse_tree(root):
	if root.left is None and root.right is None:
		print root.value
	else:
		if root.left:
			traverse_tree(root.left)
		print root.value
		if root.right:
			traverse_tree(root.right)
			
	
	
tree = None
tree = add_node(tree, 1)
add_node(tree, 0)
add_node(tree, -1)
add_node(tree, 2)
add_node(tree, 3)


 

traverse_tree(tree)




