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

banner.banner_status(colored_status="i",season_num=1)
print ("Welcome to my Hybrid Football manager & NFL game")
print ("Basic premise is you have a squad, a budget and each year you improve your team by:")
print ("1) draft new players")
print ("2) depending on age and other factors players will improve through training")
print ("3) chosing free agents")
print ("Each player can potentially play in a number of positions")
input("Press enter to continue")
banner.banner_status(colored_status="i",season_num=1)
import player_creation
player_squad=player_creation.core_run()
season_to_play=5
input("Press enter to continue")

for i in range (1,season_to_play):
    banner.banner_status(colored_status="ps",season_num=i)
    import  pre_season
    team_chosen,team_stats_chosen=pre_season.starting_preseason(squad=player_squad)
    #import team_rating
    #season_formation=team_rating.team_formation()
    #type_of_team=team_rating.best_team()
    #print (season_formation)
    banner.banner_status(colored_status="s",season_num=i)
    import season
    season.main_run(team_stats_chosen_in=team_stats_chosen)
    banner.banner_status(colored_status="cs",season_num=i)
    import  end_of_season
    end_of_season.main_run()
    banner.banner_status(colored_status="d",season_num=i)
    import end_of_season_draft
    banner.banner_status(colored_status="fa",season_num=i)
    import end_of_season_free_agency
    #player_squad=end_of_season_free_agency.create_free_agency(player_squad)
    player_squad=end_of_season_free_agency.main_run(our_squad=player_squad)




