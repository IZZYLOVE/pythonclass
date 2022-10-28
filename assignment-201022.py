print('\n(1) A program to evaluate the summation from statr to end.')
st=int(input('Enter start number '))
ed=int(input('Enter end number '))
sum=0
for i in range(st, ed+1):
    #print(i)
    sum=sum+i

print(f"The summation of {st} and {3} from start to end respectively is {sum}")


print('\n(2) A program to calculate the factorial of any number.')
n=int(input("enter a number: "))
F=1
for i in range(n, 0, -1):
    F=F*i
    #print(i)
print(f"The factorial of {n} is {F}")


print('\n(3) A program that would prompt for number of entries of numbers, and prompt you to enter each number and calculates the average of the number entered.')
nit=int(input("enter number of entries: "))
n=0
for i in range(1, nit+1):
    num=float(input(f'Enter number {i}: '))
    n=n+num
m=n/nit
print(f"The summation of entered numbers is {n} and the mean is {m}")

print('\n(4) A program to accept five numbers and calculate the sum of their squares.')
n=0;
for i in range(1, 6):
    num=float(input(f'Enter number: '))
    nums=(num*num)
    n=n+(nums)
    print(f"the squere of {num} is {nums}")
print(f"The summation of the squares of entered numbers is {n}")

print('\n(5) A program to accept a number and confirm if the number is a prime number or not, odd number or even number.')
n = int(input(f'Enter number: '))
#check if number is odd
if n%2 == 0:
    p='an even number'
else:
    p = 'an odd number'
#check if number is prime
x=0
for i in range(2, n):
    v=n%i
    #print(v)
    if v == 0:
        x=x+1
if x==0:
    print(f"The numbers {n} is a prime number and the number {n} is {p}")
else:
    print(f"The numbers {n} is not a prime number but the number {n} is {p}")


print('\n(6) A program to accept a number of fruits, prompt for the fruit names, \ncheck if entry already exist, if yes, prompts for correction, \nand finally at the end of collecting these entries, prints out the list. (limited to for loop)')

fn=input('Enter your first name ')
ln=input('Enter your lasr name ')
mynum=[]
i=1
n=int(input('Enter number of items '))
for i in range(1, n+1):
    f1=input(f'Entry {i}, enter fruit name ')
    if f1 in mynum:
        print(f"The fruit {f1} is already entered")
        f1 = input(f'Entry {i}, enter fruit name ')
        if f1 in mynum:
            print(f"The fruit {f1} is already entered")
            f1 = input(f'Entry {i}, enter fruit name ')
            if f1 in mynum:
                print(f"The fruit {f1} is already entered")
                f1 = input(f'Entry {i}, enter fruit name ')
                if f1 in mynum:
                    print(f"The fruit {f1} is already entered")
                    print(f"Last attempt to correct entry {i}, any error skips correction of entry {i}!")
                    f1 = input(f'Enter unlisted fruit name to correct entry {i} ')
                    if f1 in mynum:
                        print(f"Entry {i} correction skipped")
                    else:
                        print(f"Correction done for entry {i}")
                        mynum.append(f1)
                else:
                    print(f"Correction done for entry {i}")
                    mynum.append(f1)
            else:
                print(f"Correction done for entry {i}")
                mynum.append(f1)
        else:
            print(f"Correction done for entry {i}")
            mynum.append(f1)
    else:
        mynum.append(f1)
print(mynum)