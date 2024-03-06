print("\n\n PING SNI  \n\n")

import socket
import concurrent.futures
import time

def tcp_ping(host):
    start_time = time.time()
    try:
        with socket.create_connection((host, 80), timeout=2) as sock:
            end_time = time.time()
            result = f"{end_time - start_time:.3f} s : {host}\n"
            print(result, end='')  # Menampilkan output tanpa newline
            return result
    except Exception as e:
        end_time = time.time()
        result = f"Host {host} - unreachable - {end_time - start_time:.3f} seconds\n"
        print(result, end='')
        return result

# Membaca daftar host dari file hasil5_sni.txt
hosts = []
with open("hasil/hasil5_sni.txt", "r") as file:
    hosts = file.read().splitlines()

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(tcp_ping, host) for host in hosts]
    results = [future.result() for future in concurrent.futures.as_completed(futures)]

# Menyimpan hasil ke dalam file hasil5_sni_ping.txt
with open("hasil/hasil5_sni_ping.txt", "w") as output_file:
    for result in results:
        output_file.write(result)

print("\n\nHasil telah disimpan di file hasil/hasil5_sni_ping.txt \n")