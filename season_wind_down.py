#!/usr/bin/python3
import argparse
import logging

parser=argparse.ArgumentParser()
parser.add_argument("-v","--verbose",help="Verbose information",action="store_true")
args =parser.parse_args()

#for_testing
player_squad=[[['GK'], 'Sean', 'Robbie', 24, 19, 15, 12, 15, 16, 18, 88, 8, 4, 1, 'Leader', '****', 0, 'DP', 1910617], [['GK'], 'Banele', 'Bo', 36, 14, 20, 11, 15, 19, 16, 67, 5, 4, 0, 'Avg', '**', 0, 'DP', 3037073], [['GK'], 'Dylon', 'Sean', 26, 11, 18, 18, 13, 10, 14, 53, 1, 1, 0, 'Avg', '***', 0, 'DP', 2412897], ['LB', 'Josh', 'Master', 27, 3, 20, 14, 15, 11, 10, 71, 2, 1, 0, 'Avg', '*', 0, 'DP', 7226365], ['RB', 'Rambo', 'Haji', 30, 3, 12, 20, 13, 20, 13, 73, 6, 2, 1, 'Fighter', '**', 0, 'DP', 3460661], ['RB', 'Haji', 'Blesing', 27, 2, 12, 13, 18, 19, 16, 68, 5, 2, 0, 'Avg', '**', 0, 'DP', 3211062], ['RB', 'Peter', 'Me', 21, 1, 14, 11, 15, 10, 15, 61, 5, 1, 0, 'Avg', '*****', 0, 'DP', 5838499], ['CB', 'Robbie', 'Sean', 28, 2, 16, 13, 14, 20, 14, 73, 5, 4, 0, 'Avg', '**', 0, 'DP', 9144201], ['CB', 'Sero', 'Titch', 35, 1, 18, 14, 20, 11, 12, 68, 2, 2, 0, 'Avg', '*', 0, 'DP', 919944], ['CB', 'Ross', 'Brian', 24, 1, 14, 13, 12, 15, 18, 67, 3, 2, 0, 'Laid B', '****', 0, 'DP', 4651949], ['CB', 'Bob', 'Dylon', 18, 1, 10, 11, 19, 14, 16, 57, 4, 3, 0, 'Avg', '*****', 0, 'DP', 5424996], ['LM', 'Kim', 'Robbie', 36, 3, 14, 10, 15, 11, 16, 58, 5, 2, 0, 'Avg', '*', 0, 'DP', 1959844], ['RM', 'Titch', 'Haji', 27, 3, 10, 14, 18, 16, 16, 72, 6, 2, 1, 'Team P', '*', 0, 'DP', 1567118], ['RM', 'Blesing', 'Xavier', 19, 3, 17, 15, 11, 14, 17, 71, 4, 1, 0, 'Avg', '****', 0, 'DP', 8065792], ['RM', 'Bob', 'Blesing', 18, 3, 13, 10, 12, 14, 16, 63, 5, 4, 1, 'Fighter', '**', 0, 'DP', 4087000], ['RM', 'Zak', 'Silver', 26, 2, 11, 11, 12, 13, 14, 60, 2, 2, 1, 'Team P', '**', 0, 'DP', 2595306], ['CM', 'Haji', 'Robert', 29, 1, 19, 12, 15, 18, 17, 75, 2, 2, 0, 'Avg', '***', 0, 'DP', 5715328], ['CM', 'David', 'Robbie', 20, 1, 10, 16, 19, 14, 16, 73, 5, 1, 1, 'Team P', '***', 0, 'DP', 5923819], ['CM', 'Bo', 'Ung', 23, 1, 14, 20, 12, 19, 11, 71, 5, 2, 1, 'Leader', '***', 0, 'DP', 6908755], ['ST', 'Bruno', 'See', 36, 3, 11, 20, 19, 16, 13, 80, 6, 2, 0, 'Avg', '*', 0, 'DP', 7386474], ['ST', 'Banner', 'Titch', 24, 2, 19, 14, 16, 15, 18, 75, 6, 3, 1, 'Fighter', '****', 0, 'DP', 7491627], ['ST', 'Blesing', 'Tim', 22, 3, 14, 13, 17, 14, 13, 70, 5, 2, 0, 'Laid B', '***', 0, 'DP', 5232136], ['ST', 'See', 'Zak', 18, 3, 18, 17, 10, 14, 18, 61, 5, 1, 1, 'Fighter', '***', 0, 'DP', 7838432], ['ST', 'Piero', 'See', 37, 1, 16, 19, 11, 17, 12, 59, 6, 4, 0, 'Avg', '***', 0, 'DP', 772765]]

