#A program to check if a number is a perfect square or not
print('Check if a number is a perfect square or not')
num=int(input('Enter a number: '))
sq=num**(0.5)
if sq%1 == 0:
    print("perfect square")
else:
    print("Not a perfect square")


print('')
# C=float(input('Enter value for C: '))
# if C == 0.1 or C==0.5 or C==0.6 or C==0.8:
#     Pw = float(input('Enter value for water density(Pw): '))
#     Pa = float(input('Enter value for air density(Pa): '))
#     R = float(input('Enter value for air radius(R): '))
#     pi=(22/7)
#     g=9.8
#     V=(4/3)*pi*(R**3)
#     A=pi*(R**2)
#     Fg = V * Pw * g
#     Vt=((2*Fg)/(C*Pa*A))**(1/2)
#
#
#     print(F"Fg={Fg}")
#     print(F"V={V}")
#     print(F"A={A}")
#     print(F"Vt={Vt}")
# else:
#     print(F"{C} is not accepted only 0.1, 0.5, 0.6 or 0.8 will be accepted")

#A program to find the Highest Common Fraction (HCF) of two number
print("\nFind Highest Common Fraction")
N1 = int(input('Enter first number: '))
N2 = int(input('Enter second number: '))
if N1>=N2:
    A=N1
    B=N2
else:
    A=N2
    B=N1
x=0
while x==0:
    if A%B ==0:
        C=A%B
        HCF=B
        x=1
    else:
        C=A%B
        A=B
        B=C
#print(C)
print(HCF)

