#!/usr/bin/python3

from operator import itemgetter
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("-v","--verbose",help="Verbose information",action="store_true")
args =parser.parse_args()

import logging
#logging.basicConfig(level=logging.INFO)
#logging.debug('Debug alert')
#logging.info('Info alert')
#logging.warning('Warning alert')
#logging.error('Error alert')
#logging.critical('Critical alert')


if args.verbose:
    #print("verbosity turned on")
    logging.basicConfig(level=logging.INFO)
    logging.info('Logging turned on')
else:
    #print("verbosity not turned on")
    pass



formation_4_4_2={'GK':1,"LB":1,"RB":1,"CB":2,"DM":0,"CM":2,"LM":1,"RM":1,"AM":0,"LW":0,"ST":2,"RW":0}
formation_4_4_2_just_needed={k:v for (k,v) in formation_4_4_2.items() if v > 0}
formation_4_4_2_list_keys=list(formation_4_4_2_just_needed.keys())

test_squad=[[['GK'], 'Rambo', 'Kane', 20, 16, 9, 14, 20, 14, 14, 75, 2, 1, 0, 'Avg', '****', 0, 'DP', 821920], [['GK'], 'Li', 'Mayfield', 19, 12, 5, 19, 12, 18, 17, 61, 5, 4, 1, 'Leader', '*****', 0, 'DP', 607207], [['GK'], 'Paul', 'Roberts', 27, 13, 13, 7, 18, 19, 13, 61, 2, 4, 0, 'Avg', '*', 0, 'DP', 2791431], ['LB', 'Ross', 'Kane', 25, 3, 19, 19, 9, 19, 8, 78, 4, 2, 1, 'Fighter', '**', 0, 'DP', 5449644], ['LB', 'Gibby', 'Barrett', 29, 1, 15, 13, 6, 16, 20, 73, 4, 4, 0, 'Laid B', '**', 0, 'DP', 2472907], ['RB', 'Peter', 'Del-Piero', 32, 3, 13, 17, 14, 10, 9, 60, 6, 4, 1, 'Team P', '**', 0, 'DP', 7409013], ['RB', 'TJ', 'Mohammed', 19, 1, 9, 16, 12, 10, 6, 48, 1, 4, 1, 'Team P', '*****', 0, 'DP', 5781168], ['RB', 'See', 'Mander', 35, 1, 10, 7, 17, 15, 8, 47, 6, 1, 0, 'Avg', '***', 0, 'DP', 3548257], ['RB', 'Jimbo', 'Bishop', 31, 2, 10, 5, 8, 10, 12, 44, 3, 1, 0, 'Avg', '**', 0, 'DP', 8562484], ['CB', 'Samkelo', 'Bishop', 33, 3, 17, 16, 16, 7, 17, 68, 2, 3, 0, 'Avg', '***', 0, 'DP', 4235611], ['CB', 'Bo', 'Stimer', 24, 1, 14, 16, 5, 5, 17, 58, 3, 4, 0, 'Laid B', '*****', 0, 'DP', 3200970], ['LM', 'Simon', 'Ticker', 35, 1, 5, 5, 13, 16, 18, 57, 3, 1, 0, 'Avg', '*', 0, 'DP', 8290256], ['RM', 'Aj', 'Jean', 23, 3, 18, 16, 8, 6, 16, 60, 2, 4, 0, 'Avg', '*****', 0, 'DP', 2555510], ['RM', 'Bo', 'Hassan', 21, 1, 16, 12, 20, 7, 13, 59, 5, 4, 1, 'Leader', '***', 0, 'DP', 2835505], ['RM', 'Silver', 'Tubert', 25, 2, 17, 8, 10, 10, 13, 52, 1, 1, 0, 'Avg', '***', 0, 'DP', 2012292], ['RM', 'Ross', 'Stansfield', 31, 3, 14, 12, 9, 10, 7, 48, 1, 1, 1, 'Fighter', '***', 0, 'DP', 4849940], ['CM', 'Tommie', 'Reize', 19, 1, 16, 12, 18, 10, 12, 62, 3, 4, 1, 'Team P', '**', 0, 'DP', 8865693], ['CM', 'Banele', 'Bishop', 28, 3, 6, 12, 7, 11, 17, 48, 1, 1, 0, 'Avg', '***', 0, 'DP', 622877], ['CM', 'Banele', 'Tubert', 34, 3, 9, 8, 5, 5, 8, 30, 5, 2, 0, 'Avg', '*', 0, 'DP', 7566234], ['ST', 'Omar', 'Ribbenov', 19, 3, 17, 14, 16, 18, 7, 65, 5, 2, 0, 'Avg', '*****', 0, 'DP', 836487], ['ST', 'Banele', 'Del-Piero', 35, 1, 8, 20, 10, 20, 14, 61, 2, 2, 0, 'Avg', '*', 0, 'DP', 4112503], ['ST', 'Aj', 'Del-Piero', 27, 3, 17, 6, 17, 12, 5, 58, 4, 3, 0, 'Avg', '**', 0, 'DP', 3731537], ['ST', 'Barry', 'Smith', 35, 1, 18, 20, 8, 14, 16, 54, 2, 4, 0, 'Avg', '*', 0, 'DP', 5266273], ['ST', 'TJ', 'Smith', 20, 2, 20, 20, 11, 11, 6, 49, 5, 1, 0, 'Avg', '***', 0, 'DP', 7415303]]


