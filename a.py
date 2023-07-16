
from ping3 import ping

def ping_host(host):
    try:
        response_time = ping(host)
        if response_time is not None:
            return {"host": host, "response_time": response_time}
        else:
            return {"host": host, "response_time": float("inf")}
    except Exception as e:
        return {"host": host, "response_time": float("inf")}

host_list = []
# Baca sumber dari file
with open("zxy2.txt", "r") as file:
    for line in file:
        host_list.append(line.strip())

# Lakukan ping ke setiap host dan simpan hasilnya dalam list
ping_results = []
for host in host_list:
    result = ping_host(host)
    ping_results.append(result)

# Urutkan hasil berdasarkan waktu respons
sorted_results = sorted(ping_results, key=lambda x: x["response_time"])


# Simpan hasil ke file hasil2.txt
with open("hasil2.txt", "w") as file:
    for result in sorted_results:
        file.write(f"{result['host']} - {result['response_time']:.2f} ms\n")




