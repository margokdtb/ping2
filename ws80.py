print("\n\n SCAN WS PORT 80 \n")

#cek data unik dulu
 # Membaca file subdomain2.txt
with open("hasil2_direct.txt", "r") as file:
    data = file.readlines()

# Menghapus karakter baris baru (\n) dari setiap baris
data = [line.strip() for line in data]

# Menghapus data duplikat
data_uniq = list(set(data))

# Menyimpan hasil ke file subdomain.txt
with open("hasil2_direct.txt", "w") as file:
    for item in data_uniq:
        file.write(item + "\n")
       # print(item)
        
#end cek data unik        
        
import socket
import time

host = "id4ray.jagoan.vip"
port = 80
payload = b'HEAD / HTTP/1.1\r\nHost: id4ray.jagoan.vip\r\nUpgrade: websocket\r\n\r\n'
timeout = 2

with open("hasil2_direct.txt", "r") as file:
    proxy_servers = file.read().splitlines()
      
with open("hasil_websocket80.txt", "w") as file:
    for proxy_server in proxy_servers:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)  # Set timeout to 5 seconds
            sock.connect((proxy_server, port))

            sock.sendall(payload)

            response = sock.recv(4096)
            if response:
                status_line = response.split(b'\r\n')[0]
                status_code = status_line.split(b' ')[1]

                print("Status Code:", status_code.decode('latin-1') + " - " + proxy_server)

                if status_code == b'200':
                    file.write(proxy_server + "\n")

            sock.close()

        except socket.gaierror:
            print("Error connecting - ", proxy_server)

        except socket.timeout:
            print("Timeout - ", proxy_server)
        
        except socket.error as e:
            print("Network error:", str(e))
        
        #time.sleep(5)  # Delay 5 seconds before the next request
       
      
      
# Cek port 443 
import os
os.system("python3 wsssl.py")