print('(1) A program to calculate the area of a circle.')
P=3.145
R=float(input('Enter radius '))
A=P*(R**2)
result=f"The are of a circle with Radius {R}cm is {A}cm squared"
print(result)

print(" \n ")

print('(2) Calculate a simple interest where pricipal, time and rate will be entered by the user.')
P=float(input('enter Principal '))
R=float(input('enter Rate '))
T=float(input('enter Time years '))
I=(P*R*T)/100
result=f"The simple interest is {I} "
print(result)

print(" \n ")

print('(3) A programme to calculate your age after 10 years.')
A=10+float(input('enter your corrent age '))
result=f"Your age after 10 years is {A} "
print(result)

print(" \n ")

print('(4) A programme to calculate the area of a triangle')
H=float(input('enter h '))
B=float(input('enter b '))
A=0.5*B*H
result=f"The area is {A}cm squared"
print(result)

print(" \n ")

print('(5) A programme to calculate the total price where quantity is given')
P=float(input('enter price in Naira '))
Q=float(input('enter quantity '))
T=B*H
result=f"The total price is {T} Naira "
print(result)

print(" \n ")

print("(6) A company added 5% to every employee's salary, enter the old salary and calculate the new salary")
Old=float(input('enter old salary '))
New=((5/100)*Old)+Old
result=f"The new salary is {New} "
print(result)

print(" \n ")

print('(7) A programme to convert from celcius to Fahrenheit.')
C=float(input('enter temperature in celcius '))

F=(C*(9/5))+32
result=f"The temperatere in Fahrenheit is {F} "
print(result)