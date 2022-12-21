#!/usr/bin/python3
import argparse
import logging
import player_creation
import game_settings
import random
from termcolor import colored
import time


parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="Verbose information", action="store_true")
args = parser.parse_args()

# for_testing
player_squad = [
    [
        ["GK"],
        "Sean",
        "Robbie",
        24,
        19,
        15,
        12,
        15,
        16,
        18,
        88,
        8,
        4,
        1,
        "Leader",
        "****",
        0,
        "DP",
        1910617,
    ],
    [
        ["GK"],
        "Banele",
        "Bo",
        36,
        14,
        20,
        11,
        15,
        19,
        16,
        67,
        5,
        4,
        0,
        "Avg",
        "**",
        0,
        "DP",
        3037073,
    ],
    [
        ["GK"],
        "Dylon",
        "Sean",
        26,
        11,
        18,
        18,
        13,
        10,
        14,
        53,
        1,
        1,
        0,
        "Avg",
        "***",
        0,
        "DP",
        2412897,
    ],
    [
        "LB",
        "Josh",
        "Master",
        27,
        3,
        20,
        14,
        15,
        11,
        10,
        71,
        2,
        1,
        0,
        "Avg",
        "*",
        0,
        "DP",
        7226365,
    ],
    [
        "RB",
        "Rambo",
        "Haji",
        30,
        3,
        12,
        20,
        13,
        20,
        13,
        73,
        6,
        2,
        1,
        "Fighter",
        "**",
        0,
        "DP",
        3460661,
    ],
    [
        "RB",
        "Haji",
        "Blesing",
        27,
        2,
        12,
        13,
        18,
        19,
        16,
        68,
        5,
        2,
        0,
        "Avg",
        "**",
        0,
        "DP",
        3211062,
    ],
    [
        "RB",
        "Peter",
        "Me",
        21,
        1,
        14,
        11,
        15,
        10,
        15,
        61,
        5,
        1,
        0,
        "Avg",
        "*****",
        0,
        "DP",
        5838499,
    ],
    [
        "CB",
        "Robbie",
        "Sean",
        28,
        2,
        16,
        13,
        14,
        20,
        14,
        73,
        5,
        4,
        0,
        "Avg",
        "**",
        0,
        "DP",
        9144201,
    ],
    [
        "CB",
        "Sero",
        "Titch",
        35,
        1,
        18,
        14,
        20,
        11,
        12,
        68,
        2,
        2,
        0,
        "Avg",
        "*",
        0,
        "DP",
        919944,
    ],
    [
        "CB",
        "Ross",
        "Brian",
        24,
        1,
        14,
        13,
        12,
        15,
        18,
        67,
        3,
        2,
        0,
        "Laid B",
        "****",
        0,
        "DP",
        4651949,
    ],
    [
        "CB",
        "Bob",
        "Dylon",
        18,
        1,
        10,
        11,
        19,
        14,
        16,
        57,
        4,
        3,
        0,
        "Avg",
        "*****",
        0,
        "DP",
        5424996,
    ],
    [
        "LM",
        "Kim",
        "Robbie",
        36,
        3,
        14,
        10,
        15,
        11,
        16,
        58,
        5,
        2,
        0,
        "Avg",
        "*",
        0,
        "DP",
        1959844,
    ],
    [
        "RM",
        "Titch",
        "Haji",
        27,
        3,
        10,
        14,
        18,
        16,
        16,
        72,
        6,
        2,
        1,
        "Team P",
        "*",
        0,
        "DP",
        1567118,
    ],
    [
        "RM",
        "Blesing",
        "Xavier",
        19,
        3,
        17,
        15,
        11,
        14,
        17,
        71,
        4,
        1,
        0,
        "Avg",
        "****",
        0,
        "DP",
        8065792,
    ],
    [
        "RM",
        "Bob",
        "Blesing",
        18,
        3,
        13,
        10,
        12,
        14,
        16,
        63,
        5,
        4,
        1,
        "Fighter",
        "**",
        0,
        "DP",
        4087000,
    ],
    [
        "RM",
        "Zak",
        "Silver",
        26,
        2,
        11,
        11,
        12,
        13,
        14,
        60,
        2,
        2,
        1,
        "Team P",
        "**",
        0,
        "DP",
        2595306,
    ],
    [
        "CM",
        "Haji",
        "Robert",
        29,
        1,
        19,
        12,
        15,
        18,
        17,
        75,
        2,
        2,
        0,
        "Avg",
        "***",
        0,
        "DP",
        5715328,
    ],
    [
        "CM",
        "David",
        "Robbie",
        20,
        1,
        10,
        16,
        19,
        14,
        16,
        73,
        5,
        1,
        1,
        "Team P",
        "***",
        0,
        "DP",
        5923819,
    ],
    [
        "CM",
        "Bo",
        "Ung",
        23,
        1,
        14,
        20,
        12,
        19,
        11,
        71,
        5,
        2,
        1,
        "Leader",
        "***",
        0,
        "DP",
        6908755,
    ],
    [
        "ST",
        "Bruno",
        "See",
        36,
        3,
        11,
        20,
        19,
        16,
        13,
        80,
        6,
        2,
        0,
        "Avg",
        "*",
        0,
        "DP",
        7386474,
    ],
    [
        "ST",
        "Banner",
        "Titch",
        24,
        2,
        19,
        14,
        16,
        15,
        18,
        75,
        6,
        3,
        1,
        "Fighter",
        "****",
        0,
        "DP",
        7491627,
    ],
    [
        "ST",
        "Blesing",
        "Tim",
        22,
        3,
        14,
        13,
        17,
        14,
        13,
        70,
        5,
        2,
        0,
        "Laid B",
        "***",
        0,
        "DP",
        5232136,
    ],
    [
        "ST",
        "See",
        "Zak",
        18,
        3,
        18,
        17,
        10,
        14,
        18,
        61,
        5,
        1,
        1,
        "Fighter",
        "***",
        0,
        "DP",
        7838432,
    ],
    [
        "ST",
        "Piero",
        "See",
        37,
        1,
        16,
        19,
        11,
        17,
        12,
        59,
        6,
        4,
        0,
        "Avg",
        "***",
        0,
        "DP",
        772765,
    ],
]

