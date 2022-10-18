#!/usr/bin/python3

from termcolor import colored
import os

#print(colored('hello', 'red'), colored('world', 'green'))

#intro >> pre season >> season >> playoff  >> free_agency >> draft

def banner_status(colored_status):
    os.system('clear')
    if colored_status=="i":
        print(colored('Intro >>> ', 'green'), colored('Pre_season >>> ', 'red'),colored('Season >>> ', 'red'), colored('Play-Off >>> ', 'red'),colored('Free_Agency >>> ', 'red'), colored('Draft', 'red'))
    elif colored_status=="ps":
        print(colored('Intro >>> ', 'red'), colored('Pre_season >>> ', 'green'),colored('Season >>> ', 'red'), colored('Play-Off >>> ', 'red'),colored('Free_Agency >>> ', 'red'), colored('Draft', 'red'))
    elif colored_status=="s":
        print(colored('Intro >>> ', 'red'), colored('Pre_season >>> ', 'red'),colored('Season >>> ', 'green'), colored('Play-Off >>> ', 'red'),colored('Free_Agency >>> ', 'red'), colored('Draft', 'red'))
    elif colored_status=="po":
        print(colored('Intro >>> ', 'red'), colored('Pre_season >>> ', 'red'),colored('Season >>> ', 'red'), colored('Play-Off >>> ', 'green'),colored('Free_Agency >>> ', 'red'), colored('Draft', 'red'))
    elif colored_status=="fa":
        print(colored('Intro >>> ', 'red'), colored('Pre_season >>> ', 'red'),colored('Season >>> ', 'red'), colored('Play-Off >>> ', 'red'),colored('Free_Agency >>> ', 'green'), colored('Draft', 'red'))
    elif colored_status=="d":
        print(colored('Intro >>> ', 'red'), colored('Pre_season >>> ', 'red'),colored('Season >>> ', 'red'), colored('Play-Off >>> ', 'red'),colored('Free_Agency >>> ', 'red'), colored('Draft', 'green'))
    else:
        print(colored('Intro >>> ', 'red'), colored('Pre_season >>> ', 'red'),colored('Season >>> ', 'red'), colored('Play-Off >>> ', 'red'),colored('Free_Agency >>> ', 'red'), colored('Draft', 'red'))

if __name__ =="__main__":
    banner_status(colored_status="hi")
