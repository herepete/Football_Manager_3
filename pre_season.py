#!/usr/bin/python3

from operator import itemgetter
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("-v","--verbose",help="Verbose information",action="store_true")
args =parser.parse_args()

if args.verbose:
    print("verbosity turned on")
else:
    print("verbosity not turned on")



formation_4_4_2={'GK':1,"LB":1,"RB":1,"CB":2,"DM":0,"CM":2,"LM":1,"RM":1,"AM":0,"LW":0,"ST":2,"RW":0}
formation_4_4_2_just_needed={k:v for (k,v) in formation_4_4_2.items() if v > 0}
formation_4_4_2_list_keys=list(formation_4_4_2_just_needed.keys())

test_squad=[[['GK'], 'Rambo', 'Kane', 20, 16, 9, 14, 20, 14, 14, 75, 2, 1, 0, 'Avg', '****', 0, 'DP', 821920], [['GK'], 'Li', 'Mayfield', 19, 12, 5, 19, 12, 18, 17, 61, 5, 4, 1, 'Leader', '*****', 0, 'DP', 607207], [['GK'], 'Paul', 'Roberts', 27, 13, 13, 7, 18, 19, 13, 61, 2, 4, 0, 'Avg', '*', 0, 'DP', 2791431], ['LB', 'Ross', 'Kane', 25, 3, 19, 19, 9, 19, 8, 78, 4, 2, 1, 'Fighter', '**', 0, 'DP', 5449644], ['LB', 'Gibby', 'Barrett', 29, 1, 15, 13, 6, 16, 20, 73, 4, 4, 0, 'Laid B', '**', 0, 'DP', 2472907], ['RB', 'Peter', 'Del-Piero', 32, 3, 13, 17, 14, 10, 9, 60, 6, 4, 1, 'Team P', '**', 0, 'DP', 7409013], ['RB', 'TJ', 'Mohammed', 19, 1, 9, 16, 12, 10, 6, 48, 1, 4, 1, 'Team P', '*****', 0, 'DP', 5781168], ['RB', 'See', 'Mander', 35, 1, 10, 7, 17, 15, 8, 47, 6, 1, 0, 'Avg', '***', 0, 'DP', 3548257], ['RB', 'Jimbo', 'Bishop', 31, 2, 10, 5, 8, 10, 12, 44, 3, 1, 0, 'Avg', '**', 0, 'DP', 8562484], ['CB', 'Samkelo', 'Bishop', 33, 3, 17, 16, 16, 7, 17, 68, 2, 3, 0, 'Avg', '***', 0, 'DP', 4235611], ['CB', 'Bo', 'Stimer', 24, 1, 14, 16, 5, 5, 17, 58, 3, 4, 0, 'Laid B', '*****', 0, 'DP', 3200970], ['LM', 'Simon', 'Ticker', 35, 1, 5, 5, 13, 16, 18, 57, 3, 1, 0, 'Avg', '*', 0, 'DP', 8290256], ['RM', 'Aj', 'Jean', 23, 3, 18, 16, 8, 6, 16, 60, 2, 4, 0, 'Avg', '*****', 0, 'DP', 2555510], ['RM', 'Bo', 'Hassan', 21, 1, 16, 12, 20, 7, 13, 59, 5, 4, 1, 'Leader', '***', 0, 'DP', 2835505], ['RM', 'Silver', 'Tubert', 25, 2, 17, 8, 10, 10, 13, 52, 1, 1, 0, 'Avg', '***', 0, 'DP', 2012292], ['RM', 'Ross', 'Stansfield', 31, 3, 14, 12, 9, 10, 7, 48, 1, 1, 1, 'Fighter', '***', 0, 'DP', 4849940], ['CM', 'Tommie', 'Reize', 19, 1, 16, 12, 18, 10, 12, 62, 3, 4, 1, 'Team P', '**', 0, 'DP', 8865693], ['CM', 'Banele', 'Bishop', 28, 3, 6, 12, 7, 11, 17, 48, 1, 1, 0, 'Avg', '***', 0, 'DP', 622877], ['CM', 'Banele', 'Tubert', 34, 3, 9, 8, 5, 5, 8, 30, 5, 2, 0, 'Avg', '*', 0, 'DP', 7566234], ['ST', 'Omar', 'Ribbenov', 19, 3, 17, 14, 16, 18, 7, 65, 5, 2, 0, 'Avg', '*****', 0, 'DP', 836487], ['ST', 'Banele', 'Del-Piero', 35, 1, 8, 20, 10, 20, 14, 61, 2, 2, 0, 'Avg', '*', 0, 'DP', 4112503], ['ST', 'Aj', 'Del-Piero', 27, 3, 17, 6, 17, 12, 5, 58, 4, 3, 0, 'Avg', '**', 0, 'DP', 3731537], ['ST', 'Barry', 'Smith', 35, 1, 18, 20, 8, 14, 16, 54, 2, 4, 0, 'Avg', '*', 0, 'DP', 5266273], ['ST', 'TJ', 'Smith', 20, 2, 20, 20, 11, 11, 6, 49, 5, 1, 0, 'Avg', '***', 0, 'DP', 7415303]]


