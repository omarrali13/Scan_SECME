import socket
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style
import sys

# Target
target = input("🌐 Enter IP or domain to scan: ")

# Default port range
start_port = 1
end_port = 1024

# Banner grabbing toggle
grab_banner = True

def scan_port(port):
    try:
        # Create socket
        s = socket.socket()
        s.settimeout(1)
        s.connect((target, port))
        try:
            banner = ""
            if grab_banner:
                banner = s.recv(1024).decode().strip()
        except:
            banner = ""
        print(f"{Fore.GREEN}[+] Port {port} is OPEN {Style.RESET_ALL}{'- ' + banner if banner else ''}")
        s.close()
    except:
        pass  # silent fail for closed ports

print(f"\n🔍 Scanning {target} from port {start_port} to {end_port}...\n")

with ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(start_port, end_port + 1):
        executor.submit(scan_port, port)

print("\n✅ Scan Complete")
