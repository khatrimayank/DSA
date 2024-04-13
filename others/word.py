lis=['apple','boy','catelogue','dog','earphone','fan','gun','hammer','ice','elephant']

import random

l=len(lis) #l=10

system=lis[random.randrange(10)] #hammer

arr=[None] * len(system)

print("system guess:{}".format(system))

for j in range(len(system)):
     
    user=input("please guess a character:")

    user=str(user)

    for i in range(len(system)):

         if user==system[i]:

            arr[j]=user

            print("you right")
            


    if arr==list(system):
        print("you won")
        break

    




  






    
        
