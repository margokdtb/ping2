import http.client
import socket
import threading
import ipaddress

def check_sni(host):
    try:
        # Pengecekan apakah host adalah nama host
        try:
            ipaddress.ip_address(host)
            print(f"{host} berupa alamat IP. Dilewati.")
            return False
        except ValueError:
            pass
        
        # Membuat koneksi HTTP
        conn = http.client.HTTPSConnection(host, timeout=3)

        # Mengirimkan permintaan GET
        conn.request("GET", "/")

        # Menerima respon
        res = conn.getresponse()

        # Mengecek apakah SNI tersedia
        return res.version == 11

    except socket.timeout:
        print(f"{host} timeout")
        return False

    except socket.gaierror:
        print(f"{host} tidak valid")
        return False

    except Exception as e:
        print(f"Terjadi kesalahan pada host {host}: {e}")
        return False

# Membaca daftar host dari file
with open("subdomain.txt", "r") as file:
    hosts = file.read().splitlines()

# Membuat fungsi untuk memeriksa SNI untuk setiap host dan mencetak hasilnya
def check_sni_for_hosts(hosts):
    for host in hosts:
        is_hostname = host.count(".") >= 1  # Pengecekan apakah host adalah nama host

        if is_hostname:
            is_sni_supported = check_sni(host)

            if is_sni_supported:
                print(f"{host} mendukung SNI")
            else:
                print(f"{host} tidak mendukung SNI")
        else:
            print(f"{host} bukan nama host. Dilewati.")

# Membagi daftar host menjadi beberapa bagian
num_threads = 3
chunk_size = (len(hosts) // num_threads) + 1
host_chunks = [hosts[i:i + chunk_size] for i in range(0, len(hosts), chunk_size)]

# Membuat thread untuk setiap bagian host
threads = []
for chunk in host_chunks:
    thread = threading.Thread(target=check_sni_for_hosts, args=(chunk,))
    thread.start()
    threads.append(thread)

# Bergabung dengan setiap thread
for thread in threads:
    thread.join()