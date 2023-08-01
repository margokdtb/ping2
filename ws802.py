import requests
from termcolor import colored
import time
from concurrent.futures import ThreadPoolExecutor

print("\n CEK WS PORT 80 \n")

# Tentukan URL, payload, dan proxy
url = "http://api.myxl.xlaxiata.co.id/"
payload = {}

# Baca file hasil2_direct.txt untuk mendapatkan daftar proxy
with open("hasil2_direct.txt", "r") as file:
    proxies = file.read().splitlines()

# Fungsi untuk melakukan pengecekan proxy dan menyimpan hasil
def check_proxy(proxy):
    proxy_dict = {
        "http": proxy,
        "https": proxy
    }

    try:
        # Mulai hitung waktu
        start_time = time.time()

        # Buat koneksi dengan server menggunakan proxy
        response = requests.get(url, params=payload, proxies=proxy_dict, timeout=5)  # Batasi waktu respons menjadi 5 detik
        status = response.status_code

        # Cek apakah status code adalah 200
        if status == 200:
            print(f"{proxy} - {time.time() - start_time:.2f}s - {colored('Status : 200 OK', 'green')}")
            with open("hasil_cdnssl.txt", "a") as outfile:
                outfile.write(f"{proxy} - {time.time() - start_time:.2f}s \n")
        else:
            print(f"{proxy} - {time.time() - start_time:.2f}s - Status code: {status}")

    except requests.exceptions.RequestException as e:
        print(f"{proxy} - {time.time() - start_time:.2f}s - Error: not respon")

# Membersihkan isi file hasil_cdnssl.txt di paling atas
open("hasil_cdnssl.txt", "w").close()

# Buat thread pool dengan maksimal 4 thread
with ThreadPoolExecutor(max_workers=4) as executor:
    executor.map(check_proxy, proxies)

print("\nData Disimpan Ke hasil_cdnssl.txt \n")