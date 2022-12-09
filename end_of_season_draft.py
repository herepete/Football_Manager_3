#!/usr/bin/python3


def main_run():
    print("...end of season draft...")
    input("Press enter to continue")


if __name__ == "__main__":
    import os
    import banner

    os.system("clear")
    banner.banner_status(colored_status="d", season_num=1)
    main_run()
