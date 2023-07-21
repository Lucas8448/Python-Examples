
# List Comprehension in Python

# Creating a list of squares using list comprehension
squares = [x**2 for x in range(10)]
print("Squares: ", squares)

# Creating a list of odd numbers using list comprehension with condition
odds = [x for x in range(10) if x % 2 != 0]
print("Odds: ", odds)
