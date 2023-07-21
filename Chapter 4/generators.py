
# Generators in Python

# A simple generator function
def my_generator():
    i = 0
    while True:
        yield i
        i += 1

# Creating a generator
gen = my_generator()

# Generating some numbers
print(next(gen))
print(next(gen))
print(next(gen))
