## Python Functions - Practice Questions

This section is part of my **Python for Data Analytics** learning journey.

The goal of these exercises is to build a strong understanding of **Python Functions**, improve problem-solving skills, and develop programming logic step by step.

---

## 📚 Topic Covered

### Functions

The practice exercises cover:

* Creating functions using `def`
* Calling functions
* Parameters and arguments
* Positional arguments
* Keyword arguments
* Default parameters
* `return` statements
* `print()` vs `return`
* Multiple parameters
* Functions with lists
* Functions with strings
* Conditional logic inside functions
* Loops inside functions
* Local and global variables
* Reusable functions
* Function-based problem solving
* Data-analysis-oriented functions
* Breaking larger problems into smaller functions

---

## 🎯 Learning Objectives

By completing these exercises, I aim to:

* Understand how functions work in Python
* Learn how to create reusable blocks of code
* Understand the difference between parameters and arguments
* Understand how values are passed into functions
* Understand how `return` works
* Learn when to use `print()` and when to use `return`
* Improve logical thinking and problem-solving ability
* Practice combining functions with lists, loops, and conditional statements
* Start thinking about how functions can be applied to real-world data analysis problems

---

# 📝 Practice Questions

The exercises are divided into different difficulty levels.

## 🟢 Level 1 — Function Basics

### Questions 1–10

These exercises focus on the fundamentals of functions:

* Creating a simple function
* Calling a function
* Using parameters
* Returning values
* Performing basic mathematical operations

Topics include:

* `def`
* Function calls
* Parameters
* Arguments
* `return`

---

## 🟢 Level 2 — Parameters and Return Values

### Questions 11–20

These exercises introduce functions that perform calculations and return useful results.

Topics include:

* Multiple parameters
* Boolean return values
* Conditional statements inside functions
* Mathematical calculations
* Comparing values
* Returning different results

Examples include:

* Dividing numbers
* Calculating areas
* Checking even/odd numbers
* Checking positive/negative numbers
* Finding larger and smaller values

---

## 🟡 Level 3 — Default and Multiple Parameters

### Questions 21–30

These exercises focus on making functions more flexible and reusable.

Topics include:

* Default parameters
* Multiple parameters
* Calculations using percentages
* Salary calculations
* Profit calculations
* Temperature conversion
* Percentage calculations

Examples include:

```python
calculate_discount(price, discount=10)
```

and:

```python
calculate_salary(basic_salary, bonus)
```

---

## 🟡 Level 4 — Functions + Lists

### Questions 31–40

These exercises combine functions with Python lists.

Topics include:

* Processing lists inside functions
* Calculating totals
* Calculating averages
* Finding maximum and minimum values
* Counting values
* Filtering values
* Creating new lists
* Working with positive and negative numbers

Examples include:

```python
calculate_sum(numbers)
```

```python
calculate_average(numbers)
```

```python
find_maximum(numbers)
```

```python
count_even(numbers)
```

---

## 🟠 Level 5 — Logic Building With Functions

### Questions 41–49

These exercises focus more heavily on programming logic.

Topics include:

* String processing
* Counting vowels
* Reversing strings
* Palindrome checking
* Counting words
* Removing duplicates
* Categorizing values
* Combining multiple functions
* Basic data analysis

These exercises require breaking a problem into logical steps before writing the code.

---

## 🔴 Level 6 — Advanced Logic / Data Analytics

### Question 50

### Website Visitors Analysis

The final exercise combines:

* Functions
* Sets
* Set operations
* Multiple datasets
* Data analysis logic

The problem involves analyzing website visitors across three different days.

The tasks include finding:

* Unique visitors
* Visitors who visited every day
* Visitors who visited only one day
* Total unique visitors
* Visitors shared between specific days

This exercise is designed to combine previously learned Python concepts into a more realistic data-analysis problem.

---

# 🧠 Key Concepts to Remember

A function generally follows this structure:

```python
def function_name(parameters):
    # logic
    return result
```

For example:

```python
def calculate_profit(revenue, cost):
    return revenue - cost
```

The function can then be reused:

```python
profit = calculate_profit(50000, 30000)

print(profit)
```

Output:

```text
20000
```

---

# 🔄 Function Execution Model

A useful way to think about a function is:

```text
Input
  ↓
Function
  ↓
Processing / Logic
  ↓
Return
  ↓
Output
```

For example:

```text
Revenue = 50,000
Cost = 30,000
       ↓
calculate_profit()
       ↓
50,000 - 30,000
       ↓
20,000
```

---

# 📌 Important Distinction

One of the most important concepts in this topic is understanding the difference between `print()` and `return`.

### `print()`

Displays a value:

```python
def add(a, b):
    print(a + b)
```

### `return`

Sends a value back:

```python
def add(a, b):
    return a + b
```

The returned value can then be stored and used:

```python
result = add(10, 20)

print(result)
```

Understanding this distinction is essential for writing reusable functions.

---

# 📊 Connection to Data Analytics

Functions are extremely useful in Data Analytics because the same operation often needs to be performed repeatedly.

For example, a function can be created to:

* Clean text
* Calculate averages
* Calculate profit
* Categorize customers
* Validate data
* Calculate KPIs
* Transform values
* Process lists
* Analyze sales
* Analyze website traffic

Example:

```python
def categorize_sales(sales):
    if sales >= 100000:
        return "Excellent"
    elif sales >= 75000:
        return "Good"
    elif sales >= 50000:
        return "Average"
    else:
        return "Needs Improvement"
```

A function like this can later be used with datasets and tools such as **Pandas**.

---

# 📂 Practice Structure

The exercises can be organized in the repository like this:

```text
python-for-data-analytics/
│
├── functions/
│   ├── 01_function_basics.py
│   ├── 02_parameters_arguments.py
│   ├── 03_return_values.py
│   ├── 04_default_parameters.py
│   ├── 05_functions_with_lists.py
│   ├── 06_logic_building.py
│   └── 07_data_analysis_functions.py
│
└── README.md
```

---

# 🚀 Learning Progression

The overall learning progression for Functions is:

```text
Create a Function
       ↓
Call a Function
       ↓
Parameters
       ↓
Arguments
       ↓
Return Values
       ↓
Default Parameters
       ↓
Conditional Logic
       ↓
Functions + Lists
       ↓
Functions + Loops
       ↓
Functions + Strings
       ↓
Functions + Sets
       ↓
Multiple Functions
       ↓
Data Analysis Problems
```

---

# ✅ Practice Goal

The goal is not just to memorize function syntax.

The main objective is to develop the ability to look at a problem and think:

```text
What is the task?
       ↓
What input do I have?
       ↓
What processing is required?
       ↓
Should I create a function?
       ↓
What parameters do I need?
       ↓
What should the function return?
```

This way of thinking will become increasingly important when working with **Python, Pandas, SQL, and Data Analytics projects**.

---

## 📈 Progress

* [ ] Function Basics
* [ ] Function Calls
* [ ] Parameters
* [ ] Arguments
* [ ] Return Values
* [ ] Positional Arguments
* [ ] Keyword Arguments
* [ ] Default Parameters
* [ ] Functions with Lists
* [ ] Functions with Strings
* [ ] Functions with Conditional Statements
* [ ] Functions with Loops
* [ ] Logic-Building Problems
* [ ] Data Analytics Functions
* [ ] Complete all 50 exercises

---

## 🏁 Practice Challenge

**50 Functions Practice Questions**

The exercises progress from simple function creation to more realistic data-analysis problems.

The objective is to build **strong Python fundamentals and programming logic** before moving deeper into libraries such as **Pandas and NumPy**.
