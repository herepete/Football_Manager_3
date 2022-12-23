#!/usr/bin/python3
# print("...end of season free agency...")
# input("Press enter to continue")

import game_settings
import os
import sys
import argparse
import logging
import player_creation

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="Verbose information", action="store_true")
args = parser.parse_args()

# hacky effort to stop arge parse being imported from player_creation module
sys.argv = [sys.argv[0]]
import player_creation


if args.verbose:
    # print("verbosity turned on")
    logging.basicConfig(level=logging.INFO)
    logging.info("Logging turned on")

free_agency_list = []
current_squad_cost = 0
allowed_squad_cost = game_settings.Total_Wage_Limit

test_incoming_squad = [
    [
        ["GK"],
        "Symon",
        "Bob",
        32,
        17,
        12,
        17,
        19,
        20,
        15,
        81,
        6,
        3,
        0,
        "Avg",
        "**",
        0,
        "DP",
        5739883,
    ],
    [
        ["GK"],
        "Ben",
        "Sero",
        19,
        16,
        20,
        14,
        10,
        12,
        14,
        74,
        2,
        4,
        0,
        "Avg",
        "**",
        0,
        "DP",
        3517670,
    ],
    [
        ["GK"],
        "Tommie",
        "Me",
        30,
        10,
        15,
        13,
        11,
        20,
        20,
        50,
        6,
        1,
        0,
        "Avg",
        "***",
        0,
        "DP",
        4762932,
    ],
    [
        "LB",
        "Banele",
        "Robbie",
        35,
        3,
        20,
        11,
        13,
        20,
        10,
        74,
        2,
        3,
        0,
        "Avg",
        "***",
        0,
        "DP",
        9776619,
    ],
    [
        "LB",
        "Tommie",
        "Kim",
        17,
        1,
        17,
        11,
        17,
        10,
        11,
        62,
        5,
        3,
        0,
        "Avg",
        "***",
        0,
        "DP",
        7615501,
    ],
    [
        "RB",
        "Banele",
        "James",
        21,
        3,
        10,
        19,
        13,
        17,
        13,
        61,
        1,
        4,
        0,
        "Avg",
        "*****",
        0,
        "DP",
        767077,
    ],
    [
        "RB",
        "Aaron",
        "Barry",
        33,
        1,
        12,
        12,
        11,
        17,
        10,
        58,
        6,
        4,
        0,
        "Avg",
        "**",
        0,
        "DP",
        4408966,
    ],
    [
        "CB",
        "Piero",
        "See",
        36,
        2,
        19,
        15,
        10,
        17,
        19,
        81,
        6,
        4,
        0,
        "Avg",
        "**",
        0,
        "DP",
        7910147,
    ],
    [
        "CB",
        "Robert",
        "Hwang",
        36,
        3,
        19,
        19,
        18,
        15,
        10,
        75,
        5,
        2,
        0,
        "Avg",
        "**",
        0,
        "DP",
        1037566,
    ],
    [
        "CB",
        "Feix",
        "Tony",
        24,
        3,
        12,
        15,
        14,
        20,
        20,
        74,
        2,
        4,
        0,
        "Avg",
        "**",
        0,
        "DP",
        6338641,
    ],
    [
        "CB",
        "Haji",
        "Banele",
        32,
        1,
        13,
        12,
        15,
        13,
        17,
        64,
        1,
        4,
        1,
        "Leader",
        "**",
        0,
        "DP",
        9949750,
    ],
    [
        "LM",
        "Titch",
        "Haji",
        33,
        3,
        13,
        20,
        15,
        18,
        16,
        81,
        6,
        2,
        0,
        "Avg",
        "**",
        0,
        "DP",
        1204394,
    ],
    [
        "LM",
        "Sorba",
        "TJ",
        17,
        1,
        18,
        19,
        20,
        20,
        10,
        80,
        5,
        2,
        0,
        "Avg",
        "**",
        0,
        "DP",
        8741280,
    ],
    [
        "RM",
        "Samkelo",
        "Haji",
        36,
        3,
        13,
        19,
        14,
        16,
        15,
        77,
        4,
        4,
        1,
        "Team P",
        "***",
        0,
        "DP",
        5444686,
    ],
    [
        "RM",
        "Feix",
        "Peter",
        28,
        2,
        17,
        17,
        11,
        11,
        19,
        72,
        3,
        3,
        0,
        "Avg",
        "*",
        0,
        "DP",
        7192361,
    ],
    [
        "CM",
        "Piero",
        "Omar",
        29,
        3,
        16,
        13,
        11,
        16,
        19,
        69,
        4,
        4,
        1,
        "Leader",
        "*",
        0,
        "DP",
        8387134,
    ],
    [
        "CM",
        "Feix",
        "Dylon",
        26,
        1,
        16,
        10,
        18,
        15,
        12,
        63,
        1,
        1,
        0,
        "Avg",
        "***",
        0,
        "DP",
        9392780,
    ],
    [
        "CM",
        "Nathan",
        "Jimbo",
        27,
        1,
        20,
        12,
        12,
        14,
        13,
        63,
        4,
        3,
        0,
        "Laid B",
        "*",
        0,
        "DP",
        5463288,
    ],
    [
        "CM",
        "Jimbo",
        "Peter",
        22,
        3,
        15,
        15,
        11,
        14,
        13,
        61,
        5,
        1,
        0,
        "Laid B",
        "*****",
        0,
        "DP",
        4067236,
    ],
    [
        "ST",
        "Sean",
        "Jimbo",
        22,
        3,
        10,
        11,
        19,
        12,
        18,
        77,
        5,
        1,
        0,
        "Avg",
        "*****",
        0,
        "DP",
        1775529,
    ],
    [
        "ST",
        "See",
        "Master",
        32,
        3,
        11,
        16,
        17,
        17,
        16,
        76,
        5,
        4,
        0,
        "Avg",
        "**",
        0,
        "DP",
        1064737,
    ],
    [
        "ST",
        "Gibby",
        "Ung",
        18,
        2,
        18,
        15,
        20,
        15,
        10,
        76,
        5,
        1,
        0,
        "5-Star",
        "***",
        0,
        "DP",
        8473980,
    ],
    [
        "ST",
        "Aj",
        "Tommie",
        24,
        1,
        17,
        12,
        17,
        18,
        13,
        72,
        2,
        4,
        0,
        "Laid B",
        "*****",
        0,
        "DP",
        9622084,
    ],
    [
        "ST",
        "See",
        "Josh",
        32,
        2,
        20,
        11,
        10,
        20,
        10,
        55,
        2,
        1,
        1,
        "Leader",
        "*",
        0,
        "DP",
        5076380,
    ],
]


