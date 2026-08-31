## 🐼 Pandas Intro – Practice Questions

This folder contains **60 hands-on practice questions on Pandas Introduction**.

The purpose of these exercises is to build a strong foundation in Pandas by practicing how to create, inspect, select, filter, sort, analyze, and manipulate data using **Series and DataFrames**.

These questions are designed for beginners who are learning Pandas for **Data Analysis**.

---

## 📚 Topics Covered

The practice questions cover the following Pandas concepts:

* Importing Pandas
* Creating Pandas Series
* Creating DataFrames
* Creating DataFrames using dictionaries
* Creating DataFrames using lists
* Understanding rows and columns
* Understanding indexes
* Inspecting DataFrames
* `head()`
* `tail()`
* `shape`
* `columns`
* `dtypes`
* `info()`
* Selecting single columns
* Selecting multiple columns
* Basic calculations
* `sum()`
* `mean()`
* `min()`
* `max()`
* `count()`
* Creating new columns
* Filtering data
* Multiple conditions
* AND (`&`) conditions
* OR (`|`) conditions
* Sorting data
* `sort_values()`
* Unique values
* `unique()`
* `nunique()`
* `value_counts()`
* Grouping data
* `groupby()`
* Basic aggregation

---

# 📝 Practice Questions

## Part 1: Creating Series and DataFrames

### 1.

Import the Pandas library using the standard alias `pd`.

### 2.

Create a Pandas Series containing the numbers:

```text
10, 20, 30, 40, 50
```

### 3.

Create a Pandas Series containing the names:

```text
John, Sarah, Alex, Emma, David
```

### 4.

Create a Pandas Series containing:

```text
True, False, True, True, False
```

### 5.

Create a Series containing the ages:

```text
25, 30, 22, 35, 28
```

and assign custom indexes:

```text
A, B, C, D, E
```

### 6.

Create a DataFrame using a dictionary with the following data:

| Name  | Age | City      |
| ----- | --- | --------- |
| John  | 25  | Delhi     |
| Sarah | 30  | Mumbai    |
| Alex  | 28  | Bangalore |
| Emma  | 35  | Pune      |

### 7.

Create a DataFrame containing the following employee data:

| Employee | Department | Salary |
| -------- | ---------- | ------ |
| John     | IT         | 50000  |
| Sarah    | HR         | 60000  |
| Alex     | Finance    | 55000  |
| Emma     | IT         | 70000  |

### 8.

Create a DataFrame from a list of dictionaries containing information about 4 students with:

* Name
* Age
* Marks

### 9.

Create a DataFrame from the following list of lists:

```text
John, 25, Delhi
Sarah, 30, Mumbai
Alex, 28, Pune
```

Use the column names:

```text
Name, Age, City
```

### 10.

Create a DataFrame with the following columns:

```text
Product
Category
Price
Quantity
```

Add at least 5 rows of data.

---

# Part 2: Inspecting DataFrames

For Questions **11–20**, use the following DataFrame:

```python
data = {
    "Name": ["John", "Sarah", "Alex", "Emma", "David", "Lisa"],
    "Age": [25, 30, 28, 35, 22, 40],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Delhi"],
    "Salary": [40000, 55000, 48000, 70000, 35000, 80000]
}
```

### 11.

Create a DataFrame from the given dictionary and store it in a variable called `df`.

### 12.

Display the complete DataFrame.

### 13.

Display the first 5 rows of the DataFrame.

### 14.

Display the first 3 rows of the DataFrame.

### 15.

Display the last 5 rows of the DataFrame.

### 16.

Display the last 2 rows of the DataFrame.

### 17.

Find the number of rows and columns in the DataFrame.

### 18.

Display all column names.

### 19.

Display the data type of every column.

### 20.

Display complete information about the DataFrame using a Pandas method.

---

# Part 3: Selecting Columns

Use the same DataFrame from Questions **11–20**.

### 21.

Select and display only the `Name` column.