team_chosen = [
    [
        [
            ["GK"],
            "Sean",
            "Robbie",
            24,
            19,
            15,
            12,
            15,
            16,
            18,
            88,
            8,
            4,
            1,
            "Leader",
            "****",
            0,
            "DP",
            1910617,
        ],
        [
            "LB",
            "Josh",
            "Master",
            27,
            3,
            20,
            14,
            15,
            11,
            10,
            71,
            2,
            1,
            0,
            "Avg",
            "*",
            0,
            "DP",
            7226365,
        ],
        [
            "RB",
            "Rambo",
            "Haji",
            30,
            3,
            12,
            20,
            13,
            20,
            13,
            73,
            6,
            2,
            1,
            "Fighter",
            "**",
            0,
            "DP",
            3460661,
        ],
        [
            "CB",
            "Robbie",
            "Sean",
            28,
            2,
            16,
            13,
            14,
            20,
            14,
            73,
            5,
            4,
            0,
            "Avg",
            "**",
            0,
            "DP",
            9144201,
        ],
        [
            "CB",
            "Sero",
            "Titch",
            35,
            1,
            18,
            14,
            20,
            11,
            12,
            68,
            2,
            2,
            0,
            "Avg",
            "*",
            0,
            "DP",
            919944,
        ],
        [
            "CM",
            "Haji",
            "Robert",
            29,
            1,
            19,
            12,
            15,
            18,
            17,
            75,
            2,
            2,
            0,
            "Avg",
            "***",
            0,
            "DP",
            5715328,
        ],
        [
            "CM",
            "David",
            "Robbie",
            20,
            1,
            10,
            16,
            19,
            14,
            16,
            73,
            5,
            1,
            1,
            "Team P",
            "***",
            0,
            "DP",
            5923819,
        ],
        [
            "LM",
            "Kim",
            "Robbie",
            36,
            3,
            14,
            10,
            15,
            11,
            16,
            58,
            5,
            2,
            0,
            "Avg",
            "*",
            0,
            "DP",
            1959844,
        ],
        [
            "RM",
            "Titch",
            "Haji",
            27,
            3,
            10,
            14,
            18,
            16,
            16,
            72,
            6,
            2,
            1,
            "Team P",
            "*",
            0,
            "DP",
            1567118,
        ],
        [
            "ST",
            "Bruno",
            "See",
            36,
            3,
            11,
            20,
            19,
            16,
            13,
            80,
            6,
            2,
            0,
            "Avg",
            "*",
            0,
            "DP",
            7386474,
        ],
        [
            "ST",
            "Banner",
            "Titch",
            24,
            2,
            19,
            14,
            16,
            15,
            18,
            75,
            6,
            3,
            1,
            "Fighter",
            "****",
            0,
            "DP",
            7491627,
        ],
    ]
]


