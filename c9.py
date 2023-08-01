import http.client
import time
import socket

def clear_file():
    with open("hasil_ws80.txt", "w") as file:
        file.write("")

def send_get_request(host, port):
    try:
        conn = http.client.HTTPConnection(host, port, timeout=3)
        
        headers = {"Host": "api.myxl.xlaxiata.co.id", "Connection": "Keep-Alive",
                   "User-Agent": "[ua]", "Upgrade": "websocket"}
        
        start_time = time.time()
        
        conn.request("GET", "/", headers=headers)
        
        res = conn.getresponse()
        
        end_time = time.time()
        duration = end_time - start_time
        
        with open("hasil_ws80.txt", "a") as file:
            if duration is not None:
                file.write("{}, respon: {:.2f} s, Status: {}\n".format(host, duration, res.status))
                print("{}, respon: {:.2f} s, Status: {}".format(host, duration, res.status))
            else:
                file.write("{}, respon: Timeout, Status: {}\n".format(host, res.status))
                print("{}, respon: Timeout, Status: {}".format(host, res.status))
        
        conn.close()
    except socket.timeout:
        with open("hasil_ws80.txt", "a") as file:
            file.write("{}, respon: Timeout, Status: Timeout\n".format(host))
        print("{}, respon: Timeout, Status: Timeout".format(host))

file_path = "hasil2_direct.txt"
hosts = []
with open(file_path, "r") as file:
    hosts = file.readlines()
hosts = [host.strip() for host in hosts]

clear_file()  # Membersihkan isi file hasil_ws80.txt

for host in hosts:
    send_get_request(host, 80)
   
  
print("\n\nHasil telah disimpan di file hasil_ws80.txt\n")
