# Data Types
# ----------
# Data types define the kind of information a variable holds.
# The interpreter detects the type automatically from the assigned value.

# Integer (int) -- whole numbers, no fractions
student_id = 12345
total_books = 250
current_year = 2025

# Float (float) -- numbers with decimal places
gpa = 8.75
weight = 65.5
pi_value = 3.14159

# String (str) -- text, wrapped in single ('') or double ("") quotes
username = 'codeNinja'
course = "Data Science"
greeting = 'Hello, Python World!'

# Boolean (bool) -- True or False only
is_active = True
has_permission = False
game_over = False

# List (list) -- ordered, mutable (changeable) collection
hobbies = ["coding", "gaming", "music"]
scores = [95, 88, 92, 87]
tech_stack = ["Python", "GitHub", "VSCode"]

# Tuple (tuple) -- ordered, immutable (unchangeable) collection
rgb_color = (255, 128, 0)
days_in_week = (7, "fixed")
phone_digits = (9, 8, 7, 6, 5, 4, 3)

# Dictionary (dict) -- maps unique keys to values
profile = {
    "username": "ChichiCoder",
    "grade": 11,
    "stream": "PCM",
}
laptop_specs = {
    "ram": "16GB",
    "cpu": "i5",
    "storage": "512GB SSD",
}

# Type checking -- use type() to see a variable's data type
score = 98
name = "Alex"
is_ready = True

print(type(score))    # <class 'int'>
print(type(name))     # <class 'str'>
print(type(is_ready))  # <class 'bool'>
