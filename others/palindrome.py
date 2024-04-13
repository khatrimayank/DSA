'''s="kanaak"

if s==s[::-1]:
    print("given string is palindrome")

else:
    print("not palindrome")'''

def palindrome_or_not(s):
    for i in range(len(s)):
        if s[i]==s[len(s)-1-i]:
            continue
        else:
            return False

    return True

print(palindrome_or_not(s))
'''s='kaank'

def palindorme(string,l,h):

    while l<=h:

        if string[l]==string[h]:
            l+=1
            h-=1
            continue

        else:
            print("no")
            return


    return print("yes")

        




palindorme(s,0,len(s)-1)