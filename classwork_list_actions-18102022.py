fruits=[]
fn=input('enter first name ')
sn=input('enter second name ')
f1=input('enter first fruit')
#to add a new item to a list
fruits.append(f1)
print(fruits)

f2=input('enter fsecond fruit')

fruits.append(f2)
print(fruits)
f3=input('enter third fruit ')

fruits.append(f3)
print(fruits)

result=f"Mr {fn} {sn}'s favourite fruits are {fruits}  "
print(result)


fr=input('enter fruit to remove ')
fruits.remove(fr)
print(fruits)