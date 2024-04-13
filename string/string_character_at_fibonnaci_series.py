s=input("please enter string :")

#0,1,2,3,5,8,13,21


def fun(s):
    
    ss=""

    l=len(s)

    def fibonacci(n):

    	if n==1:
    		return 0

    	elif n==2 or n==3:
    		return 1

    	else:
    		return fibonacci(n-1)+fibonacci(n-2)

    j=0
    #mayank j=0,1,2,3,4,5
    while j<l:
    	for i in range(1,l+1):
    		if fibonacci(i)<=l and j==fibonacci(i):
    			ss+=s[j]
    			break
    		

    	j+=1
#f(1)=0,f(2)=1,f(3)=1,f(4)=2,f(5)=3,f(6)=5,f(7)=8,f(8)=13,f(9)=21 #mayank

    return(ss)

print(fun(s))



