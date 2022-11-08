import requests
import json
key='Zy3c1BVq6FWFjW1KM9U4w2dAteF1XwFy'
header={'apikey':key}
amount=input("Enter amount: ")
c_from=input("Enter the current currency: ")
c_to=input("Enter the desired currency: ")
url = f"https://api.apilayer.com/exchangerates_data/convert?to={c_to}&from={c_from}&amount={amount}"

data=requests.get(url, headers=header).json()

print(data)
input_parameters=data['query']
info_parameters=data['info']
result_parameters=data['result']
date_parameters=data['date']



print("your input parameters are as follows: ")
for key, value in input_parameters.items():
    print(f"{key}: {value}")

print("your info parameters are as follows: ")
for key, value in info_parameters.items():
    print(f"{key}: {value}")

print(f"your result is {result_parameters} ")
print(f"Date is {date_parameters} ")
