class Node:

	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
		self.next=None

def connect_at_same_level(root):

	if not root:
		return

	q=[]

	q.append(root)

	root.next=None

	while q:

		for i in range(len(q)-1):

			q[i].next=q[i+1]

		q[-1].next=None

		for i in range(len(q)):

			temp=q.pop(0)

			if temp.left:
				q.append(temp.left)

			if temp.right:
				q.append(temp.right)

	return root

def print_next_pointer(res):

	q=[]

	q.append(res)

	while q:

		n=len(q)

		print('\n')

		for i in range(n):

			temp=prev=q.pop(0)

			print(temp.data,end=" ")

			temp=temp.next

			if prev.left:
				q.append(prev.left)

			if prev.right:
				q.append(prev.right)

root = Node(10);

root.left = Node(20);
root.right = Node(30);
 
root.left.left = Node(40);
root.left.right = Node(50);

root.right.left = Node(60);
root.right.right = Node(70);

root.left.left.left = Node(80);
root.left.left.right = Node(90);

root.right.right.left = Node(100);
root.right.right.right = Node(110);
res=connect_at_same_level(root)

print_next_pointer(res)

