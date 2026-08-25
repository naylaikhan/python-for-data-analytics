# Python Sets Practice

## 📌 About This Repository

This repository contains **50 Python practice questions focused on Sets**.

The purpose of this practice is to build a strong understanding of how Python Sets work and improve problem-solving and logical thinking skills.

The questions start with basic concepts and gradually move toward more advanced and **Data Analyst-style problems**.

---

# 📚 Topics Covered

This repository covers the following Set concepts:

* Creating Sets
* Creating an empty Set
* Unique values
* Removing duplicates
* Converting Lists to Sets
* Converting Strings to Sets
* `len()` with Sets
* Membership testing using `in` and `not in`
* Adding elements using `add()`
* Adding multiple elements using `update()`
* Removing elements using `remove()`
* Safely removing elements using `discard()`
* Removing arbitrary elements using `pop()`
* Clearing Sets using `clear()`
* Looping through Sets
* Conditional statements with Sets
* Union
* Intersection
* Difference
* Symmetric Difference
* Subsets
* Supersets
* Disjoint Sets
* Set Comprehension
* Finding duplicates
* Comparing Lists using Sets
* Finding common and unique values
* Customer analysis using Sets
* Website visitor analysis

---

# 🧠 What is a Set?

A **Set** is a built-in Python data structure used to store multiple values.

The most important characteristics of a Set are:

* Sets store **unique values**
* Duplicate values are automatically removed
* Sets are **unordered**
* Sets are mutable, meaning they can be modified
* Sets do not support indexing
* Set elements must be hashable

### Example

```python
numbers = {10, 20, 20, 30, 30, 40}

print(numbers)
```

Output:

```text
{10, 20, 30, 40}
```

The duplicate values are automatically removed.

---

# 🎯 Practice Questions

The 50 questions are divided into different levels.

## Level 1: Understanding and Creating Sets

Questions **1–10** focus on:

* Creating Sets
* Creating empty Sets
* Removing duplicates
* Counting unique values
* Creating Sets from Lists
* Creating Sets from Strings
* Membership testing
* Comparing Sets

---

## Level 2: Adding and Updating Sets

Questions **11–16** focus on:

* `add()`
* Adding duplicate values
* `update()`
* Adding values from Lists
* Adding characters from Strings
* Taking user input and storing unique values

---

## Level 3: Removing Elements

Questions **17–22** focus on:

* `remove()`
* `discard()`
* `pop()`
* `clear()`
* Understanding the difference between `remove()` and `discard()`
* Removing values safely

---

## Level 4: Looping and Conditions

Questions **23–29** focus on:

* Looping through Sets
* Finding even numbers
* Using conditional statements
* Calculating the sum manually
* Counting elements based on conditions
* Finding the largest number without `max()`
* Finding the smallest number without `min()`

---

## Level 5: Set Operations

Questions **30–35** focus on the most important Set operations:

### Union

Combines all unique values from both Sets.

```python
A | B
```

or

```python
A.union(B)
```

---

### Intersection

Finds values common to both Sets.

```python
A & B
```

or

```python
A.intersection(B)
```

---

### Difference

Finds values present in one Set but not another.

```python
A - B
```

---

### Symmetric Difference

Finds values that exist in either Set but not in both.

```python
A ^ B
```

or

```python
A.symmetric_difference(B)
```

---

## Level 6: Subsets, Supersets and Disjoint Sets

Questions **36–39** focus on:

* `issubset()`
* `issuperset()`
* `isdisjoint()`

Example:

```python
A = {1, 2, 3, 4, 5}
B = {2, 3, 4}

print(B.issubset(A))
```

---

## Level 7: Set Comprehension

Questions **40–43** focus on creating Sets using concise Python syntax.

Example:

```python
numbers = {1, 2, 3, 4, 5}

squares = {x ** 2 for x in numbers}

print(squares)
```

Output:

```text
{1, 4, 9, 16, 25}
```

Set comprehensions can also include conditions:

```python
even_numbers = {x for x in range(1, 21) if x % 2 == 0}
```

---

## Level 8: Logic-Building Problems

Questions **44–48** focus on improving problem-solving skills.

Topics include:

* Finding duplicate values
* Finding unique values between two Lists
* Finding common students
* Finding students with only one skill
* Finding all unique students across multiple groups

These questions require combining:

* Sets
* Loops
* Conditional statements
* Set operations

---

## Level 9: Data Analyst-Style Problems

Questions **49–50** focus on practical data analysis scenarios.

Examples include:

### Customer Analysis

