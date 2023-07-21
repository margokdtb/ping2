import requests
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style

print("\n\n SCAN WS SSL PORT 443 \n")

def check_cloudflare_ssl(url):
    try:
        response = requests.get(f"http://{url}", timeout=2 )

        if "cloudflare" in response.headers.get("server", "").lower():
            print(f"{Fore.GREEN}{url} - Cloudflare SSL{Style.RESET_ALL}")
            return url
        else:
            return None
    except requests.exceptions.Timeout:
        print(f"{url} - Timeout")
        return None
    except requests.exceptions.RequestException as e:
        print(f"{url} - Request error")
        return None
    except Exception as e:
        print(f"{url} - Error")
        return None

# Membaca file hasil2_direct.txt 
with open("hasil2_direct.txt", "r") as file:
    hosts = file.readlines()

# Menghapus karakter newline pada setiap baris
hosts = [host.strip() for host in hosts]

# Menentukan jumlah thread yang akan digunakan
num_threads = 4

# Membagi list host menjadi bagian sesuai jumlah thread
chunks = [hosts[i:i + num_threads] for i in range(0, len(hosts), num_threads)]

results = []

with ThreadPoolExecutor(max_workers=num_threads) as executor:
    # Mengeksekusi fungsi check_cloudflare_ssl secara concurrent
    for chunk in chunks:
        results += [result for result in executor.map(check_cloudflare_ssl, chunk) if result is not None]

# Menyimpan hasil di file hasil_cdnssl.txt
with open("hasil_cdnssl.txt", "w") as file:
    for result in results:
        file.write(f"{result}\n")

# print("Scan completed!")

#print("\n Hasil tersimpan di hasil_cdnssl.txt \n")

# Menjalankan Ping
import os
os.system("python ping_sslcdn.py")