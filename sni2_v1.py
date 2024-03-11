import socket
import ssl
import warnings
import time

# Mengabaikan peringatan DeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Membuat objek SSLContext
context = ssl.SSLContext(ssl.PROTOCOL_TLS)

# Membuka file dan membaca daftar hostname
with open("hasil/hasil5_sni.txt", "r") as file:
    hostnames = file.readlines()

# Menghapus karakter baris baru dari setiap hostname
hostnames = [hostname.strip() for hostname in hostnames]

# Membuka file untuk menyimpan respon
file_respon = open("temp_file.txt", "w")

for hostname in hostnames:
    # Membuka koneksi socket ke ssl-tr1.hostip.co pada port 443
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)  # Mengatur waktu tunggu menjadi 3 detik
    try:
        sock.connect(("ssl-tr1.hostip.co", 443))
    except socket.timeout:
        print("Hostname tidak merespon dalam waktu 3 detik")
        continue

    # Melakukan handshake SSL
    try:
        ssl_sock = context.wrap_socket(sock, server_hostname=hostname)
    except (ssl.SSLError, socket.timeout) as e:
        print("not respon")
        #print("Handshake SSL gagal:", str(e))
        sock.close()
        continue

    # print("[05:57:59] Memulai layanan SSH")

    # Mengirim permintaan HTTP untuk melakukan koneksi
    request = "HEAD kh.google.com:443 HTTP/1.1\r\nHost: kh.google.com\r\n\r\n".encode("utf-8")
    ssl_sock.write(request)

    # Menerima respon HTTP
    try:
        response = ssl_sock.read()
    except socket.timeout:
        print("Permintaan HTTP tidak berhasil diterima")
        ssl_sock.close()
        sock.close()
        continue

    if response:
        print("Versi:", ssl_sock.version(), " - ", ssl_sock.server_hostname)
        file_respon.write(f"{hostname}\n")
        file_respon.flush()
    else:
        print("Koneksi tidak valid")

    # Menutup koneksi
    ssl_sock.close()
    sock.close()

# Menutup file respon
file_respon.close()
            

            
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
    with open("temp_file.txt", "r") as file:
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