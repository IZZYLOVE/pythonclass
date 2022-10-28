#A program to take a list and
# give/return the first even number in the list
def myf(*args):
    print(args)
    x=0
    for i in args:
        i=int(i)
        #print(i%2)
        if i%2==0:
            x=i
            break
    if x != 0:
        x = f"The first even number in {args} is {i}"
    else:
        x = f"There is no even number in {args}"
    return (x)
#print(myf(2,5,7,9))



# mylist=[]
# print('Enter Q to finish!')
# x='on'
# while x =='on':
#     i=input('Enter another number or Q to finish: ')
#     if i.upper() != 'Q':
#         mylist.append(i)
#     else:
#         x='off'
# #print(mylist)
# print(myf(*mylist))



def mykwf(**kwargs):
    x=''
    for key, value in kwargs.items():
        #print(key)
        #print(value)
        #print(key, value)
        if x=='':
            x=value+' '+key
        else:
            x =x+', '+ value + ' ' + key
    return (f"Mr k, please process the following phone orders for shipment; {x}")


#A program to collect a user's set of keys and values,
# generate a dictionary and use that dictionary as argument for a given function.
# This program will detect when empty values are entered by the user,
# and will not call the function if the dictionary is empty
#
print('Generate a set of keywords and their related values...')
mydict={}
x='on'
while x =='on':
    a = input('Enter a keyword or Q to finish: ').strip()
    if a.upper() == 'Q':
        x='off'
    else:
        b = input('Enter value or Q to finish: ').strip()
        if b.upper() == 'Q':
            x='off'

    if x=='on' and a!='':
        mydict[a]=b
    else:
        x='off'
if len(mydict) >0:
    print(mydict)
    print(mykwf(**mydict))
else:
    print('Operation cancelled or Empty value(s) entered')
