import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from core.config import STOP_EVENT

class TCPConnectScanner:
    def __init__(self, timeout=1, threads=100):
        self.timeout = timeout
        self.threads = threads

    def _scan_port(self, host, port):
        if STOP_EVENT.is_set():
            return None

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(self.timeout)
                if sock.connect_ex((host, port)) == 0:
                    return port
        except:
            pass
        return None

    def scan(self, host, ports):
        open_ports = []

        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = [executor.submit(self._scan_port, host, p) for p in ports]

            try:
                for future in as_completed(futures):
                    if STOP_EVENT.is_set():
                        break

                    result = future.result()
                    if result:
                        open_ports.append(result)

            except KeyboardInterrupt:
                STOP_EVENT.set()
                print("\n[!] Scan interrupted")

        return sorted(open_ports)
