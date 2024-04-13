# Definition for a binary tree node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def maxDepth(self, root):
        if not root:
            return 0
        
        left_height=self.maxDepth(root.left)
        right_height=self.maxDepth(root.right)
        
        print(left_height,right_height)
        if left_height==0:
            return 1+right_height

        if right_height==0:
            return 1+left_height

        return 1+min(left_height,right_height)



arr = root = [3,9,None,15,7]
n=len(arr)
def insert_level_order(root,arr,i,n):

    if i<n:
        
        if arr[i]==None:
            root=None

        else:

            root=Node(arr[i])

            root.left=insert_level_order(root.left,arr,(2*i+1),n)

            root.right=insert_level_order(root.right,arr,(2*i+2),n)
    

    return root

res=insert_level_order(None,arr,0,n)


soln = Solution()
max_depth = soln.maxDepth(res)
print(max_depth)
