class Node:

    def __init__ (self,val):
        self.val=val
        self.left=None
        self.right=None


arr=[1,2,3,4,5,None,None,5,6,7,8]
n=len(arr)
def insert_level_order(root,arr,i,n):

    if i<n:
        
        if arr[i]==None:
            return None

        else:

            root=Node(arr[i])

            root.left=insert_level_order(root.left,arr,(2*i+1),n)

            root.right=insert_level_order(root.right,arr,(2*i+2),n)
    

    return root
root=insert_level_order(None,arr,0,n)