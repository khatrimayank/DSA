import random

system_guess=random.randint(1000,9999)#1234

system_guess=str(system_guess)

l=0

print("system guess number=",end="")

c=["*","*","*","*"]

print("".join(c))

def validate(x):

    x=str(x)

    length_input=len(x)

    if length_input!=4:
        return False



    for i in range(length_input):

        if x[i] in ["0","1","2","3","4","5","6","7","8","9"]:

            return True

        else:
            return False



game=True

while game:
      
            user_input=(input("please guess 4 digit no:"))

            user_input=str(user_input)

            is_valid_input=validate(user_input)

            if is_valid_input!=True:
                continue


            k=0
            
            for j in range(0,4):
                if user_input[j]==system_guess[j]:
                    c[j]=user_input[j]
                    k+=1
                    continue
                
            if user_input!=system_guess:
                print("Not quite the number. But you did get {} digit(s) correct! ".format(k))
                print("system guess number=",end="")
                print("".join(c))

            l+=1

            if user_input==system_guess:
                 print("Congratulations!!")
                 print("\n you guess number in {} attempt".format(l))
                 game=False
                
