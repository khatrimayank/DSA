arr1=[1,1,3,5,2,4,3]
arr2=[1,2,3,4,5,3,8]

n1=len(arr1)
n2=len(arr2)

def equal_or_not(arr1,arr2,n1,n2):

    if n1!=n2:
        print("not equal")

    else:
        dic1={}
        dic2={}

        for i in arr1:

            if i not in dic1:
                dic1[i]=1

            else:
                dic1[i]+=1

        for i in arr2:

            if i not in dic2:
                dic2[i]=1

            else:
                dic2[i]+=1

        for k, v in dic1.items():
            if v != dic2[k]:
                return -1


   

result=equal_or_not(arr1,arr2,n1,n2)
if result!=-1:
    print("equal")

else:
    print("not equal")






