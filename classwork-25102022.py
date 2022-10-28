a=float(input('Enter a '))
b=float(input('Enter b '))
c=float(input('Enter c '))
def sulve():
    x1= -b-((b**2)-(4*a*c))**(1/2)/(2*a)
    x2= +b-((b**2)-(4*a*c))**(1/2)/(2*a)
    x=f"{x1} and {x2}"
    return x
result=sulve()
print(result)