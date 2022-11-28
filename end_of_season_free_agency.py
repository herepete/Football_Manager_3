#!/usr/bin/python3
print("...end of season free agency...")
input("Press enter to continue")

import player_creation

free_agency_list=[]

def create_free_agency():
    
    create_default_list=player_creation.create_player()

    default_squad_GK=20
    default_squad_DEF=100
    default_squad_MID=100
    default_squad_ATA=100

    for j in range(1,default_squad_GK):
        rv1=create_default_list.player_creation(play_position="GK",type_of_player="Free Agency")
    for k in range(1,default_squad_DEF):
        rv2=create_default_list.player_creation(play_position="DEF",type_of_player="Free Agency")
    for k in range(1,default_squad_MID):
        rv3=create_default_list.player_creation(play_position="MID",type_of_player="Free Agency")
    for k in range(1,default_squad_ATA):
        free_agency_list=create_default_list.player_creation(play_position="ATA",type_of_player="Free Agency")
    for i in free_agency_list:
        print(i)
    return 

create_free_agency()
# i need to create a way to call create player and have 3 variables
# random (for new team) 
# draft (age 17-24) skill 60-96
# Free Agency (age 24-36) skill 70-100 
