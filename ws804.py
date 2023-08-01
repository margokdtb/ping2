print("\n\n SCAN WS PORT 80 \n")

import requests

url = 'http://idray.jagoan.vip'
timeout = 5 # Batas waktu tunggu dalam detik

# Baca file proxy
with open('hasil2_direct.txt', 'r') as file:
    proxy_list = file.read().splitlines()

headers = {
    'Host': 'idray.jagoan.vip',
    'Connection': 'Upgrade',
    'User-Agent': '[ua]',
    'Upgrade': 'websocket'
}

with open('hasil_websocket80.txt', 'w') as hasil_file:  # Buka file hasil
    for proxy in proxy_list:
        proxy_with_port = f'http://{proxy}:80'
        proxy2 = f'{proxy}'
        proxies = {
            'http': proxy_with_port
        }

        try:
            response = requests.head(url, proxies=proxies, headers=headers,  timeout=timeout)
            if response.status_code == 200:
                hasil = f'{proxy2} - Respon: {response.status_code}'
                hasil2 = f'{proxy2}\n'
                hasil_file.write(hasil2)
                print(hasil)
            else:
                print(f'{proxy2}, Invalid respon')
            # break  # Berhenti setelah mendapatkan respons yang berhasil
        except requests.exceptions.RequestException as e:
            print(f'{proxy2}: timeout')
        except requests.exceptions.Timeout:
            print(f'{proxy2}: timeout')
        except requests.exceptions.ProxyError:
            print(f'{proxy2}: not valid')