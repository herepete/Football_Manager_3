#!/usr/bin/python3
"""
Script to create and summarize a squad 
"""

import argparse
import os

# os.system('clear')

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="Verbose information", action="store_true")
parser.add_argument(
    "--benchmark",
    help="Create lots of players, a useful command is ./player_creation.py --benchmark | head -3998 | awk '{print $(NF-7),$(NF-6)}' | sort | uniq | wc -l ",
    action="store_true",
)
parser.add_argument(
    "-n", "--namecheck", help="Check Logic on player names", action="store_true"
)
args = parser.parse_args()


if args.verbose:
    print("verbosity turned on")

# else:
#    print("verbosity not turned on")


# squad_of_players_list is our squad of players
squad_of_players_list = []
avalible_poistions = ["GK", "LB", "RB", "CB", "LM", "RM", "CM", "ST"]

Start_up_parameters = {
    "age_min": "17",
    "age_max": "37",
    "skill_min": "10",
    "skill_max": "20",
}
Free_Agency_parameters = {
    "age_min": "24",
    "age_max": "37",
    "skill_min": "12",
    "skill_max": "20",
}

first_name_list_memory = [
    "Peter",
    "Bob",
    "James",
    "Tony",
    "Aj",
    "Bo",
    "Nathan",
    "Gibby",
    "Tim",
    "Anchor",
    "Jimbo",
    "Paul",
    "Simon",
    "Symon",
    "See",
    "Silver",
    "Titch",
    "Rambo",
    "Robbie",
    "TJ",
    "David",
    "John",
    "Michael",
    "Paul",
    "Andrew",
    "David",
    "Sero",
    "Ian",
    "Brian",
    "Barry",
    "Li",
    "Omar",
    "Junior",
    "Blesing",
    "Banele",
    "Samkelo",
    "Ross",
    "Dylon",
    "Master",
    "Junior",
    "Ung",
    "Me",
    "Nsoki",
    "Zak",
    "Banner",
    "Tommie",
    "Feix",
    "Piero",
    "Robert",
    "Pervis",
    "Xavier",
    "Bruno",
    "Joao",
    "Kim",
    "Hwang",
    "Kieffer",
    "Sorba",
    "Ben",
    "Rubin",
    "Aaron",
    "Haji",
    "Josh",
    "Sean",
    "Shaq",
]
last_name_list_memory = [
    "White",
    "Mander",
    "Bishop",
    "Garrett",
    "Winston",
    "Mayfield",
    "Shearer",
    "Rooney",
    "Tucker",
    "Racker",
    "Hutch",
    "Kane",
    "Del-Piero",
    "Seemen",
    "Locker",
    "Teng",
    "Tubert",
    "Smith",
    "Roberts",
    "Curtis",
    "Hammer",
    "Wang",
    "Chen",
    "Smith",
    "Zhang",
    "Costa",
    "Ribbenov",
    "Stimer",
    "Reize",
    "Lemon",
    "Jean",
    "Mohammed",
    "Ticker",
    "Barrett",
    "Manning",
    "Rogan",
    "Musk",
    "Turing",
    "Ali",
    "Fatima",
    "Hassan",
    "Charles",
    "Omar",
    "Stansfield",
    "Moore",
    "Weah",
    "Reyna",
    "Dest",
    "Foden",
    "Callagher",
    "Karimi",
    "Jalali",
    "Ahmed",
    "Jong",
    "Frimpong",
    "Pacho",
    "Blank",
    "Olsen",
    "Larsen",
    "Skov",
    "Rabiot",
    "Thuram",
    "Ifa",
    "Skhiri",
    "Dahmen",
    "Draper",
    "Oviedo",
    "Ruiz",
    "Lopez",
    "Trapp",
    "Muller",
    "Brandt",
    "Ito",
    "Tanaka",
    "Asano",
    "Torres",
    "Asensio",
    "Fati",
    "Faes",
    "Witsel",
    "Doku",
]


