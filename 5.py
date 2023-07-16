import os
os.system("clear")

print("\n\n SCAN SNI  \n\n")

os.system("bugscanner-go scan sni -f subdomain.txt --threads 16 --timeout 8 --deep 3 " )


print("\n\n Proses Selesai \n")
