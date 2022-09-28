#!/usr/bin/python3

import argparse
import collections
import os
os.system('clear')

parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="increase output verbosity")
parser.add_argument("--benchmark", help="Create lots of players, a useful command is ./player_creation.py --benchmark | awk '{print $(NF-3),$(NF-2)}' | sort | uniq | wc -l ", action="store_true")
args = parser.parse_args()
#if args.verbosity:
#	print("verbosity turned on")


squad_of_players_list=[]
avalible_poistions=["GK","LB","RB","CB","LM","RM","CM","DM","AM","ST","LW","RW"]


class print_nicer_output():

    def default_squad(self,squad_to_print):
        for k in squad_of_players_list:
            try:
                #breakpoint()
                if type(k[0])== str:
                    temp_position=(k[0])
                else:
                    temp_position=' '.join(k[0])
                print('{:<20s}{:<10s}{:>10s}{:>10s}{:>10s}'.format(temp_position,k[1],k[2],str(k[3]),str(k[4])))
            except:
                import pdb
                pdb.set_trace()

    def test_print(self):
        print('{:=<20}'.format('hello'))
        print('{:_^20}'.format('hello'))
        print('{:=>20}'.format('hello'))



class create_player():

    import random
    global squad_of_players_list

    def player_name(self):
        first_name_list=["Peter","Bob","James","Tony","Aj","Bo","Nathan","Gibby","Tim","Anchor","Jimbo","Paul","Simon","Symon","See","Silver","Titch","Rambo","Robbie","TJ"]
        last_name_list=["White","Mander","Bishop","Garrett","Winston","Mayfield","Shearer","Rooney","Tucker","Racker","Hutch","Kane","Del-Piero","Seemen","Locker","Teng","Tubert","Smith","Roberts","Curtis","Hammer"]
        random_choice_first_name=self.random.choice(first_name_list)
        random_choice_last_name=self.random.choice(last_name_list)
        self.first_name=random_choice_first_name
        self.last_name=random_choice_last_name

    def player_skill(self):
        random_skill=self.random.randint(70,96)
        self.random_skill=random_skill

    def player_age(self):
        random_age=self.random.randint(18,36)
        self.random_age=random_age


    def create_position(self):
        defender_choice_position=["LB","RB","CB"]
        midfield_choice_position=["LM","RM","CM","DM","AM"]
        attacker_choice_position=["ST","LW","RW"]
        player_selected_position=[]

        global avalible_poistions
        
        if self.play_position=="GK":
            self.final_player_position=["GK"]
        elif self.play_position=="DEF":
            random_player_poistions=self.random.randint(1,3)
            for i in range(random_player_poistions):
                random_position_selected=self.random.choice(defender_choice_position)
                player_selected_position.append(random_position_selected)
                defender_choice_position.remove(random_position_selected)
            self.final_player_position=player_selected_position
        elif self.play_position=="MID":
            random_player_poistions=self.random.randint(1,3)
            for i in range(random_player_poistions):
                random_position_selected=self.random.choice(midfield_choice_position)
                player_selected_position.append(random_position_selected)
                midfield_choice_position.remove(random_position_selected)
            self.final_player_position=player_selected_position

        else:
            #we are presuming a Sticker
            random_player_poistions=self.random.randint(1,2)
            for i in range(random_player_poistions):
                random_position_selected=self.random.choice(attacker_choice_position)
                player_selected_position.append(random_position_selected)
                attacker_choice_position.remove(random_position_selected)
            self.final_player_position=player_selected_position


    def player_creation(self,play_position):
        global squad_of_players
        self.player_name()
        self.player_skill()
        self.player_age()
        self.play_position=play_position
        self.create_position()
        try:
            temp_build=[self.final_player_position,self.first_name,self.last_name,self.random_age,self.random_skill]
            squad_of_players_list.append(temp_build)
        except:
            import pdb
            pdb.set_trace

