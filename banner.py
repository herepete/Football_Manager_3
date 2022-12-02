#!/usr/bin/python3

from termcolor import colored
import os

#print(colored('hello', 'red'), colored('world', 'green'))

#intro >> pre season >> season >> playoff  >> free_agency >> draft

def banner_status(colored_status,season_num):
    os.system('clear')
    print (f"Season {season_num}")
    if colored_status=="i":
        print(colored('Intro >>> ', 'green'), colored('Pre_season >>> ', 'red'),colored('Regular Season >>> ', 'red'), colored('Play-Off >>> ', 'red'),colored('Season Wind down >>> ', 'red'),colored('Draft >>> ', 'red'), colored('Free_Agency', 'red'))
    elif colored_status=="ps":
        print(colored('Intro >>> ', 'red'), colored('Pre_season >>> ', 'green'),colored('Regular Season >>> ', 'red'), colored('Play-Off >>> ', 'red'),colored('Season Wind down >>> ', 'red'),colored('Draft >>> ', 'red'), colored('Free_Agency', 'red'))
    elif colored_status=="s":
        print(colored('Intro >>> ', 'red'), colored('Pre_season >>> ', 'red'),colored('Regular Season >>> ', 'green'), colored('Play-Off >>> ', 'red'),colored('Season Wind down >>> ', 'red'),colored('Draft >>> ', 'red'), colored('Free_Agency', 'red'))
    elif colored_status=="po":
        print(colored('Intro >>> ', 'red'), colored('Pre_season >>> ', 'red'),colored('Regular Season >>> ', 'red'), colored('Play-Off >>> ', 'green'),colored('Season Wind down >>> ', 'red'),colored('Draft >>> ', 'red'), colored('Free_Agency', 'red'))
    elif colored_status=="cs":
        print(colored('Intro >>> ', 'red'), colored('Pre_season >>> ', 'red'),colored('Regular Season >>> ', 'red'), colored('Play-Off >>> ', 'red'),colored('Season Wind down >>> ', 'green'),colored('Draft >>> ', 'red'), colored('Free_Agency', 'red'))
    elif colored_status=="fa":
        print(colored('Intro >>> ', 'red'), colored('Pre_season >>> ', 'red'),colored('Regular Season >>> ', 'red'), colored('Play-Off >>> ', 'red'),colored('Season Wind down >>> ', 'red'),colored('Draft >>> ', 'red'), colored('Free_Agency', 'green'))
    elif colored_status=="d":
        print(colored('Intro >>> ', 'red'), colored('Pre_season >>> ', 'red'),colored('Regular Season >>> ', 'red'), colored('Play-Off >>> ', 'red'),colored('Season Wind down >>> ', 'red'),colored('Draft >>> ', 'green'), colored('Free_Agency', 'red'))
    else:
        print(colored('Intro >>> ', 'red'), colored('Pre_season >>> ', 'red'),colored('Regular Season >>> ', 'red'), colored('Play-Off >>> ', 'red'),colored('Season Wind down >>> ', 'red'),colored('Draft >>> ', 'red'), colored('Free_Agency', 'red'))

if __name__ =="__main__":
    import time
    time_delay=1.5
    banner_status(colored_status="i",season_num=1)
    time.sleep(time_delay)
    banner_status(colored_status="ps",season_num=1)
    time.sleep(time_delay)
    banner_status(colored_status="s",season_num=1)
    time.sleep(time_delay)
    banner_status(colored_status="po",season_num=1)
    time.sleep(time_delay)
    banner_status(colored_status="cs",season_num=1)
    time.sleep(time_delay)
    banner_status(colored_status="d",season_num=1)
    time.sleep(time_delay)
    banner_status(colored_status="fa",season_num=1)
    time.sleep(time_delay)
    banner_status(colored_status="hi",season_num=1)
