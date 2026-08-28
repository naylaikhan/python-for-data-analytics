# Python List Comprehensions - 50 Practice Questions

## 📌 About This Repository

This repository contains **50 practice questions on Python List Comprehensions**, designed to help beginners improve their understanding of Python syntax, problem-solving, and programming logic.

The questions are arranged from **basic to more challenging levels**. They cover creating lists, filtering data, applying conditions, working with strings, nested lists, and solving practical problems using list comprehensions.

This repository is part of my Python learning journey as I build my skills for **Data Analytics**.

---

## 🎯 Learning Objectives

By completing these exercises, I aim to improve my understanding of:

* Creating lists using list comprehensions
* Replacing traditional `for` loops with list comprehensions
* Applying conditions using `if`
* Using `if-else` expressions inside list comprehensions
* Filtering elements from a list
* Performing mathematical operations
* Working with strings
* Using built-in functions such as `len()` and `abs()`
* Using `range()`
* Working with indexes using `enumerate()`
* Creating tuples using list comprehensions
* Flattening nested lists
* Building problem-solving and programming logic

---

# 📚 What Are List Comprehensions?

A **list comprehension** is a short and concise way to create a new list in Python.

Instead of writing:

```python
numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number * number)

print(squares)
```

We can write:

```python
numbers = [1, 2, 3, 4, 5]

squares = [number * number for number in numbers]

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

---

# 🧠 Basic Syntax

## Simple List Comprehension

```python
new_list = [expression for item in iterable]
```

Example:

```python
numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]
```

---

## List Comprehension With `if`

```python
new_list = [expression for item in iterable if condition]
```

Example:

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [number for number in numbers if number % 2 == 0]
```

Output:

```text
[2, 4, 6]
```

---

## List Comprehension With `if-else`

```python
new_list = [value_if_true if condition else value_if_false for item in iterable]
```

Example:

```python
numbers = [1, 2, 3, 4, 5]

result = ["Even" if number % 2 == 0 else "Odd" for number in numbers]
```

Output:

```text
['Odd', 'Even', 'Odd', 'Even', 'Odd']
```

---

# 📝 Practice Questions

The repository contains **50 practice questions** divided into five sections.

## 1️⃣ Basic List Comprehensions

This section focuses on the basic structure of list comprehensions.

Topics include:

* Creating lists using `range()`
* Squaring numbers
* Cubing numbers
* Multiplying numbers
* Adding values to list elements
* Converting numbers to strings
* Converting strings to uppercase and lowercase
* Finding the length of strings

**Questions:** 1–10

---

## 2️⃣ List Comprehensions With Conditions

This section focuses on filtering elements using conditions.

Topics include:

* Even numbers
* Odd numbers
* Positive numbers
* Negative numbers
* Numbers within a specific range
* Divisibility conditions
* Filtering names based on length
* Filtering words based on characters

**Questions:** 11–20

---

## 3️⃣ List Comprehensions With `if-else`

This section focuses on applying different logic based on conditions.

Topics include:

* Even or odd classification
* Positive, negative, and zero classification
* Pass or fail conditions
* Adult or minor classification
* High or low categorization
* Mathematical transformations based on conditions
* Applying discounts
* Categorizing values

**Questions:** 21–30

---

## 4️⃣ Working With Strings

This section focuses on using list comprehensions with string data.

Topics include:

* Converting text to uppercase
* Converting text to lowercase
* Reversing strings
* Removing extra spaces
* Filtering email addresses
* Finding the first character
* Finding the last character
* Extracting first names
* Finding string lengths

**Questions:** 31–40

---

## 5️⃣ More Challenging Problems

This section combines multiple concepts and focuses more on programming logic.

Topics include:

* Combining mathematical operations and conditions
* Using `abs()`
* Calculating proportions
* Working with indexes using `enumerate()`
* Flattening nested lists
* Creating tuples
* Applying multiple conditions
* Categorizing sales data

**Questions:** 41–50

---

# 💻 Sample Solutions

## Example 1: Square Every Number

```python
numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

---

## Example 2: Filter Even Numbers

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)
```

Output:

```text
[2, 4, 6]
```

---

## Example 3: Using `if-else`

```python
numbers = [1, 2, 3, 4, 5]

result = ["Even" if number % 2 == 0 else "Odd" for number in numbers]

print(result)
```

Output:

```text
['Odd', 'Even', 'Odd', 'Even', 'Odd']
```

---

# 📂 Suggested Repository Structure

```text
list-comprehension-practice/
│
├── README.md
│
├── questions/
│   ├── basic_questions.py
│   ├── conditional_questions.py
│   ├── if_else_questions.py
│   ├── string_questions.py
│   └── advanced_questions.py
│
└── solutions/
    ├── basic_solutions.py
    ├── conditional_solutions.py
    ├── if_else_solutions.py
    ├── string_solutions.py
    └── advanced_solutions.py
```

You can also keep all questions and solutions in a single file while practicing:

```text
list_comprehension_practice.py
```

---

# 🚀 How to Use This Repository

1. Clone or download the repository.

2. Open the Python file in your preferred code editor.

3. Read one question at a time.

4. Try solving the problem yourself using a list comprehension.

5. Run the code and check your output.

6. Compare your solution with the expected output where provided.

7. Move to the next question only after understanding the logic.

---

# 🛠️ Requirements

To run the exercises, you need:

* Python 3.x
* A code editor such as VS Code, PyCharm, or Jupyter Notebook

No external libraries are required.

---

# 📈 Topics Practiced

```text
Python
│
├── Lists
├── For Loops
├── List Comprehensions
├── Conditional Statements
│   ├── if
│   ├── if-else
│   └── Multiple Conditions
│
├── Strings
│   ├── upper()
│   ├── lower()
│   ├── strip()
│   ├── split()
│   └── Slicing
│
├── Built-in Functions
│   ├── len()
│   ├── abs()
│   ├── range()
│   ├── enumerate()
│   └── sum()
│
└── Problem Solving
```

---

# 🎯 Goal

The goal of these exercises is not just to memorize list comprehension syntax.

The main objective is to understand the logic behind:

```text
Iterable
    ↓
Loop through each item
    ↓
Apply an operation or condition
    ↓
Create a new list
```

By practicing these problems, I am working on writing cleaner and more concise Python code while strengthening my problem-solving skills.

---

# 📊 Connection to Data Analytics

List comprehensions are useful when working with data because they can help perform operations such as:

* Cleaning text data
* Transforming values
* Filtering records
* Categorizing data
* Creating calculated values
* Preparing data before analysis

For example:

```python
sales = [1200, 450, 800, 1500, 300, 2000, 950]

categories = [
    "High" if sale >= 1500
    else "Medium" if sale >= 800
    else "Low"
    for sale in sales
]

print(categories)
```

Output:

```text
['Medium', 'Low', 'Medium', 'High', 'Low', 'High', 'Medium']
```

These same logical concepts can later be applied when working with libraries such as **Pandas** and **NumPy**.

---

# 📌 Progress

* [x] Basic List Comprehensions
* [x] List Comprehensions With Conditions
* [x] List Comprehensions With `if-else`
* [x] String Operations
* [x] Advanced Practice Problems
* [ ] Complete all solutions independently
* [ ] Review and optimize solutions

---

# 👩‍💻 Author

**Naila Iram**

Aspiring Data Analyst | Python | SQL | Power BI | Data Analytics

---

⭐ If you find this repository useful, feel free to star it!
