#!/usr/bin/python3
"""
Script to create and summarize a squad 
"""

import argparse
import os

#os.system('clear')
print ("This is what your squad looks like...")

parser = argparse.ArgumentParser()
parser.add_argument("-v","--verbose",help="Verbose information",action="store_true")
parser.add_argument("--benchmark", help="Create lots of players, a useful command is ./player_creation.py --benchmark | head -3998 | awk '{print $(NF-7),$(NF-6)}' | sort | uniq | wc -l ", action="store_true")
args = parser.parse_args()

if args.verbose:
    print("verbosity turned on")
#else:
#    print("verbosity not turned on")


# squad_of_players_list is our squad of players
squad_of_players_list=[]
avalible_poistions=["GK","LB","RB","CB","LM","RM","CM","ST"]


class print_nicer_output():


    def default_squad(self,squad_to_print):
        if args.verbose:
            print("About to print...",squad_to_print)
        print ("PST    Name                  AGE |SKILLS             |PHYSICAL|OVERAL|CONTRACT | TRAINING         | HISTORY    ")
        print ("                                 |GK   TA   PAS  SHO |FT  PA  | OVE  |COS   CL | SPE    CHA   TS  | EX HI")
        print ("================================================================================================================")
        for k in squad_of_players_list:
            try:
                #breakpoint()
                if args.verbose:
                    print ("working on...",k)
                if type(k[0])== str:
                    temp_position=(k[0])
                    player_name=k[1]+ " " +k[2]
                    if args.verbose:
                        print ("ko=",k[0])
                        print("ko zero string hit")
                else:
                    temp_position=' '.join(k[0])
                    player_name=k[1]+ " " +k[2]
                    if args.verbose:
                        print("ko zero string hit")

                #print('{:<12s}{:<15s}{:>10s}{:>5s}{:>5s}{:>15s}{:>12s}{:>5s}{:>5s}'.format(temp_position,player_name,str(k[3]),str(k[4]),str(k[5]),str(k[6]),str(k[7]),str(k[8]),str(k[9]),str(k[10])))
                print('{:<6s}{:<18s}{:>7s}  |{:>2s}{:>5s}{:>5s}{:>5s}  |{:>2s}  {:>2s}  |{:>4s}  |{:>2s}{:>5s}  |{:>3s}{:>8s}{:>6s} |{:>3s}{:>3s}'.format(temp_position,player_name,str(k[3]),str(k[4]),str(k[5]),str(k[6]),str(k[7]),str(k[8]),str(k[9]),str(k[10]),str(k[11]),str(k[12]),str(k[13]),str(k[14]),str(k[15]),str(k[16]),str(k[17]),str(k[18])))
                #breakpoint()
            except Exception as e:
                print ("Woops i errored=",e)
                breakpoint()

    def print_key(self):
        print ("========")
        print("PST=Position")
        print("SKILLS   - GK=GoalKeeper Skills,TA=Tackling,PAS=Passing,SHO=Shooting")
        print("PHYSICAL - FT=Fitness,PA=Pace")
        print("OVERAL   - OVE=Overall")
        print("CONTRACT - COS=Cost per season,CL=Contract")
        print("TRAINING - SPE=Special attributes (Experience+CHA), CHA=Special Skills (L=Leader,5SR=% Star Recruit,TP=Team Player,LB=Laid Back,Avg=Average Player), TS=Training Speed")
        print("HISTORY  - EX=Experience,HI=History(DP=Default Player)")
        print ("========")
        

            


