import requests
import threading

def check_cloudflare_ssl(url, results):
    try:
        response = requests.get(f"http://{url}", timeout=5)

        if "cloudflare" in response.headers.get("server", "").lower():
            results.append(url)
            print(f"{url} - Cloudflare SSL detected!")
        else:
            print(f"{url} - No Cloudflare SSL detected.")
    except requests.exceptions.Timeout:
        print(f"{url} - Timeout occurred.")
    except requests.exceptions.RequestException as e:
        print(f"{url} - Request error occurred: {e}")
    except Exception as e:
        print(f"{url} - Error occurred: {e}")

def process_host(url_list, results):
    for url in url_list:
        check_cloudflare_ssl(url, results)

# Membaca file hasil2_direct.txt
with open("hasil2_direct.txt", "r") as file:
    hosts = file.readlines()

# Menghapus karakter newline pada setiap baris
hosts = [host.strip() for host in hosts]

# Menentukan jumlah thread yang akan digunakan
num_threads = 4

# Memecah list host menjadi jumlah thread yang sesuai
chunks = [hosts[i:i + num_threads] for i in range(0, len(hosts), num_threads)]

# Membuat thread untuk setiap chunk host
threads = []
results = []
for chunk in chunks:
    thread = threading.Thread(target=process_host, args=(chunk, results))
    threads.append(thread)
    thread.start()

# Menampilkan proses pemindaian
for thread in threads:
    thread.join()
    print("Thread finished execution.")

# Menyimpan hasil di file hasil_cdnssl.txt
with open("hasil_cdnssl.txt", "w") as file:
    for result in results:
        file.write(f"{result}\n")

print("Scan completed!")

print("\n Hasil tersimpan di hasil_cdnssl.txt \n")

# Menjalankan Ping 
import os
os.system("python ping_sslcdn.py")