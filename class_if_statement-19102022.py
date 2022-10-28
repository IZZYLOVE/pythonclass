age=int(input('Enter age '))
country=input('enter country of birth ')
if age >= 18 and country.upper() == 'NIGERIA':
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')

print('\n')

fruits=['cucumber','cashew','kiwi','pinapple','apple']
ordered_fruits=input('order a fruit')
if ordered_fruits in fruits:
    print('your order is noted')
else:
    print('The requested fruit is not available')

print('\n')
score=float(input('Enter your score '))
if score > 100:
    print('Your grade is out of range')
elif score >= 70:
    print('Your grade is A')
elif score >= 60:
    print('Your grade is B')
elif score >= 50:
    print('Your grade is C')
elif score > 45:
    print('Your grade is D')
elif score >= 40:
    print('Your grade is E')
else:
    print('Your grade is F')

print('\n')
score = float(input('Enter your score '))
if score <=100:
    if score >= 70:
        print('Your grade is A')
    elif score >= 60:
        print('Your grade is B')
    elif score >= 50:
        print('Your grade is C')
    elif score > 45:
        print('Your grade is D')
    elif score >= 40:
        print('Your grade is E')
    else:
        print('Your grade is F')
else:
    print('Your grade is out of range')