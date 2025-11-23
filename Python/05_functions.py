# -------------------------------
# FUNCTIONS IN PYTHON
# -------------------------------

# Functions are reusable blocks of code.
# They help avoid repetition and make programs organized.

# Define a simple function
def greet():
    print("Hello from a function!")

greet()  
# Output: Hello from a function!

# Function with parameters (inputs)
def greet_person(name):
    print("Hello,", name)

greet_person("Alice")  
# Output: Hello, Alice

# Function with multiple parameters
def add(a, b):
    return a + b  # return sends the result back

x, y = 3, 4
result = add(x, y)
print("Sum:", result)  
# Output: Sum: 7

# Default parameter values
def power(base, exponent=2):
    return base ** exponent

print("Power with default exponent:", power(5))  
# Output: 25
print("Power with custom exponent:", power(2, 3))  
# Output: 8

# Keyword arguments
print("Keyword arguments:", power(exponent=4, base=3))  
# Output: 81

# Functions can return multiple values
def divide_and_remainder(x, y):
    return x // y, x % y

quotient, remainder = divide_and_remainder(10, 3)
print("Quotient:", quotient, "Remainder:", remainder)  
# Output: Quotient: 3 Remainder: 1
