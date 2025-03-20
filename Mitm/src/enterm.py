import time
import asyncio
import scapy
from termcolor import colored
import os
import src.mitm as mitm
import src.dos as dos
import gui
import argparse
# import tui for future tui class to seperate gui in enterm


## DDOS
# Broadcast storm
# Packet flood (TCP, UDP)


class Enterm:
    def __init__(self):
        parser = argparse.ArgumentParser(description="Enter")
        parser.add_argument("--gui", action="store_true", help="Run in gui")
        # Check if gui or terminal default: term
        if parser.gui:
            pass
        # check for cls or clear
        if os.name == "nt":
            self.clear_term = "cls"
        else:
            self.clear_term = "clear"

        self.logo = """
_______________         __                        
\_   _____/__  ____/  |_  ___________  _____  
|    __)_\  \/  /\   __\/ __ \_  __ \/     \ 
|        \>    <  |  | \  ___/|  | \/  Y Y  \ 
/_______  /__/\_ \ |__|  \___  >__|  |__|_|  /
\/      \/           \/            \/ 
                    """

        self.mainmenu = """
Please Enter Your Option
1. MiTM       3. Quit
2. DoS
                        """
     
    # function sinply for ease of use when coding
    def clear(self):
        os.system(self.clear_term)

    def display_menu(self):
        while True:
            self.clear()
            print(colored(self.logo, "blue"))
            print(colored(self.mainmenu, "red"))

            try:
                choice = int(input())
            except ValueError as e:
                print("[Error] Choice not recognized")
                time.sleep(1)
                continue

            self.clear()
            match choice:
                case 1:
                    attack = mitm.Mitm()
                    attack.loop()
                case 2:
                    attack = dos.DoS()
                    attack.arp_poison()
                case 3:
                    self.quit()

    def cleanup(self):
        pass

    def quit(self):
        self.cleanup()
        quit()
            

