def longestValidParentheses(s):

    n=len(s)
    
    maxlength=0

    left=0

    right=0
   
    for i in range(n):
            
        if s[i]=='(':
            
            left+=1

        else:
            
            right+=1

        if left==right and maxlength<(left+right):

            maxlength=left+right

        elif right>left:
            left=right=0

    left=0

    right=0
   
    for i in range(n-1,-1,-1):
            
        if s[i]=='(':
            
            left+=1

        else:
            
            right+=1

        if left==right and maxlength<(left+right):

            maxlength=(left+right)

        elif right<left:
            left=right=0

    print(maxlength)

s="(()))())("

longestValidParentheses(s)

'''def longest(s):

    n=len(s)

    max_length=0

    ss=[]

    ss.append(-1)

    for i in range(n):

        if s[i]=="(" :

            ss.append(i)

        elif s[i]==")" :

            ss.pop()

            if not ss:

                ss.append(i)

            else:

                a=len(ss)  

                if max_length<(i-ss[a-1]):

                    max_length=i-ss[a-1]

    print(max_length)

s=")()())"

longest(s)'''