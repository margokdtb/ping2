import re

print("\n\n Silakan isi file input_lama.txt terlebih dahulu. \n\n")

# Konfirmasi dari pengguna
konfirmasi = input("Apakah Anda sudah mengisi file input_lama.txt? (y/n) ")

if konfirmasi.lower() == 'y':
    # Membaca file input_lama.txt dan mengambil subdomain
    with open('input_lama.txt', 'r') as file:
        data = file.read()
        subdomains = re.findall(r'\b(?:[A-Za-z0-9]+\.)+[A-Za-z]{2,}\b', data)
    
    # Menggunakan set untuk membuat host yang unik
    unique_hosts = set(subdomains)

    # Menyimpan host yang unik dalam file subdomain.txt
    with open('subdomain.txt', 'w') as file:
        for host in unique_hosts:
            file.write(host + '\n')

    print('Data telah disimpan di subdomain.txt')

else:
    print("Pastikan untuk mengisi file input_lama.txt sebelum menjalankan program ini.")