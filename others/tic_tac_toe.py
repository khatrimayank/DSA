Null_matrix=[[0,0,0],[0,0,0],[0,0,0]]

def matrix():
    for i in range(3):
        print(Null_matrix[i])

matrix()

player_1=True
player_2=True

k=0

while player_1 and player_2:

        if k<9:

        
            a=int(input("please enter the row no :"))
            b=int(input("please enter the column no :"))

            if (a==1 or a==2 or a==3) and (b==1 or b==2 or b==3):

                if Null_matrix[a-1][b-1]==0:

                    if k%2==0:
                        c=1
                        
                    elif k%2!=0:
                        c=2

                    k+=1
                    print("k=",k)
                        
                    Null_matrix[a-1][b-1]=int(c)

                    matrix()

                else:
                    print("please try again space is not empty")
                    continue

                if Null_matrix[0][0]==Null_matrix[1][1]==Null_matrix[2][2]==1 or Null_matrix[0][2]==Null_matrix[1][1]==Null_matrix[2][0]==1 :
                    print("player 1 won")
                    player_1=False
                    break

                if Null_matrix[0][0]==Null_matrix[1][1]==Null_matrix[2][2]==2 or Null_matrix[0][2]==Null_matrix[1][1]==Null_matrix[2][0]==2 :
                    print("player 2 won")
                    player_2=False
                    break

                s=0
                
                if Null_matrix[s][s]==Null_matrix[s][s+1]==Null_matrix[s][s+2]==1 or Null_matrix[s+1][s]==Null_matrix[s+1][s+1]==Null_matrix[s+1][s+2]==1 or Null_matrix[s+2][s]==Null_matrix[s+2][s+1]==Null_matrix[s+2][s+2]==1:
                    print("player 1 won")
                    player_1=False
                    break

                if Null_matrix[s][s]==Null_matrix[s+1][s]==Null_matrix[s+2][s]==1 or Null_matrix[s][s+1]==Null_matrix[s+1][s+1]==Null_matrix[s+2][s+1]==1 or Null_matrix[s][s+2]==Null_matrix[s+1][s+2]==Null_matrix[s+2][s+2]==1:
                    print("player 1 won")
                    player_1=False
                    break
                    
                        
                if Null_matrix[s][s]==Null_matrix[s][s+1]==Null_matrix[s][s+2]==2 or Null_matrix[s+1][s]==Null_matrix[s+1][s+1]==Null_matrix[s+1][s+2]==2 or Null_matrix[s+2][s]==Null_matrix[s+2][s+1]==Null_matrix[s+2][s+2]==2:
                    print("player 2 won")
                    player_1=False
                    break
                    

                if Null_matrix[s][s]==Null_matrix[s+1][s]==Null_matrix[s+2][s]==2 or Null_matrix[s][s+1]==Null_matrix[s+1][s+1]==Null_matrix[s+2][s+1]==2 or Null_matrix[s][s+2]==Null_matrix[s+1][s+2]==Null_matrix[s+2][s+2]==2:
                    print("player 2 won")
                    player_1=False
                    break


            else:
                print("you enter wrong value plaese try again")
                continue
        else:
            print("MATCH DRAW")
            break
            






