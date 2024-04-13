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
