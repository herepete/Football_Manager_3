#!/usr/bin/python3

from operator import itemgetter
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="Verbose information", action="store_true")
args = parser.parse_args()

import logging
import random

# https://blog.finxter.com/copy-list-of-lists-in-python-shallow-vs-deep/#:~:text=To%20create%20a%20shallow%20copy,the%20inner%20and%20outer%20lists.
import copy

"""
Trying to detail how the program flows

    if __name__=="__main__"
              |
    starting_preseason(squad)
              |
            formation_choice()              
--------------------------------------------------------------------------------------------
              |                 |                       |                       |
-best_avliable_team(squad)   -best_young_team() -best_blended_team()   -offer_choice_to_user()
              |
    create_team_score


def best_avliable_team(localsquad):
    purporse: get best team
    in: (squad)
    return: (team ratings)
def best_young_team():
def best_blended_team():
def create_team_score(first_11,type_of_team):
def formation_choice():
def offer_choice_to_user():
def starting_preseason(squad):
    this is what is called and where the grunge work happens
"""


if args.verbose:
    # print("verbosity turned on")
    logging.basicConfig(level=logging.INFO)
    logging.info("Logging turned on")
else:
    # print("verbosity not turned on")
    pass


# when i was thinking about adding multiple formations i had a more complex structure which i have carried on with the below 3 variables
formation_4_4_2 = {
    "GK": 1,
    "LB": 1,
    "RB": 1,
    "CB": 2,
    "DM": 0,
    "CM": 2,
    "LM": 1,
    "RM": 1,
    "AM": 0,
    "LW": 0,
    "ST": 2,
    "RW": 0,
}
formation_4_4_2_just_needed = {k: v for (k, v) in formation_4_4_2.items() if v > 0}
formation_4_4_2_list_keys = list(formation_4_4_2_just_needed.keys())

