# Python CheatSheet 🐍

A comprehensive Python reference guide covering fundamentals to advanced concepts. Perfect for beginners and as a quick reference for experienced developers.

## Table of Contents

- [Basics](#basics)
- [Data Types](#data-types)
- [Math Operations](#math-operations)
- [Error Handling](#error-handling)
- [Functions](#functions)
- [Conditionals](#conditionals)
- [Loops](#loops)
- [List Methods](#list-methods)
- [Built-in Functions](#built-in-functions)
- [Modules](#modules)
- [Classes & Objects](#classes--objects)

---

## Basics

### Print
Prints a string to the console.
```python
print("Hello World")
```

### Input
Gets user input from the console.
```python
name = input("What's your name? ")
```

### Comments
Use `#` to add comments (ignored by Python).
```python
# This is a comment
print("This is code")  # Inline comment
```

### Variables
Store data with descriptive names.
```python
my_name = "Angela"
my_age = 12
```

### The += Operator
Convenient way to modify variables.
```python
my_age = 12
my_age += 4  # my_age is now 16
```

---

## Data Types

### Integers
Whole numbers without decimal points.
```python
my_number = 354
```

### Floating Point Numbers
Numbers with decimal places.
```python
my_float = 3.14159
# Division always returns a float
result = 4 / 3  # Returns 1.3333...
```

### Strings
Sequence of characters enclosed in quotes.
```python
my_string = "Hello"
```

### String Concatenation
Combine strings using the `+` operator.
```python
result = "Hello" + "Angela"  # "HelloAngela"
```

### Escaping Strings
Use backslash `\` to include special characters.
```python
speech = "She said: \"Hi\""
print(speech)  # Prints: She said: "Hi"
```

### F-Strings
Insert variables into strings.
```python
days = 365
print(f"There are {days} days in a year")
```

### Converting Data Types
```python
# Converting to different types
n = 354
new_n = float(n)     # 354.0
text = str(n)        # "354"
integer = int(3.14)  # 3
```

### Checking Data Types
```python
n = 3.14159
print(type(n))  # <class 'float'>
```

---

## Math Operations

### Arithmetic Operators
```python
3 + 2    # Addition: 5
4 - 1    # Subtraction: 3
2 * 3    # Multiplication: 6
5 / 2    # Division: 2.5
5 ** 2   # Exponent: 25
```

### The Modulo Operator
Returns the remainder after division.
```python
5 % 2    # Returns 1
# Useful for checking odd/even numbers
```

### Assignment Operators
```python
my_number = 4
my_number += 2   # Add: 6
my_number -= 1   # Subtract: 5
my_number *= 3   # Multiply: 15
my_number /= 5   # Divide: 3.0
```

---

## Error Handling

### Syntax Error
Code doesn't follow Python syntax rules.
```python
# Wrong: extra parenthesis
print(12 + 4))
# SyntaxError: unmatched ')'
```

### Name Error
Using undefined variables (case-sensitive).
```python
my_number = 4
my_Number + 2  # NameError: 'my_Number' not defined
```

### Zero Division Error
Attempting to divide by zero.
```python
5 % 0  # ZeroDivisionError
```

---

## Functions

### Creating Functions
```python
def my_function():
    print("Hello")
    name = input("Your name: ")
    print("Hello")
```

### Calling Functions
```python
my_function()  # Execute the function
```

### Functions with Parameters
```python
def add(n1, n2):
    print(n1 + n2)

add(2, 3)  # Prints: 5
```

### Functions with Return Values
```python
def add(n1, n2):
    return n1 + n2

result = add(2, 3)  # result = 5
```

### Keyword Arguments
```python
def divide(n1, n2):
    return n1 / n2

# Positional arguments
result1 = divide(10, 5)

# Keyword arguments (order doesn't matter)
result2 = divide(n2=5, n1=10)
```

### Variable Scope
Variables inside functions are local.
```python
n = 2

def my_function():
    n = 3
    print(n)  # Prints: 3

print(n)        # Prints: 2
my_function()   # Prints: 3
```

---

## Conditionals

### If Statements
```python
n = 5
if n > 2:
    print("Larger than 2")
```

### If-Else
```python
age = 18
if age > 16:
    print("Can drive")
else:
    print("Don't drive")
```

### If-Elif-Else
```python
weather = "sunny"
if weather == "rain":
    print("bring umbrella")
elif weather == "sunny":
    print("bring sunglasses")
elif weather == "snow":
    print("bring gloves")
```

### Comparison Operators
```python
>    # Greater than
<    # Less than
>=   # Greater than or equal
<=   # Less than or equal
==   # Equal to
!=   # Not equal to
```

### Logical Operators
```python
# AND: both conditions must be true
if age > 16 and age < 65:
    print("Can work")

# OR: at least one condition must be true
if age < 16 or age > 200:
    print("Can't drive")

# NOT: reverses the condition
if not age > 65:
    print("Not a senior")
```

---

## Loops

### While Loops
Repeat while condition is true.
```python
n = 1
while n < 100:
    print(n)
    n += 1
```

### For Loops
Iterate over sequences.
```python
all_fruits = ["apple", "banana", "orange"]
for fruit in all_fruits:
    print(fruit)
```

### Range in For Loops
```python
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 8):     # 2, 3, 4, 5, 6, 7
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8
    print(i)
```

### Using _ in For Loops
When you don't need the loop variable.
```python
for _ in range(100):
    print("Hello")  # Do something 100 times
```

### Break
Exit the loop early.
```python
scores = [34, 67, 99, 105]
for score in scores:
    if score > 100:
        print("Invalid score")
        break
    print(score)
```

### Continue
Skip current iteration, continue with next.
```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # Prints only odd numbers
```

### Infinite Loops
⚠️ Be careful! These run forever.
```python
while True:
    print("This runs forever")
```

---

## List Methods

### Creating Lists
```python
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["text", 123, 3.14, True]
```

### List Indexing
```python
letters = ["a", "b", "c"]
print(letters[0])   # "a" (first item)
print(letters[-1])  # "c" (last item)
print(letters[-2])  # "b" (second from end)
```

### List Slicing
```python
letters = ["a", "b", "c", "d"]
print(letters[1:3])   # ["b", "c"] (start included, end excluded)
print(letters[:2])    # ["a", "b"] (from start)
print(letters[2:])    # ["c", "d"] (to end)
print(letters[:])     # ["a", "b", "c", "d"] (entire list)
```

### Adding Items
```python
# Append single item
fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)  # ["apple", "banana", "orange"]

# Extend with another list
fruits.extend(["grape", "mango"])
# or
fruits += ["grape", "mango"]
```

### List Operations
```python
# Length
len(fruits)

# Check if item exists
if "apple" in fruits:
    print("Apple found")

# Remove items
fruits.remove("banana")    # Remove by value
popped = fruits.pop()      # Remove and return last item
popped = fruits.pop(0)     # Remove and return item at index
del fruits[0]              # Delete item at index

# Insert at specific position
fruits.insert(1, "kiwi")

# Sort lists
numbers = [3, 1, 4, 1, 5]
numbers.sort()             # Modifies original list
sorted_nums = sorted(numbers)  # Returns new sorted list

# Reverse
numbers.reverse()
```

---

## Built-in Functions

### Range
Generate sequences of numbers.
```python
# range(start, end, step)
for i in range(6, 0, -2):
    print(i)  # Prints: 6, 4, 2
```

### Random
```python
import random

# Random integer (inclusive)
n = random.randint(1, 10)  # 1 to 10

# Random choice from list
colors = ["red", "blue", "green"]
chosen = random.choice(colors)

# Shuffle list
random.shuffle(colors)
```

### Round
Round numbers to nearest integer.
```python
round(4.6)    # 5
round(4.3)    # 4
round(4.5)    # 4 (banker's rounding)
```

### Absolute Value
```python
abs(-4.6)     # 4.6
abs(4.6)      # 4.6
```

### Min/Max
```python
numbers = [1, 5, 3, 9, 2]
print(min(numbers))  # 1
print(max(numbers))  # 9
```

### Sum
```python
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # 15
```

---

## Modules

### Importing Modules
```python
# Import entire module
import random
n = random.randint(1, 5)

# Import specific functions
from random import randint, choice
n = randint(1, 5)
item = choice([1, 2, 3])

# Import with alias
import random as r
n = r.randint(1, 5)

# Import everything (not recommended)
from random import *
n = randint(1, 5)
```

### Common Standard Library Modules
```python
import math
import datetime
import os
import sys
import json
```

---

## Classes & Objects

### Creating a Class
```python
class MyClass:
    pass  # Empty class
```

### Class with Methods
```python
class Car:
    def drive(self):
        print("The car is moving")
    
    def stop(self):
        print("The car stopped")
```

### Creating Objects
```python
my_car = Car()
my_car.drive()  # "The car is moving"
```

### Class Variables
Shared by all instances.
```python
class Car:
    wheels = 4  # Class variable
    
car1 = Car()
car2 = Car()
print(car1.wheels)  # 4
print(car2.wheels)  # 4
```

### The __init__ Method
Constructor called when creating objects.
```python
class Car:
    def __init__(self, make, model):
        self.make = make      # Instance variable
        self.model = model    # Instance variable
        print("Car created!")

my_car = Car("Toyota", "Camry")
print(my_car.make)   # "Toyota"
print(my_car.model)  # "Camry"
```

### Instance Variables vs Class Variables
```python
class Car:
    wheels = 4  # Class variable (shared)
    
    def __init__(self, color):
        self.color = color  # Instance variable (unique)

car1 = Car("red")
car2 = Car("blue")

print(car1.color)   # "red"
print(car2.color)   # "blue"
print(car1.wheels)  # 4
print(car2.wheels)  # 4
```

### Class Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def breathe(self):
        print("Breathing")

class Fish(Animal):  # Fish inherits from Animal
    def __init__(self, name):
        super().__init__(name)  # Call parent constructor
    
    def breathe(self):
        super().breathe()       # Call parent method
        print("underwater")

nemo = Fish("Nemo")
nemo.breathe()
# Output:
# Breathing
# underwater
```

### Method Overriding
```python
class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):  # Override parent method
        print("Woof!")

class Cat(Animal):
    def sound(self):  # Override parent method
        print("Meow!")

dog = Dog()
cat = Cat()
dog.sound()  # "Woof!"
cat.sound()  # "Meow!"
```

---

## Best Practices

### Naming Conventions
```python
# Variables and functions: snake_case
user_name = "john"
def calculate_total():
    pass

# Classes: PascalCase
class BankAccount:
    pass

# Constants: UPPER_CASE
MAX_USERS = 100
```

### Code Organization
```python
# 1. Imports
import random
from datetime import datetime

# 2. Constants
MAX_ATTEMPTS = 3

# 3. Classes
class GamePlayer:
    pass

# 4. Functions
def main():
    pass

# 5. Main execution
if __name__ == "__main__":
    main()
```

### Error Prevention
```python
# Use try-except for error handling
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

## Quick Reference Card

| Operation | Syntax | Example |
|-----------|--------|---------|
| Print | `print()` | `print("Hello")` |
| Input | `input()` | `name = input("Name: ")` |
| Comment | `#` | `# This is a comment` |
| Assignment | `=` | `x = 5` |
| Equality | `==` | `if x == 5:` |
| Not equal | `!=` | `if x != 5:` |
| String format | `f""` | `f"Hello {name}"` |
| List | `[]` | `items = [1, 2, 3]` |
| Dictionary | `{}` | `data = {"key": "value"}` |
| Function | `def` | `def my_func():` |
| Class | `class` | `class MyClass:` |
| Import | `import` | `import math` |
| For loop | `for in` | `for i in range(5):` |
| While loop | `while` | `while x < 10:` |
| If statement | `if` | `if condition:` |

---

*This cheatsheet covers fundamental Python concepts. For more advanced topics, refer to the official Python documentation at [python.org](https://docs.python.org/).*