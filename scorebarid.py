import random as rn

teamA_score = 0
teamB_score = 0

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

call = input()
if call == 'head':
    print('that team won')
elif call == 'tail':
    print('that team won')
else :
    print('invlaid call')