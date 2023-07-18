print("\n CEK HOST SSL CDN PORT 443 \n")

import requests
import re
import concurrent.futures

def check_ssl_cdn(host):
    if re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", host):
        print(f"{host} berupa IP address. Diabaikan.")
        return ""
        
    try:
        response = requests.get(f"https://{host}", timeout=5)
        
        if 'CF-RAY' in response.headers:
            result = f"{host}\n"
            print(f"{host} adalah CDN SSL")
        else:
            print(f"{host} bukan CDN SSL")
            result = ""
            
        return result
    except requests.exceptions.Timeout:
        print(f"Waktu permintaan habis untuk host {host}. Diabaikan.")
        return ""
    except requests.exceptions.RequestException as e:
        if isinstance(e, requests.exceptions.ConnectionError) and 'NameResolutionError' in str(e):
            print(f"{host} Tidak dapat mengakses host . Diabaikan.")
        else:         
            print(f"{host} SSL CDN Tidak Valid")
        return ""

# List host yang akan diperiksa
with open('hasil2_direct.txt', 'r') as file:
    hosts = file.read().splitlines()

# Memanggil fungsi untuk memeriksa setiap host secara paralel dengan multithreading
results = []
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(check_ssl_cdn, host) for host in hosts]
    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        if result:
            results.append(result)

# Menyimpan hasil ke file cdn1.txt
with open('hasil_cdnssl.txt', 'w') as file:
    file.writelines(results)

print("\n Proses selesai. Hasil tersimpan di hasil_cdnssl.txt \n")

# Menjalankan Ping 
import os
os.system("python ping_sslcdn.py")