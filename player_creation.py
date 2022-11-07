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
else:
    print("verbosity not turned on")


# squad_of_players_list is our squad of players
squad_of_players_list=[]
avalible_poistions=["GK","LB","RB","CB","LM","RM","CM","ST"]


class print_nicer_output():


    def default_squad(self,squad_to_print):
        print ("Position    Name                      Age  Gk   Ft   Pa   Ta  Pas  Sho Spe Ove Cost  CL    TS    SS   HI")
        for k in squad_of_players_list:
            try:
                #breakpoint()
                if type(k[0])== str:
                    temp_position=(k[0])
                else:
                    temp_position=' '.join(k[0])
                    player_name=k[1]+ " " +k[2]

                #print('{:<12s}{:<15s}{:>10s}{:>5s}{:>5s}{:>15s}{:>12s}{:>5s}{:>5s}'.format(temp_position,player_name,str(k[3]),str(k[4]),str(k[5]),str(k[6]),str(k[7]),str(k[8]),str(k[9]),str(k[10])))
                print('{:<12s}{:<18s}{:>10s}{:>5s}{:>5s}{:>5s}{:>5s}{:>5s}{:>5s}{:>5s}{:>5s}{:>5s}{:>5s}{:>5s}{:>8s}{:>6s}{:>3s}'.format(temp_position,player_name,str(k[3]),str(k[4]),str(k[5]),str(k[6]),str(k[7]),str(k[8]),str(k[9]),str(k[10]),str(k[11]),str(k[12]),str(k[13]),str(k[14]),str(k[15]),str(k[16]),str(k[17]),str(k[18])))
            except Exception as e:
                print ("Woops i errored=",e)
                breakpoint()

    def print_key(self):
        print ("========")
        print("CL=Contract Left")
        print("TS=Training Speed (1 star is poor and 5 is superb")
        print("SS=Special Skills (L=Leader,5SR=% Star Recruit,TP=Team Player,LB=Laid Back)")
        print("HI=History")
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
        random_skill=self.random.randint(3,5)
        self.random_skill_special_skill=random_skill

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
            player_special_trait="L"
        elif special_traits_random_number==8:
            player_special_trait="TP"
        elif special_traits_random_number==9:
             player_special_trait="5SR"
        elif special_traits_random_number==5:
             player_special_trait="LB"
        else:
             player_special_trait="None"
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


    def player_creation(self,play_position):
        #Where all the magic happens to create a Squad
        global squad_of_players
        self.player_name()
        #self.create_position()
        #breakpoint()
        if play_position=="GK":
            self.player_skill_gk(0)
        else:
            self.player_skill_gk(1)
        self.player_skill_pace()
        self.player_skill_fitness()
        self.player_skill_tackle()
        self.player_skill_passing()
        self.player_skill_shooting()
        self.player_skill_special_skill()
        
        self.player_age()
        self.play_position=play_position
        self.create_position()
        self.random_contract()
        self.calc_player_wage()
        self.player_training_speed()
        self.special_traits()
        self.player_id()
        self.player_experience=0
        self.player_history=""
        try:
            # X Y and Z are added for future use
            temp_build=[self.final_player_position,self.first_name,self.last_name,self.random_age,self.random_skill_gk,self.random_skill_fitness,self.random_skill_pace,self.random_skill_tackle,self.random_skill_passing,self.random_skill_shooting,self.random_skill_special_skill,15,self.player_wage,self.random_contract_year,self.random_personality,self.player_special_trait,self.player_experience,self.player_history,self.random_player_id]
            if args.verbose:
                print("Here is my temp build ... ",temp_build)
            
            squad_of_players_list.append(temp_build)
        except:
            print("oops something went wrong when creating the squad")
            breakpoint()

class Squad_stats_and_feedback():

    def cost_of_squad(self,squad_to_check):
        total_cost=0
        for cost_of_player in squad_to_check:
            temp_cost=int(cost_of_player[5])
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
            temp_skill=player[4]
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
        print ("\nPlayers per position")
        print ("         GK=",master_position_count.get("GK"))
        try:
            pass
            #print('LB={:<5} CB={:<5} RB={:<5}'.format((master_position_count.get("LB")),master_position_count.get("CB"),master_position_count.get("RB")))
            #print('LM={:<5} CM={:<5} RM={:<5}'.format((master_position_count.get("LM")),master_position_count.get("CM"),master_position_count.get("RM")))
            #print('ST={:<5}'.format(master_position_count.get("ST"))

        except:
            breakpoint()


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
                    gk_highest_rating=i[4]
            if "LB" in i[0]:
                if i[4]>lb_highest_rating:
                    lb_highest_rating=i[4]
            if "RB" in i[0]:
                if i[4]>rb_highest_rating:
                    rb_highest_rating=i[4]
            if "CB" in i[0]:
                if i[4]>cb_highest_rating:
                    cb_highest_rating=i[4]
            if "LM" in i[0]:
                if i[4]>lm_highest_rating:
                    lm_highest_rating=i[4]
            if "RM" in i[0]:
                if i[4]>rm_highest_rating:
                    rm_highest_rating=i[4]
            if "CM" in i[0]:
                if i[4]>cm_highest_rating:
                    cm_highest_rating=i[4]
            if "ST" in i[0]:
                if i[4]>s_highest_rating:
                    s_highest_rating=i[4]


        print ("\nHighest Rated")
        print ("       GK=",gk_highest_rating)
        print ("LB={}  CB={}  RB={}".format(lb_highest_rating,cb_highest_rating,rb_highest_rating))
        print ("LM={}  CM={}  RM={}".format(lm_highest_rating,cm_highest_rating,rm_highest_rating))
        print ("ST={}".format(s_highest_rating))

        
        
        
        

def core_run():

    create_default_list=create_player()

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

    nicer_output=print_nicer_output()
    nicer_output.default_squad(squad_to_print=squad_of_players_list)
    nicer_output.print_key()
    squad_feedback_call=Squad_stats_and_feedback()
    squad_feedback_call.squad_feedback(squad_to_check=squad_of_players_list)
    squad_feedback_call.cost_of_squad(squad_to_check=squad_of_players_list)
    breakpoint()
    #remove duplicates from list


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

