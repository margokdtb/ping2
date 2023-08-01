print("\n\n CEK PORT 443 \n")

import socket

def check_port_443(host):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # set timeout dalam detik
        result = sock.connect_ex((host, 443))
        sock.close()
        if result == 0:
            return True
        else:
            return False
    except Exception as e:
        print("Terjadi kesalahan saat mencoba menghubungi host:", str(e))
        return False

def main():
    hosts = []

    with open("hasil_websocket80.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            host = line.strip()
            hosts.append(host)
    
    results = []

    for host in hosts:
        if check_port_443(host):
            result = f"{host} \n "
            results.append(result)
            result2 = f"{host} - port 443 OK"
            print(result2)
            
    if results:
        with open("hasil_cdnssl.txt", "w") as file:
            file.writelines(results)
            #print("Hasil pengecekan port 443 berhasil disimpan ke dalam file hasil_cek_port_443.txt")
    else:
        print("Tidak support")

if __name__ == "__main__":
    main()
   
# Menjalankan Ping
import os
os.system("python ping_sslcdn.py")