# give me something to test locally
test_squad = [
    [
        ["GK"],
        "Rambo",
        "Kane",
        20,
        16,
        9,
        14,
        20,
        14,
        14,
        75,
        2,
        1,
        0,
        "Avg",
        "****",
        0,
        "DP",
        821920,
    ],
    [
        ["GK"],
        "Li",
        "Mayfield",
        19,
        12,
        5,
        19,
        12,
        18,
        17,
        61,
        5,
        4,
        1,
        "Leader",
        "*****",
        0,
        "DP",
        607207,
    ],
    [
        ["GK"],
        "Paul",
        "Roberts",
        27,
        13,
        13,
        7,
        18,
        19,
        13,
        61,
        2,
        4,
        0,
        "Avg",
        "*",
        0,
        "DP",
        2791431,
    ],
    [
        "LB",
        "Ross",
        "Kane",
        25,
        3,
        19,
        19,
        9,
        19,
        8,
        78,
        4,
        2,
        1,
        "Fighter",
        "**",
        0,
        "DP",
        5449644,
    ],
    [
        "LB",
        "Gibby",
        "Barrett",
        29,
        1,
        15,
        13,
        6,
        16,
        20,
        73,
        4,
        4,
        0,
        "Laid B",
        "**",
        0,
        "DP",
        2472907,
    ],
    [
        "RB",
        "Peter",
        "Del-Piero",
        32,
        3,
        13,
        17,
        14,
        10,
        9,
        60,
        6,
        4,
        1,
        "Team P",
        "**",
        0,
        "DP",
        7409013,
    ],
    [
        "RB",
        "TJ",
        "Mohammed",
        19,
        1,
        9,
        16,
        12,
        10,
        6,
        48,
        1,
        4,
        1,
        "Team P",
        "*****",
        0,
        "DP",
        5781168,
    ],
    [
        "RB",
        "See",
        "Mander",
        35,
        1,
        10,
        7,
        17,
        15,
        8,
        47,
        6,
        1,
        0,
        "Avg",
        "***",
        0,
        "DP",
        3548257,
    ],
    [
        "RB",
        "Jimbo",
        "Bishop",
        31,
        2,
        10,
        5,
        8,
        10,
        12,
        44,
        3,
        1,
        0,
        "Avg",
        "**",
        0,
        "DP",
        8562484,
    ],
    [
        "CB",
        "Samkelo",
        "Bishop",
        33,
        3,
        17,
        16,
        16,
        7,
        17,
        68,
        2,
        3,
        0,
        "Avg",
        "***",
        0,
        "DP",
        4235611,
    ],
    [
        "CB",
        "Bo",
        "Stimer",
        24,
        1,
        14,
        16,
        5,
        5,
        17,
        58,
        3,
        4,
        0,
        "Laid B",
        "*****",
        0,
        "DP",
        3200970,
    ],
    [
        "LM",
        "Simon",
        "Ticker",
        35,
        1,
        5,
        5,
        13,
        16,
        18,
        57,
        3,
        1,
        0,
        "Avg",
        "*",
        0,
        "DP",
        8290256,
    ],
    [
        "RM",
        "Aj",
        "Jean",
        23,
        3,
        18,
        16,
        8,
        6,
        16,
        60,
        2,
        4,
        0,
        "Avg",
        "*****",
        0,
        "DP",
        2555510,
    ],
    [
        "RM",
        "Bo",
        "Hassan",
        21,
        1,
        16,
        12,
        20,
        7,
        13,
        59,
        5,
        4,
        1,
        "Leader",
        "***",
        0,
        "DP",
        2835505,
    ],
    [
        "RM",
        "Silver",
        "Tubert",
        25,
        2,
        17,
        8,
        10,
        10,
        13,
        52,
        1,
        1,
        0,
        "Avg",
        "***",
        0,
        "DP",
        2012292,
    ],
    [
        "RM",
        "Ross",
        "Stansfield",
        31,
        3,
        14,
        12,
        9,
        10,
        7,
        48,
        1,
        1,
        1,
        "Fighter",
        "***",
        0,
        "DP",
        4849940,
    ],
    [
        "CM",
        "Tommie",
        "Reize",
        19,
        1,
        16,
        12,
        18,
        10,
        12,
        62,
        3,
        4,
        1,
        "Team P",
        "**",
        0,
        "DP",
        8865693,
    ],
    [
        "CM",
        "Banele",
        "Bishop",
        28,
        3,
        6,
        12,
        7,
        11,
        17,
        48,
        1,
        1,
        0,
        "Avg",
        "***",
        0,
        "DP",
        622877,
    ],
    [
        "CM",
        "Banele",
        "Tubert",
        34,
        3,
        9,
        8,
        5,
        5,
        8,
        30,
        5,
        2,
        0,
        "Avg",
        "*",
        0,
        "DP",
        7566234,
    ],
    [
        "ST",
        "Omar",
        "Ribbenov",
        19,
        3,
        17,
        14,
        16,
        18,
        7,
        65,
        5,
        2,
        0,
        "Avg",
        "*****",
        0,
        "DP",
        836487,
    ],
    [
        "ST",
        "Banele",
        "Del-Piero",
        35,
        1,
        8,
        20,
        10,
        20,
        14,
        61,
        2,
        2,
        0,
        "Avg",
        "*",
        0,
        "DP",
        4112503,
    ],
    [
        "ST",
        "Aj",
        "Del-Piero",
        27,
        3,
        17,
        6,
        17,
        12,
        5,
        58,
        4,
        3,
        0,
        "Avg",
        "**",
        0,
        "DP",
        3731537,
    ],
    [
        "ST",
        "Barry",
        "Smith",
        35,
        1,
        18,
        20,
        8,
        14,
        16,
        54,
        2,
        4,
        0,
        "Avg",
        "*",
        0,
        "DP",
        5266273,
    ],
    [
        "ST",
        "TJ",
        "Smith",
        20,
        2,
        20,
        20,
        11,
        11,
        6,
        49,
        5,
        1,
        0,
        "Avg",
        "***",
        0,
        "DP",
        7415303,
    ],
]

first_11_best_team_chosen = []
first_11_best_team_chosen_team_rating = []
first_11_best_young_team_chosen = []
first_11_best_young_team_chosen_team_rating = []
first_11_best_blended_team_chosen = []
first_11_best_blended_team_chosen_team_rating = []


def sort_team(incoming_squad):
    global squad_of_players_list
    # group players by position (first into indvidual list and then combine them later on)
    incoming_squad_in = incoming_squad
    gk_list = []
    dl_list = []
    dr_list = []
    cb_list = []
    lm_list = []
    rm_list = []
    cm_list = []
    st_list = []
    rebuilt_team = []
    for player in incoming_squad_in:
        if player[0][0] == "GK":
            gk_list.append(player)
        elif player[0] == "LB":
            dl_list.append(player)
        elif player[0] == "RB":
            dr_list.append(player)
        elif player[0] == "CB":
            cb_list.append(player)
        elif player[0] == "LM":
            lm_list.append(player)
        elif player[0] == "RM":
            rm_list.append(player)
        elif player[0] == "CM":
            cm_list.append(player)
        elif player[0] == "ST":
            st_list.append(player)
        else:
            raise Exception("105 odd position input 2 player=", player)
        # sort by players overall rating
    gk_list = sorted(gk_list, key=lambda x: x[19], reverse=True)
    dl_list = sorted(dl_list, key=lambda x: x[19], reverse=True)
    dr_list = sorted(dr_list, key=lambda x: x[19], reverse=True)
    cb_list = sorted(cb_list, key=lambda x: x[19], reverse=True)
    lm_list = sorted(lm_list, key=lambda x: x[19], reverse=True)
    rm_list = sorted(rm_list, key=lambda x: x[19], reverse=True)
    cm_list = sorted(cm_list, key=lambda x: x[19], reverse=True)
    st_list = sorted(st_list, key=lambda x: x[19], reverse=True)

    # rebuilt list after being sorted by position and overall value
    for player_gk in gk_list:
        rebuilt_team.append(player_gk)
    for player_dl in dl_list:
        rebuilt_team.append(player_dl)
    for player_dr in dr_list:
        rebuilt_team.append(player_dr)
    for player_cb in cb_list:
        rebuilt_team.append(player_cb)
    for player_lm in lm_list:
        rebuilt_team.append(player_lm)
    for player_rm in rm_list:
        rebuilt_team.append(player_rm)
    for player_cm in cm_list:
        rebuilt_team.append(player_cm)
    for player_st in st_list:
        rebuilt_team.append(player_st)
    # overwrite our global varliable with our newley ordered squad
    return rebuilt_team