def print_our_squad(our_squad):
    """ Print our Squad
        Input =Our Squad
        Output= Print squad,print key
    """
    player_creation.print_nicer_output_default_squad(our_squad)
    player_creation.print_nicer_output_print_key()


def squad_feedback(our_squad):
    
    """
    get squad feedback
    input=our_squad
    output=print to screen cost of squad,feedback,character,players,per_position,rating per position
    """
    player_creation.Squad_stats_and_feedback_cost_of_squad(squad_to_check=our_squad)
    player_creation.Squad_stats_and_feedback_squad_feedback(squad_to_check=our_squad)
    player_creation.Squad_stats_and_feedback_char_of_team(squad_to_check=our_squad)
    player_creation.Squad_stats_and_feedback_players_per_position(squad_to_check=our_squad)
    player_creation.Squad_stats_and_feedback_rating_per_position(squad_to_check=our_squad)


def safety_check_squad_size(our_squad):

    """
    safety check on squad
    input =our_squad
    return= 0 everything is good, 1 there is a problem
    """
    # check squad size is correct
    # check we have enough players at each position:
    # min 3 GK
    # min 1 LB
    # min 1 RB
    # min 2 CB
    # min 1 LM
    # min 1 RM
    # min 2 CM
    # min 5 ST
    # return 0 for success + reason
    # return 1 for failure + reason

    # check length
    players_in_squad = len(our_squad)
    if players_in_squad != 24:
        return (1, "Squad number not correct it should be 24")

    GK_found = 0
    LB_found = 0
    RB_found = 0
    CB_found = 0
    LM_found = 0
    RM_found = 0
    CM_found = 0
    ST_found = 0
    odd_player_found = 0

    for i in our_squad:
        if "GK" in i[0]:
            GK_found += 1
        elif "LB" in i[0]:
            LB_found += 1
        elif "RB" in i[0]:
            RB_found += 1
        elif "CB" in i[0]:
            CB_found += 1
        elif "LM" in i[0]:
            LM_found += 1
        elif "RM" in i[0]:
            RM_found += 1
        elif "CM" in i[0]:
            CM_found += 1
        elif "ST" in i[0]:
            ST_found += 1
        else:
            odd_player_found += 1

    if odd_player_found != 0:
        return (1, "Odd player found")
    elif GK_found < 3:
        return (1, "Not Enough GK found")
    elif LB_found < 1:
        return (1, "Not Enough LB found")
    elif RB_found < 1:
        return (1, "Not Enough RB found")
    elif CB_found < 2:
        return (1, "Not Enough CB found")
    elif LM_found < 1:
        return (1, "Not Enough LM found")
    elif RM_found < 1:
        return (1, "Not Enough RM found")
    elif CM_found < 2:
        return (1, "Not Enough CM found")
    elif ST_found < 5:
        return (1, "Not Enough ST found")
    else:
        return (0, "Everything looks good")

    breakpoint()


