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
import banner

banner.banner_status(colored_status="i")
print ("Welcome to my Hybrid Football manager & NFL game")
print ("Basic premise is you have a squad, a budget and each year you improve your team by:")
print ("1) draft new players")
print ("2) depending on age and other factors players will improve through training")
print ("3) chosing free agents")
print ("Each player can potentially play in a number of positions")
input("Press enter to continue")
banner.banner_status(colored_status="i")
import player_creation
player_squad=player_creation.core_run()
season_to_play=2
input("Press enter to continue")

for i in range (1,season_to_play):
    banner.banner_status(colored_status="ps")
    import  pre_season
    import team_rating
    #season_formation=team_rating.team_formation()
    #type_of_team=team_rating.best_team()
    #print (season_formation)
    banner.banner_status(colored_status="s")
    import season
    banner.banner_status(colored_status="fa")
    import end_of_season_free_agency
    banner.banner_status(colored_status="d")
    import end_of_season_draft



