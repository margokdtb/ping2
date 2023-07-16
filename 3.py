import concurrent.futures
import socket

filename = "input.txt"
result = []

def check_response(host):
    try:
        with socket.create_connection((host, 80), timeout=1) as sock:
            response_time = sock.gettimeout()
            result.append((host, response_time))
    except ConnectionError:
        pass

with open(filename, 'r') as file:
    lines = file.readlines()

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for line in lines:
        data = line.strip().split()
        if data[2] == "200":
            host = data[0].split(":")[0]
            futures.append(executor.submit(check_response, host))

    for future in concurrent.futures.as_completed(futures):
        future.result()

sorted_result = sorted(result, key=lambda x: x[1])

with open("hasil2.txt", 'w') as output_file:
    for host, response_time in sorted_result:
        output_file.write(f"{host} -  Time: {response_time:.2f} s\n")
        print(f"{host} -  Time: {response_time:.2f} s")

print("\n\nHasil telah disimpan di file hasil3.txt\n")