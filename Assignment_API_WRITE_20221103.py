
import requests
import json
key='Zy3c1BVq6FWFjW1KM9U4w2dAteF1XwFy'
header={'apikey':key}
amount=input("Enter amount: ")
c_from=input("Enter the current currency: ").upper()
c_to=input("Enter the desired currency: ").upper()
fname=input("Enter file name: ")
url = f"https://api.apilayer.com/exchangerates_data/convert?to={c_to}&from={c_from}&amount={amount}"

data=requests.get(url, headers=header).json()
print("\n")
print(data)
filename=f"{fname}.txt"


input_parameters=data['query']
info_parameters=data['info']
result_parameters=data['result']
date_parameters=data['date']



mytxt="your input parameters are as follows: "
print(mytxt)
with open(filename, 'w') as file_object:
    file_object.write(str(mytxt))
for key, value in input_parameters.items():
    mytxt=f"{key}: {value}"
    print(mytxt)
    with open(filename, 'w') as file_object:
        file_object.write(str(mytxt))

print('\n')
mytxt="your info parameters are as follows: "
print(mytxt)
with open(filename, 'w') as file_object:
    file_object.write(str(mytxt))

for key, value in info_parameters.items():
    mytxt=f"{key}: {value}"
    print(mytxt)
    with open(filename, 'w') as file_object:
        file_object.write(str(mytxt))

mytxt=f"your result is {result_parameters} "
print(mytxt)
with open(filename, 'w') as file_object:
    file_object.write(str(mytxt))

mytxt=f"Date is {date_parameters} "
print(mytxt)
with open(filename, 'w') as file_object:
    file_object.write(str(mytxt))
