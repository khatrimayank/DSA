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

class Solution:
    def diameter(self,root):
        self.count=0
        def max_depth(root):
            if not root:
                return 0

            left_height=max_depth(root.left)
            right_height=max_depth(root.right)
            self.count=max(self.count,left_height+right_height)
            return 1+max(left_height,right_height)

        max_depth(root)
        return self.count
sol=Solution()
result=sol.diameter(root)
print(result)

'''
class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.next=None

class solution:

    def __init__(self):
        self.dia=0

    def result(self,root):

        def diameter(root):

            if not root:
                return 0
            
            l_h=diameter(root.left)

            r_h=diameter(root.right)

            self.dia=max(self.dia,l_h+r_h)

            return 1+max(l_h,r_h)

        diameter(root)

        return self.dia





root = Node(10);

root.left = Node(20);
root.right = Node(30);

root.left.left = Node(40);
root.left.right = Node(50);

root.left.left.left= Node(60);
root.left.right.left = Node(70);
root.left.left.left.left= Node(80);

d=solution()
print(d.result(root))