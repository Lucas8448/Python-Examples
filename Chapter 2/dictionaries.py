
# Dictionaries in Python

# Creating a dictionary
person = {
    "name": "John Doe",
    "age": 30,
    "height": 5.9
}
print("Person: ", person)

# Accessing dictionary elements
print("Name: ", person["name"])

# Modifying dictionary elements
person["name"] = "Jane Doe"
print("Person: ", person)

# Adding elements to the dictionary
person["weight"] = 70
print("Person: ", person)

# Removing elements from the dictionary
del person["height"]
print("Person: ", person)