team_chosen=[[[['GK'], 'Sean', 'Robbie', 24, 19, 15, 12, 15, 16, 18, 88, 8, 4, 1, 'Leader', '****', 0, 'DP', 1910617], ['LB', 'Josh', 'Master', 27, 3, 20, 14, 15, 11, 10, 71, 2, 1, 0, 'Avg', '*', 0, 'DP', 7226365], ['RB', 'Rambo', 'Haji', 30, 3, 12, 20, 13, 20, 13, 73, 6, 2, 1, 'Fighter', '**', 0, 'DP', 3460661], ['CB', 'Robbie', 'Sean', 28, 2, 16, 13, 14, 20, 14, 73, 5, 4, 0, 'Avg', '**', 0, 'DP', 9144201], ['CB', 'Sero', 'Titch', 35, 1, 18, 14, 20, 11, 12, 68, 2, 2, 0, 'Avg', '*', 0, 'DP', 919944], ['CM', 'Haji', 'Robert', 29, 1, 19, 12, 15, 18, 17, 75, 2, 2, 0, 'Avg', '***', 0, 'DP', 5715328], ['CM', 'David', 'Robbie', 20, 1, 10, 16, 19, 14, 16, 73, 5, 1, 1, 'Team P', '***', 0, 'DP', 5923819], ['LM', 'Kim', 'Robbie', 36, 3, 14, 10, 15, 11, 16, 58, 5, 2, 0, 'Avg', '*', 0, 'DP', 1959844], ['RM', 'Titch', 'Haji', 27, 3, 10, 14, 18, 16, 16, 72, 6, 2, 1, 'Team P', '*', 0, 'DP', 1567118], ['ST', 'Bruno', 'See', 36, 3, 11, 20, 19, 16, 13, 80, 6, 2, 0, 'Avg', '*', 0, 'DP', 7386474], ['ST', 'Banner', 'Titch', 24, 2, 19, 14, 16, 15, 18, 75, 6, 3, 1, 'Fighter', '****', 0, 'DP', 7491627]]]





if args.verbose:
    #print("verbosity turned on")
    logging.basicConfig(level=logging.INFO)
    logging.info('Logging turned on')

def to_add():

    print ("I need to add:")
    print ("==============")
    print ("Reduce player contracts - 1 year #done")
    print ("Age + 1 year #done ")
    print ("Edit player Training Skill and remove 5 Star Recruit if over 26")
    print ("Player training +- dependant on age and Special skill & TS #done")
    print ("working on players creation to allow overall rating to be called externally (See commented out line where values are passed in rather than using self)")
    print ("work on logic at the end, need a fair way to dock/increase player skills almost like we have x points to distrubute around, then get new player overall and flag changes,also need function for max and min checks (0 and 20) , maybe any skills not maxed or 0 add to list, get random item from list and deduct x , keep going until all points taken")
    print ("==============")
    print ("renew contracts non renew player get replace by a random, wage of player reflected by overall rating")
    print ("Sell players")
    print ("Buy players?")
    input()

