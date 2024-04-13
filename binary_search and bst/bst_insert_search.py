class Node:

    def __init__(self,data):

        self.data=data

        self.left=None

        self.right=None


def insert(root,val):

    if not root:
        return Node(val)

    if val<=root.data:
        root.left=insert(root.left,val)
        

    elif val>root.data:
        root.right=insert(root.right,val)
    

    return root


root=Node(50)

insert(root,10)

insert(root,20)

insert(root,30)

insert(root,40)

insert(root,60)

insert(root,70)


def inorder(root):

    if not root:

        return

    inorder(root.left)
    print(root.data)
    inorder(root.right)

inorder(root)

def search(root,val):
    if not root:
        return False

    elif val==root.data:
        return True

    elif val<root.data:
        return search(root.left,val)
        
    elif val>root.data:
        return search(root.right,val)

res=search(root,70)

print(res)