if args.verbose:
    # print("verbosity turned on")
    logging.basicConfig(level=logging.INFO)
    logging.info("Logging turned on")


def to_add():

    """
        temp dumping ground for general notes, will be deleted later on before go live
        input =none
        output print information to screen
    """

    print("I need to add:")
    print("==============")
    print("Edit player Training Skill and remove 5 Star Recruit if over 26")
    print("Sell players")
    print("Expiring contracts")
    input()


def main_run(my_squad, my_firstx1, season_result,season_we_are_in):

    """ This it the bulk of the module contract,age,expirence and training changes are made, 
values for season np=no playoffs dg=divisonal game cg=championship game, w=winners
    input= mysquad,myfirstx1, season result (see above)
    output = change to squad


"""
    # Age +1
    # Contract -1
    # Improve Skills
    # Reduce Skills
    # Change Training Speed
    # Change Charasteics

    Players_improvements = []
    Players_Reductions = []
    player_total_changes=[]

    import player_creation

    #initaiate_player_creation = player_creation.create_player()

    # experience
    np_exp_gained_in_first_11 = 2
    np_exp_gained_in_squad = 1
    dg_exp_gained_in_first_11 = 3
    dg_exp_gained_in_squad = 1
    cg_exp_gained_in_first_11 = 4
    cg_exp_gained_in_squad = 2
    w_exp_gained_in_first_11 = 5
    w_exp_gained_in_squad = 3

    # slightly elobrate loop through squad if player is in first x1 give relevant experience if not give other experience
    for player in my_squad:
        # print(player)
        player_id = player[18]
        player_found = 0
        for player_in_first11 in my_firstx1:
            try:
                if player_id == player_in_first11[18]:
                    # print("Player is in first X1")
                    player_found = 1
            except Exception as e:
                print(e)
                print("Woops")
                breakpoint()
                raise Exception("103 i Errored - player id seems to be missing")
        # squad player
        if player_found == 0:
            if season_result == "np":
                player[16] = np_exp_gained_in_squad
            elif season_result == "dg":
                player[16] = dg_exp_gained_in_squad
            elif season_result == "cg":
                player[16] = cg_exp_gained_in_squad
            elif season_result == "w":
                player[16] = w_exp_gained_in_squad
            else:
                print("not sure what kind of season this was")
        # frrst team player
        else:
            if season_result == "np":
                player[16] = np_exp_gained_in_first_11
            elif season_result == "dg":
                player[16] = dg_exp_gained_in_first_11
            elif season_result == "cg":
                player[16] = cg_exp_gained_in_first_11
            elif season_result == "w":
                player[16] = w_exp_gained_in_first_11
            else:
                print("not sure what kind of season this was")

        # print(player)
    #print ("As the season has drawen to a close, life moves on and these changes have been made:")
    list_of_jobs=["All players have had their experience increase (factors include, play off progresion and if in first X1)","All Players have Aged +1","All Players have had their contract -1","All Players as a result of Age,Luck and personal traits have had change in their skill sets...","Training","Player Retirement","Training Tweaks","expiring contract"]
    done_list=[]
    for i in list_of_jobs:
        #print ("As the season has drawen to a close, life moves on and these changes have been made:")
        done_list.append(i)
        time.sleep(1)
        banner.banner_status(colored_status="cs", season_num=1)
        print ("As the season has drawen to a close, life moves on and these changes have been made:")
        for j in done_list: 
            print(j,u'\u2713')
            #time.sleep(0.5)
            
            if i == "All players have had their experience increase (factors include, play off progresion and if in first X1)": 
    
                # age+1 and contract-1
                for player in my_squad:
                    player_age = player[3]
                    player_age += 1
                    player[3] = player_age

                    player_contract_length = player[12]
                    player_contract_length -= 1
                    player[12] = player_contract_length
                continue
            elif i == "All Players have Aged +1": 
                continue
            
    #player_creation.print_nicer_output_default_squad(my_squad)

            elif i == "All Players have had their contract -1":
                continue
            elif i ==  "All Players as a result of Age,Luck and personal traits have had change in their skill sets...":
                continue
            elif i == "Training":
                print ("=========")

                # training_increase & decrease
                for player_training in my_squad:
                    # create player score based on age,training speed and char
                    player_position=player_training[0]
                    #if type(player_position)==list :
                    #    player_position=player_position[0]
            
                    player_age_i = player_training[3]
                    player_char = player_training[14]
                    player_training_speed = player_training[15]
                    player_current_overall= player_training[10]
                    perfect_age = 25
                    build_player_score = perfect_age - player_age_i
                    if player_char == "Avg":
                        build_player_score += 1
                    elif player_char == "Leader":
                        build_player_score += 3
                    elif player_char == "5-Star":
                        build_player_score += 7
                    elif player_char == "Team P":
                        build_player_score += 2
                    elif player_char == "Fighter":
                        build_player_score += 4
                    elif player_char == "Laid B":
                        build_player_score -= 1
                    else:
                        print("pass not sure what char you are...")
                        raise Exception(
                        "104 i Errored - Unexpected Player Charastric player=", player_training
                    )
                        print()
                    # check length but could of also done if player_training_speed="*":
                    if len(player_training_speed) == 1:
                        build_player_score -= 1
                    elif len(player_training_speed) == 2:
                        build_player_score -= 0
                    elif len(player_training_speed) == 3:
                        build_player_score += 2
                    elif len(player_training_speed) == 4:
                        build_player_score += 4
                    elif len(player_training_speed) == 5:
                        build_player_score += 5
                    else:
                        print("pass not sure what training speed  you are...")

                    # create a random number taking into account build_player_score
                    # positive score
                    if build_player_score > 0:
                        how_lucky_are_we_feeling_skill_change = random.randint(
                            0, build_player_score
                        )
                    # negative score
                    else:
                        how_lucky_are_we_feeling_skill_change = random.randint(
                            build_player_score, 2
                        )
                    #print(player_training[1],player_training[2],"Player build player score = ",how_lucky_are_we_feeling_skill_change)
                    player_gk_skill = player_training[4]
                    player_tackle_skill = player_training[5]
                    player_pass_skill = player_training[6]
                    player_shoot_skill = player_training[7]
                    player_fitness_skill = player_training[8]
                    player_pace_skill = player_training[9]
                    player_special_skill = player_training[13]


                    # determine which skill is highest
                    #print("before skill change...")
                    #print(player_training)
                    if player_gk_skill >= (
                        player_tackle_skill
                        and player_pass_skill
                        and player_shoot_skill
                        and player_fitness_skill
                        and player_pace_skill
                    ):
                        new_skill_level = player_training[4] + how_lucky_are_we_feeling_skill_change
                        if new_skill_level < 0:
                            new_skill_level = 1
                        if new_skill_level > 20:
                            new_skill_level = 20
                        player_training[4] = new_skill_level
                    else:
                        # loop through each 'how luck are we feeling skill change '
                        # abs turns a positive into a negative number
                        #randomly take a skill to reduce

                        #help work our what incrementtor we should use
                        if how_lucky_are_we_feeling_skill_change > 0:
                            incremental_skill_change=1
                        else:
                            incremental_skill_change=-1
                        for _ in range(abs(how_lucky_are_we_feeling_skill_change)):
                            #build list of skills to increase
                            random_list_source=[]
                            if player_training[4] !=20:
                                random_list_source.append(4)
                            if player_training[5] !=20:
                                random_list_source.append(5)
                            if player_training[6] !=20:
                                random_list_source.append(6)
                            if player_training[7] !=20:
                                random_list_source.append(7)
                            if player_training[8] !=20:
                                random_list_source.append(8)
                            if player_training[9] !=20:
                                random_list_source.append(9)
                            if not random_list_source:
                                print("ahhh no skills i can increase, what do to?")
                                breakpoint()
                

        
                            random_number_of_skill_to_change=random.choice(random_list_source)
                            new_skill_level = player_training[random_number_of_skill_to_change] + incremental_skill_change
                            if new_skill_level < 0:
                                new_skill_level = 1
                            if new_skill_level > 20:
                                new_skill_level = 20
                                print ("Er players skill has hit 20",player_training)
                                print ("*** i need some better logic here to try permission change else where",player_training)
                            player_training[random_number_of_skill_to_change] = new_skill_level

                    # get new player rating
    
                    #player_creation.player_rating(self, final_player_position="GK")
                    new_overall_rating=player_creation.create_player_player_rating( 
                    final_player_position_in=player_position,
                    random_skill_gk_in=player_training[4],
                    random_skill_tackle_in=player_training[5],
                    random_skill_passing_in=player_training[6],
                    random_skill_shooting_in=player_training[7],
                    random_skill_fitness_in=player_training[8],
                    random_skill_pace_in=player_training[9],
                    random_skill_special_skill_in=player_training[13])
                    #print("New Overall score...",new_overall_rating)

                    temp_build=[player_training[0],player_training[1], player_training[2], player_training[3], player_training[10],new_overall_rating]
                    player_total_changes.append(temp_build)
                print_nicer_output_players_change_from_training(squad_to_print=player_total_changes)
                input("Press enter to continue")
                #breakpoint()
                break
            #break

            elif i == "Player Retirement":
                
                my_squad_after_retirment=time_to_retire(my_squad)
                input("Press enter to continue")
                break
    
            elif i == "Training Tweaks":
    
                my_squad_after_training_tweaks=tweak_training_and_personality(my_squad_after_retirment)
                input("Press enter to continue")
                break

            elif i == "expiring contract":
                #input("press enter to continue")
                expiring_contract(squad_in=my_squad_after_training_tweaks)
                input("Press enter to continue")
                break

            else:
                input("press enter to continue")
    

