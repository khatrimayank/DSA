# using enumerate function

# it is used to loop through container/iterable
# return index with value at particular index (index,value) 
# used for loop , or converted in list,tuple

s="abcdef"

l=[]

for key,value in enumerate(s):

	l.append(value)

print(l)


#using split method

s="a b c d e f"

print(s.split(" "))

#using slicing

s="abcdef"

l=[]

l[:0]=s

print(l)

#using list comprehensive

s='abcdef'

l=[i for i in s]

print(l)