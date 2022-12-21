#!/usr/bin/python3

#can be changed
Total_Wage_Limit = 200
time_out_between_games=0.1

#at the moemnt only min values are used during testing but i expect a random number to be created beween min and max
free_agency_gk_min =2
free_agency_d_min =2
free_agency_m_min =2
free_agency_a_min =2

free_agency_gk_max =4
free_agency_d_max =4
free_agency_m_max =4
free_agency_a_max =4

start_thinking_about_retirement_age=36

Start_up_parameters = {
    "age_min": "17",
    "age_max": "37",
    "skill_min": "10",
    "skill_max": "20",
}
Free_Agency_parameters = {
    "age_min": "24",
    "age_max": "37",
    "skill_min": "12",
    "skill_max": "20",
}

Random_poor_parameters = {
    "age_min": "24",
    "age_max": "35",
    "skill_min": "10",
    "skill_max": "14",
}


first_name_list_memory = [
    "Peter",
    "Bob",
    "James",
    "Tony",
    "Aj",
    "Bo",
    "Nathan",
    "Gibby",
    "Tim",
    "Anchor",
    "Jimbo",
    "Paul",
    "Simon",
    "Symon",
    "See",
    "Silver",
    "Titch",
    "Rambo",
    "Robbie",
    "TJ",
    "David",
    "John",
    "Michael",
    "Paul",
    "Andrew",
    "David",
    "Sero",
    "Ian",
    "Brian",
    "Barry",
    "Li",
    "Omar",
    "Junior",
    "Blesing",
    "Banele",
    "Samkelo",
    "Ross",
    "Dylon",
    "Master",
    "Junior",
    "Ung",
    "Me",
    "Nsoki",
    "Zak",
    "Banner",
    "Tommie",
    "Feix",
    "Piero",
    "Robert",
    "Pervis",
    "Xavier",
    "Bruno",
    "Joao",
    "Kim",
    "Hwang",
    "Kieffer",
    "Sorba",
    "Ben",
    "Rubin",
    "Aaron",
    "Haji",
    "Josh",
    "Sean",
    "Shaq",
]
last_name_list_memory = [
    "White",
    "Mander",
    "Bishop",
    "Garrett",
    "Winston",
    "Mayfield",
    "Shearer",
    "Rooney",
    "Tucker",
    "Racker",
    "Hutch",
    "Kane",
    "Del-Piero",
    "Seemen",
    "Locker",
    "Teng",
    "Tubert",
    "Smith",
    "Roberts",
    "Curtis",
    "Hammer",
    "Wang",
    "Chen",
    "Smith",
    "Zhang",
    "Costa",
    "Ribbenov",
    "Stimer",
    "Reize",
    "Lemon",
    "Jean",
    "Mohammed",
    "Ticker",
    "Barrett",
    "Manning",
    "Rogan",
    "Musk",
    "Turing",
    "Ali",
    "Fatima",
    "Hassan",
    "Charles",
    "Omar",
    "Stansfield",
    "Moore",
    "Weah",
    "Reyna",
    "Dest",
    "Foden",
    "Callagher",
    "Karimi",
    "Jalali",
    "Ahmed",
    "Jong",
    "Frimpong",
    "Pacho",
    "Blank",
    "Olsen",
    "Larsen",
    "Skov",
    "Rabiot",
    "Thuram",
    "Ifa",
    "Skhiri",
    "Dahmen",
    "Draper",
    "Oviedo",
    "Ruiz",
    "Lopez",
    "Trapp",
    "Muller",
    "Brandt",
    "Ito",
    "Tanaka",
    "Asano",
    "Torres",
    "Asensio",
    "Fati",
    "Faes",
    "Witsel",
    "Doku",
]

#should not be changed
avalible_poistions = ["GK", "LB", "RB", "CB", "LM", "RM", "CM", "ST"]
default_squad_GK = 4
default_squad_DEF = 9
default_squad_MID = 9
default_squad_ATA = 6



if __name__ == "__main__":
    print("This is nothing runable in this script...")