def pick_top_eleven(squad):

    localsquad = squad
    best_team_chosen = []
    players_found = 0
    # loop until i have built a team
    while True:
        if len(best_team_chosen) == 11:
            break
        for position, num_players_needed in formation_4_4_2_just_needed.items():
            players_found = 0
            logging.info("Loop details %s %s", position, num_players_needed)
            # break out of this loop if we have all the players we need
            if len(best_team_chosen) == 11:
                break
                players_found = 0

            # loop through each player
            for player in localsquad:
                player_index_position = 0
                # we have all the players we need
                if num_players_needed == players_found:
                    logging.info("num of players needed found")
                    break
                else:
                    # if player fits posistion
                    if (position in player[0][0]) or (position in player[0]):
                        logging.info("i want to add a player %s %s ", position, player)
                        best_team_chosen.append(player)
                        logging.info("Players added to team chosen %s ", player)
                        players_found += 1

                player_index_position += 1

    return best_team_chosen


def best_avliable_team(localsquad):
    # purporse: get best team
    # in: (squad)
    # return: (team ratings)
    best_team_chosen = pick_top_eleven(squad=localsquad)
    # get team score
    gk_score, def_score, ata_score, fitness_score, special_score = create_team_score(
        first_11=best_team_chosen, type_of_team="Best Avliable Team"
    )
    logging.info("Print Best Avaliable Team")
    for i in localsquad:
        logging.info(i)

    global first_11_best_team_chosen
    global first_11_best_team_chosen_team_rating
    first_11_best_team_chosen.append(best_team_chosen)
    first_11_best_team_chosen_team_rating.append(
        [gk_score, def_score, ata_score, fitness_score, special_score]
    )

    return (gk_score, def_score, ata_score, fitness_score, special_score)


def best_young_team(squad_in):
    # purporse:
    # in: (squad)
    # return: (team ratings)

    # so far incoming list is copied and a random number (this will be changed to some kind of caculation based on age,skill etc...) is appeneded to the end of the squad
    # next step sort list by position and the new random number
    # as per above function pick best team, (could that be a new function i.e pick_best 11)

    # look at best under 24 players and fill out the rest
    # scoring system? age+skill+younger players get an increased score + training speed
    # then pop
    # temp_squad=squad_in.copy()
    temp_squad = copy.deepcopy(squad_in)

    index_number = -1
    # for player in temp_squad:
    for player in squad_in.copy():
        index_number += 1
        create_score = 0
        if player[3] < 21:
            create_score += 13
        elif player[3] < 24:
            create_score += 7
        else:
            pass
        create_score += player[10]

        temp_squad[index_number].append(create_score)
    temp_squad = sort_team(temp_squad)

    logging.info("Print Best Young Team")
    for i in temp_squad:
        logging.info(i)
    best_team_chosen = pick_top_eleven(squad=temp_squad)
    gk_score, def_score, ata_score, fitness_score, special_score = create_team_score(
        first_11=best_team_chosen, type_of_team="Best Young Team   "
    )

    global first_11_best_young_team_chosen
    global first_11_best_young_team_chosen_team_rating
    first_11_best_young_team_chosen.append(best_team_chosen)
    first_11_best_young_team_chosen_team_rating.append(
        [gk_score, def_score, ata_score, fitness_score, special_score]
    )

    return (gk_score, def_score, ata_score, fitness_score, special_score)


