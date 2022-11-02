class Nutrition:
    def eat(self):
        return 'dog food includes Garri, yam, rice, beans'


class Dog:
    kingdom=''
    family='animal'


    def __init__(self, name, color, age):
        self.name=name
        self.age=age
        self.color=color

    def bark(self):
        return f"{self.name} barks loudly"
    def description(self):
        return f"The name of my dog is {self.name}, my dog is {self.age} years old, my dos is {self.color} in color."


my_dog=Dog("Bingo", "Black", 12)
print(my_dog.description())
victor_dog=Dog('Perry','Red', 5)
print(victor_dog.description())


#creat nigerian_dog to inherit from the Oiginal class Dog
print("INHERITANCE")
class Nigrian_dog(Dog):
    def __init__(self, name, color, age):
        super().__init__(name, color, age)

    #to call another class from  a method in this class. say we creat a new class called Nutrition
    def food(self):
        self.diet=Nutrition()
        return self.diet

    def cough(self):
        return f"Nigerian dogs cough"
    #to overide a method inherited from the supper class, we redefine that method in the child class
    def bark(self):
        return f"{self.name} barks quietly"

my_dogn=Nigrian_dog("Bingo","blue",33)
print(my_dogn.description())
print(my_dogn.cough())
print(my_dog.bark())
print(my_dogn.bark())

print("CONTAINMENT")