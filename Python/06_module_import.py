# -------------------------------
# MODULES & IMPORTS
# -------------------------------

# Modules are files that contain Python code (functions, classes, variables).
# Importing lets us use code written by others or ourselves.

# ---------------------------------
# 1. PRE-WRITTEN MODULES (STANDARD LIBRARY)
# ---------------------------------

import random  # Import the entire random module

# random.randint(a, b): returns a random integer between a and b (inclusive)
print("Random integer between 1 and 10:", random.randint(1, 10))
# Output: varies each run, e.g. 7

# random.choice(list): returns a random element from a list
fruits = ["apple", "banana", "cherry"]
print("Random fruit:", random.choice(fruits))
# Output: varies each run, e.g. banana

# random.shuffle(list): shuffles the list in place
random.shuffle(fruits)
print("Shuffled fruits:", fruits)
# Output: order will vary each run

# random.random(): returns a float between 0 and 1
print("Random float between 0 and 1:", random.random())
# Output: varies each run, e.g. 0.5342

# ---------------------------------
# 2. CUSTOM MODULES (YOUR OWN FILES)
# ---------------------------------
# Suppose we create a file called 05_functions.py with the following content:
# ---------------------------------
# def add(a, b):
#     return a + b
#
# x = 3
# ---------------------------------
# Save this as helper.py in the same folder as this script.

# Import the custom module
import helper

# Use the function from helper.py
print("Using helper.add:", helper.add(5, 4))
# Output: 9

# Access the variable from helper.py
print("Using helper.my_variable:", helper.my_variable)
# Output: 3

# ---------------------------------
# 3. DIFFERENT IMPORT STYLES
# ---------------------------------

# (a) from module import function
# This imports only the specific function you need.
from helper import add
print("Using add directly:", add(10, 5))
# Output: 15
# Comment: "from _ import _" means you import only what you specify, not the whole module.

# (b) import module as alias
# This gives the module a shorter name.
import random as rnd
print("Random integer with alias:", rnd.randint(1, 5))
# Output: varies each run
# Comment: "import _ as _" means you import the module but give it a nickname (alias).
