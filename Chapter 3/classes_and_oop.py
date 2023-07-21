
# Classes and Object-Oriented Programming in Python

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

# Creating an object
john = Person("John Doe", 30)

# Calling a method
john.greet()
