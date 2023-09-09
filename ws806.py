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
  

import requests
from requests.exceptions import Timeout

proxy_list = []

with open("hasil2_direct.txt", "r") as file:
    for line in file:
        subdomain = line.strip()
        proxy_url = "http://" + subdomain
        proxy_list.append(proxy_url)

url = "http://id4ray.jagoan.vip"

with open("hasil_websocket80.txt", "w") as output_file:
    for proxy in proxy_list:
        proxies = {
            "http": proxy
        }
        
        proxy2 = proxy.split("//")[1]

        try:
            response = requests.head(url, proxies=proxies, timeout=2)
            if response.status_code == 200:
                print(response.status_code, "OK", proxy2)
                output_file.write(f"{proxy2}\n")
            else:
                print(response.status_code, proxy2)
        except Timeout:
            print(proxy2, "melebihi waktu respons")
        except requests.exceptions.RequestException as e:
            print("gagal", proxy2)
            
# Cek port 443 
import os
os.system("python3 wsssl.py")