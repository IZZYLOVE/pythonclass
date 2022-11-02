
#assignment operators
firs_number=8
firs_number +=4
print(firs_number)

firs_number=8
firs_number -=4
print(firs_number)


firs_number=8
firs_number *=4
print(firs_number)

firs_number=8
firs_number /=4
print(firs_number)

#arithmetic operators
#the + operator
firs_number=8
second_number =4
result=firs_number+second_number
print(result)

#the - operator
firs_number=8
second_number =4
result=firs_number-second_number
print(result)

#the * operator
firs_number=8
second_number =4
result=firs_number*second_number
print(result)

#the / operator
firs_number=8
second_number =4
result=firs_number/second_number
print(result)

#the % operator
firs_number=8
second_number =4
result=firs_number%second_number
print(result)

#the ** operator
firs_number=8
second_number =4
result=firs_number**second_number
print(result)


print("class work")
P=float(input('enter P '))
R=float(input('enter R '))
T=float(input('enter T '))
I=(P*R*T)/100
A=I+P
print("Simple interest is " + str(I) + " and the amount is "+ str(A))

result=f"the interest is {I} and the amount is {A}"
print(result)


#A program to solve quadratic equation
print('A program to solve quadratic equation')
a=float(input('enter a '))
b=float(input('enter b '))
c=float(input('enter c '))
x1=(-b+(b**2-4*a*c)**(1/2))/(2*a)
x2=(-b-(b**2-4*a*c)**(1/2))/(2*a)
roots=f"x1 = {x1} and x2 = {x2}"
print(roots)



#A program to solve equation
print('A program to solve quadratic equation')
R=8.314
T=float(input('enter T '))
b=float(input('enter b '))
v=float(input('enter v '))
a=float(input('enter a '))

P=((R*T)/(v-b))-((a)/(v**2))
roots=f"P = {P} "
print(roots)