def print_nicer_output_default_squad(squad_to_print):
        if args.verbose:
            print("About to print...", squad_to_print)
        print(
            "PST    Name                  AGE |SKILLS             |PHYSICAL|OVERAL|CONTRACT | TRAINING         | HISTORY    "
        )
        print(
            "                                 |GK   TA   PAS  SHO |FT  PA  | OVE  |COS   CL | SPE    CHA   TS  | EX HI"
        )
        print(
            "================================================================================================================"
        )
        for k in squad_to_print:
            # for k in squad_of_players_list:
            try:
                if args.verbose:
                    print("working on...", k)
                if type(k[0]) == str:
                    temp_position = k[0]
                    player_name = k[1] + " " + k[2]
                    if args.verbose:
                        print("ko=", k[0])
                        print("ko zero string hit")
                else:
                    temp_position = " ".join(k[0])
                    player_name = k[1] + " " + k[2]
                    if args.verbose:
                        print("ko zero string hit")

                # print('{:<12s}{:<15s}{:>10s}{:>5s}{:>5s}{:>15s}{:>12s}{:>5s}{:>5s}'.format(temp_position,player_name,str(k[3]),str(k[4]),str(k[5]),str(k[6]),str(k[7]),str(k[8]),str(k[9]),str(k[10])))
                print(
                    "{:<6s}{:<18s}{:>7s}  |{:>2s}{:>5s}{:>5s}{:>5s}  |{:>2s}  {:>2s}  |{:>4s}  |{:>2s}{:>5s}  |{:>3s}{:>8s}{:>6s} |{:>3s}{:>3s}".format(
                        temp_position,
                        player_name,
                        str(k[3]),
                        str(k[4]),
                        str(k[5]),
                        str(k[6]),
                        str(k[7]),
                        str(k[8]),
                        str(k[9]),
                        str(k[10]),
                        str(k[11]),
                        str(k[12]),
                        str(k[13]),
                        str(k[14]),
                        str(k[15]),
                        str(k[16]),
                        str(k[17]),
                        str(k[18]),
                    )
                )
            except Exception as e:
                raise Exception("107 i errored - printing squad output player=", k)

def print_nicer_output_print_key():
        print("========")
        print("PST=Position", end="|")
        print(
            "SKILLS   - GK=GoalKeeper Skills,TA=Tackling,PAS=Passing,SHO=Shooting",
            end="|",
        )
        print("PHYSICAL - FT=Fitness,PA=Pace", end="|")
        print("OVERAL   - OVE=Overall", end="|")
        print("CONTRACT - COS=Cost per season,CL=Contract", end="|")
        print(
            "TRAINING - SPE=Special attributes (Experience+CHA), CHA=Special Skills (L=Leader,5SR=% Star Recruit,TP=Team Player,LB=Laid Back,Avg=Average Player), TS=Training Speed",
            end="|",
        )
        print("HISTORY  - EX=Experience,HI=History(DP=Default Player)")
        print("========")



global squad_of_players_list
import random

def create_player_player_name():
        # create a random first and last name
        first_name_list = first_name_list_memory
        last_name_list = first_name_list_memory
        random_choice_first_name = random.choice(first_name_list)
        random_choice_last_name = random.choice(last_name_list)
        return(random_choice_first_name,random_choice_last_name)
        if args.verbose:
            print("new player name created=", last_name)

def create_player_random_contract():
        random_contract_year = random.randint(1, 4)
        return random_contract_year

def create_player_player_skill_gk(out_of_position=0):
        # give a random skill
        if out_of_position == 0:
            random_skill = random.randint(10, 20)
            random_skill_gk = random_skill
        else:
            random_skill = random.randint(1, 3)
            random_skill_gk = random_skill
        return (random_skill_gk)

def create_player_player_skill_fitness():
        random_skill = random.randint(skill_min, skill_max)
        random_skill_fitness = random_skill
        return random_skill_fitness

def create_player_player_skill_pace():
        random_skill = random.randint(skill_min, skill_max)
        random_skill_pace = random_skill
        return (random_skill_pace)

def create_player_player_skill_tackle():
        random_skill = random.randint(skill_min, skill_max)
        random_skill_tackle = random_skill
        return (random_skill_tackle)

