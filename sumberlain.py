import re

print("\n\n Isi dulu file sumber_pcapdroid.txt \n\n")

# Konfirmasi dari pengguna
konfirmasi = input("sudah mengisi file? (y/n) ")

if konfirmasi.lower() == 'y':
    # Membaca file sumber_pcapdroid.txt dan mengambil subdomain dan ip
    with open('sumber/sumber_pcapdroid.txt', 'r') as file:
        data = file.read()
        subdomains = re.findall(r'\b(?:[A-Za-z0-9]+\.)+[A-Za-z]{2,}\b', data)
        ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', data)
    
    # Menggunakan set untuk membuat subdomain dan ip yang unik
    unique_subdomains = set(subdomains)
    unique_ips = set(ips)

    # Menyimpan subdomain dan ip yang unik dalam file hasil.txt
    with open('subdomain.txt', 'w') as file:
        #file.write("Subdomains:\n")
        for subdomain in unique_subdomains:
            file.write(subdomain + '\n')
        
        # file.write("\nIPs:\n")
        for ip in unique_ips:
            file.write(ip + '\n')
            
    # import os
    # os.system("python unik3.py")

    print('\n Data telah disimpan di hasil.txt')

else:
    print("\n Pastikan untuk mengisi file sumber_pcapdroid.txt sebelum menjalankan program ini.")