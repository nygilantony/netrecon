import socket

def grab_banner(host, port):
    try:
        with socket.socket() as s:
            s.settimeout(1)
            s.connect((host, port))
            return s.recv(1024).decode(errors="ignore").strip()
    except:
        return None