class create_player():

    global squad_of_players_list
    import random

    def player_name(self):
        # create a random first and last name
        first_name_list=["Peter","Bob","James","Tony","Aj","Bo","Nathan","Gibby","Tim","Anchor","Jimbo","Paul","Simon","Symon","See","Silver","Titch","Rambo","Robbie","TJ","David","John","Michael","Paul","Andrew","David","Sero","Ian","Brian","Barry","Li","Omar","Junior","Blesing","Banele","Samkelo","Ross","Dylon","Master","Junior","Ung","Me","Nsoki","Zak","Banner","Tommie"]
        last_name_list=["White","Mander","Bishop","Garrett","Winston","Mayfield","Shearer","Rooney","Tucker","Racker","Hutch","Kane","Del-Piero","Seemen","Locker","Teng","Tubert","Smith","Roberts","Curtis","Hammer","Wang","Chen","Smith","Zhang","Costa","Ribbenov","Stimer","Reize","Lemon","Jean","Mohammed","Ticker","Barrett","Manning","Rogan","Musk","Turing","Ali","Fatima","Hassan","Charles","Omar","Stansfield"]
        random_choice_first_name=self.random.choice(first_name_list)
        random_choice_last_name=self.random.choice(last_name_list)
        self.first_name=random_choice_first_name
        self.last_name=random_choice_last_name
        if args.verbose:
            print("new player name created=",self.last_name)


    def random_contract(self):
        random_contract_year=self.random.randint(1,4)
        self.random_contract_year=random_contract_year


    def player_skill_gk(self,out_of_position=0):
        #give a random skill
        if out_of_position==0:
            random_skill=self.random.randint(10,20)
            self.random_skill_gk=random_skill
        else:
            random_skill=self.random.randint(1,3)
            self.random_skill_gk=random_skill

    def player_skill_fitness(self):
        random_skill=self.random.randint(5,20)
        self.random_skill_fitness=random_skill
    def player_skill_pace(self):
        random_skill=self.random.randint(5,20)
        self.random_skill_pace=random_skill
    def player_skill_tackle(self):
        random_skill=self.random.randint(5,20)
        self.random_skill_tackle=random_skill
    def player_skill_passing(self):
        random_skill=self.random.randint(5,20)
        self.random_skill_passing=random_skill
    def player_skill_shooting(self):
        random_skill=self.random.randint(5,20)
        self.random_skill_shooting=random_skill
    def player_skill_special_skill(self):
        # default to 0
        # + 1 fir various skill types
        # if expereince is over 5 any extra year = + 1
        # maximum of 5
        temp_count=0
        if ("Fighter") in self.player_special_trait:
            temp_count+=1
        if ("Leader") in self.player_special_trait:
            temp_count+=1
        if ("Team P") in self.player_special_trait:
            temp_count+=1
            #print(self.player_special_trait)
            #breakpoint()
        if self.player_experience_level >5:
            temp_count=temp_count+ (self.player_experience_level % 5)
        if temp_count > 5:
            temp_count=5
        self.random_skill_special_skill=temp_count

    def player_age(self):
        #guve a random age
        random_age=self.random.randint(18,36)
        self.random_age=random_age

    def player_training_speed(self):
        if self.random_age > 25:
            random_player_personality=["***","**","*"]
        else:
            random_player_personality=["*****","****","***","**"]
        random_personality_choice=self.random.choice(random_player_personality)
        
        self.random_personality=random_personality_choice

    def special_traits(self):
        special_traits_random_number=self.random.randint(1,10)
        if special_traits_random_number==7:
            #Leader
            player_special_trait="Leader"
        elif special_traits_random_number==8:
            #Team Player
            player_special_trait="Team P"
        elif special_traits_random_number==9:
            if self.random_age < 24:
            #% star recurit (high potential)
                 player_special_trait="5-Star"
            else:
                 player_special_trait="Avg"
        elif special_traits_random_number==5:
             #laid back
             player_special_trait="Laid B"
        elif special_traits_random_number==4:
             player_special_trait="Fighter"
        else:
             player_special_trait="Avg"
        self.player_special_trait=player_special_trait
                

    def calc_player_wage(self):
        #15 highest
        #basic .600K
        #if self.random_skill > 94:
        #    player_wage=15
        #elif self.random_skill > 92:
        #    player_wage=12
        #elif self.random_skill > 92:
        #    player_wage=10
        #elif self.random_skill > 90:
        #    player_wage=9
        #elif self.random_skill > 87:
        #    player_wage=8
        #elif self.random_skill > 83:
        #    player_wage=7
        #elif self.random_skill > 80:
        #    player_wage=6
        #else:
        #    import random
        #    player_wage=random.randint(1,6)
        import random
        player_wage=random.randint(1,6)
        
        self.player_wage=player_wage
        
    def create_position(self):
        #give a random position (some players get more than 1 position)
        defender_choice_position=["LB","RB","CB"]
        midfield_choice_position=["LM","RM","CM"]
        attacker_choice_position=["ST"]
        player_selected_position=[]
        import random

        global avalible_poistions
        
        if self.play_position=="GK":
            self.final_player_position=["GK"]
        elif self.play_position=="DEF":
            #determine how many position a player can play, the choices are weighted to make player in 3 positions quite rare
            #random_player_poistions=self.random.randint(1,3)
            self.final_player_position=random.choice(defender_choice_position)
        elif self.play_position=="MID":
            self.final_player_position=random.choice(midfield_choice_position)

        else:
            #we are presuming a Sticker
            #determine how many position a player can play,  the choices are weighted to make player in 3 positions quite rare
            #random_player_poistions=self.random.choices([1,2], weights=(70, 30,), k=1)
            self.final_player_position="ST"


    def player_id(self):
        import random
        self.random_player_id=random.randint (1,9999999)
        #return random_player_id

    def player_experience(self,default):
        if default=="1":
            self.player_experience_level=0
        else:
            #not expecting this to hit but includding for future use
            self.player_experience_level=10


    def player_rating(self):
        #work out score out of 100 and then /5 to give 
        if self.final_player_position[0]=="GK":
            # so 85% gk skill, and 
            # 5% from fitness,passing and special skill
            self.overall_score=int((self.random_skill_gk/20)*85+(self.random_skill_fitness/20)*5+(self.random_skill_passing/20)*5+ (self.random_skill_special_skill)    )
        elif self.final_player_position=="LB" or self.final_player_position=="RB":
            # so 37% from Tacking
            # 20 from Pace and Passing
            # 15 from Fitness
            # 5 from Special skill
            # 3 from Shooting
            self.overall_score=int((self.random_skill_tackle/20)*37+(self.random_skill_fitness/20)*15+(self.random_skill_passing/20)*20+(self.random_skill_pace/20)*20 + (self.random_skill_special_skill)+(self.random_skill_shooting/20)*3)
        elif self.final_player_position=="CB":
            # so 40% from Tacking
            # 18 from Fitness and Pace
            # 13 from Passing
            # 8 from Special skill
            # 3 from Shooting
            self.overall_score=int((self.random_skill_tackle/20)*40+(self.random_skill_fitness/20)*18+(self.random_skill_passing/20)*13+(self.random_skill_pace/20)*18 + (self.random_skill_special_skill/5)*8+(self.random_skill_shooting/20)*3)
        elif self.final_player_position=="LM" or self.final_player_position=="RM":
            # 25 from Fitness,passing and Pace
            # 10 Tacking and Shooting
            # 5 from Special skill
            self.overall_score=int((self.random_skill_tackle/20)*10+(self.random_skill_fitness/20)*25+(self.random_skill_passing/20)*25+(self.random_skill_pace/20)*25 + (self.random_skill_special_skill)+(self.random_skill_shooting/20)*10)
        elif self.final_player_position=="CM":
            # 21 from Fitness 
            # 18 Pace,Passing,Shooting
            # 15 Tackling
            # 10 from Special skill
            self.overall_score=int((self.random_skill_tackle/20)*15+(self.random_skill_fitness/20)*21+(self.random_skill_passing/20)*18+(self.random_skill_pace/20)*18 + (self.random_skill_special_skill/5)*10+(self.random_skill_shooting/20)*18)
        elif self.final_player_position=="ST":
            # 50 from Shooting
            # 19 Pace
            # 14 Fitness
            # 9 Passing
            # 8 from Special skill
            self.overall_score=int((self.random_skill_fitness/20)*14+(self.random_skill_passing/20)*9+(self.random_skill_pace/20)*19 + (self.random_skill_special_skill/5)*8+(self.random_skill_shooting/20)*50)
        else:
            print ("Unexpected player position=",self.final_player_position)
            breakpoint()
        


    def player_creation(self,play_position):
        #Where all the magic happens to create a Squad
        # the order is quite important here as variables are reliant on previous functions
        global squad_of_players
        self.player_name()
        if play_position=="GK":
            self.player_skill_gk(0)
        else:
            self.player_skill_gk(1)
        self.player_skill_pace()
        self.player_skill_fitness()
        self.player_skill_tackle()
        self.player_skill_passing()
        self.player_skill_shooting()
        #self.player_skill_special_skill()
        
        self.player_age()
        self.play_position=play_position
        self.create_position()
        self.random_contract()
        self.calc_player_wage()
        self.player_training_speed()
        self.special_traits()
        self.player_id()
        self.player_experience("1")
        self.player_history="DP"
        self.player_skill_special_skill()
        self.player_rating()
        try:
            # X Y and Z are added for future use
            #temp_build=[self.final_player_position,self.first_name,self.last_name,self.random_age,self.random_skill_gk,self.random_skill_fitness,self.random_skill_pace,self.random_skill_tackle,self.random_skill_passing,self.random_skill_shooting,self.random_skill_special_skill,self.overall_score,self.player_wage,self.random_contract_year,self.random_personality,self.player_special_trait,self.player_experience_level,self.player_history,self.random_player_id]
            temp_build=[self.final_player_position,self.first_name,self.last_name,self.random_age,self.random_skill_gk,self.random_skill_tackle,self.random_skill_passing,self.random_skill_shooting,self.random_skill_fitness,self.random_skill_pace,self.overall_score,self.player_wage,self.random_contract_year,self.random_skill_special_skill,self.player_special_trait,self.random_personality,self.player_experience_level,self.player_history,self.random_player_id]
            if args.verbose:
                print("Here is my temp build ... ",temp_build)
                print ("...Here is the breakdown of each variable...")
                print ("self.final_player_position=",self.final_player_position)
                print ("self.first_name=",self.first_name)
                print ("self.last_name=",self.last_name)
                print ("self.random_age=",self.random_age)
                print ("self.random_skill_gk=",self.random_skill_gk)
                print ("self.random_skill_tackle=",self.random_skill_tackle)
                print ("self.random_skill_passing=",self.random_skill_passing)
                print ("self.random_skill_shooting=",self.random_skill_shooting)
                print ("self.random_skill_fitness=",self.random_skill_fitness)
                print ("self.random_skill_pace=",self.random_skill_pace)
                print ("self.overall_score=",self.overall_score)
                print ("self.player_wage=",self.player_wage)
                print ("self.random_contract_year=",self.random_contract_year)
                print ("self.random_skill_special_skill=",self.random_skill_special_skill)
                print ("self.player_special_trait=",self.player_special_trait)
                print ("self.random_personality=",self.random_personality)
                print ("self.player_experience_level=",self.player_experience_level)
                print ("self.player_history=",self.player_history)
                print ("self.random_player_id=",self.random_player_id)
            
            squad_of_players_list.append(temp_build)
        except Exception as e:
            print("oops something went wrong when creating the squad")
            print ("Error reads=",e)
            breakpoint()

