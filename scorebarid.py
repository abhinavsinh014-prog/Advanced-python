import random 

teamA_score = 0
teamB_score = 0

n = int(input("enter number of overs :"))
total_scoe = 0

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

winner_choice = input("bating or bowling :")

for overs in range(0,n) :
    for balls in range(1,7) :
        print(f"Over:{overs}.{balls}")
        run = int(input())


        total_scoe += run
    print(f"Score : {total_scoe}  Over : {overs+1}")


