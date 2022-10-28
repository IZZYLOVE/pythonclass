class Dog:
    '''a simple attempt to model a dog'''
    def __init__(self, name, age):
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
