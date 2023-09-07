import re

with open('sumber/sumber_lain.txt', 'r') as file:
    data = file.read()
    subdomains = re.findall(r'\b(?:[A-Za-z0-9]+\.)+[A-Za-z]{2,}\b', data)
    ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', data)

with open('subdomain.txt', 'w') as output_file:
    for subdomain in subdomains:
        output_file.write(f"{subdomain}\n")
        print(f"{subdomain}")

    for ip in ips:
         output_file.write(f"{ip}\n")
         print(f"{ip}")

print("Hasil telah disimpan ke file subdomain.txt")