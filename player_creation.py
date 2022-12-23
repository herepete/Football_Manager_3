#!/usr/bin/python3
"""
Script to create and summarize a squad 
"""

import argparse
import os
import random
import time
import game_settings

__version__ = '1.0.0'
__author__ = 'Peter White'

#importing setting from game_settings file
wage_limit=game_settings.Total_Wage_Limit
avalible_poistions=game_settings.avalible_poistions
Start_up_parameters=game_settings.Start_up_parameters
Free_Agency_parameters=game_settings.Free_Agency_parameters
Random_poor_parameters=game_settings.Random_poor_parameters
first_name_list_memory=game_settings.first_name_list_memory
last_name_list_memory=game_settings.last_name_list_memory

# squad_of_players_list is our squad of players
squad_of_players_list = []

def argparse_calls():
    """a function to setup argparse for us
       input =None
       return=args
        """

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
    try:
        return args()
    except:
        pass

def print_nicer_output_default_squad(squad_to_print,print_index="n",print_header="y"):
        """a function to print the squad into a nice format
           input = List of players to print, print index (enumeration) used in contract renewal, print_header=y or n (used in checking change of player skills and you want a nice easy comparision)
           output =  print to screen
        """


        if print_index=="y":        
        #we will print very similar to no but just with an index, this can be used to help the user select a certain player
            if print_header=="y":
                print(
                    "Index PST    Name                  AGE |SKILLS             |PHYSICAL|OVERAL|CONTRACT | TRAINING         | HISTORY    "
                )
                print(
                    "                                       |GK   TA   PAS  SHO |FT  PA  | OVE  |COS   CL | SPE    CHA   TS  | EX HI"
                )
                print(
                    "================================================================================================================"
                )
            index_number=1
            for k in squad_to_print:
                # for k in squad_of_players_list:
                try:
                    #if args.verbose:
                    #    print("working on...", k)
                    if type(k[0]) == str:
                        temp_position = k[0]
                        player_name = k[1] + " " + k[2]
                        #if args.verbose:
                        #    print("ko=", k[0])
                        #    print("ko zero string hit")
                    else:
                        temp_position = " ".join(k[0])
                        player_name = k[1] + " " + k[2]
                        #if args.verbose:
                         #   print("ko zero string hit")

                    # print('{:<12s}{:<15s}{:>10s}{:>5s}{:>5s}{:>15s}{:>12s}{:>5s}{:>5s}'.format(temp_position,player_name,str(k[3]),str(k[4]),str(k[5]),str(k[6]),str(k[7]),str(k[8]),str(k[9]),str(k[10])))
                    print(
                        "{:<6s}{:<6s}{:<18s}{:>7s}  |{:>2s}{:>5s}{:>5s}{:>5s}  |{:>2s}  {:>2s}  |{:>4s}  |{:>2s}{:>5s}  |{:>3s}{:>8s}{:>6s} |{:>3s}{:>3s}".format(
                            str(index_number),
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
                    index_number+=1
                except Exception as e:
                    print("Error=",e)
                    raise Exception("107-A i errored - printing squad output player=", k)

        else:
            if print_header=="y":
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
                    #if args.verbose:
                    #    print("working on...", k)
                    if type(k[0]) == str:
                        temp_position = k[0]
                        player_name = k[1] + " " + k[2]
                        #if args.verbose:
                        #    print("ko=", k[0])
                        #    print("ko zero string hit")
                    else:
                        temp_position = " ".join(k[0])
                        player_name = k[1] + " " + k[2]
                        #if args.verbose:
                         #   print("ko zero string hit")

                    # print('{:<12s}{:<15s}{:>10s}{:>5s}{:>5s}{:>15s}{:>12s}{:>5s}{:>5s}'.format(temp_position,player_name,str(k[3]),str(k[4]),str(k[5]),str(k[6]),str(k[7]),str(k[8]),str(k[9]),str(k[10])))
                    print(
                        "{:<6s}{:<18s}{:>7s}  |{:>2s}{:>5s}{:>5s}{:>5s}  |{:>2s}  {:>2s}  |{:>4s}  |{:>2s}{:>5s}  |{:>3s}{:>8s}{:>6s} |{:>3s} {:>3s}".format(
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
                    print("Error=",e)
                    breakpoint()
                    raise Exception("107-B i errored - printing squad output player=", k)


def print_nicer_output_print_key():
        """a function to print the squad key
           input = none
           output = print to screen
    """
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



def create_player_player_name():
        """create a random first and last name
           input = none
           return = a random combination of first name and last name
"""
        first_name_list = first_name_list_memory
        last_name_list = first_name_list_memory
        random_choice_first_name = random.choice(first_name_list)
        random_choice_last_name = random.choice(last_name_list)
        return(random_choice_first_name,random_choice_last_name)
        if args.verbose:
            print("new player name created=", last_name)

def create_player_random_contract():
        """create a random contract length
           input = none 
           return = a random contract year between 1 and 4 """
        random_contract_year = random.randint(1, 4)
        return random_contract_year

def create_player_player_skill_gk(out_of_position=0):
        """give a random gk skill
            input = out_of_position if GK = 0 else 1
            return = random_skill_gk -dependant on input score will be between 1 and 20"""
        if out_of_position == 0:
            random_skill = random.randint(10, 20)
            random_skill_gk = random_skill
        else:
            random_skill = random.randint(1, 3)
            random_skill_gk = random_skill
        return (random_skill_gk)

def create_player_player_skill_fitness():
        """give a random fitness  skill
           input  = none
           return = random skill fitness take setting from game_settings.py but typically between 10 and 20

"""
        random_skill = random.randint(skill_min, skill_max)
        random_skill_fitness = random_skill
        return random_skill_fitness

def create_player_player_skill_pace(): 
        """give a random pace skill
           input = none
           return = random skill pace take setting from game_settings.py but typically between 10 and 20
"""
        random_skill = random.randint(skill_min, skill_max)
        random_skill_pace = random_skill
        return (random_skill_pace)

def create_player_player_skill_tackle():
        """give a random tackle skill
           input = none
           return = random skill tackle take setting from game_settings.py but typically between 10 and 20
"""
        random_skill = random.randint(skill_min, skill_max)
        random_skill_tackle = random_skill
        return (random_skill_tackle)

def create_player_player_skill_passing():
        """give a random passing skill
           input = none
           return = random skill passing take setting from game_settings.py but typically between 10 and 20
"""
        random_skill = random.randint(skill_min, skill_max)
        random_skill_passing = random_skill
        return (random_skill_passing)

def create_player_player_skill_shooting():
        """give a random shooting skill
           input = none
           return = random skill shooting take setting from game_settings.py but typically between 10 and 20

"""
        random_skill = random.randint(skill_min, skill_max)
        random_skill_shooting = random_skill
        return (random_skill_shooting)

def create_player_player_skill_special_skill(player_special_trait,player_experience_level):
        """calculate specical skill
         default to 0
         + 1 for various skill types
         if expereince is over 5 any extra year = + 1
         maximum of 5

         input =  player_special_trait i.e 'Fighter',player_experience_level i.e '1'
         return = random skill player special skill based on player experience and special traits

"""
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
        """ give a random age
            input = none
           return = random age take setting from game_settings.py but typically 17 and 27

"""
        random_age = random.randint(age_min, age_max)
        return (random_age)

def create_player_player_training_speed(random_age_in):
        """ calculate a semi random training speed 
            input  = random_age_in i.e '27'
            return = based on age and some randomness you will get a "*" rating where * is the worst and ****** is the best
"""
        if random_age_in > 25:
            random_player_personality = ["***", "**", "*"]
        else:
            random_player_personality = ["*****", "****", "***", "**"]
        random_personality_choice = random.choice(random_player_personality)

        random_personality = random_personality_choice
        return(random_personality)

def create_player_special_traits(random_age):
        """calculate a random special trait
           input = random_age i.e '27'
           output = special trait based on random choice you can either be "AVG" (average) , Leader, Team Player, 5-Star , Laid back or Fighter """
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

def create_player_calc_player_wage(overall_score):
        """calculate player overall wage
        input = none 
        output = based on players overall score create a wage"""
        #global overall_score

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

def create_player_create_position(play_position):
        """give a random position
            input = play_position i.e 'GK'
            return = position choice"""
        defender_choice_position = ["LB", "RB", "CB"]
        midfield_choice_position = ["LM", "RM", "CM"]
        attacker_choice_position = ["ST"]
        player_selected_position = []

        #global avalible_poistions

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
        """create a hopefully unique player id (used as a unqiue identifier)
            input = none 
            return = player id which is a combo of the current millisecond time and a random number """

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
        """Create a default players experience
            input = max default is passed through
            output =expereince will be a number between 0 and variable passed in"""
        #if default == "1":
        #    player_experience_level = 0
        #else:
            # not expecting this to hit but includding for future use
         #   player_experience_level = 10

        player_experience_level=random.randint(0,int(default))

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
        """ work out score out of 100 
            input = position, then gk,tackle,passing,shooting,fitness,pace and special skills
            output = overall_score depending on input do some number crunching and produce a score out of 100 i.e '92' """
        #global overall_score

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
            breakpoint()
            raise Exception(
                "108 i Errored - Unexpected player position=", final_player_position_in
            )
        return (overall_score)
        

def create_player_player_creation(play_position, type_of_player, return_player=0):
        """ Where all the magic happens to create a Squad
         the order is quite important here as variables are reliant on previous functions 
        input = 
            play_position i.e GK, 
            type_of_player (Start Up,Free Agency,Draft or else) -this effects player history and skill of player 
            return_player default to 0 if 1 a player is returned-used when players being created outside this script and a player is wanted)
        output = a squad of players """
        global age_min, age_max, skill_min, skill_max, overall_score,squad_of_players_list
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

        elif type_of_player == "Random Poor":
            age_min = int(Random_poor_parameters["age_min"])
            age_max = int(Random_poor_parameters["age_max"])
            skill_min = int(Random_poor_parameters["skill_min"])
            skill_max = int(Random_poor_parameters["skill_max"])
            squad_of_players_list=[]

        else:
            age_min = int(Start_up_parameters["age_min"])
            age_max = int(Start_up_parameters["age_max"])
            skill_min = int(Start_up_parameters["skill_min"])
            skill_max = int(Start_up_parameters["skill_max"])

        global squad_of_players
        first_name_created,second_name_created=create_player_player_name()
        if play_position == "GK":
            gk_skill_created=create_player_player_skill_gk(0)
        else:
            gk_skill_created=create_player_player_skill_gk(1)
        pace_skill_created=create_player_player_skill_pace()
        fitness_skill_created=create_player_player_skill_fitness()
        tackle_skill_created=create_player_player_skill_tackle()
        passing_skill_created=create_player_player_skill_passing()
        shooting_skill_created=create_player_player_skill_shooting()

        age_created=create_player_player_age()

        #if Random Poor i am going to force a particular position
        if type_of_player=="Random Poor":
            player_position_created=play_position
        else:    
            player_position_created=create_player_create_position(play_position)
        player_contract_created=create_player_random_contract()
        training_speed_created=create_player_player_training_speed(age_created)
        special_trait_skill_created=create_player_special_traits(age_created)
        player_id_created=create_player_player_id()
        if type_of_player=="Random Poor":
            player_experience_created=create_player_player_experience("4")
        elif type_of_player=="Start Up":
            player_experience_created=create_player_player_experience("4")
        elif type_of_player=="Free Agency":
            player_experience_created=create_player_player_experience("10")
        else:
            #including drated and detauy players
            player_experience_created=create_player_player_experience("1")
        #print("type of player=",type_of_player)
        #input()
        if type_of_player=="Random Poor":
            player_history_created=create_player_player_history = "Replacement"
        elif type_of_player=="Start Up":
            player_history_created=create_player_player_history = "DP"
        elif type_of_player=="Draft":
            player_history_created=create_player_player_history = "Draft"
        elif type_of_player=="Free Agency":
            player_history_created=create_player_player_history = "FA"
        else:
            player_history_created=create_player_player_history = "UN"
        player_special_skill_created=create_player_player_skill_special_skill(special_trait_skill_created,player_experience_created)
        try:
            player_overall_score_created=create_player_player_rating(
                final_player_position_in= player_position_created,
                random_skill_gk_in=gk_skill_created,
                random_skill_tackle_in=tackle_skill_created,
                random_skill_passing_in=passing_skill_created,
                random_skill_shooting_in=shooting_skill_created,
                random_skill_fitness_in=fitness_skill_created,
                random_skill_pace_in=pace_skill_created,
                random_skill_special_skill_in=player_special_skill_created,
            )
        except Exception as e:
            raise Exception("109 i Errored - creating player, error=",e)
            
        player_wage_created=create_player_calc_player_wage(player_overall_score_created)
        try:
            temp_build = [
                player_position_created,
                first_name_created,
                second_name_created,
                age_created,
                gk_skill_created,
                tackle_skill_created,
                passing_skill_created,
                shooting_skill_created,
                fitness_skill_created,
                pace_skill_created,
                player_overall_score_created,
                player_wage_created,
                player_contract_created,
                player_special_skill_created,
                special_trait_skill_created,
                training_speed_created,
                player_experience_created,
                player_history_created,
                 player_id_created,
            ]
            if False:
            #if args.verbose:
                print("Here is my temp build ... ", temp_build)
                print("...Here is the breakdown of each variable...")
                print("final_player_position=", player_position_created)
                print("first_name=", first_name_created)
                print("last_name=",  second_name_created)
                print("random_age=", age_created)
                print("random_skill_gk=", gk_skill_created)
                print("random_skill_tackle=", tackle_skill_created)
                print("random_skill_passing=", passing_skill_created)
                print("random_skill_shooting=", shooting_skill_created)
                print("random_skill_fitness=", fitness_skill_created)
                print("random_skill_pace=",  pace_skill_created)
                print("overall_score=", player_overall_score_created)
                print("player_wage=",  player_wage_created)
                print("random_contract_year=", player_contract_created)
                print(
                    "random_skill_special_skill=",  player_special_skill_created
                )
                print("player_special_trait=", special_trait_skill_created)
                print("random_personality=",  random_personality)
                print("player_experience_level=", player_experience_created)
                print("player_history=", player_history_created)
                print("random_player_id=", player_id_created)

            squad_of_players_list.append(temp_build)
        except Exception as e:
            print("oops something went wrong when creating the squad")
            print("Error reads=", e)
            breakpoint()
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
        if return_player==1:
            return (squad_of_players_list)


def Squad_stats_and_feedback_cost_of_squad(squad_to_check):
        """ print cost of squad 
            input = Squad to check
            output = print total squad wages"""
        total_cost = 0
        for cost_of_player in squad_to_check:
            temp_cost = int(cost_of_player[11])
            total_cost += temp_cost
        print("Total Squad Wages      =", total_cost)

def Squad_stats_and_feedback_squad_feedback(squad_to_check):
        """ print stats on squad 
            input = squad to check
            output = print average age and skill of squad
"""
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
        """ print feedback on squad per position 
            input  = squad to check
            ouput = print number of players per position"""
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
        """ print charactuer of squad 
            input = squad to check
            output = print chareacr of team
"""
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
        """ print rating per position 
            input = none 
            output = print highest rating per position"""
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

def Squad_stats_and_feedback_sort_squad(squad_in):
        """ sort squad by overall rating 
            input = squad 
            output = squad_of_players_list - a sorted squad  """
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
        return(squad_of_players_list)


def core_run():
    """ the main call in the script
     glues everything together 
    input = none
    output = our team """
    
    #create_player_player_creation()
    #create_default_list = create_player()
    #squad_feedback_call = Squad_stats_and_feedback()

    import game_settings
    default_squad_GK = game_settings.default_squad_GK
    default_squad_DEF = game_settings.default_squad_DEF
    default_squad_MID = game_settings.default_squad_MID
    default_squad_ATA = game_settings.default_squad_ATA

    

    for j in range(1, default_squad_GK):
        create_player_player_creation(
            play_position="GK", type_of_player="Start Up"
        )
    for k in range(1, default_squad_DEF):
        create_player_player_creation(
            play_position="DEF", type_of_player="Start Up"
        )
    for k in range(1, default_squad_MID):
        create_player_player_creation(
            play_position="MID", type_of_player="Start Up"
        )
    for k in range(1, default_squad_ATA):
        create_player_player_creation(
            play_position="ATA", type_of_player="Start Up"
        )
    #breakpoint()
    #print_nicer_output_default_squad(squad_of_players_list)
    # quite hacky but make sure our default squad has at least enough players in each position
    squad_of_players_list[3][0] = "LB"
    squad_of_players_list[4][0] = "RB"
    squad_of_players_list[5][0] = "CB"
    squad_of_players_list[6][0] = "CB"
    squad_of_players_list[11][0] = "LM"
    squad_of_players_list[12][0] = "RM"
    squad_of_players_list[13][0] = "CM"
    squad_of_players_list[14][0] = "CM"

    Squad_stats_and_feedback_sort_squad(squad_of_players_list)
    print_nicer_output_default_squad(squad_of_players_list)
    print_nicer_output_print_key()
    # reoder the squad to make it more readable
    # squad_feedback_call.sort_squad()
    Squad_stats_and_feedback_squad_feedback(squad_of_players_list)
    Squad_stats_and_feedback_cost_of_squad(squad_of_players_list)
    Squad_stats_and_feedback_char_of_team(squad_of_players_list)
    Squad_stats_and_feedback_players_per_position(squad_of_players_list)
    Squad_stats_and_feedback_rating_per_position(squad_of_players_list)
    return squad_of_players_list


if __name__ == "__main__":
    argparse_calls()
    #breakpoint()
    #if args.benchmark:
    #    default_squad_GK = 1000
    #    default_squad_DEF = 1000
    #    default_squad_MID = 1000
    #    default_squad_ATA = 1000
    #if args.namecheck:
    #    import itertools

    #    print("First names=", len(first_name_list_memory))
    #    print("Last names=", len(last_name_list_memory))
    #    count_permutations = len(first_name_list_memory) * len(last_name_list_memory)
    #    print("Permutations on first and last name=", count_permutations)
    #    exit()
    import os
    import banner

    os.system("clear")
    banner.banner_status(colored_status="i", season_num=1)
    core_run()
