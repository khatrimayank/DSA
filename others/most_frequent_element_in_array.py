from operator import itemgetter 

arr = [40,50,30,40,50,30,30]

def most_frequent_element(arr):
	
	dic={}

	for i in range(len(arr)):

		if arr[i] in dic:
			dic[arr[i]]+=1

		else:
			dic[arr[i]]=1

	return max(dic.items(),key=itemgetter(1))

print(most_frequent_element(arr)[0])