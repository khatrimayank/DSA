class Node:

	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None


def perfect_or_not(root):

	if not root:
		return True

	if ((root.left) and (not root.right)) or ((root.right) and (not root.left)):
		return False

	l=perfect_or_not(root.left)

	r=perfect_or_not(root.right)

	if l==True and r==True:
		return True
	else:
		return False


root = Node(10);
root.left = Node(20);
root.right = Node(30);
 
root.left.right = Node(40);
root.left.left = Node(50);
root.right.left = Node(60);
root.right.right = Node(70);
 
root.left.left.left = Node(80);
root.left.left.right = Node(90);
root.left.right.left = Node(80);
root.left.right.right = Node(90);
root.right.left.left = Node(80);
root.right.left.right = Node(90);

res=perfect_or_not(root)

print(res)