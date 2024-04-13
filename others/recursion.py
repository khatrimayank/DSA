def addition(n):

    if n==0:
        return  0

    else:
        s=n+addition(n-1)
        return s


print(addition(2))


def factorial(n):

    if n==0 or n==1:
        return 1

    elif n>1:
        s=n*factorial(n-1)
        return s 


print(factorial(10))

def binary(n):

    if n==0:
        return
    else:
         binary(n//2)
         print(n%2,end="")
        

binary(2)
