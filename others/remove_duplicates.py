# using dictionary

s="appleejksckoickxzlksdohasksachcjepoqwertyaertyuipplmnbvcxzawefvbnklpoiuytrewasxcvbnm"


'''dict={}

for i in s:

	if i not in dict:
		print(i)
		dict[i]=1'''

# without extra space

n=len(s)

for i in range(n):

	if s.count(s[i],i,-1)>1:

		continue

	else:

		print(s[i],end="")

