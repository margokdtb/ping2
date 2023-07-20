print("\n\n SCAN CLOUDFLARE \n")

import os
os.system("bugscanner-go scan direct -f subdomain.txt -o hasil2_direct.txt" )
#print("\n\nHasil telah disimpan di file hasil2_direct.txt\n")

#scan ws port 80
import ws803
import wsssl

print("\n\n HASIL DISIMPAN : \n") 
print(" - >> hasil_websocket80_ping.txt \n")
print(" - >> hasil_cdnssl443_ping.txt \n")



