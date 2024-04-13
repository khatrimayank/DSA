def parenthesis_balanced_or_not(exp):

    stack=[]

    for char in exp:

        if char in ["(","{","["]:

            stack.append(char)
            continue

        else:
            if not stack:
                return False

            current_char=stack.pop()
            if current_char=="(" and char!=")" :
                return False
            elif current_char=="{" and char!="}" :
                return 0
            elif current_char=="[" and char!="]" :
                return 0
            else:
                continue

    if not stack:
        return True



exp="]["

if parenthesis_balanced_or_not(exp):
    print("parenthesis balanced")

else:
    print("parenthesis not  balanced")

'''
s="[()[()]{[})]}]"

stack=[]

def balanced_or_not(s):

    if len(s)%2!=0:
        return False

    for i in s:
        
        if i in ["(","{","["]:
            stack.append(i)

        elif i==")" and stack.pop()!="(":
            return False

        elif i=="}" and stack.pop()!="{":
            return False

        elif i=="]" and stack.pop()!="[":
            return False

    if stack:
        return False

    return True

res=balanced_or_not(s)

if res==True:
    print("balanced")
else:
    print("not balanced")


