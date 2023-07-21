print("\n\n SCAN WS PORT 80 \n")

import http.client


# Baca file hasil2_direct.txt
with open('hasil2_direct.txt', 'r') as file:
    sumbernya = file.read().splitlines()

# Buat file hasil_websocket80
file_output = open('hasil_websocket80.txt', 'w')

# Loop melalui setiap sumber koneksi
for sumber in sumbernya:
    try:
        # Buat koneksi dengan server
        conn = http.client.HTTPConnection(sumber, 80)
        conn.timeout = 2

        # Kirim permintaan GET
        headers = {
            'Host': 'api.myxl.xlaxiata.co.id',
            'User-Agent': '[ua]', 
            'Upgrade': 'websocket'
        }

        conn.request('HEAD', '/', headers=headers)

        # Dapatkan respons dari server
        response = conn.getresponse()

        # Dapatkan status respon
        status = response.status
        status_message = response.reason

        # Cetak status respon
        print(sumber, ' -' , status, '',status_message )
        #print('Status:', status)
        #print('Status Message:', status_message)
        #print()

        # Cek jika status adalah 200
        if status == 200:
            # Simpan hasil ke file hasil_cdnssl.txt
            file_output.write( sumber + '\n')

        # Tutup koneksi
        conn.close()

    except http.client.HTTPException as e:
        # Tangani kesalahan koneksi HTTP
        print('Terjadi kesalahan HTTP:', str(e))
        print('Mengabaikan sumber koneksi:', sumber)
        print()
        continue

    except TimeoutError as e:
        # Tangani kesalahan timeout
        #print('Koneksi timeout:', str(e))
        #print('Mengabaikan sumber koneksi:', sumber)
        print(sumber, '- timeout' )
        continue

# Tutup file hasil_cdnssl.txt
file_output.close()
import os
os.system("python ping_ws.py")