# 🔄 Python Loops - Practice Questions

A beginner-friendly collection of **40 Python loop practice questions** designed to build strong programming logic through repetition, conditions, counters, accumulators, searching, and data-processing problems.

This practice set is intended for beginners who have learned the basics of Python and want to become comfortable with **`for` loops, `while` loops, `range()`, `break`, `continue`, and practical loop-based problem solving**.

---

## 📚 Topics Covered

This practice set covers:

* `for` loops
* `while` loops
* `range()`
* Looping through lists
* Looping through strings
* Conditional statements inside loops
* `break`
* `continue`
* Counters
* Accumulators
* Finding minimum and maximum values
* Searching through data
* Building new lists
* Nested loop concepts
* Data-processing logic
* Data Analyst-style problems

---

## 🎯 Learning Objectives

By completing these 40 exercises, you should be able to:

* Understand how loops execute step by step
* Repeat a task efficiently using Python
* Iterate through lists and strings
* Generate number sequences using `range()`
* Combine loops with `if`, `elif`, and `else`
* Use counters to count matching values
* Use accumulators to calculate totals
* Search for specific values
* Stop loops using `break`
* Skip iterations using `continue`
* Build new lists using loops
* Understand and write `while` loops
* Solve basic data-processing problems using loops
* Develop the logical thinking required for Data Analysis

---

# 📝 Practice Questions

## 🟢 Part 1 - Basic `for` Loops

### Questions 1–10

Practice:

* Basic `for` loops
* `range()`
* Iterating through lists
* Iterating through strings
* Increasing and decreasing sequences

| #  | Practice Problem                               |
| -- | ---------------------------------------------- |
| 1  | Print numbers from 1 to 10                     |
| 2  | Print numbers from 0 to 20                     |
| 3  | Print even numbers from 1 to 20                |
| 4  | Print odd numbers from 1 to 20                 |
| 5  | Print every number in a list                   |
| 6  | Print every name in a list                     |
| 7  | Print each character of a string               |
| 8  | Print numbers from 5 to 15                     |
| 9  | Print numbers from 10 to 100 with a step of 10 |
| 10 | Print numbers from 20 to 1 in reverse          |

---

## 🟡 Part 2 — Loops with Conditions

### Questions 11–16

Practice combining loops with conditional logic.

You will work with:

```python
if
elif
else
```

Exercises include:

* Finding even numbers
* Finding positive numbers
* Identifying positive, negative, and zero values
* Checking passing marks
* Finding numbers divisible by a particular value

---

## 🟡 Part 3 — Accumulator & Counter Logic

### Questions 17–22

This section introduces two extremely important programming patterns:

### Counter

Used when you want to count how many items satisfy a condition.

```python
count = 0

for item in items:
    if condition:
        count += 1
```

### Accumulator

Used when you want to continuously add values to a total.

```python
total = 0

for item in items:
    total += item
```

Practice problems include:

* Calculating totals
* Calculating products
* Counting positive numbers
* Counting even numbers
* Counting students who passed
* Calculating total sales

These patterns are especially important when working with datasets.

---

## 🟠 Part 4 — Finding & Searching

### Questions 23–26

Practice using loops to:

* Find the largest value
* Find the smallest value
* Search for a particular value
* Stop searching once a value is found

You will practice logic such as:

```python
if number > largest:
    largest = number
```

and:

```python
if number == target:
    break
```

---

## 🟠 Part 5 — `break` & `continue`

### Questions 27–30

Learn the difference between:

### `break`

Stops the entire loop.

```python
for number in numbers:
    if number == 5:
        break
```

### `continue`

Skips the current iteration and moves to the next one.

```python
for number in numbers:
    if number < 0:
        continue
```

Practice includes:

* Stopping a loop at a particular value
* Skipping specific values
* Stopping when a sentinel value appears
* Ignoring unwanted data

---

## 🟠 Part 6 — Building New Lists

### Questions 31–33

Practice using loops to transform existing data.

For example:

```python
numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number ** 2)
```

You will practice:

* Creating a list of squared numbers
* Filtering values into a new list
* Converting strings to uppercase

This introduces an important data-processing concept:

> **Input → Process → Output**

---

## 🔵 Part 7 — `while` Loops

### Questions 34–38

Practice:

* Basic `while` loops
* Increasing counters
* Decreasing counters
* Calculating totals
* Understanding loop termination

A typical `while` loop looks like:

```python
number = 1

while number <= 10:
    print(number)
    number += 1
```

### ⚠️ Important

Always ask yourself:

> **What will eventually make my `while` condition become `False`?**

Forgetting to update the variable can create an **infinite loop**.

---

## 🔴 Part 8 — Data Analyst-Level Challenges

### Questions 39–40

The final two questions combine multiple concepts.

You will work with transaction and sales data to calculate:

* Counts
* Totals
* Positive values
* Negative values
* Zero values
* Maximum values
* Conditional filtering

For example:

```python
transactions = [500, -200, 1000, 0, -150, 750, 1200, -50]
```

The goal is to process the dataset using **one loop** rather than writing separate logic for every value.

This is closer to the type of logical thinking you'll need when working with real-world data.

---

# 🧠 Important Concepts to Remember

## 1. Every loop has iterations

