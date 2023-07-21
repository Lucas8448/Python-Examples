
# Lambda Functions in Python

# Defining a lambda function
add = lambda x, y: x + y

# Using the lambda function
print(add(3, 4))

# Using a lambda function in a higher-order function
numbers = [1, 2, 3, 4, 5]
squares = map(lambda x: x**2, numbers)
print(list(squares))
