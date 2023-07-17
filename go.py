import os
os.system("clear")

print("\n\n SCAN BUG SSLCDN DAN SNI  \n\n")
print("\nPowered by margokdtb@gmail.com Juli 2023  \n")

import os

def display_menu():
    print("Menu:")
    print("1. Cari Sub Domain (Koneksi Internet) ")
    print("2. Scan Direct Cloudflare (Koneksi paket data)")
    print("3. Ping Direct ")
    print("4. Scan Websoket ")
    print("5. Scan SSL CDN ")
    
    print("6. Scan SNI ")
    print("7. Ping SNI ")
    print("8. Scan CDN SSL v2  ")
    print("9. Ping CDN SSL v2 (Copas dl hasil No 8 ke input.txt)")
    
    print("0. Keluar")

def run_file(file_number):
    if file_number == 1:
        os.system("python3 1.py")
    elif file_number == 2:
        os.system("python3 4.py")
    elif file_number == 3:
        os.system("python3 ping_direct.py")  
    
    elif file_number == 4:
        os.system("python3 ws80.py")
    elif file_number == 5:
        os.system("python3 cdnssl1.py") 
    elif file_number == 6:
        os.system("python3 sni1.py")
    elif file_number == 7:
        os.system("python3 sni2.py")
    elif file_number == 8:
        os.system("python3 2.py")
    elif file_number == 9:
        os.system("python3 3v1.py")
        
    elif file_number == 0:
        return
    else:
        print("Pilihan tidak valid")

while True:
    display_menu()
    try:
        choice = int(input("Masukkan pilihan (0-9): "))
        run_file(choice)
        if choice == 0:
            break
        input("Tekan enter untuk melanjutkan...")
    except ValueError:
        print("Masukkan harus berupa angka! Silakan coba lagi.")