If you have:

```python
for number in [10, 20, 30]:
    print(number)
```

there are **3 iterations**.

Think:

```text
Iteration 1 → 10
Iteration 2 → 20
Iteration 3 → 30
```

---

## 2. `range()` excludes the stop value

```python
range(1, 6)
```

produces:

```text
1 2 3 4 5
```

It does **not** include `6`.

---

## 3. `break` stops

```python
break
```

means:

> Stop the entire loop.

---

## 4. `continue` skips

```python
continue
```

means:

> Skip this iteration and move to the next one.

---

## 5. Initialize accumulators before the loop

Correct:

```python
total = 0

for number in numbers:
    total += number
```

Avoid resetting the accumulator inside the loop.

---

## 6. `while` loops need a changing condition

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

The variable changes:

```text
1 → 2 → 3 → 4 → 5 → 6
```

Eventually the condition becomes false and the loop stops.

---

# 🧩 Recommended Problem-Solving Method

For every exercise, don't immediately start typing code.

First ask yourself:

### Step 1 — What needs to be repeated?

Example:

> I need to check every number.

### Step 2 — What am I looping through?

Example:

```python
numbers
```

### Step 3 — What should happen to each item?

Example:

> Check whether the number is even.

### Step 4 — Do I need a counter?

If you're counting something:

```python
count = 0
```

### Step 5 — Do I need an accumulator?

If you're calculating a total:

```python
total = 0
```

### Step 6 — Do I need to stop or skip?

Use:

```python
break
```

or:

```python
continue
```

### Step 7 — Dry run your logic

Take a small example and manually trace:

```text
Current value
↓
Condition
↓
Action
↓
Variable update
↓
Next iteration
```

This is one of the best ways to develop programming logic.

---

# 📊 Why Loops Matter for Data Analysis

Although libraries such as **Pandas** allow you to perform many operations without explicitly writing loops, understanding loops is still important.

Loops teach you the fundamental logic behind operations such as:

* Filtering records
* Counting observations
* Calculating totals
* Searching for conditions
* Transforming values
* Processing records
* Identifying anomalies
* Applying business rules

For example, this loop:

```python
for transaction in transactions:
    if transaction > 1000:
        count += 1
```

represents a simple business question:

> **How many transactions exceeded 1,000?**

That's the type of logical thinking that later translates into SQL, Pandas, Power BI, and other analytical tools.

---

# 🚀 Difficulty Progression

| Level           | Questions | Focus                                           |
| --------------- | --------: | ----------------------------------------------- |
| 🟢 Beginner     |      1–10 | Basic `for` loops                               |
| 🟡 Beginner+    |     11–22 | Conditions, counters & accumulators             |
| 🟠 Intermediate |     23–33 | Searching, `break`, `continue`, list processing |
| 🔵 Intermediate |     34–38 | `while` loops                                   |
| 🔴 Challenge    |     39–40 | Data-processing logic                           |

---

# 📌 Rules for Practice

Try to solve the exercises **without looking for solutions immediately**.

For the first attempt, avoid using shortcuts such as:

```python
sum()
max()
min()
filter()
```

where the question specifically asks you to implement the logic using a loop.

The objective is not simply to get the correct output.

The objective is to understand:

> **How Python moves through each item and how your variables change during every iteration.**

---

# 🎯 Final Goal

After completing these 40 questions, you should be comfortable writing logic like:

```python
total = 0
count = 0

for value in data:

    if value > 0:
        total += value
        count += 1
```

and:

```python
number = 1

while number <= 10:
    print(number)
    number += 1
```

Once these patterns become natural, you will have a much stronger foundation for the next Python topics, especially **functions, lists, dictionaries, list comprehensions, and Pandas**.

---

## 📂 Repository Structure

A simple structure for this practice repository could be:

```text
Python-Loops/
│
├── README.md
│
├── loops_practice.ipynb
│
└── solutions/
    └── loops_solutions.ipynb
```

---

## ⭐ Progress Tracker

* [ ] Questions 1–10 — Basic `for` loops
* [ ] Questions 11–16 — Conditions
* [ ] Questions 17–22 — Counters & accumulators
* [ ] Questions 23–26 — Searching & finding
* [ ] Questions 27–30 — `break` & `continue`
* [ ] Questions 31–33 — Building new lists
* [ ] Questions 34–38 — `while` loops
* [ ] Questions 39–40 — Data Analyst challenges

---

## 🛠️ Technologies

* **Python 3**
* **Jupyter Notebook**
* **VS Code** / **PyCharm** / **Google Colab**

---

## 👩‍💻 Learning Approach

This repository is part of my Python learning journey, with a focus on developing **strong programming fundamentals and problem-solving skills for Data Analytics**.

The exercises progress from simple repetition to practical data-processing problems, helping bridge the gap between learning Python syntax and applying Python logic to real-world analytical scenarios.

---

## 📈 Next Steps

After completing these exercises, continue with:

1. Functions
2. Lists
3. Tuples
4. Dictionaries
5. Sets
6. List Comprehensions
7. Error Handling
8. File Handling
9. NumPy
10. Pandas

---

⭐ **If you're also learning Python, don't just memorize the syntax. Trace every loop, understand every iteration, and build the logic step by step.**