class Squad_stats_and_feedback():

    def cost_of_squad(self,squad_to_check):
        total_cost=0
        for cost_of_player in squad_to_check:
            temp_cost=int(cost_of_player[11])
            total_cost+=temp_cost
        print ("Total Squad Wages=",total_cost)

    def squad_feedback(self,squad_to_check):
        total_age=0
        total_skill=0
        global avalible_poistions
        build_squads_positions=[]
        #type_of_player=["GK","LB","RB","CB","LM","RM","CM","Def M","Ata M","ST","W"]

        for player in squad_to_check:
            temp_age=player[3]
            temp_skill=player[10]
            total_age+=temp_age
            total_skill+=temp_skill
            temp_position=player[0]
            #number of players in each position
            #breakpoint()
            for player_position in temp_position:
                build_squads_positions.append(player_position)

        average_age= total_age//len(squad_to_check)
        average_skill= total_skill//len(squad_to_check)
        print ("Average age of squad is...",average_age)
        print ("Average skill of squad is...",average_skill)
        
    def players_per_position(self,squad_to_check):
        position_count=0
        master_position_count={}
        global avalible_poistions
        for i in avalible_poistions:
            for j in squad_to_check:
                if i in j[0]:
                    position_count+=1
            master_position_count[i] =  position_count
            position_count=0
        print("=======Players per position")
        print ("         GK=",master_position_count.get("GK"))
        try:
            #pass
            print('LB={:<5} CB={:<5} RB={:<5}'.format((master_position_count.get("LB")),master_position_count.get("CB"),master_position_count.get("RB")))
            print('LM={:<5} CM={:<5} RM={:<5}'.format((master_position_count.get("LM")),master_position_count.get("CM"),master_position_count.get("RM")))
            print('         ST={:<5}'.format((master_position_count.get("ST"))))

        except:
            breakpoint()


    def char_of_team(self,squad_to_check):
        avg_players=0
        team_p_players=0
        leader_players=0
        fighter_player=0
        five_star_player=0
        laid_b_players=0
        for player in squad_to_check:
            if player[14] == "Team P":
                team_p_players+=1
            elif player[14] == "Avg":
                avg_players+=1
            elif player[14] == "Fighter":
                fighter_player+=1
            elif player[14] == "Leader":
                leader_players+=1
            elif player[14] == "5-Star":
                five_star_player+=1
            elif player[14] == "Laid B":
                laid_b_players+=1
            else:
                print ("Whops odd char found")
                breakpoint()
        print("=======Charcteur of team...")
        print ("Avg Players=",avg_players)
        print ("Team Players=",team_p_players)
        print ("Leaders=",leader_players)
        print ("Fighters=",fighter_player)
        print ("5 Star Recruits=",five_star_player)
        print ("Laid back players=",laid_b_players)
            

            


    def rating_per_position(self,squad_to_check):
        global avalible_poistions
        gk_highest_rating=0
        lb_highest_rating=0
        rb_highest_rating=0
        cb_highest_rating=0
        lm_highest_rating=0
        rm_highest_rating=0
        cm_highest_rating=0
        s_highest_rating=0
        for i in squad_to_check:
            if "GK" in i[0]:
                if i[4]>gk_highest_rating:
                    gk_highest_rating=i[10]
            elif "LB" in i[0]:
                if i[4]>lb_highest_rating:
                    lb_highest_rating=i[10]
            elif "RB" in i[0]:
                if i[4]>rb_highest_rating:
                    rb_highest_rating=i[10]
            elif "CB" in i[0]:
                if i[4]>cb_highest_rating:
                    cb_highest_rating=i[10]
            elif "LM" in i[0]:
                if i[4]>lm_highest_rating:
                    lm_highest_rating=i[10]
            elif "RM" in i[0]:
                if i[4]>rm_highest_rating:
                    rm_highest_rating=i[10]
            elif "CM" in i[0]:
                if i[4]>cm_highest_rating:
                    cm_highest_rating=i[10]
            elif "ST" in i[0]:
                if i[4]>s_highest_rating:
                    s_highest_rating=i[10]
            else:
                print("who are you?")
                breakpoint()


        #print("=======")
        print ("======Highest Rated")
        print ("       GK=",gk_highest_rating)
        print ("LB={}  CB={}  RB={}".format(lb_highest_rating,cb_highest_rating,rb_highest_rating))
        print ("LM={}  CM={}  RM={}".format(lm_highest_rating,cm_highest_rating,rm_highest_rating))
        print ("       ST={}".format(s_highest_rating))

        
    def sort_squad(self): 
        global squad_of_players_list
        #group players by position (first into indvidual list and then combine them later on)
        incoming_squad_in=squad_of_players_list
        gk_list=[]
        dl_list=[]
        dr_list=[]
        cb_list=[]
        lm_list=[]
        rm_list=[]
        cm_list=[]
        st_list=[]
        rebuilt_team=[]
        for player in incoming_squad_in:
            if player[0][0]=="GK":
                gk_list.append(player)
            elif player[0]=="LB":
                dl_list.append(player)
            elif player[0]=="RB":
                dr_list.append(player)
            elif player[0]=="CB":
                cb_list.append(player)
            elif player[0]=="LM":
                lm_list.append(player)
            elif player[0]=="RM":
                rm_list.append(player)
            elif player[0]=="CM":
                cm_list.append(player)
            elif player[0]=="ST":
                st_list.append(player)
            else:
                print("odd position input 2")
                print (player)
                breakpoint()

        #sort by players overall rating 
        gk_list=sorted(gk_list, key=lambda x: x[10],reverse=True)
        dl_list=sorted(dl_list, key=lambda x: x[10],reverse=True)
        dr_list=sorted(dr_list, key=lambda x: x[10],reverse=True)
        cb_list=sorted(cb_list, key=lambda x: x[10],reverse=True)
        lm_list=sorted(lm_list, key=lambda x: x[10],reverse=True)
        rm_list=sorted(rm_list, key=lambda x: x[10],reverse=True)
        cm_list=sorted(cm_list, key=lambda x: x[10],reverse=True)
        st_list=sorted(st_list, key=lambda x: x[10],reverse=True)
    
        #rebuilt list after being sorted by position and overall value
        for player_gk in (gk_list):
            rebuilt_team.append(player_gk)
        for player_dl in (dl_list):
            rebuilt_team.append(player_dl)
        for player_dr in (dr_list):
            rebuilt_team.append(player_dr)
        for player_cb in (cb_list):
            rebuilt_team.append(player_cb)
        for player_lm in (lm_list):
            rebuilt_team.append(player_lm)
        for player_rm in (rm_list):
            rebuilt_team.append(player_rm)
        for player_cm in (cm_list):
            rebuilt_team.append(player_cm)
        for player_st in (st_list):
            rebuilt_team.append(player_st)
        #overwrite our global varliable with our newley ordered squad 
        squad_of_players_list=rebuilt_team
        
        