def check_current_squad_cost(incoming_squad, return_or_print):
    
    """
    check current squad cost
    input =squad, return or print variable
    output= print Squad cost
    """
    global current_squad_cost
    for player_cost in incoming_squad:
        current_squad_cost += int(player_cost[11])
    if return_or_print == "p":
        print("squad_cost=", current_squad_cost)
    else:
        return current_squad_cost


def add_free_agency(fa_incoming_squad,our_squad_in):

    """menu for free agencey
    input = free agents
    output =a lot """

    while True:
        #print("To find...")
        #print("G for GK",end=" ")
        # print ("LB for LB , RB for RB , CB for CB")
        #print("D for Defender",end=" ")
        #print("M for Midfielers",end=" ")
        #print("S for Stickers",end=" ")
        #print("B for Best players avaliable",end=" ")
        #print("Y for Good Youth prospects",end=" ")
        #print("P for Special Skills")

        user_input = input("Do you wish to sign a free agent?(y) or continue to the next step of the game (c) or (t) to view current squad ")
        if user_input =="c":
            return our_squad_in
        
        Current_Squad_cost = check_current_squad_cost(
            fa_incoming_squad, return_or_print="r"
        )
        if user_input == "t":
                os.system('clear')
                player_creation.print_nicer_output_default_squad(our_squad_in)
                squad_feedback(our_squad_in)
                input("press a button to continue")
                continue
            
        if Current_Squad_cost < 0:
            input(
                "you don't have enough Cash to sign any new players,press a button to continue "
            )
            break
        elif user_input == "y":
            user_input2=input("press (a) all, (t) top 10, (tt) top 50, (f)top trainers,(s) top 20 strickers ")
            if  user_input2=="s":
                top_s = sorted(fa_incoming_squad, key=lambda x: x[10], reverse=True)
                top_s_rebuild=[]
                for si in top_s:
                    if si[0] =="ST":
                        top_s_rebuild.append(si)
                top_st_top_20=top_s_rebuild[:20]
                player_creation.print_nicer_output_default_squad(top_st_top_20,print_index="y")
                player_list=top_st_top_20

            elif  user_input2=="a":
                player_creation.print_nicer_output_default_squad(fa_incoming_squad,print_index="y")
                #player list is set accordingley so later in the script i can easier get the player id
                player_list=fa_incoming_squad
            elif  user_input2=="t":
                top_10 = sorted(fa_incoming_squad, key=lambda x: x[10], reverse=True)
                top_10 = top_10[:10]
                player_creation.print_nicer_output_default_squad(top_10,print_index="y")
                player_list=top_10
            elif  user_input2=="tt":
                top_50 = sorted(fa_incoming_squad, key=lambda x: x[10], reverse=True)
                top_50 = top_50[:50]
                player_creation.print_nicer_output_default_squad(top_50,print_index="y")
                player_list=top_50
            
            elif  user_input2=="f":
                top_trainers=sorted(fa_incoming_squad, key=lambda x: x[15], reverse=True)
                top_trainers = top_trainers[:10]
                player_creation.print_nicer_output_default_squad(top_trainers,print_index="y")
                player_list=top_trainers
            else:
                input("Invalid input detected,please press enter to continue")
            #options_avaliable_fa = []
            #for index, item in enumerate(fa_incoming_squad, start=0):
            #    print(index, item)
            #    options_avaliable_fa.append(index)
            # get and check the input
            try:

                get_player = input("which player do you want to sign? ")   
                 
                if len(player_list)>= int(get_player) >>0:
                    pass
                else:
                    input("Incorrect Value, please try again")
                    continue
            except:
                input("Invalid input detected,please press a button to continue")
                break

            #get player
            player_id=player_list[int(get_player)-1][18]
            player_index_poistion_in_complete_list=0
            for player_check in fa_incoming_squad :
                if  player_check[18] == player_id:
                    break
                else:
                    player_index_poistion_in_complete_list+=1
            get_player_position = player_list[int(get_player)-1][0]
            # GK are in a list so convert for ease of use later
            if type(get_player_position) is list:
                get_player_position = get_player_position[0]
            options_avaliable = []
            for index, item in enumerate(our_squad_in, start=0):
                # if an exact match print
                if get_player_position in (item[0]):
                    print(index, item)
                    options_avaliable.append(index)
                    continue
                # if you are a defender of some sort print the other defenders
                if (
                    get_player_position == "LB"
                    or get_player_position == "RB"
                    or get_player_position == "CB"
                ) and (item[0] == "LB" or item[0] == "RB" or item[0] == "CB"):
                    print(index, item)
                    options_avaliable.append(index)
                    continue
                # if you are a midfielder of some sort print the other miedfielder
                if (
                    get_player_position == "LM"
                    or get_player_position == "RM"
                    or get_player_position == "CM"
                ) and (item[0] == "LM" or item[0] == "RM" or item[0] == "CM"):
                    print(index, item)
                    options_avaliable.append(index)
                    continue
            # get and check the input
            try:
                get_player1 = int(
                    input(
                        "which player do you want to replace in your squad? (or press e to exit) "
                    )
                )
                if int(get_player1) not in options_avaliable:
                    input("Incorrect Value, please try again")
                    continue
                else:
                    # NEED check for minimum squad postions
                    print("Are you you want to sign...(y/n)")
                    print( player_list[int(get_player)-1])
                    print("and Release...")
                    print(our_squad_in[int(get_player1)])
                    are_you_sure = input("")
                    if are_you_sure is "x":
                        breakpoint()

                    if are_you_sure is not "y":
                        input(
                            "Valid input not found i need a 'y' press a button to continue"
                        )
                        continue

                    # delete player from our squad
                    del our_squad_in[int(get_player1)]
                    # insert Free Agent into Squad
                    our_squad_in.insert(
                        int(get_player1), fa_incoming_squad[player_index_poistion_in_complete_list]
                    )
                    # delete player from free agency so we cannot resign them
                    del fa_incoming_squad[player_index_poistion_in_complete_list]
                    print("player switched")
                    continue

            except Exception as e:
                input("Bad input please try again")
                print(e)
                breakpoint()
                raise Exception("101 i Errored - i expected a different input")

                continue

            if get_player == "e":
                break
            else:
                pass

        else:
            input("Bad Input please try again ")


