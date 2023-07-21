
# Sets in Python

# Creating a set
fruits = {"apple", "banana", "cherry"}
print("Fruits: ", fruits)

# Adding elements to the set
fruits.add("dragonfruit")
print("Fruits: ", fruits)

# Removing elements from the set
fruits.remove("banana")
print("Fruits: ", fruits)

# Set operations
other_fruits = {"cherry", "date", "elderberry"}
print("Intersection: ", fruits & other_fruits)
print("Union: ", fruits | other_fruits)
print("Difference: ", fruits - other_fruits)
