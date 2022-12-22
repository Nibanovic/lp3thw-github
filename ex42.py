## Animal is-a object
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

class Person(object):

    def __init__(self, name):
        self.name = name
        self.pet = None

class Employee(Person):

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object):
    pass

class Halibut(Fish):
    pass

class Salmon(Fish):
    pass

rover = Dog("Rover")
satan = Cat("Satan")

mary = Person("Mary")
mary.pet = satan

frank = Employee("Frank", 1234)
frank.pet = rover

flipper = Fish()
