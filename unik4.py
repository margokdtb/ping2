import concurrent.futures
import socket

datahost = set()

def clear_file(filename):
    with open(filename, 'w') as file:
        file.write('')

# Menghapus isi file subdomain.txt sebelum memulai proses pencarian IP
clear_file('subdomain.txt')

def get_ip(host):
    try:
        ip = socket.gethostbyname(host)
        return ip
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

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(process_host, hosts)

if __name__ == '__main__':
    main()