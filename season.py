#!/usr/bin/python3.7
opposition_teams=["Arsenal","Man City","Tottenham","Chelsea","Man United","Newcastle","Brighton","Bournemouth","Fulham","Liverpool","Brentford","Everton","West Ham","Leeds United","Crystal Palace","Aston Villa","Southampton","Wolves","Nottm Forest","Leicester City"]
#print (opposition_teams)
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
    
    print ("Game " + i +" Score " + str(my_goals) +  " - " + str(opp_goals))
    if my_goals >  opp_goals:
        games_won+=1
    elif opp_goals > my_goals:
        games_lost+=1
    else:
        games_drawen+=1

print ("Season record")
print ("W D L")
print (games_won,games_drawen,games_lost)

playof_needed=0
straight_to_championship_game=0
out_of_playoff=0
play_off_won=0
no_playoff=0

if games_won < 10:
    print ("Season Result - Not good enough try again next season")
    no_playoff=1
elif games_won < 12:
    playof_needed=1
    play_off_won=0
    straight_to_championship_game=0
    out_of_playoff=0
    print ("Play off needed")
else:
    playof_needed=0
    straight_to_championship_game=2
    out_of_playoff=0
    #champtionship game
    print ("Straight to Championship game nice")

while True:

    if out_of_playoff==1 or no_playoff:
        print("Un lucky try again next season")
        input("Press enter to continue")
        break
    if playof_needed==1:
        print("yeh you won")
        playof_needed=0
        play_off_won=1
        input("Press enter to continue")
    if straight_to_championship_game or play_off_won:
        print ("Season Result - You won everything nice")
        input("Press enter to continue")
        break

    


