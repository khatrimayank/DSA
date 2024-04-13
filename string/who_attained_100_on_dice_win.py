player_1_score=0
player_2_score=0

i=1

import random


while player_1_score<100 and player_2_score<100 :
    
     a=random.randint(1,10)
     player_1_score=player_1_score+a
     print("player 1 score after i turn is ={}\n".format(player_1_score))
     
     b=random.randint(1,10)
     player_2_score=player_2_score+b
     print("player 2 score after i turn is ={}\n".format(player_2_score))


     if player_1_score>=100:
         print("player 1 win")

     elif player_2_score>=100:
         print("player 2 win")

     
