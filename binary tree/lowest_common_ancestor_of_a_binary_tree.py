class Node:

    def __init__ (self,val):
        self.val=val
        self.left=None
        self.right=None



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

arr=[1,2,3,4,5]
root=insert_level_order(None,arr,0,n)

p=Node(2)
q=Node(4)

class Solution:

    def lowest_common_ancestor(root,p,q):

        if root==p or root==q:

            return root.val

        left=lowest_common_ancestor(root.left)

        right=lowest_common_ancestor(root.right)

        if not right:
            return left
        if not left:
            return right

sol=Solution()
res=sol.lowest_common_ancestor(root,p,q)
print(res)