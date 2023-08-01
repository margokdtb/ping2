import os
os.system("clear")
print("\n GUNAKAN KONEKSI INTERNET  \n\n")
domain = input("Masukan Domain: ")

#os.system("cd")
os.system("rm subdomain.txt")

os.system(f"subfinder -d {domain} -o subdomain.txt ")
print("\n\n  Data disimpan \n\n ")

import shutil
# Mengcopy file "subdomain.txt" menjadi "subdo_coba.txt"
shutil.copy("subdomain.txt", "subdomain/subdo_" +domain+".txt")
