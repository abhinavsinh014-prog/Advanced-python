import random 

team_A =  {"player_1":{"runs" : 0,"wickets":0},
           "player_2":{"runs" : 0,"wickets":0},
           "player_3":{"runs" : 0,"wickets":0},
           "player_4":{"runs" : 0,"wickets":0},
           "player_5":{"runs" : 0,"wickets":0},
           "player_6":{"runs" : 0,"wickets":0},
           "player_7":{"runs" : 0,"wickets":0},
           "player_8":{"runs" : 0,"wickets":0},
           "player_9":{"runs" : 0,"wickets":0},
           "player_10":{"runs" : 0,"wickets":0},
           "player_11":{"runs" : 0,"wickets":0}}

team_B =  {"player_1":{"runs" : 0,"wickets":0},
           "player_2":{"runs" : 0,"wickets":0},
           "player_3":{"runs" : 0,"wickets":0},
           "player_4":{"runs" : 0,"wickets":0},
           "player_5":{"runs" : 0,"wickets":0},
           "player_6":{"runs" : 0,"wickets":0},
           "player_7":{"runs" : 0,"wickets":0},
           "player_8":{"runs" : 0,"wickets":0},
           "player_9":{"runs" : 0,"wickets":0},
           "player_10":{"runs" : 0,"wickets":0},
           "player_11":{"runs" : 0,"wickets":0}}

def toss():
    winner = random.choice(["Team A", "Team B"])
    print("Toss winner:", winner)

    choice = input("Bat or Bowl: ").lower()

    if choice == "bat":
        batting = winner
    else:
        batting = "Team B" if winner == "Team A" else "Team A"

    return batting


def play_innings(overs, target=None):
    score = 0
    wickets = 0

    for over in range(overs):
        for ball in range(1, 7):

            print(f"Over {over}.{ball}")
            run = int(input("Enter run (-1 for wicket): "))

            if run == -1:
                wickets += 1
                print("WICKET!")

                if wickets == 10:
                    return score

            else:
                score += run

            if target and score > target:
                return score

        print(f"Score: {score}/{wickets}")

    return score


def declare_winner(score1, score2):
    print("\nFinal Score")
    print("Team 1:", score1)
    print("Team 2:", score2)

    if score1 > score2:
        print("Team 1 Wins")
    elif score2 > score1:
        print("Team 2 Wins")
    else:
        print("Match Draw")


overs = int(input("Enter number of overs: "))

batting_first = toss()

print("\nFirst Innings")
score1 = play_innings(overs)

print("\nSecond Innings")
score2 = play_innings(overs, score1)

declare_winner(score1, score2)