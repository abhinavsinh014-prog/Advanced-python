import random 

teamA_score = 0
teamB_score = 0

overs = input("enter number of overs :")

team_A =  {"player_1":0,
           "player_2":0,
           "player_3":0,
           "player_4":0,
           "player_5":0,
           "player_6":0,
           "player_7":0,
           "player_8":0,
           "player_9":0
           ,"player_10":0,
           "player_11":0}

team_B =  {"player_1":0,
           "player_2":0,
           "player_3":0,
           "player_4":0,
           "player_5":0,
           "player_6":0,
           "player_7":0,
           "player_8":0,
           "player_9":0
           ,"player_10":0,
           "player_11":0} 


winner = random.choice(["teamA","teamB"])

print('toss winner is ',winner)

winner_choice = input("bating or bowling")

if winner is 'teamA' :
    if winner_choice is "batting" :
