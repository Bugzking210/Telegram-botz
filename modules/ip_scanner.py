import socket

def scan(ip):
    open_ports = []
    for port in range(1, 1025):
        try:
            s = socket.socket()
            s.settimeout(0.3)
            s.connect((ip, port))
            open_ports.append(port)
            s.close()
        except:
            pass
    if not open_ports:
        return f"No open ports on {ip}."
    return f"Open ports on {ip}: {open_ports}"
