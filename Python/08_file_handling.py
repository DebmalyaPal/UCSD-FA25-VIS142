# -------------------------------
# FILE HANDLING
# -------------------------------

# This script demonstrates how to handle files in Python:
# - Writing to a file
# - Appending to a file
# - Reading from a file
# -------------------------------

# KEY IDEAS (READ THESE FIRST):
# - A file is just text stored on disk. Your Python program can create it, add to it, and read it back.
# - Use `with open(filename, mode) as f:` to safely open files. It auto-closes the file even if errors happen.
# - Modes:
#     "w" (write): creates a new file or OVERWRITES existing content.
#     "a" (append): keeps existing content and ADDS new content at the end.
#     "r" (read): opens a file for reading (file must exist).
# - Reading approaches:
#     f.read(): read the ENTIRE file as one string.
#     f.readlines(): read into a list of lines (includes newline characters).
#     for line in f: iterate line by line (memory-friendly for large files).
# - Newline characters:
#     "\n" moves to the next line. If you don’t add it, text runs together on one line.


# -------------------------------
# 1: WRITE (overwrites any existing content)
# -------------------------------
# "w" mode creates the file if it doesn't exist, or clears existing content if it does.
with open("example.txt", "w") as f:
    # Write two lines. Note the "\n" to put each on a new line.
    f.write("Line 1: Hello, this is a fresh start!\n")
    f.write("Line 2: Writing replaces old content.\n")

# After writing, let's read the entire file to see what we wrote.
with open("example.txt", "r") as f:
    print("Reading after writing (full read):")
    entire_text = f.read()           # ENTIRE content at once (string)
    print(entire_text)
    # SAMPLE OUTPUT (will look like this):
    # Line 1: Hello, this is a fresh start!
    # Line 2: Writing replaces old content.

# -------------------------------
# 2: APPEND (keeps existing content, adds new lines at the end)
# -------------------------------
# "a" mode does NOT erase old content.
with open("example.txt", "a") as f:
    f.write("Line 3: This line is appended.\n")
    f.write("Line 4: Appending keeps old content intact.\n")

# Read again to confirm that the new lines were added at the end.
with open("example.txt", "r") as f:
    print("\nReading after appending (full read):")
    entire_text_after_append = f.read()
    print(entire_text_after_append)
    # SAMPLE OUTPUT:
    # Line 1: Hello, this is a fresh start!
    # Line 2: Writing replaces old content.
    # Line 3: This line is appended.
    # Line 4: Appending keeps old content intact.

# -------------------------------
# 3: READ LINE-BY-LINE (iterate for more control)
# -------------------------------
# This is useful when you want to process each line (e.g., numbering, replacing words).
with open("example.txt", "r") as f:
    print("\nReading line by line:")
    for line in f:
        clean_line = line.strip()    # strip() removes trailing "\n" so printing looks cleaner
        print(clean_line)
    # SAMPLE OUTPUT:
    # Iteration 0 -> Line 1: Hello, this is a fresh start!
    # Iteration 1 -> Line 2: Writing replaces old content.
    # Iteration 2 -> Line 3: This line is appended.
    # Iteration 3 -> Line 4: Appending keeps old content intact.

# -------------------------------
# 4: OPTIONAL – READLINES vs READ
# -------------------------------
# .readlines() returns a list; .read() returns a single string.
with open("example.txt", "r") as f:
    print("\nUsing readlines():")
    lines_list = f.readlines()       # e.g., ["Line 1...\n", "Line 2...\n", ...]
    print(lines_list)
    # TIP: Use this when you want random access to specific lines via indexing.

# -------------------------------
# SUMMARY:
# - Use "w" to start fresh; it overwrites existing content.
# - Use "a" to add content without deleting old text.
# - Use "r" to read; choose .read(), .readlines(), or line iteration depending on needs.
# - Always include "\n" if you want separate lines when writing.
# - Prefer `with open(...)` to automatically close files and avoid resource leaks.
# -------------------------------
