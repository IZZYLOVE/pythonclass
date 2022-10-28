greeting="Hello world"
print(greeting)

# use harsh for commemt

first_number = 8
second_number = 2
result=first_number+second_number
print(result)

print(result, "people said", greeting), print("my people", greeting, result)

greet=" Hello"*3
print(greet)

name=input('what is your name? ')

print( "hello "+name)

fcolor=input('what is your favourite color? ')
print( name+" likes "+fcolor)

first_name = 'kingdom'
last_name = 'adele'
full_name = first_name +' '+last_name
print(full_name)
#convert full name to upper case
print(full_name.upper())

# the f-string command
statement = f"my nane is {full_name}, i am from Port Harcourt"
print(statement)

#a program to add two numbers
first_number = 8
second_number = 9
result001=first_number+second_number
print(result001)

#a program to divide two numbers
first_number = 8
second_number = 9
result002=first_number/second_number
print(result002)

# using f string to format my name
first_name = 'kingdom'
last_name = 'adele'
full_name1 = f"{first_name} {last_name}"
print(full_name)


weight=float(input('enter weight : '))
unit =input('enter unit ( kg or Lbs ): ')
if unit.upper()== "KG":
    converted=weight/0.45
    print("weight in KG is "+str(converted))
elif unit.upper() == "LBS":
    converted=weight * 0.45
    print("weight in Lbs is "+str(converted))
else:
    print("error, unlisted unit ")


