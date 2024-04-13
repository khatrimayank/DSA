class Node:

	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None


def check(root):

	q1=[]

	q1.append(root)

	q2=[]

	while q1:

		for i in range(len(q1)):

			if q1[0] and q1[0].left:

				q2.append(q1[0].left)

			if q1[0] and q1[0].right:

				q2.append(q1[0].right)

			q1.pop(0)

		count=0

		for i in q2:
			if (not i.left) and (not i.right):
				count+=1
		if count!=0 and count<len(q2):
			print('false')
			return 

		q1,q2=q2,q1

	print('true')
	return

root=Node(12)

root.left=Node(5)

root.right=None

root.left.left=Node(3)

root.left.right=Node(9)

root.left.left.left=Node(1)

root.left.left.right=None

root.left.right.left=Node(2)

root.left.right.right=None


check(root)