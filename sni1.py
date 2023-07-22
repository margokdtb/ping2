print("\n\n SCAN SSL \n")

import ssl
import socket
import concurrent.futures

def perform_ssl_test(hostname, port=443):
    try:
        # Membuat koneksi TCP dengan host dan port yang diberikan
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)  # Set timeout menjadi 3 detik

        # Menyambungkan socket ke host
        sock.connect((hostname, port))

        # Membuat objek SSLContext
        ssl_context = ssl.create_default_context()

        # Menonaktifkan verifikasi sertifikat (hanya gunakan untuk tes, tidak disarankan di produksi)
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        # Menginisialisasi koneksi SSL/TLS
        sock = ssl_context.wrap_socket(sock, server_hostname=hostname)

        # Mendapatkan informasi tentang protokol yang ditawarkan oleh server
        negotiated_protocol = sock.version()
        shared_ciphers = sock.cipher()

        result = ""

        # Memeriksa protokol SSL/TLS yang ditawarkan
        if negotiated_protocol:
            result += f"{negotiated_protocol}\n"

        sock.close()

        return result.strip()

    except (socket.timeout, socket.gaierror, ssl.SSLError):
        return None

# Membaca sumber host dari file "hasil2_direct.txt"
with open("hasil2_direct.txt", "r") as file:
    hostnames = file.read().splitlines()

# Membuat pool eksekutor untuk multi-threading
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Membuat list untuk menyimpan objek future
    futures = []

    # Memasukkan pekerjaan ke dalam pool eksekutor
    for hostname in hostnames:
        # Menugaskan tugas perform_ssl_test ke executor dan menyimpan hasil sebagai objek future
        future = executor.submit(perform_ssl_test, hostname)
        futures.append(future)

    # Menunggu hingga semua tugas selesai dan mendapatkan hasilnya
    results = []
    for future, hostname in zip(futures, hostnames):
        test_result = future.result()
        print(f"{hostname}:443 - {test_result}")
        
        if test_result is not None:  # Hanya menyimpan hasil yang merespons dengan benar
            results.append(f"{hostname}")

# Menyimpan hasilnya dalam file "hasil_ssl.txt"
with open("hasil5_sni.txt", "w") as file:
    file.write("\n".join(results))
   
print("\n Hasil disimpan hasil5_sni.txt \n")