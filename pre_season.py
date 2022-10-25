#!/usr/bin/python3

from operator import itemgetter


test_squad=[[['GK'], 'Junior', 'Mander', 25, 85, 7, 2, '**', 'TP', 0, '', 1484615], [['GK'], 'Bob', 'Shearer', 21, 80, 2, 3, '***', 'None', 0, '', 7791753], [['GK'], 'James', 'Charles', 24, 76, 4, 1, '****', 'None', 0, '', 4444531], [['CB'], 'Simon', 'Barrett', 26, 72, 6, 1, '**', 'None', 0, '', 6829857], [['LB', 'RB'], 'James', 'Zhang', 27, 81, 6, 3, '**', 'LB', 0, '', 4446501], [['CB', 'LB', 'RB'], 'Zak', 'Manning', 36, 77, 1, 4, '**', 'TP', 0, '', 4604175], [['LB'], 'Zak', 'Teng', 25, 78, 4, 4, '****', 'None', 0, '', 2624641], [['CB'], 'Bob', 'Manning', 35, 93, 12, 1, '***', 'L', 0, '', 3289916], [['LB'], 'Barry', 'Ali', 20, 91, 9, 3, '**', 'None', 0, '', 9289061], [['LB'], 'Symon', 'Teng', 27, 90, 8, 3, '**', 'None', 0, '', 8583758], [['CB'], 'Master', 'Smith', 28, 95, 15, 3, '***', 'LB', 0, '', 4158431], [['AM'], 'Me', 'Racker', 32, 89, 8, 2, '***', 'None', 0, '', 2049741], [['RM'], 'Paul', 'Roberts', 26, 82, 6, 4, '**', 'TP', 0, '', 5201992], [['CM', 'DM'], 'Silver', 'Curtis', 30, 71, 4, 2, '*', 'None', 0, '', 1916288], [['DM'], 'Tony', 'Bishop', 35, 74, 4, 3, '**', 'LB', 0, '', 699461], [['CM'], 'Paul', 'Garrett', 34, 87, 7, 1, '***', 'LB', 0, '', 401208], [['CM'], 'Nathan', 'Garrett', 18, 93, 12, 4, '****', 'None', 0, '', 8818879], [['LM'], 'Dylon', 'Tucker', 19, 83, 6, 1, '**', '5SR', 0, '', 7549736], [['DM'], 'Dylon', 'Zhang', 21, 90, 8, 1, '***', '5SR', 0, '', 2713236], [['RW'], 'Barry', 'Omar', 22, 71, 1, 3, '**', 'None', 0, '', 8199760], [['ST'], 'See', 'Hutch', 22, 86, 7, 3, '****', 'None', 0, '', 3850846], [['LW', 'RW'], 'Symon', 'Mayfield', 29, 76, 4, 2, '**', 'None', 0, '', 5050682], [['RW'], 'Li', 'Shearer', 20, 77, 1, 4, '**', 'None', 0, '', 3733897], [['RW'], 'Blesing', 'Garrett', 28, 90, 8, 2, '***', 'TP', 0, '', 5246984]]

#                gk,lb,rb,cb,lm,dm,cm,rm,am,lw,st,rw]
formation_4_4_2={'GK':1,"LB":1,"RB":1,"CB":2,"DM":0,"CM":2,"LM":1,"RM":1,"AM":0,"LW":0,"ST":2,"RW":0}
formation_4_4_2_just_needed={k:v for (k,v) in formation_4_4_2.items() if v > 0}
formation_4_4_2_list_keys=list(formation_4_4_2_just_needed.keys())


formation_4_3_3={'GK':1,"LB":1,"RB":1,"CB":2,"DM":0,"CM":3,"LM":0,"RM":0,"AM":0,"LW":0,"ST":3,"RW":0}
formation_4_3_3_just_needed={k:v for (k,v) in formation_4_3_3.items() if v > 0}
formation_4_3_3_list_keys=list(formation_4_3_3_just_needed.keys())

avaliable_formations=[formation_4_4_2,formation_4_3_3]
def formation_caculation():

    #    D         A 
    #GK =40%       3
    #D=  40%       20
    #DM= 8        4
    #M= 20        20
    #AM=4         8 
    #S=0          50
    #LM?
    #RM?
    #LW?
    #RW?
    #LB?
    #RB?

    #special:
    #strong/weak core
    #strong/weak flanks
    #inexperience side
    #side with leaders/team player/laid back
    

    pass

def best_player(squad,position,num_player):
    pass

def find_player_position_in_team(list_to_check,playerid):

    index_position=-1
    for players_to_check in list_to_check:
        index_position+=1
        if players_to_check[11]==playerid:
            return index_position
    print ("hmmm player not found based on playerid")
    breakpoint()
            

def best_young_team_score():
    global test_squad
    squad=test_squad
    team_built=[]
    team_chosen=[]
    #1b)
    squad_temp=squad.copy()

    # 1) loop through whats needed, 
    # 1b) make a copy of the squad so i can delete players when added to our starting 11
    # 2) loop through squad match what we have to step 1 i.e if i need 1 GK , create a shortlist of GK
    # 3) order shortlist by skill
    # 4) take number of players needed from shortlist and add to starting 11
    # 5) delete player from squad_temp

    #1)
    for needs in formation_4_4_2_just_needed.items():
        position_in_need=needs[0]
        num_players_needed=needs[1]
        print ("We need {} position={} ".format(num_players_needed, position_in_need))
        players_of_intrest=[]
        #2)
        for player in squad_temp:
            if position_in_need in player[0]:
                players_of_intrest.append(player)
        #3)
        get_n = itemgetter(4)
        players_of_intrest_sorted=sorted(players_of_intrest, key=get_n,reverse=True)
        if len(players_of_intrest_sorted) ==0:
            print("{} position not found".format(position_in_need))
            breakpoint()
            # need logic here
            #also need logic if say 2 strickers are needed and only 1 is found

        num_players_picked=0
        players_chosen=players_of_intrest_sorted[:num_players_needed]
        print ("Player Chosen ...",players_chosen)
        #4)
        team_chosen.append(players_of_intrest_sorted[:num_players_needed])
        #5)
        for chosen_player in players_chosen:
            index_position_of_player=find_player_position_in_team(list_to_check=squad_temp,playerid=chosen_player[11])
            del squad_temp[index_position_of_player]
            
        
def balanced_team_score():
    #aim for a 50 50 split across the team.
    #pass through team and pick 5 best players over 23, 
    #2nd pass through team and pick best players under 23 in positions still avaliable
    #3rd pass fill in gaps
    #if position not avaliable choose best player avaliable
    
    pass


def best_player_avaliable_score():
    #pass through and get best avaliable player
    #if position not avaliable choose best player avaliable
    pass


def print_table():

    print("         Best Avaliable  Best Young Team   Balanced team")
    print("         D  A             D  A               D A")
    print ("4-4-2   80 80            85 85              90 90  ")
    print ("4-4-2 A 80 80            85 85              90 90  ")
    print ("4-4-2 D 80 80            85 85              90 90  ")
    print ("4-3-3   80 80            85 85              90 90  ")



def starting_preseason(squad):

    print("...Pre-season...")
    best_young_team_score()
    balanced_team_score()
    best_player_avaliable_score()
    print_table()
    import team_rating
    season_formation=team_rating.team_formation()
    type_of_team=team_rating.best_team()
    print (season_formation)

if __name__=="__main__":
    best_young_team_score()