def create_player_player_skill_passing():
        random_skill = random.randint(skill_min, skill_max)
        random_skill_passing = random_skill
        return (random_skill_passing)

def create_player_player_skill_shooting():
        random_skill = random.randint(skill_min, skill_max)
        random_skill_shooting = random_skill
        return (random_skill_shooting)

def create_player_player_skill_special_skill():
        # default to 0
        # + 1 fir various skill types
        # if expereince is over 5 any extra year = + 1
        # maximum of 5
        temp_count = 0
        if ("Fighter") in player_special_trait:
            temp_count += 1
        if ("Leader") in player_special_trait:
            temp_count += 1
        if ("Team P") in player_special_trait:
            temp_count += 1
        if player_experience_level > 5:
            temp_count = temp_count + (player_experience_level % 5)
        if temp_count > 5:
            temp_count = 5
        random_skill_special_skill = temp_count
        return (random_skill_special_skill)

def create_player_player_age():
        # guve a random age
        random_age = random.randint(age_min, age_max)
        random_age = random_age
        return (random_age = random_age)

def player_training_speed():
        if random_age > 25:
            random_player_personality = ["***", "**", "*"]
        else:
            random_player_personality = ["*****", "****", "***", "**"]
        random_personality_choice = random.choice(random_player_personality)

        random_personality = random_personality_choice
        return(random_personality)

def create_player_special_traits():
        special_traits_random_number = random.randint(1, 10)
        if special_traits_random_number == 7:
            # Leader
            player_special_trait = "Leader"
        elif special_traits_random_number == 8:
            # Team Player
            player_special_trait = "Team P"
        elif special_traits_random_number == 9:
            if random_age < 24:
                #% star recurit (high potential)
                player_special_trait = "5-Star"
            else:
                player_special_trait = "Avg"
        elif special_traits_random_number == 5:
            # laid back
            player_special_trait = "Laid B"
        elif special_traits_random_number == 4:
            player_special_trait = "Fighter"
        else:
            player_special_trait = "Avg"
        player_special_trait = player_special_trait
        return (player_special_trait)

def create_player_calc_player_wage():
        global overall_score
        import random

        if overall_score > 94:
            player_wage = 15
        elif overall_score > 92:
            player_wage = 12
        elif overall_score > 90:
            player_wage = 10
        elif overall_score > 88:
            player_wage = 9
        elif overall_score > 85:
            player_wage = 8
        elif overall_score > 83:
            player_wage = 7
        elif overall_score > 80:
            player_wage = 6
        elif overall_score > 75:
            player_wage = random.randint(1, 6)
        else:
            player_wage = random.randint(1, 6)

        return(player_wage)

def create_player_create_position():
        # give a random position (some players get more than 1 position)
        defender_choice_position = ["LB", "RB", "CB"]
        midfield_choice_position = ["LM", "RM", "CM"]
        attacker_choice_position = ["ST"]
        player_selected_position = []
        import random

        global avalible_poistions

        if play_position == "GK":
            final_player_position = ["GK"]
        elif play_position == "DEF":
            # determine how many position a player can play, the choices are weighted to make player in 3 positions quite rare
            final_player_position = random.choice(defender_choice_position)
        elif play_position == "MID":
            final_player_position = random.choice(midfield_choice_position)

        else:
            # we are presuming a Sticker
            # determine how many position a player can play,  the choices are weighted to make player in 3 positions quite rare
            final_player_position = "ST"

        return(final_player_position)

def create_player_player_id():
        import random
        import time

        # get 2 value 1 millisec & a random number
        millisec = int(time.time() * 100000000)
        random_number = random.randint(1, 999999)

        # combine value into 1 string
        string_value = str(millisec) + str(random_number)

        # use just the last 12 chars as it could be 24 chars at max
        string_value = string_value[12:]
        random_player_id = string_value
        return(random_player_id)

        # return random_player_id

def create_player_player_experience(default):
        if default == "1":
            player_experience_level = 0
        else:
            # not expecting this to hit but includding for future use
            player_experience_level = 10

        return player_experience_level

    # using Kwargs to allow this to be called from outside this script
