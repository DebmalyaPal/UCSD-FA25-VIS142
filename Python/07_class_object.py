# -------------------------------
# CLASSES & OBJECTS
# -------------------------------

# Classes are blueprints for creating objects.
# Objects are instances of classes with attributes (data) and methods (functions).

# Define a class
class Student:
    # __init__ is the constructor, runs when object is created
    def __init__(self, name, age):
        self.name = name  # attribute
        self.age = age    # attribute

    # Method (function inside class)
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Create objects (instances of Student class)
s1 = Student("Alice", 20)
s1.introduce()  
# Output: My name is Alice and I am 20 years old.

s2 = Student("Bob", 22)
s2.introduce()  
# Output: My name is Bob and I am 22 years old.

# Modify attributes
s1.age = 21
print("Updated age for Alice:", s1.age)  
# Output: 21

# Add new attribute dynamically
s1.major = "Computer Science"
print("Alice's major:", s1.major)  
# Output: Computer Science



# Class with multiple methods
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

calc = Calculator()
print("Add:", calc.add(2, 3))        # Output: 5
print("Multiply:", calc.multiply(4, 5))  # Output: 20
