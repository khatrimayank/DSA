class Node:
    def __init__ (self,val):
        self.val=val
        self.left=None
        self.right=None

def insert(root,key):

    if not root:
        return Node(key)

    elif key<=root.val:
        root.left=insert(root.left,key)

    elif key>root.val:
        root.right=insert(root.right,key)

    return root

    

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


root=Node(50)
insert(root,30)
insert(root,20)
insert(root,40)
insert(root,70)
insert(root,60)
insert(root,80)
insert(root,10)


inorder(root)


def delete(root,key):

    if key<root.val:
        root.left=delete(root.left,key)
        return root

    elif key>root.val:
        root.right=delete(root.right,key)
        return root

    else:

        # 1 if key is leaf node

        if (not root.left) and (not root.right):

            return None

        # 2 if key has only one child

        elif (root.left and (not root.right)) or (root.right and (not root.left)):

            if root.left:
                root.val=root.left.val
                root.left=None
                return root

            if root.right:
                root.val=root.right.val
                root.right=None
                return root

        # 3 has both child right and left

        elif (root.left) and (root.right):

            '''temp=root.right

            while temp.left:
                temp=temp.left

            root.val=temp.val
            
            root.right=delete(root.right,temp.val)

            return root'''

            parent=root
            child=root.right

            while child.left:
                parent=child
                child=child.left
            
            if parent!=root:
                root.val=child.val
                parent.left=child.left

            else:
                root.val=child.val
                root.right=child.left

            return root




print('\n')
delete(root,70)
inorder(root)














