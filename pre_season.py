#!/usr/bin/python3

test_squad=[[['GK'], 'Aj', 'Reize', 18, 90, 8, 1, '****', 'None', 0, ''], [['GK'], 'Rambo', 'Mander', 24, 91, 9, 4, '***', '5SR', 0, ''], [['GK'], 'Zak', 'Mayfield', 27, 90, 8, 3, '***', 'None', 0, ''], [['LB'], 'Tony', 'Mohammed', 30, 78, 1, 2, '***', 'None', 0, ''], [['CB'], 'Paul', 'Omar', 21, 88, 8, 2, '****', 'LB', 0, ''], [['LB'], 'Tim', 'Kane', 21, 71, 4, 1, '*****', 'None', 0, ''], [['RB'], 'Andrew', 'Racker', 26, 75, 6, 3, '**', 'None', 0, ''], [['RB'], 'Simon', 'Garrett', 32, 95, 15, 3, '*', 'None', 0, ''], [['CB'], 'Banele', 'Wang', 21, 95, 15, 4, '***', 'None', 0, ''], [['RB'], 'Bo', 'Garrett', 31, 91, 9, 1, '***', 'L', 0, ''], [['LB', 'RB'], 'Omar', 'Tubert', 29, 79, 1, 2, '**', 'None', 0, ''], [['CM'], 'Ung', 'Ribbenov', 33, 95, 15, 2, '*', '5SR', 0, ''], [['LM', 'CM', 'RM'], 'Aj', 'Ribbenov', 23, 91, 9, 3, '*****', '5SR', 0, ''], [['LM', 'RM'], 'David', 'Racker', 22, 85, 7, 2, '**', 'None', 0, ''], [['AM', 'DM'], 'Paul', 'Charles', 35, 87, 7, 1, '**', 'None', 0, ''], [['DM', 'CM'], 'Anchor', 'Jean', 25, 93, 12, 2, '***', 'None', 0, ''], [['DM'], 'Omar', 'Omar', 27, 88, 8, 4, '**', 'TP', 0, ''], [['CM'], 'Nsoki', 'Stimer', 21, 73, 2, 3, '****', 'LB', 0, ''], [['CM', 'LM', 'AM'], 'Samkelo', 'Mohammed', 33, 84, 7, 1, '*', 'None', 0, ''], [['LW', 'ST'], 'Omar', 'Stimer', 22, 88, 8, 4, '**', 'None', 0, ''], [['LW', 'ST'], 'David', 'Ali', 36, 82, 6, 1, '***', 'None', 0, ''], [['RW'], 'See', 'Smith', 23, 79, 4, 4, '*****', 'TP', 0, ''], [['LW'], 'Nsoki', 'Shearer', 32, 92, 9, 3, '**', 'None', 0, ''], [['RW'], 'Master', 'Charles', 35, 96, 15, 3, '*', 'L', 0, '']]

#                gk,lb,rb,cb,lm,dm,cm,rm,am,lw,st,rw]
formation_4_4_2={'GK':1,"LB":1,"RB":1,"CB":2,"DM":0}
formation_4_4_2_list_keys=list(formation_4_4_2.keys())

avaliable_formations=[formation_4_4_2]

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

def best_young_team_score():
    # oass thtough team build with under 23 where possible
    # 2ns pass under 25 
    # 3rd pass anyone else
    #if position not avaliable choose best player avaliable

    #this will loop through the avaliable formations and try and find the best young team
    global test_squad
    for i in avaliable_formations:
        #add copy squad item so i can remove and add without effecting the core list which will be used later
        # next loop through the keys and then the squad to find the player i need
        #applu filters of age and sort any players found by skill pick top x players as needed in dict, once chosen remove player from avaliable players list
        for player in test_squad:
            if player[0] == "":
                pass
            
        
            breakpoint()
    
    pass


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
