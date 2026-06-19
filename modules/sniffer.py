import sys

try:
    from scapy.all import sniff, IP, TCP, UDP
except ImportError:
    print("[-] Deployment missing dependency: Run 'pip install scapy' inside your system layer.")
    sys.exit(1)

def parse_packet(packet):
    if packet.haslayer(IP):
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        
        if packet.haslayer(TCP):
            print(f" [TRAFFIC] PROTOCOL: TCP | LINK: {source_ip}:{packet[TCP].sport} ---> {destination_ip}:{packet[TCP].dport}")
        elif packet.haslayer(UDP):
            print(f" [TRAFFIC] PROTOCOL: UDP | LINK: {source_ip}:{packet[UDP].sport} ---> {destination_ip}:{packet[UDP].dport}")

def run_sniffer(interface):
    print(f"[*] Interception layer online. Monitoring traffic on: {interface if interface else 'All Active Links'}")
    print("[*] Awaiting matching frames... Use Ctrl+C to stop interception sequence.")
    print("-" * 65)
    
    if interface:
        sniff(iface=interface, prn=parse_packet, store=False)
    else:
        sniff(prn=parse_packet, store=False)
