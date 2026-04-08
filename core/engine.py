from scan.tcp_connect import TCPConnectScanner
from discovery.arp import arp_scan
from utils.services import identify
from fingerprint.banners import grab_banner
from core.config import STOP_EVENT

class ReconEngine:
    def __init__(self, config):
        self.config = config
        self.results = []

    def scan_host(self, host):
        print(f"[*] Scanning {host}")

        ports = self.config.ports or range(1, 1025)

        scanner = TCPConnectScanner(threads=self.config.threads)
        open_ports = scanner.scan(host, ports)

        if STOP_EVENT.is_set():
            return []

        return open_ports

    def full_recon(self, target):
        try:
            hosts = arp_scan(target)

            for host in hosts:
                if STOP_EVENT.is_set():
                    break

                open_ports = self.scan_host(host)

                self.results.append({
                    "ip": host,
                    "open_ports": open_ports
                })

        except KeyboardInterrupt:
            STOP_EVENT.set()
