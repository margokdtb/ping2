print("\n\n SCAN CDN SSL \n")

import os
#os.system("bugscanner-go scan direct -f subdomain.txt -o hasil2_direct.txt" )

os.system("bugscanner-go scan cdn-ssl --proxy-filename subdomain.txt --target id4ray.jagoan.vip | tee hasil/hasil_cdnssl.txt" )




print("\n\nHasil telah disimpan di file hasil_cdnssl.txt\n")

#scan ws port 80
#os.system("python ws80.py" )
# os.system("python wsssl.py" )
#import ws80
#import wsssl

#print("\n\n HASIL DISIMPAN : \n") 
#print(" - >> hasil_websocket80_ping.txt \n")
#print(" - >> hasil_cdnssl443_ping.txt \n")



