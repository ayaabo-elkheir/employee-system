#example 1

class Animal:
    def speak(self):

        print("animal speaks")

class Mammal(Animal):
    def speak(self):

        print("mammal speaks")
        super().speak()

class Human(Animal):
    def speak(self):

        print("human speaks")
        super().speak()

class Employee(Mammal, Human):
    def speak(self):

        print("employee speaks")

        super().speak()

e = Employee()
e.speak()
#according to python MRO: Employee > Mammal> Human > Animal

#example 2

class Mammal:
    def eat(self):

        print("mammal eats plants")

class Human:
    def eat(self):
        print("human eats cooked food")

class Employee(Mammal, Human):

    pass

e = Employee()
e.eat()

#bec employee inherts from mammal first,Python do eat function in mammal first

#super()	follows the MRO in multiple inheritance
#in method conflict between classes	python does the first method found according to the MRO

