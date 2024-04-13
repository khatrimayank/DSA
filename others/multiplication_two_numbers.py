number1=input("enter first number")

number2=input("enter second number")

reverse_number1="".join(reversed(number1))

reverse_number2="".join(reversed(number2))

l1=len(reverse_number1)

l2=len(reverse_number2)

#Because we always multiply elements of second number to elements of first number

if l2>l1:
    (reverse_number2,reverse_number1)=(reverse_number1,reverse_number2)

l1=len(reverse_number1)

l2=len(reverse_number2)

#arr_result will store all arrays which we will get by multiplication of second number to first number

arr_result=[0]*min(l1,l2)

#how many times new array will created=min no of elements in number1 and number2

for i in range(min(l1,l2)):

    result_hasil=0

    arr=['0']*(l1+1)


    for j in range(l1):#how many times multiplication occur for second number element

        a=(reverse_number1[j])
        b=(reverse_number2[i])

        a=int(a)
        b=int(b)

        result=(a*b)+int(result_hasil)
        result=str(result)
        if len(result)>1:
            result_number=result[1]
            result_hasil=result[0]

        else:
            result_number=result
            result_hasil=0

        arr[j]=str(result_number)

    arr[j+1]=str(result_hasil)

    print("".join(reversed(arr)))

    arr_result[i]=(list(reversed(arr)))

print(arr_result)

length=len(arr_result)

for i in range(1,length):

    for j in range(i):

        arr_result[i].append('0')

print(arr_result)

for i in range(length):

    arr_result[i]=int("".join(arr_result[i]))


i=0
j=0
while j<length:
    addition=arr_result[j]+i
    i=arr_result[j]
    j+=1

print(addition)
