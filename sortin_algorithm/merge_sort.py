def merge_sort(arr):

	if len(arr)>1:

		mid=len(arr)//2

		L=arr[:mid]

		print("L=",*L)

		R=arr[mid:]

		print("R=",*R)

		merge_sort(L)

		print("L1=",*L)

		merge_sort(R)

		print("R1=",*R)

		i=0
		j=0
		k=0
		while i<len(L) and j<len(R):
			if L[i]>R[j]:

				arr[k]=R[j]

				j+=1

			else:
				arr[k]=L[i]
				i+=1
			k+=1


		while i<len(L):
			arr[k]=L[i]
			i+=1
			k+=1

		while j<len(R):
			arr[k]=R[j]
			k+=1


		print("array sorted=",*arr)

	

		

array=[9,8,7,6,5,4,3,2,1]
merge_sort(array)

