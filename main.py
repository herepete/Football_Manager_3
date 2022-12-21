#!/usr/bin/python3
# Welcome
# Player Creation
# team report
# Season x
# play games
# play off
# end of season
# draft
# free agency

import os
import banner

banner.banner_status(colored_status="i", season_num=1)
print("Welcome to my Hybrid Football manager & NFL game")
print(
    "Basic premise is you have a given a default squad, a budget and each year you manage your team to hopefully superbowl success"
)
print()
print("Steps in a season:")
print()
print(
    "Pre_Season -Choose how you want your team selected (Youthfull, best avaliable or a blend)"
)
print("Season -Play 16 games")
print("Play-Off -if you win enough regular season games")
print(
    "End-Off-Season -players contract length is reduced by 1 and effect of training/age take effect, you can also buy/sell or renew contracts "
)
print(
    "Draft - Depending on how your season went and player sold use you Draft picks to select younger players to strenghtn your squad  "
)
print(
    "Free Agency - Fill any gaps in your squad with older more experienced players (and any undrafted players) "
)
print()
print("More detailed notes:")
print("-you must have 24 players")
print("-your team play a 4-4-2 formation")
print(
    "-your squad must have a mimumum of 3 Goalkeepers, 1 Left Back, 1 Right Back, 2 Center Backs,1 Left Midfielder, 1 Right Midfielder, 2 Center Midfielders, 5 Strickers"
)
print(
    "-So your GK/S don't have any flexability you can have flexability on the number of defenders and midfields in your squad"
)
print("-The maximum overall ratings is 100")
print("-A players overall rating is made up of players indivudal charactecstis")
print("-The Individual skills and Physical attributes are at Maximum 20")
input("Press enter to continue and start the game")
banner.banner_status(colored_status="i", season_num=1)
import player_creation

player_squad = player_creation.core_run()
season_to_play = 5
input("Press enter to continue")


