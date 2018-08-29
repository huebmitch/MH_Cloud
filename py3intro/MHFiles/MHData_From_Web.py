import requests

url = "https://tdstelecom.com/"

response = requests.get(url)

for header_name, header_value, in response.headers.items():
    print(header_name, header_value)
print('-' * 60)

print(response.content.decode())