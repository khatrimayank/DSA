string='hello world'

def reverse_word(string,ans):
    
    stack=[]

    for i in string:

        if i!=" " :
            stack.append(i)
        
        else:
            for i in range(len(stack)-1,-1,-1):
                ans+=stack.pop()  

            ans+=" "

    for i in range(len(stack)-1,-1,-1):
        ans+=stack.pop()

    return ans
ans=''
print(reverse_word(string,ans))



