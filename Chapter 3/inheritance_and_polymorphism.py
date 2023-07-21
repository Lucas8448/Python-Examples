
# Inheritance and Polymorphism in Python

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Creating objects
dog = Dog()
cat = Cat()

# Calling methods
print(dog.make_sound())
print(cat.make_sound())
