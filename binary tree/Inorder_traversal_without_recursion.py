class Node:

	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def In_Order_Traversal(root):

	if root==None:
		return

	s=[]

	while s!=None or root!=None:

		while root:
			s.append(root)
			root=root.left

		if s:
			node=s.pop()
			print(node.data)
			root=node.right
	
root=Node(1)

root.left=Node(0)

root.right=Node(3)

root.left.left=Node(4)

root.left.right=Node(5)

root.right.left=Node(6)

root.right.right=Node(7)

In_Order_Traversal(root)