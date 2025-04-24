import math

# Basic Python Operations

# 1. Print "Hello, World!"
print("Hello, World!")

# 2. Variables and Data Types
x = 10          # Integer
y = 3.14        # Float
name = "Shuvo"  # String
is_active = True  # Boolean

# 3. Basic Arithmetic Operations
a = 5
b = 2
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus
print(a ** b) # Exponentiation
print(a // b) # Floor Division

# 4. Conditional Statements
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")

# 5. Loops
# For Loop
for i in range(5):
    print(i)

# While Loop
count = 0
while count < 5:
    print(count)
    count += 1

# 6. Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Shuvo"))

# 7. Lists
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)
print(fruits[1])  # Access by index

# 8. Dictionaries
person = {"name": "Shuvo", "age": 25}
print(person["name"])
person["age"] = 26
print(person)

# 9. Classes and Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

p = Person("Shuvo", 25)
print(p.introduce())

# 10. File Handling
with open("example.txt", "w") as file:
    file.write("Hello, File!")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# 11. Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# 12. List Comprehensions
squares = [x**2 for x in range(10)]
print(squares)

# 13. Lambda Functions
add = lambda x, y: x + y
print(add(5, 3))

# 14. Modules and Imports
print(math.sqrt(16))

# 15. Advanced: Decorators
def decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()

# 16. Advanced: Generators
def generate_numbers():
    for i in range(5):
        yield i

for num in generate_numbers():
    print(num)

# 17. Advanced: Context Managers
class CustomContext:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

with CustomContext():
    print("Inside context")