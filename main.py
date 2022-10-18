#!/usr/bin/python3
# Welcome
    #Player Creation
    #team report
# Season x
    #play games
    #play off
    #end of season
    #draft
    #free agency
    
import os
os.system('clear')
print ("Welcome to my Hybrid Football manager & NFL game")
print ("Basic premise is you have a squad, a budget and each year you improve your team by:")
print ("1) draft new players")
print ("2) depending on age and other factors players will improve through training")
print ("3) chosing free agents")
print ("Each player can potentially play in a number of positions")
input("Press enter to continue")
import player_creation
player_squad=player_creation.core_run()
season_to_play=2
input("Press enter to continue")

for i in range (1,season_to_play):
    import  pre_season
    print ("Start Season=",i)
    import team_rating
    season_formation=team_rating.team_formation()
    type_of_team=team_rating.best_team()
    print (season_formation)
    import season
    import end_of_season_free_agency
    import end_of_season_draft



