file=open("activate.txt",'r')

list_file=file.readlines()

n=len(list_file)

if n<10:

	for i in range(n-1,-1,-1):

		print(list_file[i])

else:

	for i in range(n-1,n-11,-1):
		print(list_file[i].strip())

