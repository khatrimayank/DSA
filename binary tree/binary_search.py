arr=[1,2,3,4,5,6,7,8]

def binary_search(arr,beg,end,x):

    while beg<=end:

        mid=beg+(end-beg)//2

        if arr[mid]==x:
            return mid

        elif arr[mid]<x:
            beg=mid+1

        else:
            end=mid-1

    return -1


result=binary_search(arr,0,len(arr),10)


if result!=-1:
    print("element present at index",result)

else:
    print("not available")


    


