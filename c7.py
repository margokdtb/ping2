import requests
import concurrent.futures

TIMEOUT = 5  # Waktu maksimal permintaan dalam detik

def scan_cdn_ssl(item):
    if item.startswith("http"):
        url = item
    else:
        url = "https://{}".format(item)
    
    result = None  # Inisialisasi variabel result

    try:
        response = requests.get(url, verify=True, timeout=TIMEOUT)
        if response.status_code == 200:
            result = item
            # Menyimpan host yang menghasilkan respons dengan kode status 200 ke dalam file cdn_hasil.txt
            with open("hasil5_sni.txt", "a") as file:
                file.write(result + "\n")
    except requests.exceptions.RequestException:
        result = "{}: not connect".format(item)
    
    return result


def main():
    # Membaca IP dan domain dari file cdn_input.txt
    with open("hasil2_direct.txt", "r") as file:
        data = [line.strip() for line in file]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(scan_cdn_ssl, item) for item in data]

        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            print(result)


if __name__ == "__main__":
    main()
   
print("\n\n Hasil telah disimpan di file hasil5_sni.txt \n")