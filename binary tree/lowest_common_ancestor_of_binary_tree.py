class Node:

    def __init__ (self,val):
        self.val=val
        self.left=None
        self.right=None



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
n=len(arr)
root=insert_level_order(None,arr,0,n)

p=(4)
q=(5)

class Solution:

    def lowest_common_ancestor(self,root,p,q):
        
        if not root:
            return None

        if root.val==p or root.val==q:

            return root.val

        left=self.lowest_common_ancestor(root.left,p,q)

        right=self.lowest_common_ancestor(root.right,p,q)

        if not right:
            return left
        if not left:
            return right

        return root.val

sol=Solution()
res=sol.lowest_common_ancestor(root,p,q)
print(res)