def best_blended_team(squad_in_2):
    # purporse:
    # in: (squad)
    # return: (team ratings)

    # need a scoring system like age+skill
    # then pop
    # temp_squad_2=squad_in_2.copy()
    temp_squad_2 = copy.deepcopy(squad_in_2)

    index_number = -1
    for player in squad_in_2:
        index_number += 1
        create_score = 0
        if player[3] < 21:
            create_score += 8
        elif player[3] < 24:
            create_score += 5
        else:
            pass
        create_score += player[10]

        temp_squad_2[index_number].append(create_score)
    temp_squad_2 = sort_team(temp_squad_2)

    logging.info("Print Best Blended Team")
    for i in temp_squad_2:
        logging.info(i)

    best_team_chosen_2 = pick_top_eleven(squad=temp_squad_2)
    (
        gk_score2,
        def_score2,
        ata_score2,
        fitness_score2,
        special_score2,
    ) = create_team_score(
        first_11=best_team_chosen_2, type_of_team="Best Blended Team "
    )

    global first_11_best_blended_team_chosen
    global first_11_best_blended_team_chosen_team_rating
    first_11_best_blended_team_chosen.append(best_team_chosen_2)
    first_11_best_blended_team_chosen_team_rating.append(
        [gk_score2, def_score2, ata_score2, fitness_score2, special_score2]
    )

    return (gk_score2, def_score2, ata_score2, fitness_score2, special_score2)


def create_team_score(first_11, type_of_team):
    # purporse:
    # in: (squad)
    # return: (team ratings)

    # average fitness
    # def = GK*1.5 + DEF*4 + 50(MID) ?
    # ata = ATA*50(MID)?
    # lots of stuff
    gk_score = 0
    def_score = 0
    ata_score = 0
    fitness_score = 0
    special_score = 0

    for player in first_11:
        logging.info(player)
        # print(player)
        if "GK" in player[0]:
            gk_score += player[10]
            fitness_score += player[8]
            special_score += player[13]
        elif ("LB" in player[0]) or ("RB" in player[0]) or ("CB" in player[0]):
            def_score += player[10]
            fitness_score += player[8]
            special_score += player[13]
        elif ("LM" in player[0]) or ("RM" in player[0]) or ("CM" in player[0]):
            def_score += player[10] / 2
            ata_score += player[10] / 2
            fitness_score += player[8]
            special_score += player[13]
        elif "ST" in player[0]:
            ata_score += player[10]
            fitness_score += player[8]
            special_score += player[13]
        else:
            raise Exception(
                "106 unexpected player found while trying to score team... player=",
                player,
            )
    # average out score 6 is (4 full defenders) + 2 Midfielders-50% of each Mid counts)
    # average out score 4 is (2 full STK) + 2 Midfielders-50% of each Mid counts)
    def_score = int((def_score / 6))
    ata_score = int((ata_score / 4))
    fitness_score = int((fitness_score / 11))
    print(
        f"{type_of_team} {gk_score}  {def_score} {ata_score}  {fitness_score} {special_score}"
    )
    # for i in first_11:
    #    print(i)
    return (gk_score, def_score, ata_score, fitness_score, special_score)


def formation_choice(squad):
    # purporse:
    # in:
    # return:

    print(f"                   GK  DE AT  FI SP")
    try:
        best_avliable_team(squad)
        best_young_team(squad)
        best_blended_team(squad)
        offer_choice_to_user()
    except Exception as e:
        raise Exception(
            "106 - while trying to create team from squad failed ,squad=", squad
        )


def offer_choice_to_user():

    # purporse:
    # in:
    # return:
    global team_chosen
    global team_stats_chosen
    team_chosen = []
    team_stats_chosen = []
    while True:
        print("Which formation do you want to choose")
        user_input = input(
            "Best Avliable Team(a) , Best Young Team (y) or Best Blended Team(b) or Debug(x) "
        )
        if user_input == ("a"):
            team_chosen = first_11_best_team_chosen
            team_stats_chosen = first_11_best_team_chosen_team_rating
            break
        elif user_input == ("y"):
            team_chosen = first_11_best_young_team_chosen
            team_stats_chosen = first_11_best_young_team_chosen_team_rating
            break
        elif user_input == ("b"):
            team_chosen = first_11_best_blended_team_chosen
            team_stats_chosen = first_11_best_blended_team_chosen_team_rating
            break
        elif user_input == ("x"):
            print("dropping into debug")
            breakpoint()
        else:
            print("Invalid option please choose again")


def starting_preseason(squad):

    # purporse:
    # in:
    # return:

    formation_choice(squad)
    return (team_chosen, team_stats_chosen)
    # offer best avaliable v best young team v blend (scores)
    # give user choice


if __name__ == "__main__":

    # purporse:
    # in:
    # return:
    import os
    import banner

    os.system("clear")
    banner.banner_status(colored_status="ps", season_num=1)

    global squad
    squad = test_squad
    for i in squad:
        logging.info(i)
    starting_preseason(squad=test_squad)
