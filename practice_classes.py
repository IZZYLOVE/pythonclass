class Dog:
    '''a simple attempt to model a dog'''
    def __init__(self, name:str, age=1):
        '''initialize name and age attributes.'''
        self.name=name
        self.age=age

    def sit(self):
        '''simulates a dog sitting in response to a command'''
        print(f'{self.name} is now sitting.')

    def roll_over(self):
        '''simulates rolling over in response to a command'''
        print(f'{self.name} rollod over')
    def barking(self):
        '''simulates backing in response to a comand'''
        print(f'{self.name} is barking')
    def sleeping(self):
        '''simulates sleeping in response to a comand'''
        print(f'{self.name} is sleeping')
    def running(self):
        '''simulates running in response to a comand'''
        print(f'{self.name} is running')
    def playing(self):
        '''simulates playing in response to a comand'''
        print(f'{self.name} is playing')
    def eating(self):
        '''simulates eating in response to a comand'''
        print(f'{self.name} is eating')

mydog=Dog('Jack',6)
yourdog=Dog('Billy',5)

print(f"My dog's name is {mydog.name}.")
print(f"Your dog's name is {yourdog.name}.")
mydog.playing()
print('while')
yourdog.eating()
print('it is 11 am and')
mydog.sleeping()

print('\n')


class Item:
    # class attributes
    '''A class attribute is an attribute that belongs to the class
     itself but also accessible from the instance level as well '''
    # Eg pay_rate
    pay_rate=0.8 # The pay rate after 20% discount
    all=[]
    def __init__(self, name: str, price: float, quantity=1):
        '''initialize name and age attributes.'''
        #Run validations to the recieved arguments
        assert price >0, f"price {price} is not greater than zero"
        assert quantity>0, f"quantity {quantity} is not greater than zero"
        #assign to self ojects
        self.name=name
        self.price=price
        self.quantity=quantity
        # Actions to execute
        '''The comand below will append all instance into the list all'''
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        '''note the pay_rate is at the class level and can only be
        accessed from the class level and the instance level'''
        self.price=self.price*self.pay_rate
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

item1=Item("Phone", 100, 1)
item2=Item("Laptop", 1000, 3)

print("\ncalculating total price from instances")
print(item1.calculate_total_price())
print(item2.calculate_total_price())

# Accessing pay rate from the class level
print("\naccessing pay_rate from the class level")
print(Item.pay_rate)

# Accessing pay rate from the instance level
'''Note if the instance level doen't have an attribut, 
it will search for that attribute in the class .
Just as pay_rate is not in the instance level but item1 and item2 
will now search for pay_rate at the class level and access it 
if it is available'''

print("\naccessing pay_rate from the instance level")
print(item1.pay_rate)
print(item2.pay_rate)

'''Note we can use the magic attribute __dict__ to all atributes belonging to an object '''
print("\nShowing all the attributes for the class level")
print(Item.__dict__)
print("\nShowing all the attributes for the instance level")
print(item1.__dict__)
print(item2.__dict__)

'''Now let's apply the discount to overide the price attribute of 
an item'''
print("\napplying discount on price and printing the discounted price")
item1.apply_discount()
item2.apply_discount()
print(f"on 20% discount on {item1.name}, price is now {item1.price}")
print(f"on 20% discount on {item2.name}, price is now {item2.price}")

'''To have a different discount rate for a specific item, in this case
we have to assign that change to that specific item.
Say we want to apply 30% discount on the laptop instead of 20%'''

print("\nassigning item2 a different discont rate say 30%")
item1=Item("Phone", 100, 1)
item2=Item("Laptop", 1000, 3)
item2.pay_rate=0.7
item1.apply_discount()
item2.apply_discount()
print(f"on discount on {item1.name}, price is now {item1.price}")
print(f"on discount on {item2.name}, price is now {item2.price}")


item1=Item("Phone", 100, 1)
item2=Item("Laptop", 1000, 3)
item3=Item("Cable", 10, 5)
item4=Item("Mouse", 50, 5)
item5=Item("Keyboard", 75, 5)
print("\nList of the different instances that has been created and append to the list all")
print(Item.all)

print("\nAll the different instances that has been created and append to the list all")
for instance in Item.all:
    print(instance.name)