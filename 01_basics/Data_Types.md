# Data Types Guide

## Introduction
Data types define the kind of information a variable holds in Python. The interpreter detects the data type automatically from the assigned value—no manual declaration needed.

## Core Data Types

### Integer (`int`)
**Purpose**: Holds whole numbers, positive or negative, without fractions.  
**Details**: Perfect for counts, ages, or IDs where decimals aren't required.

```python
student_id = 12345
total_books = 250
current_year = 2025
```

### Float (`float`)
**Purpose**: Represents numbers with decimal places or fractions.  
**Details**: Essential for measurements, prices, or scientific calculations.

```python
gpa = 8.75
weight = 65.5
pi_value = 3.14159
```

### String (`str`)
**Purpose**: Stores sequences of characters or text.  
**Details**: Enclose text in single (`'`) or double (`"`) quotes.

```python
username = 'codeNinja'
course = "Data Science"
greeting = 'Hello, Python World!'
```

### Boolean (`bool`)
**Purpose**: Captures logical states—True or False only.  
**Details**: Used in conditions, flags, and decision-making logic.

```python
is_active = True
has_permission = False
game_over = False
```

### List (`list`)
**Purpose**: Contains multiple items in a single, ordered collection.  
**Details**: Mutable—items can be added, removed, or changed anytime.

```python
hobbies = ["coding", "gaming", "music"]
scores = [95, 88, 92, 87]
tech_stack = ["Python", "GitHub", "VSCode"]
```

### Tuple (`tuple`)
**Purpose**: Ordered collection like lists, but immutable (unchangeable).  
**Details**: Ideal for fixed data like coordinates or constants.

```python
rgb_color = (255, 128, 0)
days_in_week = (7, "fixed")
phone_digits = (9, 8, 7, 6, 5, 4, 3)
```

### Dictionary (`dict`)
**Purpose**: Maps unique keys to values for fast lookups.  
**Details**: Keys must be unique; values accessed via key names.

```python
profile = {
    "username": "ChichiCoder",
    "grade": 11,
    "stream": "PCM"
}
laptop_specs = {
    "ram": "16GB",
    "cpu": "i5",
    "storage": "512GB SSD"
}
```

## Type Checking
Use `type()` to identify a variable's data type dynamically.

```python
score = 98
name = "Alex"
is_ready = True

print(type(score))    # <class 'int'>
print(type(name))     # <class 'str'>
print(type(is_ready)) # <class 'bool'>
```
