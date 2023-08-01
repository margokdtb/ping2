import os
print("\n UNTUK MELANJUTKAN GANTI KONEKSI KE DATA \n\n")

while True:
    if input("SUDAH GANTI PAKET DATA? (y/n) ") == "y":
        os.system("python unik2.py")
        break
    else:
        print("Silakan ganti paket data terlebih dahulu.")
