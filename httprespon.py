import requests

url = input('Masukkan URL: ')
if not url.startswith('http://') and not url.startswith('https://'):
    url = 'http://' + url

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
response = requests.head(url, headers=headers)

print('\nResponse Status Code:', response.status_code)

print('Response Headers:')
for header in response.headers:
    print(header+":", response.headers[header])