def main_run(my_squad,my_firstx1,season_result):

    """values for season np=no playoffs dg=divisonal game cg=championship game, w=winners"""
    to_add()
    #Age +1
    #Contract -1 
    #Improve Skills
    #Reduce Skills
    #Change Training Speed
    #Change Charasteics
    import random
    Players_improvements=[]
    Players_Reductions=[]

    import player_creation
    initaiate_player_creation=player_creation.create_player()

    #experience
    np_exp_gained_in_first_11=2
    np_exp_gained_in_squad=1
    dg_exp_gained_in_first_11=3
    dg_exp_gained_in_squad=1
    cg_exp_gained_in_first_11=4
    cg_exp_gained_in_squad=2
    w_exp_gained_in_first_11=5
    w_exp_gained_in_squad=3

    #slightly elobrate loop through squad if player is in first x1 give relevant experience if not give other experience
    for player in my_squad:
        #print(player)
        player_id=player[18]
        player_found=0
        for player_in_first11 in my_firstx1:
            try:
                if player_id==player_in_first11[18]:
                    #print("Player is in first X1")
                    player_found=1
            except Exception as e:
                print(e)
                print("Woops")
                breakpoint()
        #squad player
        if player_found==0:
            if season_result=="np":
                player[16]=np_exp_gained_in_squad
            elif season_result=="dg":
                player[16]=dg_exp_gained_in_squad
            elif season_result=="cg":
                player[16]=cg_exp_gained_in_squad
            elif season_result=="w":
                player[16]=w_exp_gained_in_squad
            else:
                print("not sure what kind of season this was")
        #frrst team player
        else:
            if season_result=="np":
                player[16]=np_exp_gained_in_first_11
            elif season_result=="dg":
                player[16]=dg_exp_gained_in_first_11
            elif season_result=="cg":
                player[16]=cg_exp_gained_in_first_11
            elif season_result=="w":
                player[16]=w_exp_gained_in_first_11
            else:
                print("not sure what kind of season this was")

        #print(player)
    print("experience applied to all players")
        #breakpoint()

    #age+1 and contract-1
    for player in my_squad:
        player_age=player[3]
        player_age+=1
        player[3]=player_age

        player_contract_length=player[13]
        player_contract_length-=1
        player[13]=player_contract_length
    print("All players have Aged +1 and had their contract -1")
   
    #training_increase & decrease
    for player_training in my_squad:
        #create player score based on age,training speed and char
        player_age_i=player_training[3]
        player_char=player_training[14]
        player_training_speed=player_training[15]
        perfect_age=25
        build_player_score=perfect_age-player_age_i
        if player_char =="Avg":
            build_player_score+=1
        elif player_char =="Leader":
            build_player_score+=3
        elif player_char =="5-Star":
            build_player_score+=7
        elif player_char =="Team P":
            build_player_score+=2
        elif player_char =="Fighter":
            build_player_score+=4
        elif player_char =="Laid B":
            build_player_score-=1
        else:
            print("pass not sure what char you are...")
            breakpoint()
        #check length but could of also done if player_training_speed="*":
        if len(player_training_speed)==1:
            build_player_score-=1
        elif len(player_training_speed)==2:
            build_player_score-=0
        elif len(player_training_speed)==3:
            build_player_score+=2
        elif len(player_training_speed)==4:
            build_player_score+=4
        elif len(player_training_speed)==5:
            build_player_score+=5
        else:
            print("pass not sure what training speed  you are...")

        #create a random number taking into account build_player_score 
        #positive score
        if build_player_score > 0:
            how_lucky_are_we_feeling_skill_change=random.randint(0,build_player_score)
        #negative score
        else:
            how_lucky_are_we_feeling_skill_change=random.randint(build_player_score,2)
        print(how_lucky_are_we_feeling_skill_change)
        player_gk_skill=player_training[4]
        player_tackle_skill=player_training[5]
        player_pass_skill=player_training[6]
        player_shoot_skill=player_training[7]
        player_fitness_skill=player_training[8]
        player_pace_skill=player_training[9]

        #determine which skill is highest
        print("before skill change")
        print(player_training)
        if player_gk_skill >= (player_tackle_skill and player_pass_skill and player_shoot_skill and player_fitness_skill and player_pace_skill):
            new_skill_level=player_training[4]+-build_player_score
            if new_skill_level < 0:
                new_skill_level =1 
            player_training[4]=new_skill_level
        else:
            new_skill_level=player_training[8]+-build_player_score
            if new_skill_level < 0:
                new_skill_level =1 
            player_training[8]=new_skill_level
        print (player_training)
        breakpoint()
    
        #get new player rating
        
        initaiate_player_creation.player_rating(self,final_player_position='GK')
        
        
            
        #print (player_training)
        #print("Score=",build_player_score)
    

    
        


    

if __name__=="__main__":

    # purporse:
    # in: 
    # return: 
    import banner
    banner.banner_status(colored_status="cs",season_num=1)
    main_run(player_squad,team_chosen[0],"np")
