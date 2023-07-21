
# Error and Exception Handling in Python

try:
    # Attempt to divide by zero
    print(10 / 0)
except ZeroDivisionError as e:
    print("Error: ", e)

# Raising an exception
raise ValueError("This is a custom error message.")
