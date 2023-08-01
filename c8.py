import threading
import socket

# Langkah 1: Mengambil host dari file subdomain2.txt
with open("subdomain2.txt", "r") as file:
    hosts = file.read().splitlines()

# Fungsi untuk mendapatkan IP dari host dengan batasan waktu
def get_ip(host):
    try:
        ip = socket.gethostbyname(host)
        return ip
    except socket.gaierror:
        return None

# Fungsi untuk mengambil IP dari host menggunakan multi-threading dengan batasan waktu
def get_ips(hosts):
    result = []
    lock = threading.Lock()

    def process_host(host):
        ip = get_ip(host)
        if ip:
            with lock:
                result.append((host, ip))

    threads = []
    for host in hosts:
        t = threading.Thread(target=process_host, args=(host,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join(timeout=3)  # Batasan waktu 3 detik

    return result

# Langkah 2: Menggunakan multi-threading untuk mendapatkan IP dari setiap host dengan batasan waktu
host_ip_list = get_ips(hosts)

# Langkah 3: Menyimpan host dan IP ke variabel host1
host1 = [(host, ip) for host, ip in host_ip_list if ip]

# Langkah 4: Menyimpan IP unik ke variabel host2 dan menggabungkannya dengan host dari host1
host2 = list(set(ip for _, ip in host1))
host2 += [host for host, _ in host1]

# Langkah 5: Menampilkan hasil dan menyimpannya di file subdomain.txt
with open("subdomain.txt", "w") as file:
    for host, ip in host_ip_list:
        if ip:
            print(f"Host: {host}\tIP: {ip}")
            file.write(f"{host}\n")
        else:
            print(f"Gagal mendapatkan IP untuk host: {host}")