def create_player_player_rating(
        final_player_position_in,
        random_skill_gk_in,
        random_skill_tackle_in,
        random_skill_passing_in,
        random_skill_shooting_in,
        random_skill_fitness_in,
        random_skill_pace_in,
        random_skill_special_skill_in,
    ):
        # work out score out of 100 and then /5 to give
        # print("am i being called")
        global overall_score

        if final_player_position_in[0] == "GK":
            # so 85% gk skill, and
            # 5% from fitness,passing and special skill
            overall_score = int(
                (random_skill_gk_in / 20) * 85
                + (random_skill_fitness_in / 20) * 5
                + (random_skill_passing_in / 20) * 5
                + (random_skill_special_skill_in)
            )
        elif final_player_position_in == "LB" or final_player_position_in == "RB":
            # so 37% from Tacking
            # 20 from Pace and Passing
            # 15 from Fitness
            # 5 from Special skill
            # 3 from Shooting
            overall_score = int(
                (random_skill_tackle_in / 20) * 37
                + (random_skill_fitness_in / 20) * 15
                + (random_skill_passing_in / 20) * 20
                + (random_skill_pace_in / 20) * 20
                + (random_skill_special_skill_in)
                + (random_skill_shooting_in / 20) * 3
            )
        elif final_player_position_in == "CB":
            # so 40% from Tacking
            # 18 from Fitness and Pace
            # 13 from Passing
            # 8 from Special skill
            # 3 from Shooting
            overall_score = int(
                (random_skill_tackle_in / 20) * 40
                + (random_skill_fitness_in / 20) * 18
                + (random_skill_passing_in / 20) * 13
                + (random_skill_pace_in / 20) * 18
                + (random_skill_special_skill_in / 5) * 8
                + (random_skill_shooting_in / 20) * 3
            )
        elif final_player_position_in == "LM" or final_player_position_in == "RM":
            # 25 from Fitness,passing and Pace
            # 10 Tacking and Shooting
            # 5 from Special skill
            overall_score = int(
                (random_skill_tackle_in / 20) * 10
                + (random_skill_fitness_in / 20) * 25
                + (random_skill_passing_in / 20) * 25
                + (random_skill_pace_in / 20) * 25
                + (random_skill_special_skill_in)
                + (random_skill_shooting_in / 20) * 10
            )
        elif final_player_position_in == "CM":
            # 21 from Fitness
            # 18 Pace,Passing,Shooting
            # 15 Tackling
            # 10 from Special skill
            overall_score = int(
                (random_skill_tackle_in / 20) * 15
                + (random_skill_fitness_in / 20) * 21
                + (random_skill_passing_in / 20) * 18
                + (random_skill_pace_in / 20) * 18
                + (random_skill_special_skill_in / 5) * 10
                + (random_skill_shooting_in / 20) * 18
            )
        elif final_player_position_in == "ST":
            # 50 from Shooting
            # 19 Pace
            # 14 Fitness
            # 9 Passing
            # 8 from Special skill
            overall_score = int(
                (random_skill_fitness_in / 20) * 14
                + (random_skill_passing_in / 20) * 9
                + (random_skill_pace_in / 20) * 19
                + (random_skill_special_skill_in / 5) * 8
                + (random_skill_shooting_in / 20) * 50
            )
        else:
            print("Unexpected player position=", final_player_position_in)
            raise Exception(
                "108 i Errored - Unexpected player position=", final_player_position_in
            )
        return (overall_score)
        

