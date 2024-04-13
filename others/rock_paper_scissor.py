user_1_name=input("please enter player 1 name:")

user_2_name=input("please enter player 2 name:")

a=([0,0,0],
   [0,0,0],             
   [0,0,0])

def user_input(i):
    if i%2==0:
        print("{} it's your turn".format(user_1_name))
        row_input=(input("Please enter row:"))
        column_input=(input("please enter column:"))
        return [row_input,column_input]

    if i%2!=0:
        print("{} it's your turn".format(user_2_name))
        row_input=(input("Please enter row:"))
        column_input=(input("please enter column:"))
        return [row_input,column_input]

def validate_user_input(row_input,column_input):

        if row_input not in ["1","2","3"] or column_input not in ["1","2","3"] :
            print("please enter valid input ")
            return False

        else:
            return True

def enter_value_in_matrix(i,a,row_input,column_input):

    if i%2==0:

        if(a[int(row_input)-1][int(column_input)-1]==0):
            a[int(row_input)-1][int(column_input)-1]=1
            return True
        else:
            return False

    if i%2!=0:

        if(a[int(row_input)-1][int(column_input)-1]==0):
            a[int(row_input)-1][int(column_input)-1]=2
            return True
        else:
            return False

def print_matrix():
    for j in range(3):
        print(a[j])

def check_win_conditions():
    s=0
    if a[0][0]==a[1][1]==a[2][2]==1 or a[0][2]==a[1][1]==a[2][0]==1 :
        print("player 1 won")
        player_1=False
    

    elif a[0][0]==a[1][1]==a[2][2]==2 or a[0][2]==a[1][1]==a[2][0]==2 :
        print("player 2 won")
        player_2=False


        
                
    elif a[s][s]==a[s][s+1]==a[s][s+2]==1 or a[s+1][s]==a[s+1][s+1]==a[s+1][s+2]==1 or a[s+2][s]==a[s+2][s+1]==a[s+2][s+2]==1:
        print("player 1 won")
        player_1=False
    

    elif a[s][s]==a[s+1][s]==a[s+2][s]==1 or a[s][s+1]==a[s+1][s+1]==a[s+2][s+1]==1 or a[s][s+2]==a[s+1][s+2]==a[s+2][s+2]==1:
        print("player 1 won")
        player_1=False
                    
                        
    elif a[s][s]==a[s][s+1]==a[s][s+2]==2 or a[s+1][s]==a[s+1][s+1]==a[s+1][s+2]==2 or a[s+2][s]==a[s+2][s+1]==a[s+2][s+2]==2:
        print("player 2 won")
        player_1=False
      
                    

    if a[s][s]==a[s+1][s]==a[s+2][s]==2 or a[s][s+1]==a[s+1][s+1]==a[s+2][s+1]==2 or a[s][s+2]==a[s+1][s+2]==a[s+2][s+2]==2:
        print("player 2 won")
        player_1=False
     

for i in range(9):

    ret=user_input(i)
    valid_input=validate_user_input(ret[0],ret[1])
    while not valid_input:
        ret=user_input(i)
        valid_input=validate_user_input(ret[0],ret[1])

    b=enter_value_in_matrix(i,a,ret[0],ret[1])
    while not b:
        print("this row and column place not empty")
        ret=user_input(i)
        valid_input=validate_user_input(ret[0],ret[1])
        b=enter_value_in_matrix(i,a,ret[0],ret[1])

    print_matrix()
    check_win_conditions()



