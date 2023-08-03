import requests

# Fungsi untuk mendapatkan alamat IP dari jaringan saat ini
def get_ip_address():
    url = "http://ifconfig.me/ip"
    try:
        response = requests.get(url)
        response.raise_for_status()  # memunculkan exception jika terjadi kesalahan
        return response.text
    except requests.exceptions.RequestException as e:
        print("Terjadi kesalahan saat mendapatkan alamat IP:", e)
        return None

# Fungsi untuk mendapatkan informasi geografis berdasarkan IP
def get_geolocation(ip):
    url = f"http://ip-api.com/json/{ip}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # memunculkan exception jika terjadi kesalahan
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Terjadi kesalahan saat mendapatkan informasi geografis:", e)
        return None

# Fungsi untuk mencetak informasi geografis
def print_geolocation(geolocation):
    if geolocation and geolocation['status'] == 'success':
        print(f"Your IP: {geolocation['query']}")
        print(f"Country: {geolocation['country']} - {geolocation['countryCode']}")
        print(f"State: {geolocation['regionName']}")
        print(f"Town: {geolocation['city']}")
        print(f"ISP: {geolocation['isp']}")
    else:
        print("Gagal mendapatkan informasi geografis")

# Mendapatkan alamat IP dari jaringan saat ini
ip = get_ip_address()
print(f"IP from current network: {ip}")

# Jika IP ditemukan, mendapatkan informasi geografis berdasarkan IP
if ip:
    geolocation = get_geolocation(ip)

    # Mencetak informasi geografis
    print_geolocation(geolocation)