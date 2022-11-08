import json
import re
import requests

key = 'Zy3c1BVq6FWFjW1KM9U4w2dAteF1XwFy'
header = {'apikey': key}

url = f"https://api.apilayer.com/exchangerates_data/convert?to={c_to}&from={c_from}&amount={amount}"
data = requests.get(url, headers=header).json()
print("\n")
checkerror = data.get('error')  # Using .get querry method to get respone of none instead of row error
success = data.get('success')  # Using .get querry method to get respone of none instead of row error
if success == True:
    if fname != '':  # Formating file name and generating write or not switch
        filename = f"{fname}.txt"
        write = 'on'
    else:
        filename = ''
        write = 'off'
    input_parameters = data['query']
    info_parameters = data['info']
    result_parameters = data['result']
    date_parameters = data['date']
    mytxt = "YOUR INPUT PARAMETERS ARE AS FOLLOW: "
    print(mytxt)
    Mytxt = f"{mytxt}"  # Adding/appending evey print statement to a variable, to write when ready
    for key, value in input_parameters.items():
        mytxt = f"{key}: {value}"
        print(mytxt)
        Mytxt = f"{Mytxt} \n{mytxt}"

    mytxt = "\nYOUR INFO PARAMETERS ARE AS FOLLOWS: "
    print(mytxt)
    Mytxt = f"{Mytxt} \n{mytxt}"

    for key, value in info_parameters.items():
        mytxt = f"{key}: {value}"
        print(mytxt)
        Mytxt = f"{Mytxt} \n{mytxt}"

    mytxt = f"result: {result_parameters} "
    print(mytxt)
    Mytxt = f"{Mytxt} \n{mytxt}"

    mytxt = f"date: {date_parameters} "
    print(mytxt)
    Mytxt = f"{Mytxt} \n{mytxt}"

    if write == 'on':  # Using the write or not switch to write if the switch is on/(file name is given)
        with open(filename, 'w') as file_object:  # file write block
            file_object.write(str(Mytxt))

elif checkerror != 'None':
    check_message = data['error'].get('message')
    print(f"{check_message}")


convert(1, 'usd', 'ngn')