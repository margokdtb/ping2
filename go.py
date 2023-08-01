import os
os.system("clear")

print("\n\n SCAN BUG CDN SSL DAN SNI  \n\n")
print("\nPowered by margokdtb@gmail.com Juli 2023  \n")

import os

def display_menu():
    print("Menu:")
    print("1. Cari Sub Domain (Koneksi Internet) ")
    print("2. Arsip File ")
    print("3. Cek Ws (Koneksi Bug) ")

    print("4. Cek port 80 dan 443")
    
    print("5. Cek SNI  ")
    print("6. Ping SNI  ")
    
    print("7. Sumber Lain/PcapDroid (sumber_pcapdroid.txt) ")
    
    print("8. Host Terkait (Koneksi Internet) ")
    print("9. Ping Host (isi sumber_host.txt) ")
    print("10. Speedtest ")
    print("11. Ip Saya")
    print("12. HTTP Respon")
    print("0. Keluar")

def run_file(file_number):
    if file_number == 1:
        os.system("python3 1.py")
    elif file_number == 2:
        os.system("python3 pilihfile.py")
    elif file_number == 3:	
        os.system("python3 ws.py")
        
    elif file_number == 4:
        os.system("python3 ws80.py")
        
        
    elif file_number == 5:
        os.system("python3 sni1.py")
    elif file_number == 6:
        os.system("python3 sni2.py")
       
    elif file_number == 7:
        os.system("python3 sumberlain.py")    
        
 
 
    elif file_number == 8:
        os.system("python3 hostterkait.py")    
    elif file_number == 9:
        os.system("python3 ping_server.py")                  
    elif file_number == 10:
        os.system("python3 speedtest.py")                  
    elif file_number == 11:
        os.system("python3 ipsaya.py")                  
    elif file_number == 12:
        os.system("python3 httprespon.py")              
     
    elif file_number == 0:
        return
    else:
        print("Pilihan tidak valid")

while True:
    display_menu()
    try:
        choice = int(input("Masukkan pilihan : "))
        run_file(choice)
        if choice == 0:
            break
    except ValueError:
        print("Pilihan tidak valid. Masukkan angka.")
    
    input("Tekan enter untuk melanjutkan...")