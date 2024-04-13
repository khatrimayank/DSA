a=int(input("lower limit:"))
b=int(input("upper limit:"))


i=1

import random
from math import log

c = random.randrange(int(a),int(b))

e=log((b-a),2)
        
d=int(e)

print("you only have {} lfet chances".format(d))

user=int(input("please any number between range of a and b:"))
        
      
if c ==(user):
        
     print("you win")

else:
     while c!=user and d>0:
    
        if int(user)>c:
           i+=1
           print("your guess no is higher than system guess")
          

           if d>0:
                print("please try again")
                d-=1
                print("you only have {} lfet chances".format(d))
                user=int(input("please any number between range of a and b:"))
           
        else :
           i+=1
           print("your guess no is lower than system guess")
           d-=1
          
           if d>0:
                print("you only have {} lfet chances".format(d))
                print("please try again")
                user=int(input("please any number between range of a and b:"))
      
if c ==(user):
        
     print("you win in attempts={}".format(i))

else:
    print("you lose")
