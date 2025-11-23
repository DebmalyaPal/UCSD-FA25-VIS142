# -------------------------------
# LIST INDEXING & ACCESS PATTERNS
# -------------------------------

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("Initial list:", fruits)

# Index basics:
# - Positive index starts at 0 from the left: 0, 1, 2, ...
# - Negative index starts at -1 from the right: -1, -2, -3, ...
print("Index 0 (first):", fruits[0])       # 'apple'
print("Index 2 (third):", fruits[2])       # 'cherry'
print("Index -1 (last):", fruits[-1])      # 'elderberry'
print("Index -2 (second from last):", fruits[-2])  # 'date'

# Slicing basics: fruits[start:end]
# - Includes start, excludes end (end is "up to but not including")
print("Slice [1:4]:", fruits[1:4])         # ['banana', 'cherry', 'date']
print("Slice [:3] (start to index 3):", fruits[:3])  # ['apple', 'banana', 'cherry']
print("Slice [2:] (index 2 to end):", fruits[2:])    # ['cherry', 'date', 'elderberry']

# Step slicing: fruits[start:end:step]
print("Every second item [::2]:", fruits[::2])       # ['apple', 'cherry', 'elderberry']
print("Reverse list [::-1]:", fruits[::-1])          # ['elderberry', 'date', 'cherry', 'banana', 'apple']

# Slice assignment: replace a portion of the list
# (Lists are mutable; slicing can change multiple elements at once)
fruits[1:3] = ["blueberry", "cranberry"]             # replaces 'banana', 'cherry'
print("After slice assignment [1:3]:", fruits)       # ['apple', 'blueberry', 'cranberry', 'date', 'elderberry']

# Access with variables and computed indices
i = 3
print("Item at index i (i=3):", fruits[i])           # 'date'
print("Item at index len-1 (last):", fruits[len(fruits) - 1])  # 'elderberry'

# Bounds and errors:
# - Accessing an index outside the list length raises IndexError
# - Use checks to avoid errors
idx = 10
if 0 <= idx < len(fruits):
    print("Safe access at idx:", fruits[idx])
else:
    print("Index out of range:", idx)

# Finding the index of a value: list.index(value)
# - Returns the first matching index; raises ValueError if not found
try:
    pos = fruits.index("date")
    print("Index of 'date':", pos)
except ValueError:
    print("'date' not found")

# Enumerate for index + value in loops (clean and readable)
for index, item in enumerate(fruits):
    print(f"Enumerate -> index: {index}, item: {item}")

# Nested lists: access with multiple indices
matrix = [
    [1, 2, 3],      # row 0
    [4, 5, 6],      # row 1
    [7, 8, 9]       # row 2
]
print("Matrix row 1:", matrix[1])           # [4, 5, 6]
print("Matrix row 1, col 2:", matrix[1][2]) # 6

# Copy vs reference when slicing:
# - fruits[:] creates a shallow copy (new list)
copy_fruits = fruits[:]
copy_fruits[0] = "apricot"
print("Original unchanged:", fruits[0])     # 'apple'
print("Copy changed:", copy_fruits[0])      # 'apricot'
