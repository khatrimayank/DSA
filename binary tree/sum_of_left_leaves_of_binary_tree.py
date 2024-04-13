class Node:

    def __init__ (self,val):
        self.val=val
        self.left=None
        self.right=None


arr =[3,9,20,None,None,11,7]
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



res=insert_level_order(None,arr,0,n)


class Solution:
    def sum_of_left_leaves(self,root):

        if not root:
            return

        sum=leftsum=rightsum=0

        if root.left:
            leftsum=self.sum_of_left_leaves(root.left)
        
        if root.right:
            rightsum=self.sum_of_left_leaves(root.right)
  
        if root.left and (not root.left.left) and (not root.left.right):
            sum= (root.left.val)

    
        return sum+leftsum+rightsum

sol=Solution()

result=sol.sum_of_left_leaves(res)

print(result)

'''
class Node:

    def __init__ (self,val):
        self.val=val
        self.left=None
        self.right=None


arr =[3,9,20,None,None,17,7]
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



res=insert_level_order(None,arr,0,n)


class Solution:

    def __init__(self):
        self.sum=0

    def sum_of_left_leaves(self,root):

        if not root:
            return 0

        elif root.left and (not root.left.left) and (not root.left.right):
            self.sum+=root.left.val

        else:
            return

        self.sum_of_left_leaves(root.left)
        self.sum_of_left_leaves(root.right)

        return self.sum

sol=Solution()

print(sol.sum_of_left_leaves(res))


'''