Using customer data from different months to find:

* Returning customers
* New customers
* Customers who stopped appearing
* All unique customers
* Customers appearing in only one month

### Website Visitor Analysis

Using visitor data from multiple days to find:

* Total unique visitors
* Returning visitors
* Visitors common across multiple days
* Visitors appearing on only one day

These are examples of how Set operations can be useful when working with real-world datasets.

---

# 🛠️ Important Set Methods

| Method                   | Description                                                      |
| ------------------------ | ---------------------------------------------------------------- |
| `add()`                  | Adds one element                                                 |
| `update()`               | Adds multiple elements                                           |
| `remove()`               | Removes an element and raises an error if it does not exist      |
| `discard()`              | Removes an element without raising an error if it does not exist |
| `pop()`                  | Removes and returns an arbitrary element                         |
| `clear()`                | Removes all elements                                             |
| `union()`                | Combines unique values from Sets                                 |
| `intersection()`         | Finds common values                                              |
| `difference()`           | Finds values present in one Set but not another                  |
| `symmetric_difference()` | Finds values that are not common                                 |
| `issubset()`             | Checks whether one Set is a subset of another                    |
| `issuperset()`           | Checks whether one Set contains another                          |
| `isdisjoint()`           | Checks whether two Sets have no common elements                  |

---

# 🔑 Important Set Operators

| Operation            | Operator | Example  |    |    |
| -------------------- | -------- | -------- | -- | -- |
| Union                | `        | `        | `A | B` |
| Intersection         | `&`      | `A & B`  |    |    |
| Difference           | `-`      | `A - B`  |    |    |
| Symmetric Difference | `^`      | `A ^ B`  |    |    |
| Subset               | `<=`     | `A <= B` |    |    |
| Superset             | `>=`     | `A >= B` |    |    |

---

# 📂 Suggested Project Structure

```text
Python-Sets-Practice/
│
├── README.md
│
├── 01_creating_sets.py
├── 02_empty_sets.py
├── 03_removing_duplicates.py
├── 04_membership_testing.py
├── 05_adding_elements.py
├── 06_removing_elements.py
├── 07_looping_sets.py
├── 08_set_operations.py
├── 09_subsets_supersets.py
├── 10_set_comprehension.py
├── 11_logic_building.py
├── 12_customer_analysis.py
└── 13_website_visitor_analysis.py
```

You can also keep all 50 solutions in a single file:

```text
sets_practice.py
```

---

# 🚀 How to Run the Code

Clone the repository:

```bash
git clone <your-repository-url>
```

Move into the project folder:

```bash
cd Python-Sets-Practice
```

Run a Python file:

```bash
python filename.py
```

For example:

```bash
python 01_creating_sets.py
```

---

# 🧠 Learning Strategy

To get the maximum benefit from these questions:

1. Read the question carefully.
2. Try to understand the problem before writing code.
3. Think about which Set operation or method is required.
4. Write the solution yourself.
5. Run the code and check the output.
6. If the solution is wrong, debug it and understand why.
7. Avoid copying solutions without first attempting the problem.

A useful approach is to practice in this order:

```text
Questions 1–10   → Set basics
Questions 11–22  → Adding and removing elements
Questions 23–29  → Loops and conditions
Questions 30–39  → Set operations
Questions 40–43  → Set comprehension
Questions 44–48  → Logic-building problems
Questions 49–50  → Data Analyst-style problems
```

---

# 💡 Key Takeaways

By completing these exercises, you should be comfortable with:

* Understanding why Sets are useful
* Removing duplicate values
* Checking whether a value exists
* Adding and removing elements
* Looping through Sets
* Comparing groups of data
* Finding common values
* Finding unique values
* Using Union, Intersection, Difference, and Symmetric Difference
* Working with Subsets and Supersets
* Writing Set comprehensions
* Solving real-world data comparison problems

---

# 🎯 Goal

The goal of this repository is not just to memorize Set methods.

The main objective is to develop the ability to look at a problem and ask:

> **Do I need unique values?**

> **Do I need to find common values between two groups?**

> **Do I need values that exist in one group but not another?**

> **Can a Set make this problem simpler?**

Understanding these questions will help build stronger Python fundamentals and improve logical thinking for real-world programming and data analysis tasks.

---

## ⭐ Keep Practicing

The best way to learn Python is by writing code.

Don't worry if some questions feel difficult at first. Try to break each problem into smaller steps, understand the logic, and experiment with the code.

**Practice → Make Mistakes → Debug → Understand → Repeat**

Happy Coding! 🚀
