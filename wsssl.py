print("\n\n SCAN WS PORT 443 \n")

import socket

def check_port(hostname, port):
    # Membuat socket TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Menghubungkan ke host dengan port yang ditentukan
        sock.connect((hostname, port))
        return True
    except socket.error:
        return False
    finally:
        # Menutup koneksi socket
        sock.close()

# Membaca file dan menyimpan setiap baris ke dalam list
with open("hasil_websocket80.txt", "r") as file:
    lines = file.readlines()
    hosts = [line.strip() for line in lines]

port = 443

 # Membuka file hasil_cdnssl.txt untuk ditulis
with open("hasil_cdnssl.txt", "w") as file:
    for host in hosts:
        if check_port(host, port):
            result = f"Port {port} terbuka - {host}"
            result2 = f"{host}"
            print(result)
            file.write(result2 + "\n")
        else:
            result = f"Port {port} tertutup - {host}"
            print(result)
            file.write(result + "\n")
           
import os
os.system("python ping_sslcdn.py")