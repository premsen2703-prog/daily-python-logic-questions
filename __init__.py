#__init__ is the constructor method in Python. It is called when an object is created from a class and allows the class to initialize the attributes of the class.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("prem", 21)
print(p1)
