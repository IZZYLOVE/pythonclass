import requests
import json

key = 'UMMiEijAVJWnx3BCLZwSockJeM7qfCcd'
header = {'apikey': key}
payload = {}
c_from="USD"
c_to="NGN"
amount=1
url = f"https://api.apilayer.com/exchangerates_data/convert?to={c_to}&from={c_from}&amount={amount}"
response = requests.get(url, headers=header, data = payload)
print(response.status_code)
#data=response.json()
data = json.load(response.text)
print(data)

#print(data.key())
print('\n')
for key, value in data.items():
    print(key, value)