def tweak_training_and_personality(squad_in_ttandp):

    """ function to tweak play training speed and character based on age
        input = squad
        output = squad (With some changes)
    """
    changes_made=0
    for player in squad_in_ttandp:
        player_age=player[3]
        player_char=player[14]
        player_training_speed=player[15]
        #age 27 
        #reduce training speed by 1
        #change from 5 star recurit to something else
        if int(player_age) ==27:
            if changes_made==0:
                print("==================================================")
                print("Players with tweaks to training speed and Character")
                print("==================================================")
            print("Before change..",player)
            if len(player_training_speed) > 1:
                new_training_speed= len(player_training_speed)-1
                new_training_speed_as_stars="*" *  new_training_speed
                player[15]=new_training_speed_as_stars
                changes_made+=1
                print("After change..",player)
            if player_char == "5-Star":
                special_traits_random_number = random.randint(1, 4)
                if special_traits_random_number == 1:
                    # Leader
                    player_special_trait = "Leader"
                elif special_traits_random_number == 2:
                    # Team Player
                    player_special_trait = "Team P"
                elif special_traits_random_number == 3:
                    player_special_trait = "Fighter"
                else:
                    player_special_trait = "Avg"
                changes_made+=1
                player[14]=player_special_trait
                print("After change..",player)
    if changes_made!=0:
        pass
        #print ("players char or training speed changed")
    else:
        print ("No players char or training speed changed")
        
    return(squad_in_ttandp)
        
        
                

