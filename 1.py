import os
os.system("clear")
print("\n GUNAKAN KONEKSI INTERNET  \n\n")
domain = input("Masukan Domain: ")

#os.system("cd")
#os.system("cd storage/downloads/scanws/scanws")

os.system(f"subfinder -d {domain} -o subdomain2.txt")


# import os
print("\n UNTUK MELANJUTKAN GANTI KONEKSI KE PAKET DATA \n\n")

while True:
    if input("SUDAH GANTI PAKET DATA? (y/n) ") == "y":
        os.system("python unik2.py")
        break
    else:
        print("Silakan ganti paket data terlebih dahulu.")
        
print("\n\n  Data disimpan di subdomain.txt \n\n ")
