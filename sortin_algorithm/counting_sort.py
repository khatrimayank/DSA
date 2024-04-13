arr=[2,1,1,0,2,5,4,0,2,8,7,7,9,2,0,1,9]

n=len(arr)

k=max(arr)

count=[0]*(k+1)

for i in range(len(arr)):

    count[arr[i]]+=1

print(count)

for i in range(1,k+1):

    count[i]=count[i]+count[i-1]
print(count)

b=[0]*len(arr)

for i in range(len(arr),0,-1):
    b[count[arr[i-1]]-1]=arr[i-1]
    count[arr[i-1]]-=1

print(b)