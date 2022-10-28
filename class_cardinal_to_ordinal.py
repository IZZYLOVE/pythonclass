
print(f"A program that converts cardinal numbers to ordinal numbers")
def CtoO():
    prompt=input('Enter a number: ')
    last_digit=prompt[-1]

    if (len(prompt))>1:
        last_digit2=prompt[-2]
    else:
        last_digit2=0
    suffix=''
    if int(prompt)==0:
        suffix=' is not accepted'
    elif int(last_digit2)==1:
        suffix='th'
    elif int(last_digit)==1:
        suffix='st'
    elif int(last_digit)==2:
        suffix='nd'
    elif int(last_digit)==3:
        suffix='rd'
    else:
        suffix = 'th'
    print(f"{prompt}{suffix}")
CtoO()