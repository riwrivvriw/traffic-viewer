from scapy.all import sniff

def handle_packet(packet):
    print(packet.summary())

sniff(prn=handle_packet, count=10)