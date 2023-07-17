import socket
import threading

try:
    # Buka file dengan mode write
    with open("hasil_cdnssl2.tx", "w") as file:
        file.truncate(0)
    print("Proses.. ")
except FileNotFoundError:
    print("File tidak ditemukan")
except PermissionError:
    print("Tidak ada izin untuk menghapus isi file")
except Exception as e:
    print("Gagal menghapus isi file:", e)
    
def check_cloudflare_response(host, port):
    try:
        # Membuat koneksi socket ke server
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.settimeout(5)  # Batasan waktu maksimum 5 detik
        server_socket.connect((host, port))
        
        # Kirim permintaan GET
        request = f"GET / HTTP/1.1\r\nHost: {host}\r\nUpgrade: Websocket\r\nConnection: Keep-Alive\r\n\r\n"
        server_socket.sendall(request.encode())

        # Terima respons dari server
        response = server_socket.recv(4096).decode()
        
        if response.startswith('HTTP'):
            result = f"{host}:{port} OK"
        else:
            result = f"{host}:{port} Not Cloudflare"
    except socket.timeout:
        result = f"{host}:{port} not respon"
    except socket.error:
        result = f"{host}:{port} not respon"

    print(result)

    if "OK" in result:
        with open("hasil_cdnssl.txt", "a") as file:
            host_port = result.replace(":443 OK", "")
            file.write(host_port + "\n")

def main():
    try:
        with open("hasil2_direct.txt", "r") as file:
            hosts = file.read().splitlines()
    except FileNotFoundError:
        print("File hasil2_direct.txt tidak ditemukan")
        return

    port = 443

    threads = []

    for host in hosts:
        t = threading.Thread(target=check_cloudflare_response, args=(host, port))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
   
print("\n\n Hasil telah disimpan di file hasil_cdnssl.txt \n")