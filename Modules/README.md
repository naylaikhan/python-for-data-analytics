## Python Modules - Practice

This folder contains my practice exercises for **Python Modules**, starting from the basics and progressing toward practical Data Analytics use cases.

The goal is to understand how Python modules work, how to create and import my own modules, and how modules help organize and reuse code.

---

## 📚 Topics Covered

* What is a Python Module?
* Creating your own modules
* Importing modules
* `import module`
* `from module import function`
* Importing multiple functions
* Module aliases using `as`
* Function aliases
* Accessing variables from modules
* Modules containing functions and variables
* Code reusability
* Organizing large Python programs
* Standard Library modules
* `math`
* `random`
* `datetime`
* `os`
* The `__name__` variable
* `if __name__ == "__main__":`
* Packages vs Modules
* Basic module dependencies
* Modules in Data Analytics

---

# 🎯 Learning Objectives

By completing these exercises, I aim to understand:

1. What a Python module is.
2. Why modules are useful.
3. How to create a custom Python module.
4. How to import a module into another Python file.
5. How to access functions and variables from a module.
6. The difference between `import` and `from ... import`.
7. How module aliases work.
8. How Python's standard library modules are used.
9. How `__name__` works.
10. Why `if __name__ == "__main__":` is used.
11. How modules help organize larger projects.
12. How modules can be used in Data Analytics projects.

---

# 📂 Practice Structure

The exercises are divided into levels based on difficulty.

```text
Level 1 → Module Basics
Level 2 → Import Statements
Level 3 → Creating Your Own Modules
Level 4 → Multiple Modules and Logic
Level 5 → __name__ and __main__
Level 6 → Standard Library Modules
Level 7 → Data Analytics-Oriented Projects
```

---

# 🟢 Level 1 — Module Basics

### 1. Create Your First Module

Create a `greetings.py` module containing a `say_hello()` function and use it from `main.py`.

### 2. Module With a Variable

Create a `student.py` module containing student information and access the variables from another Python file.

### 3. Module With Multiple Functions

Create a `calculator.py` module containing:

```text
add()
subtract()
multiply()
divide()
```

Import and use all functions.

### 4. Accessing Module Members

Create an employee module containing variables and a function, then access them from another file.

### 5. Multiple Modules

Create separate modules for:

```text
addition
subtraction
multiplication
```

Import all three into `main.py`.

---

# 🟡 Level 2 — Import Statements

### 6. Using `import`

Use the `math` module to perform mathematical calculations.

### 7. Using `from ... import`

Import specific functions from the `math` module.

### 8. Import Multiple Functions

Import:

```python
sqrt
pow
factorial
```

from `math`.

### 9. Module Alias

Import `math` using an alias:

```python
import math as m
```

### 10. Function Alias

Import `sqrt` using an alias:

```python
from math import sqrt as square_root
```

---

# 🟠 Level 3 — Creating Your Own Modules

### 11. Temperature Module

Create functions for:

```text
Celsius → Fahrenheit
Fahrenheit → Celsius
```

### 12. Student Marks Module

Create functions for:

* Total marks
* Average marks
* Highest mark
* Lowest mark

### 13. Shopping Module

Create a function that calculates the total cost of a list of products.

### 14. Discount Module

Create a function to calculate the final price after applying a discount.

### 15. Employee Salary Module

Create functions to calculate:

* Salary
* Bonus
* Tax
* Final salary

---

# 🔴 Level 4 — Multiple Modules and Logic

### 16. Calculator Using Separate Modules

Create separate modules for:

```text
addition.py
subtraction.py
multiplication.py
division.py
```

Build a calculator using these modules.

### 17. Number Analysis Module

Create functions to determine whether numbers are:

* Positive
* Negative
* Zero
* Even
* Odd

### 18. List Analysis Module

Create functions to calculate:

* Sum
* Average
* Maximum
* Minimum
* Number of elements

### 19. String Utility Module

Create functions for:

* Character count
* Word count
* Uppercase conversion
* Lowercase conversion
* String reversal

### 20. Password Module

Create functions that check password requirements such as:

* Minimum length
* Uppercase letter
* Lowercase letter
* Digit