def create_player_player_creation(play_position, type_of_player):
        # Where all the magic happens to create a Squad
        # the order is quite important here as variables are reliant on previous functions
        global age_min, age_max, skill_min, skill_max, overall_score
        if type_of_player == "Start Up":
            age_min = int(Start_up_parameters["age_min"])
            age_max = int(Start_up_parameters["age_max"])
            skill_min = int(Start_up_parameters["skill_min"])
            skill_max = int(Start_up_parameters["skill_max"])
        elif type_of_player == "Free Agency":
            age_min = int(Free_Agency_parameters["age_min"])
            age_max = int(Free_Agency_parameters["age_max"])
            skill_min = int(Free_Agency_parameters["skill_min"])
            skill_max = int(Free_Agency_parameters["skill_max"])
        else:
            age_min = int(Start_up_parameters["age_min"])
            age_max = int(Start_up_parameters["age_max"])
            skill_min = int(Start_up_parameters["skill_min"])
            skill_max = int(Start_up_parameters["skill_max"])

        global squad_of_players
        player_name()
        if play_position == "GK":
            player_skill_gk(0)
        else:
            player_skill_gk(1)
        player_skill_pace()
        player_skill_fitness()
        player_skill_tackle()
        player_skill_passing()
        player_skill_shooting()

        player_age()
        play_position = play_position
        create_position()
        random_contract()
        player_training_speed()
        special_traits()
        player_id()
        player_experience("1")
        player_history = "DP"
        player_skill_special_skill()
        try:
            create_player.player_rating(
                final_player_position_in=final_player_position,
                random_skill_gk_in=random_skill_gk,
                random_skill_tackle_in=random_skill_tackle,
                random_skill_passing_in=random_skill_passing,
                random_skill_shooting_in=random_skill_shooting,
                random_skill_fitness_in=random_skill_fitness,
                random_skill_pace_in=random_skill_pace,
                random_skill_special_skill_in=random_skill_special_skill,
            )
        except:
            raise Exception("109 i Errored - creating player")
        calc_player_wage()
        try:
            # X Y and Z are added for future use
            temp_build = [
                final_player_position,
                first_name,
                last_name,
                random_age,
                random_skill_gk,
                random_skill_tackle,
                random_skill_passing,
                random_skill_shooting,
                random_skill_fitness,
                random_skill_pace,
                overall_score,
                player_wage,
                random_contract_year,
                random_skill_special_skill,
                player_special_trait,
                random_personality,
                player_experience_level,
                player_history,
                random_player_id,
            ]
            if args.verbose:
                print("Here is my temp build ... ", temp_build)
                print("...Here is the breakdown of each variable...")
                print("final_player_position=", final_player_position)
                print("first_name=", first_name)
                print("last_name=", last_name)
                print("random_age=", random_age)
                print("random_skill_gk=", random_skill_gk)
                print("random_skill_tackle=", random_skill_tackle)
                print("random_skill_passing=", random_skill_passing)
                print("random_skill_shooting=", random_skill_shooting)
                print("random_skill_fitness=", random_skill_fitness)
                print("random_skill_pace=", random_skill_pace)
                print("overall_score=", overall_score)
                print("player_wage=", player_wage)
                print("random_contract_year=", random_contract_year)
                print(
                    "random_skill_special_skill=", random_skill_special_skill
                )
                print("player_special_trait=", player_special_trait)
                print("random_personality=", random_personality)
                print("player_experience_level=", player_experience_level)
                print("player_history=", player_history)
                print("random_player_id=", random_player_id)

            squad_of_players_list.append(temp_build)
        except Exception as e:
            print("oops something went wrong when creating the squad")
            print("Error reads=", e)
            raise Exception(
                "115 i Errored - something went wrong when creating the squad"
            )
        # we only return aim to return values if called by above scripts
        if type_of_player == "Free Agency":
            try:
                return squad_of_players_list
            except Exception as e:
                print("Woops i broke :( ")
                raise Exception(
                    "110 i Errored - Type of player =Free agencey and i could returned squad of players list"
                )


def Squad_stats_and_feedback_cost_of_squad(squad_to_check):
        total_cost = 0
        for cost_of_player in squad_to_check:
            temp_cost = int(cost_of_player[11])
            total_cost += temp_cost
        print("Total Squad Wages      =", total_cost)

def Squad_stats_and_feedback_squad_feedback(squad_to_check):
        total_age = 0
        total_skill = 0
        global avalible_poistions
        build_squads_positions = []
        # type_of_player=["GK","LB","RB","CB","LM","RM","CM","Def M","Ata M","ST","W"]

        for player in squad_to_check:
            temp_age = player[3]
            temp_skill = player[10]
            total_age += temp_age
            total_skill += temp_skill
            temp_position = player[0]
            # number of players in each position
            for player_position in temp_position:
                build_squads_positions.append(player_position)

        average_age = total_age // len(squad_to_check)
        average_skill = total_skill // len(squad_to_check)
        print("Average age of Squad   =", average_age)
        print("Average skill of Squad =", average_skill)

