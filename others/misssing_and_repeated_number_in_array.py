arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 13, 14, 15]

n=len(arr)

curr_sum=sum(arr)

actual_sum=n*(n+1)/2

for i in range(n-1):

	if arr[i]==arr[i+1]:
		twice=arr[i]

print(f"repeated number :{twice}")

print("missing number : {}".format(int(actual_sum-(curr_sum-twice))))