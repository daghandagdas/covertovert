from scapy.all import *

def receive_icmp():
    print("Listening for ICMP packets with TTL=1...")
    sniff(filter="icmp", prn=lambda x: x.show(), count = 1)

if __name__ == "__main__":
    receive_icmp()
