import os
os.system("clear")
print("\n GUNAKAN KONEKSI INTERNET  \n\n")
domain = input("Masukan Domain: ")

#os.system("cd")
#os.system("cd storage/downloads/scanws/scanws")

os.system(f"subfinder -d {domain} -o 'subdo_{domain}.txt' ")
print("\n\n  Data disimpan \n\n ")
