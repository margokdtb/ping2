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
    print("4. Cek Ws2 (Koneksi Bug) ")
    
    print("5. Cek port 80 dan 443")
    print("6. Cek Respon 443")
    
    print("7. Cek SNI  ")
    print("8. Ping SNI  ")
    
    print("9. Sumber Lain(sumber_lain.txt) ")
    
    print("10. Host Terkait (Koneksi Internet) ")
    print("11. Ping Host (isi sumber_host.txt) ")
    print("12. Speedtest ")
    print("13. Ip Saya")
    print("14. HTTP Respon")
    print("15. Cek Respon Proxy")
    print("16. Sumber PCAPdroid (sumber_pcapdroid.txt)")
    print("17. Cek CDN SSL (subdomain.txt.txt)")
    print("18. Cek SNI V2 (subdomain.txt.txt)")
    print("0. Keluar")

def run_file(file_number):
    if file_number == 1:
        os.system("python3 1.py")
    elif file_number == 2:
        os.system("python3 pilihfile.py")
    elif file_number == 3:	
        os.system("python3 ws.py")
        
    elif file_number == 4:	
        os.system("python3 cloudflare.py")
        
    elif file_number == 5:
        os.system("python3 ws80.py")
        
    elif file_number == 6:
        os.system("python3 ws806.py")
        
        
    elif file_number == 7:
        os.system("python3 sni1.py")
    elif file_number == 8:
        os.system("python3 sni2.py")
       
    elif file_number == 9:
        os.system("python3 sumberlain.py")    
        
 
 
    elif file_number == 10:
        os.system("python3 hostterkait.py")    
    elif file_number == 11:
        os.system("python3 ping_server.py")                  
    elif file_number == 12:
        os.system("python3 speedtest.py")                  
    elif file_number == 13:
        os.system("python3 ipsaya.py")                  
    elif file_number == 14:
        os.system("python3 httprespon.py")              
    elif file_number == 15:
        os.system("python3 proxy.py")   
    elif file_number == 16:
        os.system("python3 sumber_pcapdroid.py")          

    elif file_number == 17:
        os.system("python3 cdnssl.py")      
        
    elif file_number == 18:
        os.system("python3 sniv2.py")       
 
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