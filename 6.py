import requests
import urllib3

urllib3.disable_warnings()

def send_custom_http_request(url, headers, payload):
    response = requests.get(url, headers=headers, data=payload, verify=False)
    return response

url = 'https://chat.xl.co.id'

headers = {
    'Host': 'api.myxl.xlaxiata.co.id',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Custom-Header': 'Value'
}

payload = {
    'data1': 'value1',
    'data2': 'value2'
}

response = send_custom_http_request(url, headers, payload)

if response.status_code == 200:
    print("Permintaan berhasil dengan status kode 200")
    print(response.content)
else:
    print("Permintaan gagal dengan status kode", response.status_code)