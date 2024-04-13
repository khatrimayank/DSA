a=[1,2,2,3,3,3]

def NGF(a):
    dic={}

    for i in ((a)):
        
        if i not in dic:
            dic[i]=1

        else:
            dic[i]+=1

    ans=[0]*len(a)

    stack=[]

    stack.append(0)

    for i in range(1,len(a),1):

        element=a[top(stack)]

        temp=a[i]

        while dic[temp]>dic[element]:
            ans[stack.pop()]=temp
            if len(stack)!=0:
                element=a[top(stack)]
            else:
                break

        stack.append(i)

    while len(stack)!=0:
        ans[top(stack)]=-1
        stack.pop()

    print(ans)

def top(stack):
    if len(stack)!=0:
        return stack[-1]

NGF(a)

        
