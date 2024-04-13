def bubble_sort(x):

	for i in range(len(x)):

		l=True

		for j in range(0,len(x)-i-1):

			if int(x[j])>int(x[j+1]):

				x[j],x[j+1]=x[j+1],x[j]
				l=False

		if l==True:
			break

integer=['0','1','2','3','4','5','6','7','8','9']
def validate_input_length(x):
	x=str(x)
	for i in range(len(x)):
		if x[i] not in integer or x[i]=="":
			return False
	return True

def validate_input_integer(y):
	y=str(y)
	for i in range(len(y)):
		if y[i] not in integer or x[i]=="":
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