def bubble_sort(x):#46259

	for i in range(1,len(x)):

		temp=x[i]

		j=i-1

		while j>=0 and x[j]>temp :
			x[j+1]=x[j]
			j-=1

		x[j+1]=temp


	

integer=['0','1','2','3','4','5','6','7','8','9']
def validate_input_length(x):
	x=str(x)
	for i in range(len(x)):
		if x[i] not in integer:
			return False
	return True

def validate_input_integer(y):
	y=str(y)
	for i in range(len(y)):
		if y[i] not in integer:
			return False
	return True

arr=[]
z=True

while z:

	input_length=(input("input legth of array:"))
	a=validate_input_length(input_length)
	if a!=True:
		print("please enter valid length of array")
		continue
	count=0
	while count<int(input_length):
		input_no=input("input array integer to sort:")
		b=validate_input_integer(input_no)
		if b!=True:
			print("please enter valid integer of array")
			continue
		else:
			count+=1
			arr.append(input_no)

	z=False

	print("array you entered:",arr)

	

bubble_sort(arr)

for i in range(len(arr)):
	print(arr[i],end="")