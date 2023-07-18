print("\n CEK HOST DENGAN IP UNIK \n")

import socket

with open('subdomain2.txt', 'r') as file:
    hostnames = file.read().splitlines()

unique_ips = set()
unique_hosts = []

for hostname in hostnames:
    try:
        ip = socket.gethostbyname(hostname)
        if ip not in unique_ips:
            unique_ips.add(ip)
            unique_hosts.append((hostname, ip))
        print(f"{hostname} : {ip}")
    except socket.gaierror:
        print(f"Host tidak valid: {hostname}")

with open("subdomain.txt", "w") as file:
    for host, ip in unique_hosts:
        file.write(f"{host}\n")

print("\nProses selesai. \n Host unik disimpan ke dalam file subdomain.txt")