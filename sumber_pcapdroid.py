import csv

file_path = "sumber/sumber_pcapdroid.txt"
output_file_path = "temp1.txt"

ip_list = []
host_list = []

with open(file_path, "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    
    for row in csv_reader:
        src_ip = row[1]
        dst_ip = row[3]
        host = row[9]
        
        ip_list.append(src_ip)
        ip_list.append(dst_ip)
        host_list.append(host)

print("IP Addresses:")
for ip in ip_list:
    print(ip)
    
print("\nHosts:")
for host in host_list:
    print(host)

# Simpan hasil ke file
with open(output_file_path, "w") as output_file:
    output_file.write("IP Addresses:\n")
    for ip in ip_list:
        output_file.write(ip + '\n')
    
    output_file.write("\nHosts:\n")
    for host in host_list:
        output_file.write(host + '\n')
        
        
#membuat file unik
with open("temp1.txt", "r") as file:
    lines = file.read().splitlines()
    unique_hosts = set()
    unique_ips = set()
    for line in lines:
        if line.startswith("IP"):
            continue
        elif line.startswith("Host"):
            continue
        elif line.startswith(" "):
            if '.' in line:
                unique_ips.add(line.strip())
            else:
                unique_hosts.add(line.strip())
        else:
            if '.' in line:
                unique_ips.add(line.strip())
            else:
                unique_hosts.add(line.strip())

with open("subdomain.txt", "w") as file:
    #file.write("Unique IP Addresses:\n")
    for ip in unique_ips:
        file.write(ip + "\n")

    #file.write("\nUnique Hosts:\n")
    for host in unique_hosts:
        file.write(host + "\n")

print("Data tersimpan dalam file subdomain.txt.")