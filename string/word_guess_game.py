list=["apple","banana","cat","dog","elephant","fish","goat","hammer"]

arr=[]

import random

length=len(list)

system_guess=list[random.randrange(0,length)]

print(system_guess)

print("you will have 6 attempts for each character of an system guess item")


for i in range(0,len(system_guess)):

    for j in range(0,6):

    
        user=input("guess your {} character in your {} attempt:".format(i+1,j+1)
)
        if user==system_guess[i]:
        
           arr.append(user)
           print(arr)
           break

        else:
          print("you lose your {} guess chance".format(j+1))
          if j==5:
              print("GAME OVER")


if "".join(arr)==system_guess:

      print("CONGRATULATIONS YOU WON ")

        

       

    
