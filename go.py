import os
os.system("clear")

print("\n\n SCAN BUG SSLCDN DAN SNI  \n\n")
print("\nPowered by margokdtb@gmail.com Juli 2023  \n")

import os

def display_menu():
    print("Menu:")
    print("1. Cari Sub Domain (Koneksi Internet) ")
    print("2. Cek Cloudflare (Koneksi paket data)")
    print("3. Scan Cloudflare Port 80 ")
    print("4. Scan Cloudflare SSL Port 443 ")
    print("5. Scan SNI  ")
    print("6. Ping SNI  ")
    
    print("7. Data lama (isi input_lama.txt) ")
    
    print("0. Keluar")

def run_file(file_number):
    if file_number == 1:
        os.system("python3 1.py")
    elif file_number == 2:
        os.system("python3 4.py")
    elif file_number == 3:
        os.system("python3 ws803.py")
    elif file_number == 4:
        os.system("python3 wsssl.py")    
    
        
    elif file_number == 5:
        os.system("python3 sni1.py")
    elif file_number == 6:
        os.system("python3 sni2.py")
       
    elif file_number == 7:
        os.system("python3 datalama.py")    
            
        
    elif file_number == 0:
        return
    else:
        print("Pilihan tidak valid")

while True:
    display_menu()
    choice = int(input("Masukkan pilihan : "))
    run_file(choice)
    if choice == 0:
        break
    input("Tekan enter untuk melanjutkan...")