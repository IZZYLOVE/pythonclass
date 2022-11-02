

first_number=float(input("Enter first number"))
secnd_number=float(input("Enter first number"))
try:
    result=print(first_number / secnd_number)
except:
    print("You can not divide by zero")
else:
    print(result)



first_number=float(input("Enter first number"))
secnd_number=float(input("Enter first number"))
try:
    result=print(first_number / secnd_number)
except ZeroDivisionError:
    print("You can not divide by zero")
except ValueError:
    print("Please enter a number")
else:
    print(result)