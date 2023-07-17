import os
#os.system("python 4.py" )

filename = "hasil_websocket80.txt"

# Membuka file dalam mode write dan mengosongkan isinya
with open(filename, "w") as file:
    file.write("")

import socket
import select
from concurrent.futures import ThreadPoolExecutor

def send_request(host):
    ip = socket.gethostbyname(host)
    port = 80
    request = "GET wss://api.myxl.xlaxiata.co.id/ HTTP/1.1\r\n" \
              f"Host: {host}\r\n" \
              "Connection: Upgrade\r\n" \
              "Upgrade: websocket\r\n\r\n"

    # Membuat koneksi socket ke server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)  # Mengatur waktu tunggu socket menjadi 5 detik
    sock.connect((host, port))

    try:
        # Mengirim permintaan
        sock.sendall(request.encode())

        # Menunggu hingga ada data yang bisa dibaca dari socket
        ready = select.select([sock], [], [], 5)

        if ready[0]:
            # Menerima respon dari server
            response = sock.recv(4096).decode()
            status = "OK" if "HTTP/1.1 200" in response else "Gagal"

            # Mencetak hasil dalam format host/ip status server
            result = f"{host} {status}"
            print(result)

            # Memeriksa apakah hasil statusnya OK dan menyimpan host/IP ke dalam file jika ya
            if status == "OK":
                with open("hasil_websocket80.txt", "a") as file:
                    file.write(host + "\n")

        else:
            # Waktu respon habis
            print(f"{host} Timeout")

    except socket.error as e:
        print(f"{host} Gagal - {e}")

    finally:
        # Menutup koneksi socket
        sock.close()


def main():
    # Membaca host dari file hasil2_direct.txt
    with open("hasil2_direct.txt", "r") as file:
        hosts = [line.strip() for line in file]

    # Membuat ThreadPoolExecutor dengan maksimum 5 threads
    with ThreadPoolExecutor(max_workers=5) as executor:
        # Mengirim permintaan dan mencetak hasil untuk setiap host secara paralel
        executor.map(send_request, hosts)


if __name__ == "__main__":
    main()

print("\n\nHasil telah disimpan di file hasil_websocket80.txt\n")

# Menjalankan Ping
os.system("python ping_ws.py")