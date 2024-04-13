import random

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

player_1_name=input("player 1, Please enter your name :")
player_2_name=input("\nplayer 2, Please enter your name:")


p1_score=0
p2_score=0

def play(p):

    word=random.choice(words)

    jumbled="".join(random.sample(word,len(word)))

    print("\njumbled word is:",jumbled)

    print("\n{} your turn".format(p))

    user=input("\nwhat is in your mind?")

    if user==word:
        global p1_score
        global p2_score

        if p==player_1_name:
            p1_score+=1
            print("\n{} your score is :{}".format(p,p1_score))

        else:
            p2_score+=1
            print("\n{} your score is :{}".format(p,p2_score))

 
    else:
        print("\nbetter luck next time")

for i in range(10):
    play(player_1_name)
    play(player_2_name)

if p1_score>p2_score:
    print("{} is won".format(player_1_name)

if p2_score>p1_score:
    print("{} is won".format(player_2_name)


if p1_score==p2_score:
    print("DRAW")

        
    
