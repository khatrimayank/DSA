#Inorder of Tree = 4 2 5 1 3
#Preorder of Tree= 1 2 4 5 3 
#Postorder of Tree= 4 5 2 3 1
"""   1
    /   \
   2     3
  / \
 4   5 """

class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.value=key

root=Node(1)

root.left=Node(2)

root.right=Node(3)

root.left.left=Node(4)

root.left.right=Node(5)

'''   1
    /   \
   2     3
  / \
 4   5 '''

def Inorder(root):#left root right=4 2 5 1 3

    if root:

        Inorder(root.left)

        print(root.value)

        Inorder(root.right)

def Preorder(root):#root left right=1 2 4 5 3

    if root:

        print(root.value)

        Preorder(root.left)

        Preorder(root.right)

def Postorder(root):#left right root =4 5 2 3 1

    if root:

        Postorder(root.left)

        Postorder(root.right)

        print(root.value)

Inorder(root)
print('\r')
Preorder(root)
print('\r')
Postorder(root)