def Squad_stats_and_feedback_players_per_position(squad_to_check):
        position_count = 0
        master_position_count = {}
        global avalible_poistions
        for i in avalible_poistions:
            for j in squad_to_check:
                if i in j[0]:
                    position_count += 1
            master_position_count[i] = position_count
            position_count = 0
        print("=======Players per position")
        # print ("       GK=",gk_highest_rating)
        # print ("         GK="(int(master_position_count.get("GK")))
        try:
            # pass
            print(f"         GK={master_position_count.get('GK')}")
            print(
                "LB={:<5} CB={:<5} RB={:<5}".format(
                    (master_position_count.get("LB")),
                    master_position_count.get("CB"),
                    master_position_count.get("RB"),
                )
            )
            print(
                "LM={:<5} CM={:<5} RM={:<5}".format(
                    (master_position_count.get("LM")),
                    master_position_count.get("CM"),
                    master_position_count.get("RM"),
                )
            )
            print("         ST={:<5}".format((master_position_count.get("ST"))))

        except:
            raise Exception(
                "111 i Errored - while trying to create players per position summary i errored"
            )

def Squad_stats_and_feedback_char_of_team(squad_to_check):
        avg_players = 0
        team_p_players = 0
        leader_players = 0
        fighter_player = 0
        five_star_player = 0
        laid_b_players = 0
        for player in squad_to_check:
            if player[14] == "Team P":
                team_p_players += 1
            elif player[14] == "Avg":
                avg_players += 1
            elif player[14] == "Fighter":
                fighter_player += 1
            elif player[14] == "Leader":
                leader_players += 1
            elif player[14] == "5-Star":
                five_star_player += 1
            elif player[14] == "Laid B":
                laid_b_players += 1
            else:
                print("Whops odd char found")
                raise Exception(
                    "112 i Errored - i found an odd char, player = ", player
                )
        print("=======Charcteur of team...")
        print(
            "Avg_Players | Team_Players | Leaders | Fighters | 5_Star_Recruits | Laid back players"
        )
        print(
            "====================================================================================="
        )
        print(
            "{:<12}| {:<13}| {:<8}| {:<9}| {:<16}| {:<15}".format(
                avg_players,
                team_p_players,
                leader_players,
                fighter_player,
                five_star_player,
                laid_b_players,
            )
        )
        # print (f"{avg_players}          |{team_p_players}             | {leader_players}       | {fighter_player}        |{five_star_player}            |{laid_b_players} ")

def Squad_stats_and_feedback_rating_per_position(squad_to_check):
        global avalible_poistions
        gk_highest_rating = 0
        lb_highest_rating = 0
        rb_highest_rating = 0
        cb_highest_rating = 0
        lm_highest_rating = 0
        rm_highest_rating = 0
        cm_highest_rating = 0
        s_highest_rating = 0
        for i in squad_to_check:
            if "GK" in i[0]:
                if i[4] > gk_highest_rating:
                    gk_highest_rating = i[10]
            elif "LB" in i[0]:
                if i[4] > lb_highest_rating:
                    lb_highest_rating = i[10]
            elif "RB" in i[0]:
                if i[4] > rb_highest_rating:
                    rb_highest_rating = i[10]
            elif "CB" in i[0]:
                if i[4] > cb_highest_rating:
                    cb_highest_rating = i[10]
            elif "LM" in i[0]:
                if i[4] > lm_highest_rating:
                    lm_highest_rating = i[10]
            elif "RM" in i[0]:
                if i[4] > rm_highest_rating:
                    rm_highest_rating = i[10]
            elif "CM" in i[0]:
                if i[4] > cm_highest_rating:
                    cm_highest_rating = i[10]
            elif "ST" in i[0]:
                if i[4] > s_highest_rating:
                    s_highest_rating = i[10]
            else:
                print("who are you?")
                raise Exception("113 i Errored - i found an odd position, player = ", i)

        # print("=======")
        print("======Highest Rated")
        print(f"       GK={gk_highest_rating}")
        print(
            "LB={}  CB={}  RB={}".format(
                lb_highest_rating, cb_highest_rating, rb_highest_rating
            )
        )
        print(
            "LM={}  CM={}  RM={}".format(
                lm_highest_rating, cm_highest_rating, rm_highest_rating
            )
        )
        print("       ST={}".format(s_highest_rating))

