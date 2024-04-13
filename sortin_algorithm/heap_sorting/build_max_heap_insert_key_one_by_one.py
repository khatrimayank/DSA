array=[1, 3, 5, 4, 6, 13,10, 9, 8, 15, 17]


def max_heap(arr,n):

	i=1

	while i<n:

		parent=(i-1)//2

		parent_of_parent=(parent-1)//2

		if arr[i]>arr[parent]:

			arr[i],arr[parent]=arr[parent],arr[i]

		while parent_of_parent>=0 and  arr[parent]>arr[parent_of_parent]:

			arr[parent],arr[parent_of_parent]=arr[parent_of_parent],arr[parent]
			parent_of_parent=(parent_of_parent-1)//2
			parent=(parent-1)//2

		i+=1



	print(arr)


max_heap(array,len(array))
