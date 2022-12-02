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
print ("Basic premise is you have a given a default squad, a budget and each year you manage your team to hopefully superbowl success")
print()
print ("Steps in a season:")
print()
print ("Pre_Season -Choose how you want your team selected (Youthfull, best avaliable or a blend)")
print ("Season -Play 16 games")
print ("Play-Off -if you win enough regular season games")
print ("End-Off-Season -players contract length is reduced by 1 and effect of training/age take effect, you can also buy/sell or renew contracts ")
print ("Draft - Depending on how your season went and player sold use you Draft picks to select younger players to strenghtn your squad  ")
print ("Free Agency - Fill any gaps in your squad with older more experienced players (and any undrafted players) ")
print ()
print ("More detailed notes:")
print ("-you must have 24 players")
print ("-your team play a 4-4-2 formation")
print ("-your squad must have a mimumum of 3 Goalkeepers, 1 Left Back, 1 Right Back, 2 Center Backs,1 Left Midfielder, 1 Right Midfielder, 2 Center Midfielders, 5 Strickers")
print ("-So your GK/S don't have any flexability you can have flexability on the number of defenders and midfields in your squad")
print ("-The maximum overall ratings is 100")
print ("-A players overall rating is made up of players indivudal charactecstis")
print ("-The Individual skills and Physical attributes are at Maximum 20")
input("Press enter to continue and start the game")
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