class Squad_stats_and_feedback():
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
        #print(collections.Counter(build_squads_positions).most_common())
        #print ("Team Layout")
        #print ("       GK=3    ")
        #print ("LB=2 , CB=5 ,RB=3")
        #print ("       DM=2")
        #print ("LM=2 , CM=5 , RM=3")
        #print ("       AM=2")
        #print ("LW=2   ST=3 , RW=4")
        #print ("Highest Rated")
        #print ("       GK=81    ")
        #print ("LB=82 , CB=75 ,RB=84")
        #print ("       DM=77")
        #print ("LM=81 , CM=77 , RM=99")
        #print ("       AM=56")
        #print ("LW=73   ST=85 , RW=74")
        
    def players_per_position(self,squad_to_check):
        position_count=0
        master_position_count={}
        global avalible_poistions
        for i in avalible_poistions:
            for j in squad_to_check:
                if i in j[0]:
                    position_count+=1
            master_position_count[i] =  position_count
            #print(i, position_count)
            position_count=0
        print ("Players per position")
        print ("         GK=",master_position_count.get("GK"))
        try:
            print('LB={:<5} CB={:<5} RB={:<5}'.format((master_position_count.get("LB")),master_position_count.get("CB"),master_position_count.get("RB")))
            print('         DM= {}'.format((master_position_count.get("DM"))))
            print('LM={:<5} CM={:<5} RM={:<5}'.format((master_position_count.get("LM")),master_position_count.get("CM"),master_position_count.get("RM")))
            print('         AM {}'.format((master_position_count.get("AM"))))
            print('LW={:<5} ST={:<5} RW={:<5}'.format((master_position_count.get("LW")),master_position_count.get("ST"),master_position_count.get("RW")))

        except:
            breakpoint()


    def rating_per_position(self,squad_to_check):
        global avalible_poistions
        gk_highest_rating=0
        lb_highest_rating=0
        rb_highest_rating=0
        cb_highest_rating=0
        dm_highest_rating=0
        lm_highest_rating=0
        rm_highest_rating=0
        cm_highest_rating=0
        am_highest_rating=0
        lw_highest_rating=0
        rw_highest_rating=0
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
            if "DM" in i[0]:
                if i[4]>dm_highest_rating:
                    dm_highest_rating=i[4]
            if "LM" in i[0]:
                if i[4]>lm_highest_rating:
                    lm_highest_rating=i[4]
            if "RM" in i[0]:
                if i[4]>rm_highest_rating:
                    rm_highest_rating=i[4]
            if "CM" in i[0]:
                if i[4]>cm_highest_rating:
                    cm_highest_rating=i[4]
            if "AM" in i[0]:
                if i[4]>am_highest_rating:
                    am_highest_rating=i[4]
            if "LW" in i[0]:
                if i[4]>lw_highest_rating:
                    lw_highest_rating=i[4]
            if "RW" in i[0]:
                if i[4]>rw_highest_rating:
                    rw_highest_rating=i[4]
            if "ST" in i[0]:
                if i[4]>s_highest_rating:
                    s_highest_rating=i[4]


        print ("Highest Rated")
        print ("       GK=",gk_highest_rating)
        print ("LB={}  CB={}  RB={}".format(lb_highest_rating,cb_highest_rating,rb_highest_rating))
        print ("       DM={}".format(dm_highest_rating))
        print ("LM={}  CM={}  RM={}".format(lm_highest_rating,cm_highest_rating,rm_highest_rating))
        print ("       AM={}".format(am_highest_rating))
        print ("LW={}  ST={} RW={}".format(lw_highest_rating,s_highest_rating,rw_highest_rating))

        
        
        
        



create_default_list=create_player()

if args.benchmark:
    default_squad_GK=100
    default_squad_DEF=100
    default_squad_MID=100
    default_squad_ATA=100

else:
    #i need to sort out numbering if is say 4 GK it will create 3
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
squad_feedback_call=Squad_stats_and_feedback()
squad_feedback_call.squad_feedback(squad_to_check=squad_of_players_list)
#remove duplicates from list


squad_feedback_call.players_per_position(squad_to_check=squad_of_players_list)
squad_feedback_call.rating_per_position(squad_to_check=squad_of_players_list)
