arr=[1,2,3,4,5,6,7,8,9,0]


n=len(arr)

k=int(input("enter group size :"))

for i in range(0,n,k):

    arr[i:i+k]=arr[i:i+k][::-1]


print(arr)