import socket
import time

datahost = set()

def clear_file(filename):
    with open(filename, 'w') as file:
        file.write('')

clear_file('subdomain.txt')

def get_ip(host):
    try:
        start_time = time.time()  # Waktu awal sebelum pemanggilan gethostbyname
        ip = socket.gethostbyname(host)
        end_time = time.time()  # Waktu akhir setelah pemanggilan gethostbyname
        
        response_time = end_time - start_time  # Menghitung waktu respons
        
        if response_time > 2:
            raise TimeoutError("Connection timeout")
        
        return ip
    except TimeoutError:
        return None
    except:
        return None

def process_host(host):
    global datahost
    ip = get_ip(host)
    if ip:
        if ip not in datahost:
            with open('subdomain.txt', 'a') as file:
                file.write(host + '\n')
                print(host)
            datahost.add(ip)

def main():
    with open('subdomain2.txt', 'r') as file:
        hosts = file.read().splitlines()

    for host in hosts:
        process_host(host)

if __name__ == '__main__':
    main()