### 22.

Select and display only the `Salary` column.

### 23.

Select the `Name` and `Age` columns together.

### 24.

Select the `Name`, `City`, and `Salary` columns together.

### 25.

Store the `Age` column in a variable called `ages`.

### 26.

Find the data type of the object returned when selecting a single column:

```python
df["Name"]
```

### 27.

Find the data type of the object returned when selecting multiple columns:

```python
df[["Name", "Age"]]
```

---

# Part 4: Basic Calculations and New Columns

Use the same DataFrame.

### 28.

Calculate the average salary of all employees.

### 29.

Find the highest salary.

### 30.

Find the lowest salary.

### 31.

Find the total salary of all employees.

### 32.

Count the number of non-missing values in the `Salary` column.

### 33.

Create a new column called `Annual Salary` by multiplying the monthly `Salary` by 12.

### 34.

Create a new column called `Bonus` where every employee receives 10% of their salary.

### 35.

Create a new column called `Salary After Raise` by increasing every employee's salary by 5%.

---

# Part 5: Filtering Data

Use the same DataFrame.

### 36.

Display all employees whose age is greater than 30.

### 37.

Display all employees whose age is less than 30.

### 38.

Display all employees whose salary is greater than 50,000.

### 39.

Display all employees who live in Delhi.

### 40.

Display all employees who live in Mumbai.

### 41.

Display employees whose salary is greater than 50,000 and whose age is greater than 30.

### 42.

Display employees who belong to Delhi or Mumbai.

### 43.

Display employees whose age is between 25 and 35.

### 44.

Display employees whose salary is less than 50,000.

### 45.

Display the names and salaries of employees earning more than 50,000.

---

# Part 6: Sorting Data

Use the same DataFrame.

### 46.

Sort the DataFrame by `Age` in ascending order.

### 47.

Sort the DataFrame by `Age` in descending order.

### 48.

Sort the DataFrame by `Salary` from lowest to highest.

### 49.

Sort the DataFrame by `Salary` from highest to lowest.

### 50.

Sort the DataFrame first by `City` and then by `Salary`.

---

# Part 7: Unique Values and Frequency

Use the same DataFrame.

### 51.

Find all unique cities in the DataFrame.

### 52.

Find the number of unique cities.

### 53.

Count how many employees belong to each city.

### 54.

Find the city with the highest number of employees.

### 55.

Count how many employees have each age.

---

# Part 8: Grouping Data

Use the same DataFrame.

### 56.

Find the average salary for each city.

### 57.

Find the total salary for each city.

### 58.

Find the maximum salary for each city.

### 59.

Find the minimum age for each city.

### 60.

Create a summary showing, for each city:

* Average salary
* Maximum salary
* Minimum salary
* Number of employees

---

## 🎯 Learning Objective

By completing these exercises, you should be able to:

* Create Pandas Series and DataFrames
* Understand the structure of tabular data
* Inspect a dataset before analysis
* Select single and multiple columns
* Perform basic calculations
* Create new columns
* Filter data using conditions
* Apply multiple filtering conditions
* Sort data
* Find unique values and frequencies
* Group and summarize data
* Perform basic data analysis using Pandas

---

## 🛠️ Technologies Used

* Python
* Pandas
* Jupyter Notebook

---

## 📂 Suggested Repository Structure

```text
Pandas-Intro/
│
├── README.md
│
└── pandas_intro_practice.ipynb
```

---

## 🚀 Key Takeaway

Pandas is one of the most important Python libraries for Data Analysis.

The most important concept to understand is:

```text
Data
 ↓
Pandas
 ↓
DataFrame
 ↓
Inspect
 ↓
Filter
 ↓
Transform
 ↓
Analyze
 ↓
Insights
```

These 60 practice questions focus on building the foundation required before moving to more advanced Pandas topics such as data cleaning, indexing, merging, joining, pivot tables, datetime operations, and advanced data analysis.

Happy Coding! 🐼🐍
