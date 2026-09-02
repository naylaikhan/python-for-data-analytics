## NumPy Practice – 50 Coding Questions

This folder contains **50 hands-on NumPy practice questions** designed to build practical Python and data analysis skills.

The exercises progress from basic NumPy array creation and indexing to statistical analysis, filtering, reshaping, axis operations, and a mini data analysis challenge.

### 📌 About NumPy

**NumPy (Numerical Python)** is a Python library used for numerical computing and working with arrays.

It provides powerful tools for:

* Creating and manipulating arrays
* Performing mathematical calculations
* Statistical analysis
* Filtering data
* Reshaping data
* Working with multidimensional data
* Performing vectorized operations
* Generating random data

NumPy is also an important foundation for libraries such as **Pandas**, which is widely used in data analysis.

---

### 🎯 Learning Objectives

By completing these exercises, I aim to develop the ability to:

* Create NumPy arrays
* Understand 1D and 2D arrays
* Work with array dimensions and shapes
* Access individual elements
* Slice arrays
* Perform arithmetic operations on arrays
* Apply conditions and filters
* Calculate statistical measures
* Generate numerical sequences
* Create arrays of zeros and ones
* Reshape arrays
* Work with rows and columns
* Understand `axis`
* Use vectorized operations
* Use `np.where()`
* Work with unique values
* Handle `NaN` values
* Apply NumPy concepts to simple business-analysis problems

---

## 📚 Practice Questions

### Level 1 — Creating and Understanding Arrays

### Questions 1–10

Topics covered:

* `np.array()`
* 1D arrays
* 2D arrays
* `np.arange()`
* `np.linspace()`
* `np.zeros()`
* `np.ones()`
* `np.full()`
* `.ndim`
* `.shape`
* `.size`
* `.dtype`

Exercises include creating arrays, generating numerical sequences, creating 2D arrays, and inspecting array properties.

---

### Level 2 — Indexing and Slicing

### Questions 11–20

Topics covered:

* Positive indexing
* Negative indexing
* Array slicing
* 2D indexing
* Row selection
* Column selection
* Reversing arrays

These exercises focus on learning how to access specific values and portions of NumPy arrays.

---

### Level 3 — Arithmetic Operations

### Questions 21–30

Topics covered:

* Addition
* Subtraction
* Multiplication
* Division
* Percentage calculations
* Array-to-array operations
* Profit calculations
* Discounts
* Price increases
* Percentage growth

These exercises introduce **element-wise operations** and demonstrate how NumPy can be used for practical business calculations.

---

### Level 4 — Statistical Operations

### Questions 31–38

Topics covered:

* `np.sum()`
* `np.mean()`
* `np.median()`
* `np.min()`
* `np.max()`
* `np.std()`
* `np.var()`

The exercises use practical examples involving:

* Sales
* Employee salaries
* Customer ages

The goal is to become comfortable performing basic statistical analysis using NumPy.

---

### Level 5 — Filtering and Conditions

### Questions 39–45

Topics covered:

* Boolean conditions
* Boolean indexing
* Filtering arrays
* Counting values satisfying conditions
* `np.where()`

Practical scenarios include:

* Finding high-value sales
* Identifying customers above a certain age
* Finding failed students
* Identifying high-value transactions
* Categorizing values as `"High"` or `"Low"`

---

### Level 6 — Reshaping, Axis and Practical Analysis

### Questions 46–50

Topics covered:

* `.reshape()`
* Row-wise calculations
* Column-wise calculations
* `axis=0`
* `axis=1`
* Business-oriented analysis
* Combining multiple NumPy concepts

The final questions move from individual operations toward complete analytical tasks.

---

# 🧠 Key NumPy Concepts Practiced

