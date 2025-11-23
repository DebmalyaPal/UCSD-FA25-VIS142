# 🐍 Python Basics – Course Summary

Welcome to the **Python Basics** folder!  
This directory contains step‑by‑step `.py` files with extensive comments and examples.  
Each file builds naturally on the previous one, so you can progress smoothly from beginner concepts to object‑oriented programming.

---

## 📂 Contents

### 01_intro.py
- Printing text (`print`)
- Basic arithmetic operations
- Variables and assignments
- Loops (`for`, `while`)
- Conditional statements (`if`, `else`)
- Comments and their importance

### 02_data_structures.py
- Introduction to **lists, tuples, dictionaries**
- Mutability vs immutability
- Adding/removing elements (`append`, `remove`, `insert`, `pop`, `extend`, `clear`)
- Dictionary operations (`update`, direct assignment, `pop`, `keys`, `values`, `items`)
- Practical examples with outputs

### 03_list.py
- Indexing (positive and negative)
- Slicing (`start:end:step`)
- Reverse lists (`[::-1]`)
- Enumerate for index + value
- Nested lists and accessing elements
- Copy vs reference (`[:]` vs assignment)

### 04_string.py
- String basics and indexing
- Slicing and step slicing
- Common methods (`upper`, `lower`, `replace`, `split`, `strip`)
- Searching (`find`, `count`)
- Concatenation and repetition
- String formatting (`f-strings`, `.format`)
- Escape characters (`\n`, `\t`, `\"`)

### 05_functions.py
- Defining functions
- Parameters and return values
- Default arguments
- Keyword arguments
- Returning multiple values
- Reusability and organization

### 06_module_import.py
- Importing **pre‑written modules** (e.g., `random`)
  - `randint`, `choice`, `shuffle`, `random`
- Importing **custom modules** (e.g., `helper.py`) [NOTE: 05_functions renamed to helper.py]
  - Functions and variables from your own files
- Import styles:
  - `import module`
  - `from module import function`
  - `import module as alias`

### 07_class_object.py
- Introduction to **Object‑Oriented Programming**
- Defining classes and constructors (`__init__`)
- Attributes and methods
- Creating objects (instances)
- Modifying attributes
- Understanding self as reference to current object
- Adding new attributes dynamically
- Example: `Student` and `Calculator` classes

### 08_file_handling.py
- Writing to files (`"w"` mode) → creates new file or overwrites existing content
- Appending to files (`"a"` mode) → adds new content at the end without deleting old content
- Reading from files (`"r"` mode) → open and read entire file or line by line
- Using `with open(...)` for safe file handling (auto‑closes files)
- Difference between `.read()`, `.readlines()`, and iterating line by line
- Importance of newline characters (`\n`) when writing

---

## 🎯 How to Use
1. Start with `01_intro.py` and run it line by line.  
2. Progress through each file in order, each builds on the previous concepts.  
3. Read the comments carefully; they explain definitions and expected outputs.  
4. Try modifying the examples or adding your own experiments.  
5. Use this README as a roadmap while exploring the `.py` files.

---

## ✨ Motivation
By the end of these lessons, you’ll have built a strong foundation in Python — from printing your first line to writing classes and objects.  
