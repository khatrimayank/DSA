array = [7,6,10,5,9,2,1,15,7]

def partition(arr,start,end):

    pivot_index=start

    pivot=arr[pivot_index]

    while start<end:

        while arr[start]<=pivot and start<end-1:
            start+=1

        while arr[end]>pivot and end>0:
            end-=1

        if start<end:
            arr[start],arr[end]=arr[end],arr[start]


    arr[end],arr[pivot_index] = arr[pivot_index], arr[end]

    return end


def quick_sort(arr,start,end):
    if start<end:
        loc=partition(arr,start,end)
        quick_sort(arr,start,loc-1)
        quick_sort(arr,loc+1,end)



quick_sort(array,0,len(array)-1)

print(array)

