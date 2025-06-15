import socket
from urllib.parse import urlparse

def print_banner():
    banner = r"""
  ___       _          ____             _       ____      _               
 / _ \  ___| |_ ___   |  _ \  __ _ _ __| | __  / ___|   _| |__   ___ _ __ 
| | | |/ __| __/ _ \  | | | |/ _` | '__| |/ / | |  | | | | '_ \ / _ \ '__|
| |_| | (__| || (_) | | |_| | (_| | |  |   <  | |__| |_| | |_) |  __/ |   
 \___/ \___|\__\___/  |____/ \__,_|_|  |_|\_\  \____\__, |_.__/ \___|_|   
                                                    |___/                 
 ____                            _ 
/ ___|  __ _ _   _  __ _ _ __ __| |
\___ \ / _` | | | |/ _` | '__/ _` |
 ___) | (_| | |_| | (_| | | | (_| |
|____/ \__, |\__,_|\__,_|_|  \__,_|
          |_|                      

    🛠️  Website to IP Extractor
    👤 Made by: Ariyan Bin Bappy
    ☠️  Group: Octo Dark Cyber Squad X Root Cyber
    ⚠️  For authorized testing only 
"""
    print(banner)

def clean_domain(input_url):
    parsed = urlparse(input_url)
    if parsed.scheme:
        return parsed.netloc
    return input_url.strip().split('/')[0]

def extract_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        return None

def main():
    print_banner()
    user_input = input("🔗 Enter your website: ").strip()
    domain = clean_domain(user_input)
    ip = extract_ip(domain)

    if ip:
        print(f"\n✅ Domain: {domain}")
        print(f"🌐 Resolved IP Address: {ip}")
    else:
        print(f"\n❌ Could not resolve IP for: {domain}")

if __name__ == "__main__":
    main()
