import array as arr

a=arr.array('i',[1,2,3,4,5,6,7,8,9,0])

no_of_times_left_rotation=input("enter no. for which you want to rotate array=")

print("array before rotation=",end="")

for i in a:
    print(i,"",end="")

k=1

length_of_a=len(a)

while k<=int(no_of_times_left_rotation):

    for i in range(length_of_a-1):

        c=a[i]
        a[i]=a[i+1]
        a[i+1]=c

    print("\n",a)

    k+=1






