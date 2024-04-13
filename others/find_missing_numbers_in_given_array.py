num=[1,4,50,23,12,53]

low=50

high=55

def find_missing_numbers(num,low,high):

	num.sort()

	index_of_low=index_of_low_binary_search(num,low,0,len(num)-1)

	if index_of_low!=None:

		for i in range(low+1,high+1):

			if i not in num[index_of_low:]:

				print(i)

	elif index_of_low==None:

		for i in range(low,high+1):

			if i not in num:

				print(i)


	
def index_of_low_binary_search(num,low,start,end):
    
    if start>end:
    	return None

	mid=(start+end)//2

	if num[mid]==low:
		return mid

	elif num[mid]>low:
		index_of_low_binary_search(num,low,start,mid-1)

	elif num[mid]<low:
		index_of_low_binary_search(num,low,mid+1,end)

	else:
		return None

find_missing_numbers(num,low,high)

'''
def find_missing_numbers(num, low, high):
    num_set = set(num)
    missing_numbers = []

    for i in range(low, high + 1):
        if i not in num_set:
            missing_numbers.append(i)

    return missing_numbers

num = [1, 4, 50, 23, 12, 53]
low = 50
high = 55

missing_numbers = find_missing_numbers(num, low, high)
print("Missing numbers:", missing_numbers)'''