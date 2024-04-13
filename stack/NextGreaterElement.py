s=[11, 13, 21, 3]

def NextGreaterElement(s):

    stack=[]

    stack.append(s[0])

    for i in range(1,len(s),1):
        
        temp=s[i]

        if len(stack)!=0:
            element=stack[len(stack)-1]

        while temp>element:

            print(element,'-->',temp)
            stack.pop()
            if len(stack)!=0:
                element=stack[len(stack)-1]

            break

        stack.append(temp)

    while len(stack)!=0:
        print(stack.pop(),"--> -1")


NextGreaterElement(s)







    