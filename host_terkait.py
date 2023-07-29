import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def get_connected_hosts(url):
    try:
        if not url.startswith('http'):
            url = 'http://' + url

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        linked_hosts = set()

        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                parsed_url = urlparse(href)
                linked_hosts.add(parsed_url.netloc)

        return linked_hosts

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Meminta pengguna untuk memasukkan URL
url = input("Masukkan URL: ")

# Pemanggilan fungsi untuk mendapatkan host yang terlibat
hosts = get_connected_hosts(url)

if hosts:
    print(f"Host yang terlibat dalam halaman web {url}:")
    for host in hosts:
        print(host)
else:
    print("Tidak ada host yang terlibat dalam halaman web tersebut")

# Menyimpan hasil host ke file subdomain.txt
with open("subdomain.txt", "w") as file:
    #file.write(f"Host yang terlibat dalam halaman web {url}:\n") 
    for host in hosts:
        file.write(host + "\n")

print("Hasil host telah disimpan ke file subdomain.txt")