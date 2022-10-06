#!/usr/bin/python
opposition_teams=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
print (opposition_teams)
games_in_season=16
my_defense=90
my_attack=90
import random
games_won=0
games_drawen=0
games_lost=0

for i in opposition_teams:
    opposition_defence=random.randint(80,100)
    opposition_attack=random.randint(80,100)
    if opposition_defence > my_attack:
        my_goals=random.randint(2,5)
    else:
        my_goals=random.randint(0,2)

    if opposition_attack > my_defense:
        opp_goals=random.randint(2,5)
    else:
        opp_goals=random.randint(0,2)
    
    print ("Game " + i +" Score" + str(my_goals) +  " - " + str(opp_goals))
    if my_goals >  opp_goals:
        games_won+=1
    elif opp_goals > my_goals:
        games_lost+=1
    else:
        games_drawen+=1

print ("Season record W D L")
print ("        ",games_won,games_drawen,games_lost)
        