def core_run():

    create_default_list=create_player()
    squad_feedback_call=Squad_stats_and_feedback()

    default_squad_GK=4
    default_squad_DEF=9
    default_squad_MID=9
    default_squad_ATA=6

    for j in range(1,default_squad_GK):
        create_default_list.player_creation(play_position="GK")
    for k in range(1,default_squad_DEF):
        create_default_list.player_creation(play_position="DEF")
    for k in range(1,default_squad_MID):
        create_default_list.player_creation(play_position="MID")
    for k in range(1,default_squad_ATA):
        create_default_list.player_creation(play_position="ATA")

    squad_feedback_call.sort_squad()
    nicer_output=print_nicer_output()
    nicer_output.default_squad(squad_to_print=squad_of_players_list)
    nicer_output.print_key()
    #reoder the squad to make it more readable
    #squad_feedback_call.sort_squad()
    squad_feedback_call.squad_feedback(squad_to_check=squad_of_players_list)
    squad_feedback_call.cost_of_squad(squad_to_check=squad_of_players_list)
    squad_feedback_call.char_of_team(squad_of_players_list)
    squad_feedback_call.players_per_position(squad_to_check=squad_of_players_list)
    squad_feedback_call.rating_per_position(squad_to_check=squad_of_players_list)
    return (squad_of_players_list)

if __name__ == "__main__":
    core_run()
    if args.benchmark:
        default_squad_GK=1000
        default_squad_DEF=1000
        default_squad_MID=1000
        default_squad_ATA=1000
