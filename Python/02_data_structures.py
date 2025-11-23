# -------------------------------
# DATA STRUCTURES
# -------------------------------



# -------------------------------
# LIST: ordered, mutable (can be changed)
# -------------------------------
fruits = ["apple", "banana", "cherry"]
print("Initial list:", fruits)

# append(): adds element at the end
fruits.append("orange")
print("After append:", fruits)  # ['apple', 'banana', 'cherry', 'orange']

# insert(): adds element at a specific position
fruits.insert(1, "grape")  # insert 'grape' at index 1
print("After insert:", fruits)  # ['apple', 'grape', 'banana', 'cherry', 'orange']

# remove(): removes the first occurrence of a value
fruits.remove("banana")
print("After remove:", fruits)  # ['apple', 'grape', 'cherry', 'orange']

# pop(): removes element at given index (default last) and returns it
removed_item = fruits.pop()  # removes 'orange'
print("After pop:", fruits)  # ['apple', 'grape', 'cherry']
print("Popped item:", removed_item)  # 'orange'

# extend(): adds elements from another list
fruits.extend(["kiwi", "mango"])
print("After extend:", fruits)  # ['apple', 'grape', 'cherry', 'kiwi', 'mango']

# clear(): removes all elements
fruits.clear()
print("After clear:", fruits)  # []




# -------------------------------
# TUPLE: ordered, immutable (cannot be changed)
# -------------------------------
coordinates = (10, 20, 30)
print("Tuple:", coordinates)

# Access elements by index
print("First element:", coordinates[0])  # 10
print("Last element:", coordinates[-1])  # 30

# Tuples cannot be modified (no append/remove), but can be used for fixed data




# -------------------------------
# DICTIONARY: key-value pairs
# -------------------------------

student = {"name": "Alice", "age": 20, "major": "CS"}
print("Initial dictionary:", student)
# {'name': 'Alice', 'age': 20, 'major': 'CS'}

# Access value by key
print("Student name:", student["name"])  # Alice

# Add new key-value
student["year"] = "Sophomore"
print("After adding key:", student)
# {'name': 'Alice', 'age': 20, 'major': 'CS', 'year': 'Sophomore'}

# --- Update Method 1: update() ---
# Adds or modifies multiple key-value pairs at once
student.update({"age": 21, "GPA": 3.8})
print("After update() method:", student)
# {'name': 'Alice', 'age': 21, 'major': 'CS', 'year': 'Sophomore', 'GPA': 3.8}

# --- Update Method 2: direct assignment ---
# Modify a single existing key directly
student["age"] = 22   # changes age from 21 to 22
print("After direct assignment:", student)
# {'name': 'Alice', 'age': 22, 'major': 'CS', 'year': 'Sophomore', 'GPA': 3.8}

# pop(): removes a key and returns its value
removed_major = student.pop("major")
print("After pop:", student)
# {'name': 'Alice', 'age': 22, 'year': 'Sophomore', 'GPA': 3.8}
print("Removed value:", removed_major)  # 'CS'

# keys(), values(), items(): view dictionary contents
print("Keys:", student.keys())
# dict_keys(['name', 'age', 'year', 'GPA'])
print("Values:", student.values())
# dict_values(['Alice', 22, 'Sophomore', 3.8])
print("Items:", student.items())
# dict_items([('name', 'Alice'), ('age', 22), ('year', 'Sophomore'), ('GPA', 3.8)])

# clear(): removes all items
student.clear()
print("After clear:", student)  # {}
