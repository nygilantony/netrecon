import subprocess

def arp_scan(target):
    print(f"[*] ARP scanning {target}")

    try:
        result = subprocess.check_output(f"arp-scan {target}", shell=True).decode()
        hosts = []

        for line in result.split("\n"):
            if "." in line:
                hosts.append(line.split()[0])

        return hosts

    except:
        print("[!] arp-scan not installed or failed")
        return []
