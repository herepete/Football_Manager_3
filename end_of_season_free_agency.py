#!/usr/bin/python3
print("...end of season free agency...")
input("Press enter to continue")

import player_creation

def create_free_agency():
    
    create_default_list=player_creation.create_player()

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
    breakpoint()

create_free_agency()
# i need to create a way to call create player and have 3 variables
# random (for new team) 
# draft (age 17-24) skill 60-96
# Free Agency (age 24-36) skill 70-100 
