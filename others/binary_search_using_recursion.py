'''arr=[1,2,3,4,5,6,7,8]

def binary_search(arr,beg,end,x):

    if beg>end:
        return -1

    mid=beg+(end-beg)//2

    if arr[mid]==x:
        return mid

    elif arr[mid]<x:
        return binary_search(arr,mid+1,end,x)

    else:
        return binary_search(arr,beg,mid-1,x)

        


result=binary_search(arr,0,len(arr),8)


if result!=-1:
    print("element present at index",result)

else:
    print("not available")'''

'''def searchInsert(nums,target,beg,end):
    
    middle=beg+(end-beg)//2

    if end>beg:
        if nums[middle]>target:
            if middle!=beg:
                return searchInsert(nums,target,beg,middle-1)
            else:
                return searchInsert(nums,target,beg,middle)
            
        elif nums[middle]<target:
            return searchInsert(nums,target,middle+1,end)
        else :
            print("index=",middle)
            return
    else:
        if nums[middle]<target:
            print("index=", middle+1)
        else:
            print("index=",middle)
        return

nums=[1,3,4,5,9]
target=5

searchInsert(nums,target,0,len(nums)-1)'''


list=[1,3,8,31,54,67,98,101]

l=len(list)#l=8

def binary_search(list,start,end,n):
    
    ret=-1

    if n<list[0] or n>list[l-1]:
        return ret

    else:

        if start>end:
            return ret

        else:
            mid=(start+(end-start)//2)

            if list[mid]==n:
                print(list[mid])
                return mid

            elif list[mid]>n:
                return binary_search(list,start,mid-1,n)

            elif list[mid]<n:
                return binary_search(list,mid+1,end,n)

            return ret

number=int(input("please enter number you want to search :"))

index=binary_search(list,0,l,number)

print(index)

if index!=-1:
    print("number available at index :",index)

else:
    print("not available")