# Testing data#
"""
player_squad=[[['GK'], 'Sean', 'Robbie', 24, 19, 15, 12, 15, 16, 18, 88, 8, 4, 1, 'Leader', '****', 0, 'DP', 1910617], [['GK'], 'Banele', 'Bo', 36, 14, 20, 11, 15, 19, 16, 67, 5, 4, 0, 'Avg', '**', 0, 'DP', 3037073], [['GK'], 'Dylon', 'Sean', 26, 11, 18, 18, 13, 10, 14, 53, 1, 1, 0, 'Avg', '***', 0, 'DP', 2412897], ['LB', 'Josh', 'Master', 27, 3, 20, 14, 15, 11, 10, 71, 2, 1, 0, 'Avg', '*', 0, 'DP', 7226365], ['RB', 'Rambo', 'Haji', 30, 3, 12, 20, 13, 20, 13, 73, 6, 2, 1, 'Fighter', '**', 0, 'DP', 3460661], ['RB', 'Haji', 'Blesing', 27, 2, 12, 13, 18, 19, 16, 68, 5, 2, 0, 'Avg', '**', 0, 'DP', 3211062], ['RB', 'Peter', 'Me', 21, 1, 14, 11, 15, 10, 15, 61, 5, 1, 0, 'Avg', '*****', 0, 'DP', 5838499], ['CB', 'Robbie', 'Sean', 28, 2, 16, 13, 14, 20, 14, 73, 5, 4, 0, 'Avg', '**', 0, 'DP', 9144201], ['CB', 'Sero', 'Titch', 35, 1, 18, 14, 20, 11, 12, 68, 2, 2, 0, 'Avg', '*', 0, 'DP', 919944], ['CB', 'Ross', 'Brian', 24, 1, 14, 13, 12, 15, 18, 67, 3, 2, 0, 'Laid B', '****', 0, 'DP', 4651949], ['CB', 'Bob', 'Dylon', 18, 1, 10, 11, 19, 14, 16, 57, 4, 3, 0, 'Avg', '*****', 0, 'DP', 5424996], ['LM', 'Kim', 'Robbie', 36, 3, 14, 10, 15, 11, 16, 58, 5, 2, 0, 'Avg', '*', 0, 'DP', 1959844], ['RM', 'Titch', 'Haji', 27, 3, 10, 14, 18, 16, 16, 72, 6, 2, 1, 'Team P', '*', 0, 'DP', 1567118], ['RM', 'Blesing', 'Xavier', 19, 3, 17, 15, 11, 14, 17, 71, 4, 1, 0, 'Avg', '****', 0, 'DP', 8065792], ['RM', 'Bob', 'Blesing', 18, 3, 13, 10, 12, 14, 16, 63, 5, 4, 1, 'Fighter', '**', 0, 'DP', 4087000], ['RM', 'Zak', 'Silver', 26, 2, 11, 11, 12, 13, 14, 60, 2, 2, 1, 'Team P', '**', 0, 'DP', 2595306], ['CM', 'Haji', 'Robert', 29, 1, 19, 12, 15, 18, 17, 75, 2, 2, 0, 'Avg', '***', 0, 'DP', 5715328], ['CM', 'David', 'Robbie', 20, 1, 10, 16, 19, 14, 16, 73, 5, 1, 1, 'Team P', '***', 0, 'DP', 5923819], ['CM', 'Bo', 'Ung', 23, 1, 14, 20, 12, 19, 11, 71, 5, 2, 1, 'Leader', '***', 0, 'DP', 6908755], ['ST', 'Bruno', 'See', 36, 3, 11, 20, 19, 16, 13, 80, 6, 2, 0, 'Avg', '*', 0, 'DP', 7386474], ['ST', 'Banner', 'Titch', 24, 2, 19, 14, 16, 15, 18, 75, 6, 3, 1, 'Fighter', '****', 0, 'DP', 7491627], ['ST', 'Blesing', 'Tim', 22, 3, 14, 13, 17, 14, 13, 70, 5, 2, 0, 'Laid B', '***', 0, 'DP', 5232136], ['ST', 'See', 'Zak', 18, 3, 18, 17, 10, 14, 18, 61, 5, 1, 1, 'Fighter', '***', 0, 'DP', 7838432], ['ST', 'Piero', 'See', 37, 1, 16, 19, 11, 17, 12, 59, 6, 4, 0, 'Avg', '***', 0, 'DP', 772765]]

team_stats_chosen=[[88, 70, 73, 15, 5]]

team_chosen=[[[['GK'], 'Sean', 'Robbie', 24, 19, 15, 12, 15, 16, 18, 88, 8, 4, 1, 'Leader', '****', 0, 'DP', 1910617], ['LB', 'Josh', 'Master', 27, 3, 20, 14, 15, 11, 10, 71, 2, 1, 0, 'Avg', '*', 0, 'DP', 7226365], ['RB', 'Rambo', 'Haji', 30, 3, 12, 20, 13, 20, 13, 73, 6, 2, 1, 'Fighter', '**', 0, 'DP', 3460661], ['CB', 'Robbie', 'Sean', 28, 2, 16, 13, 14, 20, 14, 73, 5, 4, 0, 'Avg', '**', 0, 'DP', 9144201], ['CB', 'Sero', 'Titch', 35, 1, 18, 14, 20, 11, 12, 68, 2, 2, 0, 'Avg', '*', 0, 'DP', 919944], ['CM', 'Haji', 'Robert', 29, 1, 19, 12, 15, 18, 17, 75, 2, 2, 0, 'Avg', '***', 0, 'DP', 5715328], ['CM', 'David', 'Robbie', 20, 1, 10, 16, 19, 14, 16, 73, 5, 1, 1, 'Team P', '***', 0, 'DP', 5923819], ['LM', 'Kim', 'Robbie', 36, 3, 14, 10, 15, 11, 16, 58, 5, 2, 0, 'Avg', '*', 0, 'DP', 1959844], ['RM', 'Titch', 'Haji', 27, 3, 10, 14, 18, 16, 16, 72, 6, 2, 1, 'Team P', '*', 0, 'DP', 1567118], ['ST', 'Bruno', 'See', 36, 3, 11, 20, 19, 16, 13, 80, 6, 2, 0, 'Avg', '*', 0, 'DP', 7386474], ['ST', 'Banner', 'Titch', 24, 2, 19, 14, 16, 15, 18, 75, 6, 3, 1, 'Fighter', '****', 0, 'DP', 7491627]]]
"""


for i in range(1, season_to_play):
    banner.banner_status(colored_status="ps", season_num=i)
    import pre_season

    team_chosen, team_stats_chosen = pre_season.starting_preseason(squad=player_squad)
    # fixing a bug where list is to nested
    team_chosen=team_chosen[0]
    # import team_rating
    # season_formation=team_rating.team_formation()
    # type_of_team=team_rating.best_team()
    # print (season_formation)
    banner.banner_status(colored_status="s", season_num=i)
    import season

    season.main_run(team_stats_chosen_in=team_stats_chosen, season_num_in=i)
    banner.banner_status(colored_status="cs", season_num=i)
    import season_wind_down

    season_wind_down_returned_squad=season_wind_down.main_run(player_squad,team_chosen,"np")
    banner.banner_status(colored_status="d", season_num=i)
    import end_of_season_draft

    banner.banner_status(colored_status="fa", season_num=i)
    import end_of_season_free_agency

    # player_squad=end_of_season_free_agency.create_free_agency(player_squad)
    player_squad = end_of_season_free_agency.main_run(our_squad=player_squad)
