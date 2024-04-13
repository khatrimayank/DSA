n=int(input("enter number till u want prime numbers :"))

def is_prime(no):

	for i in range(2,int(no**0.5)+1):
		if no%i==0:
			return False

	return True

def print_prime_numbers(n):

	for i in range (2,n):

		if is_prime(i):
			print(i)

		else:
			continue

print_prime_numbers(n)
