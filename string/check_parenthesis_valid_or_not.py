p=input("please enter parenthesis :")#"([]{[()]})"

l=len(p)

s=[]

def f(p,l,s):

	if l%2==0:
		for i in p:
			print("i=",i)
			if i not in ["(",")","{","}","[","]"]:
				return False

			else:
				if i in ["(","{","["]:
					s.append(i)
					print("s=",s)

				elif len(s) :
					if i=="}"  :
						s.pop()
					elif i==")":
						s.pop()
					elif (i=="]"):
						s.pop()
					else:
						return False

					print('s=',s)

	else:
		return False

ans=f(p,l,s)

if ans==False:
	print("not valid")

else:
	print("valid")