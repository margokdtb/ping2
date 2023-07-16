import os
os.system("clear")

print("\n\n SCAN BUG SSLCDN DAN SNI  \n\n")
print("\nPowered by margokdtb@gmail.com Juli 2023  \n")

import os

def display_menu():
    print("Menu:")
    print("1. Cari Sub Domain (Koneksi Internet) ")
    print("2. Scan Direct Websoket (Koneksi paket data)")
    print("3. Ping Direct (Koneksi paket data)")
    print("4. Scan SSL CDN (Koneksi paket data) ")
    print("5. Ping SSL CDN (Copas dl hasil No 2 ke input.txt)")
    print("6. Scan SNI (Koneksi paket data) ")
    print("7. Ping SNI (Koneksi paket data) ")
    
    print("0. Keluar")

def run_file(file_number):
    if file_number == 1:
        os.system("python3 1.py")
    elif file_number == 2:
        os.system("python3 4.py")
    elif file_number == 3:
        os.system("python3 ping_direct.py")  
    elif file_number == 4:
        os.system("python3 2.py") 
    elif file_number == 5:
        os.system("python3 3v1.py")
    elif file_number == 6:
        os.system("python3 sni1.py")
    elif file_number == 7:
        os.system("python3 sni2.py")
        
    elif file_number == 0:
        return
    else:
        print("Pilihan tidak valid")

while True:
    display_menu()
    choice = int(input("Masukkan pilihan (0-7): "))
    run_file(choice)
    if choice == 0:
        break
    input("Tekan enter untuk melanjutkan...")
