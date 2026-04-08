import threading

STOP_EVENT = threading.Event()

class Config:
    def __init__(self, threads=50, safe_mode=False, ports=None):
        self.threads = threads
        self.safe_mode = safe_mode
        self.ports = ports
