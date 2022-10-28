# for i in range(1, 6):
#     print(i)
#
# for i in range(20, 0, -1):
#         print(i)
#
# fruits=['Orange', 'Pear', 'Mango', 'Apple', 'Pineapple']
# for i in range (len(fruits)):
#     print(fruits[i])
#
# #anther way to printout everything in a list
# for fruit in fruits:
#     print(fruits)

# #class work
#
# mynum=[]
# for i in range(0, 17):
#     mynum.append(i)
#
# for v in mynum:
#     v=int(v)
#     if v%2 == 0:
#         print(f"{v} is even")
#     else:
#         print(f"{v} is odd")

#
# fn=input('Enter first name ')
# ln=input('Enter lasr name ')
# mynum=[]
# i=1
# for i in range(1, 6):
#     f1=input(f'Enter fruit {i} ')
#     mynum.append(f1)
#
# print(mynum)

#
# #fruits=['Mango', 'Cashew', 'Kiwi', 'Pinapple', 'Apple', 'Water-melon', 'guava', 'Cucumber', 'Banana']
# acailable_fruits=['Cashew', 'Guava', 'Apple', 'Mango', 'Cucumber']
# order=[]
# print("Make your order")
# nit=int(input("enter number of item: "))
# for i in range(nit):
#     fruit=input('Enter fruit name: ')
#     if fruit in acailable_fruits:
#         order.append(fruit)
#         print(f"{fruit} has been added to your cart")
#     else:
#         print(f"Your ordered items are: {order}")
#
#
#

print('\n(1) A program to evaluate the summation from statr to end')
st=int(input('Enter start number '))
ed=int(input('Enter end number '))
for i in range(st, ed+1):
    print(i)
    st=st+i

print(st)

print('\n(2) A program to calculate the factorial of any number')


print('\n(3) A program that would prompt for number of entries of numbers, and prompt you to enter each number and calculates the average of the number entered')
