s='kaank'

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