# using join()

l=['a','b','c','d','e','f']

print("".join(l))

# using lamda+reduce


# using enumerate function

s=['g','e','e','k','s','f','o','r','g','e','e','k']
x="".join([str(i) for a,i in enumerate(s)])
print(x)

# using list comprehensive
s=['g','e','e','k','s','f','o','r','g','e','e','k']
x="".join([str(i) for i in s])
print(x)

# using reduce

import functools
 
def convert(s):
 
    str1 = functools.reduce(lambda x,y : x+y, s)
    return str1
     
s = ['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's']
print(convert(s))