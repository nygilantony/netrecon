#!/usr/bin/env python3
import argparse
import sys
import os

from core.config import Config, STOP_EVENT
from core.engine import ReconEngine
from output.console import print_results
from output.reports import save_reports

# =========================
# COLORS
# =========================
WHITE  = "\033[97m"
GREEN  = "\033[92m"
CYAN   = "\033[96m"
YELLOW = "\033[93m"
RESET  = "\033[0m"

# =========================
# BANNER
# =========================
BANNER = r"""
 ███╗   ██╗███████╗████████╗██████╗ ███████╗ ██████╗ ██████╗
 ████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔════╝██╔═══██╗
 ██╔██╗ ██║█████╗     ██║   ██████╔╝█████╗  ██║     ██║   ██║
 ██║╚██╗██║██╔══╝     ██║   ██╔══██╗██╔══╝  ██║     ██║   ██║
 ██║ ╚████║███████╗   ██║   ██║  ██║███████╗╚██████╗╚██████╔╝
 ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝

 NetRecon v2.1 | Modular Network Reconnaissance Framework
"""

# =========================
# ARGUMENTS
# =========================
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", help="Target IP / CIDR")
    parser.add_argument("--threads", type=int, default=50)
    return parser.parse_args()

# =========================
# PORT PROFILE
# =========================
def select_port_profile():
    print(f"{CYAN}\nSelect Port Scan Profile:{RESET}")
    print("  1 = 1–1024     (Well-known / Safe)")
    print("  2 = 1–5000     (Fast extended)")
    print("  3 = 1–30000    (Aggressive)")
    print("  4 = 1–65535    (Full scan)")

    choice = input("Enter choice (1-4): ").strip()

    if choice == "1":
        return list(range(1, 1025)), "1–1024"
    elif choice == "2":
        return list(range(1, 5001)), "1–5000"
    elif choice == "3":
        return list(range(1, 30001)), "1–30000"
    elif choice == "4":
        return list(range(1, 65536)), "1–65535"
    else:
        print(f"{YELLOW}[!] Invalid choice, defaulting to 1–1024{RESET}")
        return list(range(1, 1025)), "1–1024"

# =========================
# MAIN
# =========================
def main():
    STOP_EVENT.clear()

    os.system("clear")

    # Banner in CYAN
    print(f"{CYAN}{BANNER}{RESET}")

    args = parse_args()

    if not args.target:
        args.target = input("Enter target: ").strip()

    # Confirm authorization
    confirm = input("\nConfirm authorized scan? (yes/no): ")
    if confirm.lower() != "yes":
        print(f"{YELLOW}[!] Scan aborted{RESET}")
        sys.exit(1)

    # Select ports
    ports, profile = select_port_profile()
    print(f"{CYAN}[*] Selected port range: {profile}{RESET}")

    # =========================
    # WHITE MODE (Discovery Phase)
    # =========================
    print(WHITE)

    config = Config(
        threads=args.threads,
        ports=ports
    )

    engine = ReconEngine(config)

    try:
        engine.full_recon(args.target)
    finally:
        # Reset color after ARP phase
        print(RESET)

    # =========================
    # GREEN MODE (Results)
    # =========================
    print(f"{GREEN}")
    print_results(engine.results)
    print(f"{RESET}")

    save_reports(engine.results)
    print(f"{GREEN}[+] Report saved successfully{RESET}")

# =========================
# ENTRY
# =========================
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        STOP_EVENT.set()
        print(f"\n{YELLOW}[!] Scan interrupted by user{RESET}")
        sys.exit(0)
