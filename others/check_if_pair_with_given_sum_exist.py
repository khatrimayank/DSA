def fun(num,target):

	d={}

	for index,value in enumerate(num) :

		temp=target-value

		if temp in d:
			
			return True

		d[value]=index

	return False


target=int(input("enter target between 1 to 100 :"))
num=[1,4,21,42,54,56,32,51]

print(fun(num,target))