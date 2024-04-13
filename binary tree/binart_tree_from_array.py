arr = [1, 2, 3]
n=len(arr)
def insert_level_order(root,arr,i,n):

    if i<n:

        root=Node(arr[i])

        root.left=insert_level_order(root.left,arr,(2*i+1),n)

        root.right=insert_level_order(root.right,arr,(2*i+2),n)
    

    return root

res=insert_level_order(None,arr,0,n)


soln = Solution()
max_depth = soln.maxDepth(res)
print(max_depth)