---

# 🔴 Level 5 — `__name__` and `__main__`

### 21. Understanding `__name__`

Create a module that prints the value of:

```python
__name__
```

Run it directly and then import it from another file.

Observe the difference.

### 22. `if __name__ == "__main__"`

Create a calculator module containing functions and a testing section protected by:

```python
if __name__ == "__main__":
```

### 23. Module With Functions and Main Code

Create a student module containing reusable functions and a separate testing section.

### 24. Compare Two Modules

Create two modules and observe the value of `__name__` when they are run directly and imported.

### 25. Module Testing

Create a `math_tools.py` module and test all its functions using:

```python
if __name__ == "__main__":
```

---

# 🔴 Level 6 — Standard Library Modules

### 26. Random Number Module

Use:

```python
import random
```

to create a number guessing game.

The program should generate a random number between 1 and 100 and continue until the user guesses correctly.

### 27. Date and Time Module

Use:

```python
import datetime
```

to work with dates and calculate the number of days between two dates.

### 28. File and Directory Module

Use:

```python
import os
```

to:

* Find the current working directory
* List files and folders
* Count items
* Find `.py` files

---

# 🔵 Level 7 — Data Analytics Practice

### 29. Sales Analysis Module

Create a `sales_analysis.py` module containing functions to calculate:

* Total sales
* Average sales
* Highest sale
* Lowest sale
* Number of sales above a specified amount

Use a list of sales transactions and generate a simple analysis report.

---

# 🚀 30. Mini Data Analytics Project

Create a modular sales analysis project:

```text
sales_project/
│
├── main.py
├── data.py
├── calculations.py
└── report.py
```

### `data.py`

Store sales transaction data.

### `calculations.py`

Create functions for:

* Total sales
* Average sales
* Highest sale
* Lowest sale
* Total transactions
* Sales by category

### `report.py`

Create functions to display a formatted sales report.

### `main.py`

Import the required modules and generate the final report.

---

# 💡 Key Concepts Learned

The main concepts practiced in this section are:

```python
import module
```

```python
from module import function
```

```python
import module as alias
```

```python
from module import function as alias
```

```python
if __name__ == "__main__":
```

---

# 📊 Modules in Data Analytics

Modules are an essential part of Python Data Analytics.

Common modules and libraries I will use include:

| Module / Library | Purpose                        |
| ---------------- | ------------------------------ |
| `math`           | Mathematical operations        |
| `random`         | Random data generation         |
| `datetime`       | Dates and times                |
| `os`             | Files and directories          |
| `json`           | JSON data                      |
| `re`             | Regular expressions            |
| `pandas`         | Data manipulation and analysis |
| `numpy`          | Numerical computing            |
| `matplotlib`     | Data visualization             |
| `seaborn`        | Statistical visualization      |

Common Data Analytics imports include:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

---

# 🧠 Key Takeaway

A Python module is essentially a Python file containing reusable code.

Instead of writing everything inside one large Python file, I can organize my code into separate modules and import them when needed.

```text
Python File
     ↓
   Module
     ↓
Reusable Code
     ↓
    import
     ↓
Another Python Program
```

This makes Python programs:

* Easier to understand
* Easier to maintain
* Easier to debug
* More reusable
* Better organized

---

# 🏆 Progress

* [ ] Understand what a module is
* [ ] Create custom modules
* [ ] Import modules
* [ ] Use `from ... import`
* [ ] Use module aliases
* [ ] Work with standard library modules
* [ ] Understand `__name__`
* [ ] Understand `if __name__ == "__main__":`
* [ ] Create multi-module projects
* [ ] Apply modules to Data Analytics

---

## 🐍 Next Step

After completing Modules, continue practicing Python concepts such as:

```text
Modules
   ↓
File Handling
   ↓
Exception Handling
   ↓
Object-Oriented Programming
   ↓
Pandas
   ↓
NumPy
   ↓
Data Cleaning
   ↓
Data Analysis
   ↓
Data Visualization
```

The ultimate goal is to use Python not only to understand programming fundamentals but also to solve **real-world Data Analytics problems**.
