def insert_heap(arr,n,value):

	arr.append(value)

	i=n

	while True:

		if i>0:
			
			parent=(i-1)//2

			if arr[i]>arr[parent]:

				arr[i],arr[parent]=arr[parent],arr[i]

				i=parent

			else:
				break

		else:
			break

	print(arr)

array=[70,50,40,45,35,39,16,10,9]

insert_heap(array,len(array),60)






