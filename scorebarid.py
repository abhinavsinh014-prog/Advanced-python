import random 

n = int(input("enter number of overs :"))

total_score_1st = 0
total_score_2nd = 0
wickets_1st = 0
wickets_2nd = 0

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

if winner_choice == 'bating' :
    print(f"{winner} choose to bating first ")
elif winner_choice == 'bowling' :
    print(f"{winner} choose to feilding first ")

print("Let's Start the Game")

for inning in range(1,3):
    if inning == 1:
      print(f"{"1st inning"}")
      for overs in range(0,n) :
        for balls in range(1,7) :
            print(f"Over:{overs}.{balls}")
            run = int(input())
            if run == -1:
                wickets_1st += 1
                if wickets_1st==11:
                    break
            else:
                total_score_1st += run
        print(f"Score : {total_score_1st}  Over : {overs+1} wickets : {wickets_1st}")
    else:
        print(f"{"2nd inning"}")
        for overs in range(0,n) :
            for balls in range(1,7) :
                print(f"Over:{overs}.{balls}")
                run = int(input())
                if run == -1:
                    wickets_2nd+= 1
                    if wickets_2nd==11:
                        break
                else:
                    total_score_2nd += run
                    if total_score_1st<total_score_2nd :
                        break
        print(f"Score : {total_score_2nd}  Over : {overs+1} wickets : {wickets_2nd}")

if total_score_1st<total_score_2nd:
    print("Team 2 is winner")
else:
    print("Team 1 is winner")