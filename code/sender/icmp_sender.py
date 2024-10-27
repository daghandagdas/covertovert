from scapy.all import *

def send_icmp():
    target = "receiver"
    source = "sender"

    packet = IP(src=source, dst=target, ttl=1) / ICMP()

    send(packet)

if __name__ == "__main__":
    send_icmp()
