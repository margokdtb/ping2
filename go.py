import os
os.system("clear")

print("\n\n SCAN BUG SSLCDN DAN SNI  \n\n")
print("\nPowered by margokdtb@gmail.com Juli 2023  \n")

import os

def display_menu():
    print("Menu:")
    print("1. Cari Sub Domain (Koneksi Internet) ")
    
    print("2. Scan Websoket (Koneksi Data) ")
    print("3. Scan SSL CDN (Koneksi Data) ")
    
    print("4. Scan SNI (Koneksi Data) ")
    print("5. Ping SNI (Koneksi Data) ")
    
    
    
    print("0. Keluar")

def run_file(file_number):
    if file_number == 1:
        os.system("python3 1.py")
    
    elif file_number == 2:
        os.system("python3 ws80.py")
    elif file_number == 3:
        os.system("python3 cdnssl1.py") 
    elif file_number == 4:
        os.system("python3 sni1.py")
    elif file_number == 5:
        os.system("python3 sni2.py")

        
    elif file_number == 0:
        return
    else:
        print("Pilihan tidak valid")

while True:
    display_menu()
    try:
        choice = int(input("Masukkan pilihan (0-5): "))
        run_file(choice)
        if choice == 0:
            break
        input("Tekan enter untuk melanjutkan...")
    except ValueError:
        print("Masukkan harus berupa angka! Silakan coba lagi.")