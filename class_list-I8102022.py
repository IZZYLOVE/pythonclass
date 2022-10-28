import math
print(math.sqrt(4))

from math import sqrt

print(sqrt(9))

a=1
b=4
c=1
x=(-b+(math.sqrt(b**2-4*a*c)))/(2*a)
print(str(x))
print('\n')

print(math.sin(30*math.pi/180))
print('\n')

print(math.sin(math.radians(30)))
print('\n')
print(math.log10(100))

print('\n')
print('dealing with a exponential')
y=math.exp(2)
print(y)

print('\n')
print('TOPIC: LIST')
fruit='orange'

#for a list
fruits=['Oronge', 'Strawberry', 'Guava', 'Casgew', 'Mango']
print(fruits)

print('\n')
# select a single item in a list we use index
# the index in python starts from 0
print(fruits[0])


#to add a new item to a list
fruits.append('Blackberry')
print(fruits)


#to add a new item to a list
print("append left")
fruits.appendleft('Blackberr0')
print(fruits)

#to replace an item in a lista
fruits[3]='apple'
print(fruits)



#to remove an item in a list
del fruits[3]
print(fruits)

#to select a set of items from a list
print(fruits[1:6])

#to remove the last item in a list
print(fruits.pop())

#to remove an item in a list with the pop function we add the index
print(fruits.pop(2))


