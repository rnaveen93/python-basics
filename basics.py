print("Hello World")

first_name = "Naveen"
last_name = "Kumar"

full_name =f"{first_name} {last_name}"
print(f"Hello {full_name.title()}!")

apostrophe_use = "One of python's strength is its diverse community"
print(apostrophe_use)

# String concatenation
first_name = "Naveen"
last_name = "Kumar"
full_name = first_name + " " + last_name
print(full_name)
# String methods
print(full_name.title())  # Title case
print(full_name.upper())  # Upper case  
print(full_name.lower())  # Lower case
# Stripping whitespace
favorite_language = " python "
print(favorite_language)
favorite_language.rstrip()  # Removes trailing whitespace   
favorite_language.lstrip()  # Removes leading whitespace
favorite_language.strip()  # Removes leading and trailing whitespace
# Using variables in strings

#Numbers
# Integers
age = 23
print(f"Happy {age}rd Birthday!")
# Float
height = 5.9
print(f"Your height is {height} feet.")
# Arithmetic operations
addition = 5 + 3
subtraction = 10 - 2
multiplication = 4 * 2
division = 16 / 2
print(f"Addition: {addition}, Subtraction: {subtraction}, Multiplication: {multiplication}, Division: {division}")
# Using underscores in large numbers
large_number = 1_000_000
print(f"Large number with underscores: {large_number}")
# Constants
PI = 3.14159
print(f"Value of PI: {PI}")


# Lists
# Creating a list
fruits = ["apple", "banana", "cherry"]
print(f"Fruits: {fruits}")

# Accessing elements in a list
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# Modifying elements in a list
fruits[1] = "orange"
print(f"Modified fruits: {fruits}")

# Adding elements to a list
fruits.append("grape")
print(f"Fruits after appending: {fruits}")

# Removing elements from a list
fruits.remove("orange")
print(f"Fruits after removing orange: {fruits}")

# Sorting a list
fruits.sort()
print(f"Sorted fruits: {fruits}")

# Reversing a list
fruits.reverse()
print(f"Reversed fruits: {fruits}")

# List slicing
print(f"First two fruits: {fruits[:2]}")
print(f"Last two fruits: {fruits[-2:]}")

# List length
print(f"Number of fruits: {len(fruits)}")

# List comprehension
squared_numbers = [x**2 for x in range(10)]
print(f"Squared numbers: {squared_numbers}")

#Loop the list
magicians = ["Alice", "David", "Eve"]
for magician in magicians:
    print(f"Magician name is {magician}\n")

# Looping through a list with index
for index, fruit in enumerate(fruits):
    print(f"Fruit {index + 1}: {fruit}")

# Looping through a list with range
for i in range(len(fruits)):
    print(f"Fruit {i + 1}: {fruits[i]}")

# Looping through a list
for fruit in fruits:
    print(f"Fruit: {fruit}")


# Numberical list, prnts from 1 to 5
for value in range(1, 6):
    print(value)

#List of numbers
print("\nList of numbers:")
numbers = list(range(1, 6))
print(numbers)


#List of even numbers
print("\nList of even numbers:")
numbers = list(range(2, 10, 2))
print(numbers)

#Squares of numbers
print("\nSquares of numbers:")
squares = []
for values in range(1, 11):
    square = values ** 2
    squares.append(square)
print(squares)

#Squares of numbers - consise
print("\nSquares of numbers:")
squares = []
for values in range(1, 11):
    squares.append(values ** 2)
print(squares)

#Simple statistics with list of numbers

print("\nSimple statistics with list of numbers:")
numbers = list(range(1, 11))
print(f"Numbers: {numbers}")
print(f"Min {min(numbers)}")
print(f"Max {max(numbers)}")
print(f"Sum {sum(numbers)}")

# List comprehensions
print("\n List comprehensions:")

squares = [value ** 2 for value in range(1, 11)]
print(squares)

print("\n square of even numbers list comprehensions:")
even_sqaures = [value ** 2 for value in range(2, 11, 2)]
print(even_sqaures)


#List slicing
players_list = ['Naveen', "Kumar", "Alice", "Bob", "Charlie"]
print(f"Print first three players:{players_list[:3]}")

#Copying a list
my_foods =["pizza", "burger", "meals"]

breakfast = my_foods[:]
print(f"BreakFast: {breakfast}")
print(f"my_foods:{my_foods}")

breakfast.append("Idli")
print(f"BreakFast: {breakfast}")
print(f"my_foods:{my_foods}")
