arr=[74,665,142 ,112, 54, 69, 148, 45 ,63, 158, 38 ,60 ,124, 142 ,130, 179, 117, 36, 191, 43 ,89, 107 ,41 ,143 ,65 ,49 ,47 ,6 ,91, 130 ,171 ,151, 7 ,102, 194 ,149 ,30, 24 ,85, 155 ,157, 41, 167, 177 ,132, 109, 145, 40, 27, 124, 138, 139, 119, 83, 130, 142, 34, 116 ,40 ,59 ,105, 131, 178 ,107, 74, 187, 22 ,146, 125, 73, 71, 30, 178, 174 ,98, 113]

n=len(arr)

s=739


def fun(arr,n,s):

    curr_sum=0

    start_index=0

    if s==0 and 0 not in arr:

        return -1

    for i in range(n):

        curr_sum+=arr[i]

        while curr_sum>s:

            curr_sum-=arr[start_index]

            start_index+=1

        if curr_sum==s:
            return(start_index,i)

    if curr_sum!=s:
        return("NOT FOUND")

print(fun(arr,n,s))