def best_avliable_team(localsquad):
    best_team_chosen=[]
    players_found=0
    #loop until i have built a team
    while True:
        ids_to_delete=[]
        if len(best_team_chosen)== 11:
            break
        for position,num_players_needed in formation_4_4_2_just_needed.items():
            players_found=0
            logging.info('Loop details %s %s',position,num_players_needed)
            #break out of this loop if we have all the players we need
            if len(best_team_chosen) ==11:
                break
            #if we have found the players we need delete from the list
            if (num_players_needed == players_found) and players_found>0:
                for delete_me_id in ids_to_delete:
                    del localsquad[delete_me_id]
                players_found=0
            
            #loop through each player
            for player in localsquad:
                player_index_position=0
                #we have all the players we need
                if num_players_needed == players_found:
                    logging.info('num of players needed found')
                    break
                else:
                    #if player fits posistion
                    if (position in player[0][0]) or (position in player[0]):
                        logging.info('i want to add a player %s %s ',position,player)
                        #breakpoint()
                        best_team_chosen.append(player)
                        ids_to_delete.append(player_index_position)
                        logging.info('Players added to team chosen %s ',player)
                        players_found+=1
                        #breakpoint()
                        #logging.info('4 Player Found variable =%s',players_found)
                
                player_index_position+=1
    #get team score
    local_def_score,local_ata_score=create_team_score(first_11=best_team_chosen)
    return(local_def_score,local_ata_score)
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
    gk_score=0
    def_score=0
    ata_score=0
    fitness_score=0
    special_score=0

    for player in first_11:
        print(player)
        if "GK" in player[0]:
            gk_score+=player[10]
            fitness_score+=player[8]
            special_score+=player[13]
        elif ("LB" in player[0]) or ("RB" in player[0]) or ("CB" in player[0]) :
            def_score+=player[10]
            fitness_score+=player[8]
            special_score+=player[13]
        elif ("LM" in player[0]) or ("RM" in player[0]) or ("CM" in player[0]) :
            def_score+=player[10]
            ata_score+=player[10]
            fitness_score+=player[8]
            special_score+=player[13]
        elif ("ST" in player[0]):
            ata_score+=player[10]
            fitness_score+=player[8]
            special_score+=player[13]
        else:
            print("unexpected player found while trying to score team...")
            breakpoint()
    def_score=int((def_score/8))
    ata_score=int((ata_score/6))
    fitness_score=int((fitness_score/11))
    print ("temp team score")
    print ("gk_score=",gk_score)
    print ("def_score=",def_score)
    print ("ata_score=",ata_score)
    print ("fitness_score=",fitness_score)
    print ("special_score=",special_score)
    
    
    breakpoint()
        
    return(110,109)


def formation_choice():
    best_avliable_team(squad)
    best_young_team()
    best_blended_team()
    offer_choice_to_user()


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
    #offer best avaliable v best young team v blend (scores)
    #give user choice
    pass

if __name__=="__main__":
    global squad
    squad=test_squad
    for i in squad:
        print(i)
    starting_preseason(squad=test_squad)
