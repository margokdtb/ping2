import os
os.system("clear")
print("\n GUNAKAN KONEKSI INTERNET  \n\n")
domain = input("Masukan Domain: ")

#os.system("cd")
#os.system("cd storage/downloads/scanws/scanws")

os.system(f"subfinder -d {domain} -o subdomain2.txt")

print("\n\n  Data disimpan di subdomain2.txt \n\n ")

import os
os.system("python unik1.py")