def best_avliable_team():
    #pop best players from the list
    #what happens if a position is not avaliable?
    # do i maybe need a copy of the list to edit rather than using Squad?
    best_team_chosen=[]
    players_found=0
    #inelligent way to loop through all poistions , once found break the loop delete the players chosen and try again for the next posistion
    while True:
        #players_found=0
        players_found=0
        ids_to_delete=[]
        #safety break
        if len(best_team_chosen) > 11:
            print("breaking for safety reasons")
            break
        #breakpoint()
        for position,num_players_needed in formation_4_4_2_just_needed.items():
            #players_found=0
            #breakpoint()
            #break out of this loop if we have all the players we need
            print("loop details",position,num_players_needed)
            if (num_players_needed == players_found) and players_found>0:
                for delete_me_id in ids_to_delete:
                    del squad[delete_me_id]
                players_found=0
                        
            for player in squad:
                player_index_position=0
                #we have all the players we need
                #breakpoint()
                if num_players_needed == players_found:
                    print ("num of players needed found")
                    break
                else:
                    if (position in player[0][0]) or (position in player[0]):
                        print("i want to add a player",position,position in player)
                        #breakpoint()
                        best_team_chosen.append(player)
                        ids_to_delete.append(player_index_position)
                        print ("Player added to team chosed=",player)
                        players_found+=1
                        break
                
                player_index_position+=1

    breakpoint()
    create_team_score(first_11)
    return()
def best_young_team():
    #look at best under 24 players and fill out the rest 
    #scoring system? age+skill+younger players get an increased score + training speed
    #then pop
    def_score=55
    att_score=55
    return(def_score,att_score)
def best_blended_team():
    #need a scoring system like age+skill
    #then pop
    def_score=65
    att_score=65
    return(def_score,att_score)
def create_team_score(first_11):
    # average fitness
    # def = GK*1.5 + DEF*4 + 50(MID) ?
    # ata = ATA*50(MID)?
    # lots of stuff
    pass



def formation_choice():
    best_avliable_team()
    best_young_team()
    best_blended_team()


def offer_choice_to_user():
    print ("Which formation do you want to choose")
    print ("Average Team age, Average Overall team rating, gk rating, def overall, mid overall, ata overall,special overall")
    print ("1) youth -28,70,65,45,80,21,5 ")
    print ("2) best -55 ")
    print ("3) balanced -55 ")
    formation_methodology="Youth"
    return (formation_methodology)



def starting_preseason(squad):
    formation_choice()
    offer_choice_to_user()
    #offer best avaliable v best young team v blend (scores)
    #give user choice
    pass

if __name__=="__main__":
    global squad
    squad=test_squad
    starting_preseason(squad=test_squad)
