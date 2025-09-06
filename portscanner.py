import socket

def scan_ports(target, start_port=1, end_port=1024):
    print(f"Scanning {target} from port {start_port} to {end_port}...")
    open_ports = []
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            result = s.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
        except Exception:
            pass
        finally:
            s.close()
    return open_ports

if __name__ == "__main__":
    target = input("Enter target host (IP or domain): ")
    start_port = int(input("Enter start port [default 1]: ") or "1")
    end_port = int(input("Enter end port [default 1024]: ") or "1024")

    open_ports = scan_ports(target, start_port, end_port)
    if open_ports:
        print(f"Open ports on {target}: {open_ports}")
    else:
        print(f"No open ports found on {target} in range {start_port}-{end_port}.")