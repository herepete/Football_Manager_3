#!/usr/bin/python3

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

