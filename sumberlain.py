import json

# Load data from sumberlain.txt
with open("sumber_knock.txt", "r") as file:
    data = json.load(file)

# Create empty lists for hosts and IPs
hosts = []
ips = []

# Extract host and IP from each item in data
for key, value in data.items():
    host = key
    ip = value.get('ipaddr', [])  # Use get() method with default value [] if 'ipaddr' key is not present
    
    # Add host and IP to the respective lists
    hosts.append(host)
    ips.extend(ip)

# Save the results to subdomain.txt
with open("subdomain2.txt", "w") as file:
    file.write("Hosts:\n")
    for host in hosts:
        file.write(host + "\n")
    file.write("\nIPs:\n")
    for ip in ips:
        file.write(ip + "\n")
        
import os
os.system("python unik3.py")

print("\n Processing completed. The results have been saved to subdomain.txt.")