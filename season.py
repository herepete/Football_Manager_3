#!/usr/bin/python3.7
opposition_teams=["Arsenal","Man City","Tottenham","Chelsea","Man United","Newcastle","Brighton","Bournemouth","Fulham","Liverpool","Brentford","Everton","West Ham","Leeds United","Crystal Palace","Aston Villa","Southampton","Wolves","Nottm Forest","Leicester City"]
#print (opposition_teams)
games_in_season=16


def main_run(team_stats_chosen_in):
    #format of input
    #gk_score,def_score,ata_score,fitness_score,special_score)
    #team_stats_chosen_in = [[88, 64, 61, 11, 2]]

    our_gk=team_stats_chosen_in[0][0]
    our_def=team_stats_chosen_in[0][1]
    our_ata=team_stats_chosen_in[0][2]
    our_fit=team_stats_chosen_in[0][3]
    our_special_score=team_stats_chosen_in[0][4]

    import random

    games_won=0
    games_drawen=0
    games_lost=0

    for i in opposition_teams:
        opposition_gk=random.randint(80,100)
        opposition_def=random.randint(80,100)
        opposition_att=random.randint(80,100)
        opposition_fitness=random.randint(1,20)
        opposition_special=random.randint(1,15)
        # extra differences
        difference_fitness=our_fit-opposition_fitness
        difference_special_score=our_special_score-opposition_special


        #print (f"our def={our_def} our att={our_ata} opp def={opposition_def} opp ata={opposition_att}")
        #shots us
        difference_our_att_opp_def=(our_ata-opposition_def)/10
        #setting a minumum number of shots
        if difference_our_att_opp_def <3:
            difference_our_att_opp_def=3    
        # shots on target us
        difference_our_att_opp_gk=((our_ata-opposition_gk)+difference_fitness+difference_special_score)/3

        #shots opposition
        difference_opp_ata_our_def=(opposition_att-our_def)/10
        #setting a minimum number of shots
        if difference_opp_ata_our_def <3:
            difference_opp_ata_our_def=3
        # shots on target opp
        difference_opp_att_our_gk=((opposition_att-our_gk)+difference_fitness+difference_special_score)/3

        #setting minumum number of shots on target us 
        if difference_our_att_opp_gk < 1:
            difference_our_att_opp_gk=1

        #setting minumum number of shots on target opp
        if difference_opp_att_our_gk < 1:
            difference_opp_att_our_gk=1
        


        

         
        #goals
        try:
            my_goals=random.randint(0,int(difference_our_att_opp_gk))
            opp_goals=random.randint(0,int(difference_opp_att_our_gk))
        except:
            print("wooops goals error")
            breakpoint()
    
        print ("Game " + i +" Score " + str(my_goals) +  " - " + str(opp_goals))
        if my_goals >  opp_goals:
            games_won+=1
        elif opp_goals > my_goals:
            games_lost+=1
        else:
            games_drawen+=1

    print ("Season record")
    print ("W D L")
    print (games_won,games_drawen,games_lost)

    playof_needed=0
    straight_to_championship_game=0
    out_of_playoff=0
    play_off_won=0
    no_playoff=0

    if games_won < 10:
        print ("Season Result - Not good enough try again next season")
        no_playoff=1
    elif games_won < 12:
        playof_needed=1
        play_off_won=0
        straight_to_championship_game=0
        out_of_playoff=0
        print ("Play off needed")
    else:
        playof_needed=0
        straight_to_championship_game=2
        out_of_playoff=0
        #champtionship game
        print ("Straight to Championship game nice")

    while True:

        if out_of_playoff==1 or no_playoff:
            print("Un lucky try again next season")
            input("Press enter to continue")
            break
        if playof_needed==1:
            print("yeh you won")
            playof_needed=0
            play_off_won=1
            input("Press enter to continue")
        if straight_to_championship_game or play_off_won:
            print ("Season Result - You won everything nice")
            input("Press enter to continue")
            break
    


