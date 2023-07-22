import os
os.system("clear")

print("\n\n SCAN SNI  \n\n")

os.system("bugscanner subdomain.txt --mode ssl --output hasil5_sni.txt  --port 443 " )
#os.system("bugscanner-go scan sni -f subdomain.txt --threads 16 --timeout 8 --deep 3" )


print("\n\n Proses Selesai \n")
print(" Hasil disimpan Ke -> hasil5_sni.txt  \n")
