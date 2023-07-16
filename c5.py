import os
import re
import subprocess

with open('input.txt', 'r') as f:
    with open('hasil2.txt', 'w') as f2:
        for line in f:
            ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)[0]
            print(ip)
            response = subprocess.Popen(['ping', '-c', '1', ip], stdout=subprocess.PIPE).communicate()[0]
            time = re.findall(r'time=([0-9]+\.?[0-9]*)', str(response))[0]
            print(f'{ip} - {time} ms')
            f2.write(f'{ip} - {time} ms\n')
