size=128

count=[0]*size

string="teestsample"


def maximumcharacter(string):


    maxim=0

    for i in string:

        count[ord(i)]+=1

    for i in string:

        if maxim<count[ord(i)]:

            maxim=count[ord(i)]

            c=i
    return(c)

      


z=maximumcharacter(string)
print(z)
