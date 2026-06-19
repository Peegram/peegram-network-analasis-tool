#!/usr/bin/env python3
import argparse
import sys
from modules.scanner import run_scanner
from modules.sniffer import run_sniffer

def display_banner():
    print("=" * 65)
    print("      pOS NETPULSE : TERMINAL NETWORK ANALYSIS ENGINE     ")
    print("               Engineered by Peegram                      ")
    print("=" * 65)

def main():
    display_banner()
    
    parser = argparse.ArgumentParser(description="Peegram Network Analysis CLI Utility")
    parser.add_argument("-m", "--mode", choices=["scan", "sniff"], required=True,
                        help="Execution mode: 'scan' (active reconnaissance) or 'sniff' (passive monitoring)")
    parser.add_argument("-t", "--target", help="Target IP address or host subnet (Required for scan mode)")
    parser.add_argument("-i", "--interface", default=None, help="Target hardware interface (Optional for sniff mode)")

    args = parser.parse_args()

    if args.mode == "scan":
        if not args.target:
            print("[-] CRITICAL ERROR: Active scanning requires a target host address (-t).")
            sys.exit(1)
        run_scanner(args.target)
        
    elif args.mode == "sniff":
        run_sniffer(args.interface)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[-] Operational termination sequence initiated by user. Exiting safely.")
        sys.exit(0)
