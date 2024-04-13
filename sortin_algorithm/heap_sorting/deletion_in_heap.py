def heapify(arr,n,i):

    left_children=(2*i)+1

    right_children=(2*i)+2

    largest=i


    if left_children<n and arr[largest]<arr[left_children]:
        largest=left_children

    if right_children<n and arr[largest]<arr[right_children]:
        largest=right_children

    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]

        heapify(arr,n,largest)



def build_heap(arr,n):

    start_index=(n//2)-1

    for i in range(start_index,-1,-1):

        heapify(arr,n,i)

    print(arr)

def deletion_in_max_heap(arr,n,value):

    index_value=arr.index(value)

    arr[n-1],arr[index_value]=arr[index_value],arr[n-1]

    del arr[n-1]

    n=n-1

    build_heap(arr,n)

array=[1, 3, 5, 4, 6, 13,10, 9, 8, 15, 17]

deletion_in_max_heap(array,len(array),8)


