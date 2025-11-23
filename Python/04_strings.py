# -------------------------------
# STRINGS IN PYTHON
# -------------------------------

# Strings are sequences of characters enclosed in quotes
greeting = "Hello, Python!"
print("Original string:", greeting)  
# Output: Hello, Python!

# Length of string using len()
print("Length of greeting:", len(greeting))  
# Output: 14

# -------------------------------
# INDEXING
# -------------------------------
# Positive index starts at 0 from the left
print("First character (index 0):", greeting[0])  
# Output: H

# Negative index starts at -1 from the right
print("Last character (index -1):", greeting[-1])  
# Output: !

print("Second last character (index -2):", greeting[-2])  
# Output: n


# -------------------------------
# SLICING
# -------------------------------
# Syntax: string[start:end] (end is excluded)
print("First 5 characters:", greeting[:5])  
# Output: Hello

print("Characters from index 7 to end:", greeting[7:])  
# Output: Python!

print("Characters from index 0 to 7:", greeting[0:7])  
# Output: Hello, 

# Step slicing
print("Every second character:", greeting[::2])  
# Output: Hlo yhn!

print("Reverse string:", greeting[::-1])  
# Output: !nohtyP ,olleH


# -------------------------------
# STRING METHODS
# -------------------------------
# upper(): convert to uppercase
print("Uppercase:", greeting.upper())  
# Output: HELLO, PYTHON!

# lower(): convert to lowercase
print("Lowercase:", greeting.lower())  
# Output: hello, python!

# replace(): replace part of the string
print("Replace 'Python' with 'World':", greeting.replace("Python", "World"))  
# Output: Hello, World!

# split(): split string into list by delimiter
print("Split by comma:", greeting.split(","))  
# Output: ['Hello', ' Python!']

# strip(): remove whitespace from start and end
text = "   padded text   "
print("Before strip:", text)  
# Output: '   padded text   '
print("After strip:", text.strip())  
# Output: 'padded text'


# -------------------------------
# SEARCHING
# -------------------------------
# find(): returns index of first occurrence, -1 if not found
print("Index of 'Python':", greeting.find("Python"))  
# Output: 7

# count(): counts occurrences of substring
print("Count of 'l':", greeting.count("l"))  
# Output: 2


# -------------------------------
# STRING CONCATENATION
# -------------------------------
first = "Hello"
second = "World"
combined = first + " " + second
print("Concatenated string:", combined)  
# Output: Hello World


# -------------------------------
# STRING REPETITION
# -------------------------------
laugh = "ha"
print("Repetition:", laugh * 3)  
# Output: hahaha


# -------------------------------
# STRING FORMATTING
# -------------------------------
name = "Alice"
age = 20
print("Using f-string:", f"My name is {name} and I am {age} years old.")  
# Output: My name is Alice and I am 20 years old.

print("Using format():", "My name is {} and I am {} years old.".format(name, age))  
# Output: My name is Alice and I am 20 years old.


# -------------------------------
# ESCAPE CHARACTERS
# -------------------------------
# \n = newline, \t = tab, \" = double quote
print("Line1\nLine2")  
# Output:
# Line1
# Line2

print("Column1\tColumn2")  
# Output: Column1    Column2

print("She said \"Hello\"")  
# Output: She said "Hello"
