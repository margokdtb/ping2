import socket
import time

# Mengatur waktu timeout menjadi 5 detik
socket.setdefaulttimeout(5)

with open('subdomain2.txt', 'r') as file:
    hostnames = file.read().splitlines()

unique_ips = set()
unique_hosts = []

for hostname in hostnames:
    try:
        start_time = time.time()  # Memulai mengukur waktu
        ip = socket.gethostbyname(hostname)
        elapsed_time = time.time() - start_time  # Menghitung waktu yang diperlukan
        if elapsed_time > 3:  # Jika waktu yang diperlukan lebih dari 3 detik, skip cek IP
            print(f"Skip cek IP untuk {hostname}: took {elapsed_time} seconds")
        else:
            if ip not in unique_ips:
                unique_ips.add(ip)
                unique_hosts.append((hostname, ip))
            print(f"{hostname} : {ip}")
    except socket.gaierror:
        print(f"Host tidak valid: {hostname}")
        continue  # Melewati host yang tidak valid

with open("subdomain.txt", "w") as file:
    for host, ip in unique_hosts:
        file.write(f"{host}\n")

print("\nProses selesai. Host unik disimpan ke dalam file subdomain.txt")