def time_to_retire(squad_in):
    """ a function to decide if players want to retire
        logic- if player is older than 'old age' as per game_settings file,player has a 50:50 chance of retiring and been replaced by a random 
        input -squad_in  (squad after age,contract and training have taken effect)
        output- squad_out (squad + any retirements)
    """
    old_age=game_settings.start_thinking_about_retirement_age
    players_retired=0
    print ("===========")
    print ("Retirement")
    print ("===========")
    for player in squad_in:
        players_age=player[3]
        players_position=player[0]
        player_id=player[18]
        #if type(players_position) == list:
        #    players_position=players_position[0]
        if players_age > old_age:
            shall_i_retire = random.randint (0,1)
            if shall_i_retire==1:
                print("Player has decided to retire...",player[0],player[1],player[2],player[3],player[10])
                new_random_player_returned=new_player_needed(position_in_need=players_position)
                updated_squad=replace_player(squad_in=squad_in,player_to_replace_uniqee_id=player_id,new_player=new_random_player_returned)
                players_retired+=1
            else:
                pass
                #print("Player has decided not to retire...",player)

    if  players_retired == 0:
        print("No players wanted to Retire :) ")
        return squad_in
        #player_creation.print_nicer_output_default_squad(updated_squad)

    return updated_squad
        


