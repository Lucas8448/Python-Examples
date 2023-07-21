
# Exception Handling in Python

try:
    # Attempt to divide by zero
    print(10 / 0)
except ZeroDivisionError as e:
    print("Error: ", e)

# Using finally
try:
    print("Hello")
finally:
    print("This line is always printed.")
