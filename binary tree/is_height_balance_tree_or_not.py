class Node:

	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

'''def height_balance_tree(root):

	a=height_of_node(root.left)

	b=height_of_node(root.right)

	if (a-b)>1 or (b-a)>1:
		return False

	if root.left:
		height_balance_tree(root.left)

	if root.right:
		height_balance_tree(root.right)

	return True

def height_of_node(node):

	if not node:
		return 0

	l=height_of_node(node.left)

	r=height_of_node(node.right)

	return 1+max(l,r)'''

def height_balance_tree(root):

	if not root:
		return 0

	l=height_balance_tree(root.left)

	if l==-1:
		return False

	r=height_balance_tree(root.right)

	if r==-1:
		return False

	if abs(l-r)>1:
		return -1

	return 1+max(l,r)




root = Node(10);

root.left = Node(20);
root.right = Node(30);
 
root.left.left = Node(40);

res=height_balance_tree(root)

print(res)

if res==False:
	print("not balanced")

else:
	print('balanced')