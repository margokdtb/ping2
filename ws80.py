print("\n\n SCAN WS PORT 80 \n")

import socket

def send_request(hosts, payload):
    with open('hasil_websocket80.txt', 'w') as file:
        for host in hosts:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2)
                s.connect((host, 80))

                request = f'HEAD / HTTP/1.1\r\nHost: idray.jagoan.vip\r\nUpgrade: websocket\r\n\r\n'
                s.send(request.encode())

                response = s.recv(4096)
                response_decoded = response.decode()
                status_line = response_decoded.split('\r\n')[0]
                status_code = status_line.split()[1]

                server_header = None
                if 'Server: ' in response_decoded:
                    server_header = response_decoded.split('Server: ')[1].split('\r\n')[0]

                result = f'{host} - {status_code} - {server_header if server_header else "Unknown"}'
                result2 = f'{host}'
                print(result)

                if status_code == '200' and server_header == 'cloudflare':
                    file.write(result2 + '\n')

                #s.send(payload.encode())

                s.close()
            except socket.gaierror:
                print(f'{host} - Invalid hostname')
            except socket.timeout:
                print(f'{host} - timeout')

hosts = []

with open('hasil2_direct.txt', 'r') as file:
    for line in file:
        hosts.append(line.strip())

payload = 'payload data yang ingin dikirim'

send_request(hosts, payload)


# Cek port 443 
import os
os.system("python3 wsssl.py")