import platform, socket

def get_info():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return f"""
💻 Hostname: {hostname}
🌐 IP Address: {ip}
🧠 System: {platform.system()}
🔢 Version: {platform.version()}
🧬 Architecture: {platform.machine()}
"""
