class Node:

	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def Level_Order_Traversal(root):

	if root==None:
		return

	q=[]

	q.append(root)

	while q:
		if q[0].left:
			q.append(q[0].left)
		if q[0].right:
			q.append(q[0].right)
		print(q[0].data)
		q.pop(0)


root=Node(1)

root.left=Node(0)

root.right=Node(3)

root.left.left=Node(4)

root.left.right=Node(5)

root.right.left=Node(6)

root.right.right=Node(7)

Level_Order_Traversal(root)