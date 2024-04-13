class Node:

	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None


'''def complete_or_not(root):

	q1=[]

	q1.append(root)

	if (q1[0].left and not q1[0].right) or (not q1[0].left and q1[0].right):
		return False

	q2=[]

	while q1:

		for i in range(len(q1)):

			if q1[0] and q1[0].left:
				q2.append(q1[0].left)

			if q1[0] and q1[0].right:
				q2.append(q1[0].right)

			q1.pop(0)

		for i in range(len(q2)-1):

			if (q2[i].left) and (not q2[i].right):
				return False

			if (q2[i].right) and (not q2[i].left):
				return False

			if (not q2[i].left or not q2[i].right ) and (q2[i+1].left or q2[i+1].right):
				return False

			if (q2[i].left.left or q2[i].left.right or q2[i].right.left or q2[i].right.right and (not q2[i+1].left or not q2[i+1].right)):
				return False



		if q2:
			if ((not q2[-1].left) and (q2[-1].right)):
				return False


		q1,q2=q2,q1

	return True'''

def complete_or_not(root):

	q=[]

	q.append(root)
	flag=False

	while q:

		temp=q.pop(0)
		if temp==None:
			flag=True

		else:
			if flag:
				return False
			q.append(temp.left)
			q.append(temp.right)

	return True


root = Node(10);

root.left = Node(20);
root.right = Node(30);
 
root.left.right = Node(50);
root.left.left = Node(40);
root.right.left = Node(60);
root.right.right = Node(70);
 
root.left.left.left = Node(80);
root.left.left.right = Node(90);
root.left.right.left = Node(100);
root.left.right.right = Node(110);
root.right.left.left = Node(120);
root.right.left.right = Node(130);


res=complete_or_not(root)

print(res)