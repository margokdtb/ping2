print("\n\n CEK PROXY \n")
print("\n Format Proxy ->> host:port \n")
import requests

proxy = input('Masukkan proxy : ').strip()

if ':' in proxy:
    host, port = proxy.split(':')
    proxies = {
        'http': f'http://{host}:{port}'
    }
else:
    proxies = {
        'http': f'http://{proxy}:80'
    }

url = 'http://api.myxl.xlaxiata.co.id'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

try:
    response = requests.head(url, headers=headers, proxies=proxies, timeout=5)  # Batasi waktu respon menjadi 5 detik
    
    print('\nResponse Status Code:', response.status_code)

    print('Response Headers:')
    for header in response.headers:
        print(header+":", response.headers[header])
        
except requests.exceptions.RequestException as e:
    #print("\nError:", e)
    print("Proxy Not Respon")