def new_player_needed(position_in_need):
    """a function to help create a new player, typically used when a player leaves through retirement/selling or out of contract
    input - position in need i.e GK as we will be swapping like for like to keep the squad in good shape
    output -new random player
    """

    new_random_player=[]
    new_random_player=player_creation.create_player_player_creation(play_position=position_in_need, type_of_player="Random Poor",return_player=1)
    try:
        print("here is the replacement...",new_random_player[0][0],new_random_player[0][1],new_random_player[0][2],new_random_player[0][3],new_random_player[0][10])
    except:
        breakpoint()
    return (new_random_player)


def replace_player(squad_in,player_to_replace_uniqee_id,new_player):
    """a function to remove 1 player and insert a new one
    input = squad, player to replace unique id , new player (output of new_player_needed function call)
    output = new squad
    """
    index_of_player=0
    player_to_replace_index_number=0
    for player in squad_in:
        if player[18] == player_to_replace_uniqee_id:
            player_to_replace_index_number=index_of_player
        else:
            index_of_player+=1

    #player_creation.print_nicer_output_default_squad(squad_in[0])
    del squad_in[player_to_replace_index_number]
    squad_in.insert(player_to_replace_index_number,new_player[0])
    #player_creation.print_nicer_output_default_squad(squad_in[0])
    return (squad_in)
    
def expiring_contract(squad_in):

    """function to deal with out of contract players
    input = squad
    output =squad (with ammeneded contracts or replacement players)

    """

    print("======================================")
    print("Lets check out of contract players...")
    print("======================================")
    #out_of_contract_players_offers=[]
    number_or_runs=0
    while True:
        out_of_contract_players=[]
        for ex_player in squad_in:
            player_contract_length=ex_player[12]
            if  player_contract_length ==0:
                out_of_contract_players.append(ex_player)
                #player_name=ex_player[1] + " " + ex_player[2]
                #player_overall=ex_player[10]
                #player_current_wage=ex_player[11]
                #player_id=ex_player[18]
                #player_1_year_contract=4
                #player_2_year_contract=5
                #player_3_year_contract=6
                #player_4_year_contract=7
                #temp_dict_player_offer={"Name":player_name,"player_overall":player_overall,"player_wage": player_current_wage,"player_id": player_id,"1 year contract": player_1_year_contract,"2 year contract": player_2_year_contract,"3 year contract": player_3_year_contract,"4 Year contact":player_4_year_contract}
                #breakpoint()
                
        if len(out_of_contract_players) == 0 and number_or_runs==0:
            print("No out of contract players")
        if len(out_of_contract_players) == 0:
            return(squad_in)
        player_creation.print_nicer_output_default_squad(out_of_contract_players,print_index="y")
        try:
            number_or_runs+=1
            user_input_ex=input("press an (index) number to interact with the player or press (r) to release all players ")
            if user_input_ex=="r":
                print("Release them all")
                for each_player in out_of_contract_players:
                    npn=new_player_needed(each_player[0])
                    replace_player(squad_in,each_player[18],npn)
                input("All outstanding players released, press enter to continue")
                continue
            min_range=1
            max_range=len(out_of_contract_players)
            if max_range >= int(user_input_ex)  >= min_range:
                pass
            else:
                print("You did not select a valid number")
                breakpoint()
                input("Press enter to continue")
                continue
        except:
            print ("Invalid input , please try again")
            input("Press enter to continue")
            continue
        players_choice=input ("Do you want to (offer a new contract(n)  or release the player(r)")
        #maybe include some kind of squad overview so we can inderstand how import the player is
        if players_choice != "n" and  players_choice != "r":
            print ("Invalid input , please try again")
            input("Press enter to continue")
        if players_choice == "r":
            input_release=input("are you sure you want to relase this player?(y/n)")
            if input_release =="y":
                player_index_to_delete=int(user_input_ex)-1
                player_to_release_id=out_of_contract_players[player_index_to_delete][18]
                player_position_to_replace=out_of_contract_players[player_index_to_delete][0]

                new_random_player_returned=new_player_needed(position_in_need= player_position_to_replace)
                updated_squad=replace_player(squad_in=squad_in,player_to_replace_uniqee_id= player_to_release_id,new_player=new_random_player_returned)
                input("The player has been replaced, please press enter to continue") 
                
            else:
                print("Release not confirmed")
                breakpoint()
                continue
        if players_choice == "n":

            #get the players variables
            player_index_to_renew=int(user_input_ex)-1
            player_id_to_renew=out_of_contract_players[player_index_to_renew][18]
            player_overall_to_renew=out_of_contract_players[player_index_to_renew][10]
            player_current_wage_to_renew=out_of_contract_players[player_index_to_renew][11]
        
            #build contract offer
            one_year_offer=int(player_current_wage_to_renew)
            two_year_offer=int(player_current_wage_to_renew)+2
            three_year_offer=int(player_current_wage_to_renew)+3
            four_year_offer=int(player_current_wage_to_renew)+4
            
            #offer contract
            print ("1) -one year contract wage=",one_year_offer)
            print ("2) -two year contract wage=",two_year_offer)
            print ("3) -three year contract wage=",three_year_offer)
            print ("4) -four year contract wage=",four_year_offer)
        
            user_contract_input=input("please enter a choice of 1-4 ")
            #sanity check user input
            try:
                user_contract_input_int=int(user_contract_input)
                if user_contract_input_int not in (1,2,3,4):
                    print("bad input lets try again")
                    input ("press enter to continue")
                    continue
            except:
                print ("bad input lets try again")
                input ("press enter to continue")
                continue

            #check index of player 
            index_of_player=0
            player_to_replace_index_number=0
            for player in squad_in:
                if player[18] == player_id_to_renew:
                    player_to_replace_index_number=index_of_player
                else:
                    index_of_player+=1

            #set new wage and length of contract
            if user_contract_input=="1":
                new_wage=one_year_offer
            elif user_contract_input=="2":
                new_wage=two_year_offer
            elif user_contract_input=="3":
                new_wage=three_year_offer
            elif user_contract_input=="4":
                new_wage=four_year_offer
            else:
                print ("something odd happened")
                breakpoint()
            
            squad_in[player_to_replace_index_number][11]=new_wage
            squad_in[player_to_replace_index_number][12]=user_contract_input
            print("Changes made")
            input ("press enter to continue")
            player_creation.print_nicer_output_default_squad(squad_in)
            input ("press enter to continue")

            

            
            #update players contract and length

            
    
    breakpoint()

 


