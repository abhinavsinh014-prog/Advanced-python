import random 

teamA_score = 0
teamB_score = 0

n = int(input("enter number of overs :"))
total_scoe = 0
wickets = 0
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
for inning in range(1,3):
    if inning == 1:
      print(f"{"1st inning"}")
    else:
        print(f"{"2nd inning"}")
    for overs in range(0,n) :
        for balls in range(1,7) :
            print(f"Over:{overs}.{balls}")
            run = int(input())
            if run == -1:
                wickets += 1
                if wickets==11:
                    break
            else:
                total_scoe += run
    print(f"Score : {total_scoe}  Over : {overs+1} wickets : {wickets}")


