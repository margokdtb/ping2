import socket
import time

filename = "input.txt"
result = []

with open(filename, 'r') as file:
    lines = file.readlines()

for line in lines:
    data = line.strip().split()
    if data[2] == "200":
        host = data[0].split(":")[0]
        try:
            start_time = time.time()
            socket.create_connection((host, 80), timeout=1)
            result.append((host, time.time() - start_time))
        except ConnectionError:
            pass

sorted_result = sorted(result, key=lambda x: x[1])

with open("hasil2.txt", 'w') as output_file:
    for host, response_time in sorted_result:
        output_file.write(f"{host} - Time: {response_time:.2f} s\n")
        print(f"{host} - Time: {response_time:.2f} s")

print("Hasil telah disimpan di file hasil2.txt")