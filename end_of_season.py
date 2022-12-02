#!/usr/bin/python3
import argparse
import logging

parser=argparse.ArgumentParser()
parser.add_argument("-v","--verbose",help="Verbose information",action="store_true")
args =parser.parse_args()





if args.verbose:
    #print("verbosity turned on")
    logging.basicConfig(level=logging.INFO)
    logging.info('Logging turned on')

def main_run():
    print ("I need to add:")
    print ("==============")
    print ("Add player contracts - 1 year")
    print ("Player training +- dependant on age and Special skill")
    print ("renew contracts non renew player get replace by a random")
    print ("Sell players")
    print ("Buy players?")
    input()


if __name__=="__main__":

    # purporse:
    # in: 
    # return: 
    import banner
    banner.banner_status(colored_status="cs",season_num=1)
    main_run()