def print_nicer_output_players_change_from_training(squad_to_print):
        """a function to print the players changes into a nice format
           input = List of players to print
           output =  print to screen
        """
        print(
            "PST    Name                  AGE |Old_Overall   New_Overall Change "
        )
        print(
            "================================================================================================================"
        )
        for k in squad_to_print:
            # for k in squad_of_players_list:
            try:
                fullname=str(k[1])+" "+str(k[2])
                position_to_print=k[0]
                if type(position_to_print) == list:
                    position_to_print=position_to_print[0]
                change_in_skill=int(k[5])-int(k[4])

                # print('{:<12s}{:<15s}{:>10s}{:>5s}{:>5s}{:>15s}{:>12s}{:>5s}{:>5s}'.format(temp_position,player_name,str(k[3]),str(k[4]),str(k[5]),str(k[6]),str(k[7]),str(k[8]),str(k[9]),str(k[10])))
                #print('{:<6s}{:<18s}{:>7s}  |{:>2s}{:>5s}'.format(str(k[0]), str(k[1]), str(k[2]), str(k[3]), str(k[4])))
                print('{:<6s}{:<18s}{:>7s}  | {:>2s}{:>12s}{:>13s}'.format(str(position_to_print), fullname, str(k[3]), str(k[4]),str(k[5]),str(change_in_skill)),end =" ")
                if change_in_skill > 2:
                    print(colored("Big training boost ", "green"))
                elif change_in_skill < -2:
                    print(colored("Large training loss ", "red"))
                else:
                    print(colored("Average ", "yellow"))

                #        str(k[1]),
                #        str(k[2]),
                #        str(k[3]),
                #        str(k[4]))
            except Exception as e:
                breakpoint
                print("Error=",e)
                raise Exception("207  i errored - printing squad output player=", k)



if __name__ == "__main__":

    # purporse:
    # in:
    # return:
    import banner

    banner.banner_status(colored_status="cs", season_num=1)
    #to_add()
    #player_creation.print_nicer_output_default_squad(player_squad)
    main_run(player_squad, team_chosen[0], "np",2)