def create_free_agency():

    """create the Free agencey players
    input =none 
    output = free agencey players """

    #global free_agency_list
    
    default_squad_GK = game_settings.free_agency_gk_min
    default_squad_DEF = game_settings.free_agency_d_min
    default_squad_MID = game_settings.free_agency_m_min
    default_squad_ATA = game_settings.free_agency_a_min

    for j in range(1, default_squad_GK):
        rv1 = player_creation.create_player_player_creation(
            play_position="GK", type_of_player="Free Agency"
        )
    for k in range(1, default_squad_DEF):
        rv2 =  player_creation.create_player_player_creation(
            play_position="DEF", type_of_player="Free Agency"
        )
    for k in range(1, default_squad_MID):
        rv3 =  player_creation.create_player_player_creation(
            play_position="MID", type_of_player="Free Agency"
        )
    for k in range(1, default_squad_ATA):
        free_agency_list =  player_creation.create_player_player_creation(
            play_position="ATA", type_of_player="Free Agency"
        )
    return free_agency_list


# create_free_agency()
# i need to create a way to call create player and have 3 variables
# random (for new team)
# draft (age 17-24) skill 60-96
# Free Agency (age 24-36) skill 70-100


def main_run(our_squad):
    
    """core run
    input= our squad
    output=  a lot 
    """

    print("Here is our squad, lets look at free agencey for some replacements...")
    print_our_squad(our_squad)
    squad_feedback(our_squad)
    rv1, rv2 = safety_check_squad_size(our_squad)
    # print(f"***Squad check is {rv1} and feedback is {rv2}****")
    fa_list=create_free_agency()
    check_current_squad_cost(our_squad, return_or_print="r")
    returned_squad=add_free_agency(fa_list,our_squad)
    print("Allowed Squad Cost=", allowed_squad_cost)
    print("Wage Left=", allowed_squad_cost - current_squad_cost)
    return(returned_squad)


if __name__ == "__main__":
    our_squad = test_incoming_squad
    os.system("clear")
    import banner

    banner.banner_status(colored_status="fa", season_num=1)
    main_run(our_squad)
