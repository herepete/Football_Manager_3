#!/usr/bin/python3.7

def team_formation():
    print ("Which formation do you want to choose for the season, You have the option of ...")
    print ("1 4-4-2 (default)")
    print ("2 4-4-2 (attacking with 1*AM and 1*CM)")
    print ("3 4-4-2 (defending with 1*DM and 1*CM)")
    print ("4 4-3-3 (with 3*CM and 1*LW 1*S 1*RW)")
    try:
        user_input=int(input())
        if user_input ==1:
            print ("4-4-2-Normal")
            return ("4-4-2-Normal")
        if user_input ==2:
            print ("4-4-2-Attack")
            return ("4-4-2-Attack")
        elif user_input ==3:
            print ("4-4-2-Defender")
            return ("4-4-2-Defender")
        elif user_input ==4:
            print ("4-3-3-Normal")
            return ("4-3-3-Normal")
        else:
            print ("Unrgonized number so defaulting to a 4-4-2-Normal")
            return ("4-4-2-Normal")
    except:
            print ("Odd input given so we are going for a 4-4-2-Normal")
            return ("4-4-2-Normal")
    
    
def best_team():
    print ("And are we focusing on:") 
    print ("1 best team avaliable(default)?")
    print ("2 best young team avaliable?")
    print ("3 balanced team of age and Quality avaliable?")
    try:
        user_input=int(input())
        if user_input ==1:
            print ("Best team avaliable choosen(default)")
            return("Best")
        elif  user_input ==2:
            print ("Best Young team avaliable choosen")
            return("Youth")
        elif  user_input ==3:
            print ("Best Balanced team avaliable choosen")
            return("Balance")
        else:
            print ("unrgonized number default to Best Balanced team avaliable")
            return("Best")
    except:
            print ("Odd input given so we are going for Best team avaliable choosen")
            return("Best")
            

if __name__=="__main__" :
    print ("Nothing to do")
