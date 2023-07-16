
import os

def display_menu():
    print("Menu:")
    print("1. Cari Sub Domain")
    print("2. Scan Direct")
    print("3. Scan SSL CDN")
    print("0. Keluar")

def run_file(file_number):
    if file_number == 1:
        os.system("python3 1.py")
    elif file_number == 2:
        os.system("python3 2.py")
    elif file_number == 3:
        os.system("python3 3.py")
    elif file_number == 0:
        return
    else:
        print("Pilihan tidak valid")

while True:
    display_menu()
    choice = int(input("Masukkan pilihan (0-3): "))
    run_file(choice)
    if choice == 0:
        break
    input("Tekan enter untuk melanjutkan...")
