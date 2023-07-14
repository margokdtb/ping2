import os
os.system("clear")

domain = input("Masukan Domain: ")

#os.system("cd")
#os.system("cd storage/downloads/scanws/scanws")


os.system(f"subfinder -d {domain} -o xyz.txt")
os.system("bugscanner-go scan direct -f xyz.txt -o zxy2.txt" )
os.system("python c4.py")
print("\nHasil Ping Disimpan Ke -> hasil_80.txt dan hasil_443.txt  \n\n")