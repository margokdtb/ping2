#CEK SSL

import socket
import ssl
from urllib.request import Request, ProxyHandler, build_opener, install_opener
from concurrent.futures import ThreadPoolExecutor

# Informasi proxy
proxy_host = "ssl-tr1.hostip.co"
proxy_port = 443
proxy_username = "fastssh.com-niken30a"
proxy_password = "123a"

# List server_hostname yang akan dihubungi
server_hostnames = []

# Membaca server_hostname dari file hasil5_sni.txt
with open("hasil/hasil5_sni.txt", "r") as f:
    server_hostnames = [line.strip() for line in f]

# Membuat handler proxy
proxy_handler = ProxyHandler({
    'https': f"{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}"
})
opener = build_opener(proxy_handler)
install_opener(opener)

def connect_server(hostname):
    try:
        # Membuat socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Menghubungkan ke server dengan menggunakan proxy HTTPS
        sock.connect((proxy_host, proxy_port))

        # Menginisialisasi SSL context
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        # Membuat koneksi SSL
        secure_sock = context.wrap_socket(sock, server_hostname=hostname)

        # Mengirim payload
        # secure_sock.send(b"GET / HTTP/1.0\r\nHost: ssl-tr1.hostip.co\r\n\r\n")

        # Menerima respons
        # response = secure_sock.recv(4096)

        # Mengembalikan informasi koneksi jika versi TLS adalah TLSv1.3
        if secure_sock.version() == "TLSv1.3":
            return f"{secure_sock.version()} - {secure_sock.server_hostname}"

    # except Exception as e:
       # Mengembalikan pesan error
       # return f"Error: {e}"

    finally:
        # Menutup koneksi socket
        if 'secure_sock' in locals():
            secure_sock.close()
        if 'sock' in locals():
            sock.close()

# Membuat ThreadPoolExecutor dengan jumlah thread sesuai dengan jumlah server_hostname
with ThreadPoolExecutor(max_workers=len(server_hostnames)) as executor:
    # Submit setiap tugas dari connect_server ke executor
    results = executor.map(connect_server, server_hostnames)

# Menyimpan hasil ke dalam file
with open("hasil/hasil5_sni.txt", "w") as f:
    for result in results:
        if result:
            f.write(f"{result}\n")
            print(result)
            
#mecari host unik
file_path = 'hasil/hasil5_sni.txt'
temp_file_path = 'temp_file.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

updated_lines = [line.replace('TLSv1.3 - ', '') for line in lines]

with open(temp_file_path, 'w') as file:
    file.writelines(updated_lines)

import os
os.replace(temp_file_path, file_path)

#print('Data berhasil diperbarui dan disimpan kembali ke file yang sama.')
            
#CEK PING
import ping3
import concurrent.futures
from tqdm import tqdm

print("\n\n  ")

def ping_host(host):
    try:
        response_time = ping3.ping(host, timeout=2)  # Set timeout to 2 seconds
        if response_time is None:
            response_time = 999  # Use a high value to represent unreachable hosts
    except Exception as e:
        response_time = 999  # Use a high value to represent hosts with ping error
    return (host, response_time)

def main():
    with open("hasil/hasil5_sni.txt", "r") as file:
        host_list = file.read().splitlines()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = []
        for host in host_list:
            results.append(executor.submit(ping_host, host))

        with tqdm(total=len(results), desc="Pinging hosts") as pbar:
            sorted_results = []
            for future in concurrent.futures.as_completed(results):
                sorted_results.append(future.result())
                pbar.update(1)

        sorted_results = sorted(sorted_results, key=lambda x: x[1])

        with open("hasil/hasil5_sni_ping.txt", "w") as output_file:
            for result in sorted_results:
                host, response_time = result
                output_file.write(f"Time: {response_time:.2f} s - {host} \n")
                print(f"Time: {response_time:.2f} s - {host}")

if __name__ == "__main__":
    main()
   
print("\n\nHasil telah disimpan di file hasil5_sni_ping.txt \n")