| Concept               | Example              |
| --------------------- | -------------------- |
| Import NumPy          | `import numpy as np` |
| Create array          | `np.array()`         |
| Generate sequence     | `np.arange()`        |
| Evenly spaced values  | `np.linspace()`      |
| Zeros                 | `np.zeros()`         |
| Ones                  | `np.ones()`          |
| Filled array          | `np.full()`          |
| Dimensions            | `.ndim`              |
| Shape                 | `.shape`             |
| Number of elements    | `.size`              |
| Data type             | `.dtype`             |
| Indexing              | `arr[0]`             |
| Slicing               | `arr[1:4]`           |
| Filtering             | `arr[arr > 500]`     |
| Total                 | `np.sum()`           |
| Average               | `np.mean()`          |
| Median                | `np.median()`        |
| Minimum               | `np.min()`           |
| Maximum               | `np.max()`           |
| Standard deviation    | `np.std()`           |
| Variance              | `np.var()`           |
| Reshaping             | `arr.reshape()`      |
| Conditional values    | `np.where()`         |
| Unique values         | `np.unique()`        |
| Missing values        | `np.nan`             |
| Random data           | `np.random`          |
| Row/column operations | `axis`               |

---

# 💼 Data Analytics Applications

These exercises are designed around situations that are relevant to Data Analytics.

### Sales Analysis

```python
sales = np.array([1000, 1500, 2000, 2500])
```

Possible analysis:

* Total sales
* Average sales
* Highest sale
* Lowest sale
* Sales growth

### Customer Analysis

```python
ages = np.array([22, 35, 41, 28, 19, 52])
```

Possible analysis:

* Average customer age
* Youngest customer
* Oldest customer
* Customers above a certain age

### Financial Analysis

```python
sales = np.array([1000, 2000, 3000])
cost = np.array([600, 1200, 1800])
```

Possible analysis:

* Profit
* Average profit
* Highest profit
* Lowest profit

### Transaction Analysis

```python
transactions = np.array([
    1200, 450, 2300, 800,
    1500, 3200, 700, 1800
])
```

Possible analysis:

* Average transaction value
* High-value transactions
* Transaction counts
* Transaction distribution

---

# 📈 Difficulty Progression

```text
Level 1
Array Creation
     ↓
Level 2
Indexing & Slicing
     ↓
Level 3
Arithmetic Operations
     ↓
Level 4
Statistics
     ↓
Level 5
Filtering & Conditions
     ↓
Level 6
Reshaping & Axis
     ↓
Mini Data Analysis
```

The purpose of this progression is to first understand **how NumPy works**, then gradually use it to solve **data-analysis problems**.

---

# 🔑 Important NumPy Mindset

One of the main ideas I am practicing is **thinking in arrays rather than individual values**.

Instead of thinking:

```text
100 × 1.10
200 × 1.10
300 × 1.10
400 × 1.10
```

NumPy allows:

```python
sales * 1.10
```

This is known as **vectorized operation**.

Another important concept is filtering:

```python
sales[sales > 500]
```

which can be read as:

> "Give me the sales values where sales are greater than 500."

These concepts will be useful when moving from NumPy to **Pandas and real-world data analysis**.

---

# 🛠️ Tools Used

* Python
* NumPy
* Jupyter Notebook / Google Colab
* Git
* GitHub

---

# 📂 Suggested Folder Structure

```text
python-for-data-analytics/
│
├── NumPy/
│   │
│   ├── README.md
│   ├── numpy_practice.ipynb
│   └── numpy_practice.py
│
└── ...
```

---

# 🚀 Progress

* [ ] NumPy basics
* [ ] Array creation
* [ ] Indexing and slicing
* [ ] Arithmetic operations
* [ ] Statistical operations
* [ ] Boolean filtering
* [ ] `np.where()`
* [ ] Reshaping
* [ ] Axis operations
* [ ] Mini data analysis challenge

---

## 📌 Next Step

After completing these NumPy exercises, the next focus is **Pandas**, where these numerical concepts can be applied to real-world tabular datasets and Data Analyst workflows.
