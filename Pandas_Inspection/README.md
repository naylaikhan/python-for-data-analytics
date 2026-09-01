# Pandas Inspection – Practice Questions

## 📌 Overview

This repository section contains **30 practical questions on Pandas Inspection**.

Pandas Inspection is the process of exploring and understanding a dataset before performing data cleaning, analysis, or visualization. These exercises are designed to help build a strong understanding of how to inspect the structure, content, data types, missing values, duplicates, and statistical information in a Pandas DataFrame.

---

## 📚 Topics Covered

The practice questions cover the following Pandas Inspection concepts:

* `head()`
* `tail()`
* `sample()`
* `shape`
* `shape[0]`
* `shape[1]`
* `columns`
* `index`
* `dtypes`
* `info()`
* `describe()`
* `describe(include="object")`
* `describe(include="all")`
* `min()`
* `max()`
* `mean()`
* `median()`
* `sum()`
* `count()`
* `unique()`
* `nunique()`
* `value_counts()`
* `isnull()`
* `isnull().sum()`
* Missing value percentage calculation
* `duplicated()`
* `duplicated().sum()`

---

# 📝 Practice Questions

## Basic Inspection

### 1.

Create the following DataFrame:

```python
data = {
    "Name": ["Aisha", "Rahul", "John", "Sara", "David"],
    "Age": [25, 32, 28, 35, 40],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"],
    "Salary": [40000, 60000, 50000, 75000, 90000]
}
```

Store it in a DataFrame called `df` and display the first 5 rows.

---

### 2.

Using the same DataFrame, display only the first 3 rows.

---

### 3.

Display the last 2 rows of the DataFrame.

---

### 4.

Display one random row from the DataFrame.

---

### 5.

Display 3 random rows from the DataFrame.

---

# Shape and Structure

### 6.

Find the total number of rows and columns in the DataFrame.

---

### 7.

Find only the total number of rows.

---

### 8.

Find only the total number of columns.

---

### 9.

Display all column names in the DataFrame.

---

### 10.

Display the index of the DataFrame.

---

# Data Types

### 11.

Check the data type of every column in the DataFrame.

---

### 12.

Check the data type of only the `Salary` column.

---

### 13.

Use one Pandas command to get information about:

* Number of rows
* Column names
* Non-null values
* Data types

---

# Statistical Inspection

### 14.

Generate a statistical summary of all numerical columns.

---

### 15.

Find the minimum value in the `Age` column.

---

### 16.

Find the maximum value in the `Salary` column.

---

### 17.

Find the average age of all people in the DataFrame.

---

### 18.

Find the median salary.

---

### 19.

Find the total of all salaries.

---

### 20.

Find how many non-missing values exist in the `Age` column.

---

# Unique Values and Frequency

### 21.

Display all unique cities present in the `City` column.

---

### 22.

Find the total number of unique cities.

---

### 23.

Find how many times each city appears in the DataFrame.

---

### 24.

Display statistical information specifically for text/object columns.

---

### 25.

Generate a summary that includes both numerical and text columns.

---

# Missing Values and Duplicates

For the following questions, use this DataFrame:

```python
data = {
    "Name": ["Aisha", "Rahul", "John", "Sara", "Rahul"],
    "Age": [25, 32, None, 35, 32],
    "City": ["Delhi", "Mumbai", None, "Pune", "Mumbai"],
    "Salary": [40000, 60000, 50000, None, 60000]
}

df = pd.DataFrame(data)
```

### 26.

Check which values in the DataFrame are missing.

---

### 27.

Find the number of missing values in each column.

---

### 28.

Calculate the percentage of missing values in each column.

---

### 29.

Check which rows are duplicates.

---

### 30.

Find the total number of duplicate rows in the DataFrame.

---

# 🎯 Learning Objectives

After completing these exercises, you should be able to:

* Inspect the first and last records of a dataset.
* Check random records from a DataFrame.
* Understand the size and structure of a dataset.
* Identify rows and columns.
* Inspect column names and indexes.
* Check data types of columns.
* Understand DataFrame information using `info()`.
* Generate statistical summaries using `describe()`.
* Identify minimum, maximum, mean, median, and total values.
* Find unique values and count their occurrences.
* Identify missing values in a dataset.
* Calculate missing value percentages.
* Detect duplicate rows.
* Perform a basic data inspection workflow before starting analysis.

---

# 💡 Key Takeaway

Before cleaning or analyzing a dataset, it is important to first understand what the dataset contains.

A typical Pandas inspection workflow looks like this:

```python
df.head()

df.tail()

df.sample()

df.shape

df.columns

df.dtypes

df.info()

df.describe()

df.isnull().sum()

df.duplicated().sum()
```

For categorical columns:

```python
df["Column"].unique()

df["Column"].nunique()

df["Column"].value_counts()
```

> **Inspect → Understand → Clean → Analyze → Visualize → Interpret**

Understanding your dataset is the first step toward performing accurate and meaningful data analysis.

---

⭐ If you found this repository useful, consider giving it a star!
