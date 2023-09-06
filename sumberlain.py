def extract_host_ip(data):
    host_ip_list = []
    lines = data.split('\n')
    for line in lines:
        line = line.strip()
        if line:
            if ' - ' in line:
                host_ip = line.split(' - ')[-1].strip()
                host_ip_list.append(host_ip)
            elif '.' in line:
                host_ip_list.append(line)
    return host_ip_list

filename = "sumber/sumber_lain.txt"
output_filename = "subdomain.txt"

with open(filename, "r", encoding="latin-1") as file:
    data = file.read()

host_ip_list = extract_host_ip(data)

with open(output_filename, "w") as file:
    for host_ip in host_ip_list:
        file.write(host_ip + "\n")