def Squad_stats_and_feedback_sort_squad():
        global squad_of_players_list
        # group players by position (first into indvidual list and then combine them later on)
        incoming_squad_in = squad_of_players_list
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
                print("odd position input 2")
                print(player)
                raise Exception("114 i Errored - odd position found player = ", player)

        # sort by players overall rating
        gk_list = sorted(gk_list, key=lambda x: x[10], reverse=True)
        dl_list = sorted(dl_list, key=lambda x: x[10], reverse=True)
        dr_list = sorted(dr_list, key=lambda x: x[10], reverse=True)
        cb_list = sorted(cb_list, key=lambda x: x[10], reverse=True)
        lm_list = sorted(lm_list, key=lambda x: x[10], reverse=True)
        rm_list = sorted(rm_list, key=lambda x: x[10], reverse=True)
        cm_list = sorted(cm_list, key=lambda x: x[10], reverse=True)
        st_list = sorted(st_list, key=lambda x: x[10], reverse=True)

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
        squad_of_players_list = rebuilt_team


def core_run():

    create_default_list = create_player()
    squad_feedback_call = Squad_stats_and_feedback()

    default_squad_GK = 4
    default_squad_DEF = 9
    default_squad_MID = 9
    default_squad_ATA = 6

    for j in range(1, default_squad_GK):
        create_default_list.player_creation(
            play_position="GK", type_of_player="Start Up"
        )
    for k in range(1, default_squad_DEF):
        create_default_list.player_creation(
            play_position="DEF", type_of_player="Start Up"
        )
    for k in range(1, default_squad_MID):
        create_default_list.player_creation(
            play_position="MID", type_of_player="Start Up"
        )
    for k in range(1, default_squad_ATA):
        create_default_list.player_creation(
            play_position="ATA", type_of_player="Start Up"
        )

    # quite hacky but make sure our default squad has at least enough players in each position
    squad_of_players_list[3][0] = "LB"
    squad_of_players_list[4][0] = "RB"
    squad_of_players_list[5][0] = "CB"
    squad_of_players_list[6][0] = "CB"
    squad_of_players_list[11][0] = "LM"
    squad_of_players_list[12][0] = "RM"
    squad_of_players_list[13][0] = "CM"
    squad_of_players_list[14][0] = "CM"

    squad_feedback_call.sort_squad()
    nicer_output = print_nicer_output()
    nicer_output.default_squad(squad_to_print=squad_of_players_list)
    nicer_output.print_key()
    # reoder the squad to make it more readable
    # squad_feedback_call.sort_squad()
    squad_feedback_call.squad_feedback(squad_to_check=squad_of_players_list)
    squad_feedback_call.cost_of_squad(squad_to_check=squad_of_players_list)
    squad_feedback_call.char_of_team(squad_of_players_list)
    squad_feedback_call.players_per_position(squad_to_check=squad_of_players_list)
    squad_feedback_call.rating_per_position(squad_to_check=squad_of_players_list)
    return squad_of_players_list


if __name__ == "__main__":
    if args.benchmark:
        default_squad_GK = 1000
        default_squad_DEF = 1000
        default_squad_MID = 1000
        default_squad_ATA = 1000
    if args.namecheck:
        import itertools

        initaite_cp = create_player()
        initaite_cp.player_name()
        print("First names=", len(first_name_list_memory))
        print("Last names=", len(last_name_list_memory))
        count_permutations = len(first_name_list_memory) * len(last_name_list_memory)
        print("Permutations on first and last name=", count_permutations)
        exit()
    import os

    os.system("clear")
    import banner

    banner.banner_status(colored_status="i", season_num=1)
    core_run()
