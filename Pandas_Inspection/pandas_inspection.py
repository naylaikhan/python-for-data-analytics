
import pandas as pd

"""1.

Create the following DataFrame:

data = {
    "Name": ["Aisha", "Rahul", "John", "Sara", "David"],
    "Age": [25, 32, 28, 35, 40],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"],
    "Salary": [40000, 60000, 50000, 75000, 90000]
}

Store it in a DataFrame called df and display the first 5 rows."""

print("==== Solution 1 ====")

data = {
    "Name": ["Aisha", "Rahul", "John", "Sara", "David"],
    "Age": [25, 32, 28, 35, 40],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"],
    "Salary": [40000, 60000, 50000, 75000, 90000]
}

df = pd.DataFrame(data)
print(df.head(5))

"""2.

Using the same DataFrame, display only the first 3 rows."""

print("==== Solution 2 ====")

print(df.head(3))

"""3.

Display the last 2 rows of the DataFrame.
"""
print("==== Solution 3 ====")

print(df.tail(2))

"""4.

Display one random row from the DataFrame."""

print("==== Solution 4 ====")

print(df.sample())

"""5.

Display 3 random rows from the DataFrame.
"""

print("==== Solution 5 ====")

print(df.sample(3))

"""6.

Find the total number of rows and columns in the DataFrame."""

print("==== Solution 6 ====")

print("total number of rows and columns in the DataFrame",df.shape)

"""7.

Find only the total number of rows."""

print("==== Solution 7 ====")

print("total number of rows :",df.shape[0])

"""8.

Find only the total number of columns."""

print("==== Solution 8 ====")

print("total number of columns :",df.shape[1])

"""9.

Display all column names in the DataFrame."""

print("==== Solution 9 ====")

print(df.columns)

"""10.

Display the index of the DataFrame."""

print("==== Solution 10 ====")

print(df.index)

"""11.

Check the data type of every column in the DataFrame."""

print("==== Solution 11 ====")

print(df.dtypes)

"""12.

Check the data type of only the Salary column."""

print("==== Solution 12 ====")

print(df["Salary"].dtypes)

"""13.

Use one Pandas command to get information about:

number of rows
column names
non-null values
data types"""

print("==== Solution 13 ====")

print(df.info())

"""14.

Generate a statistical summary of all numerical columns."""

print("==== Solution 14 ====")

print(df.describe())

"""15.

Find the minimum value in the Age column."""

print("==== Solution 15 ====")

print(df["Age"].min())

"""16.

Find the maximum value in the Salary column."""

print("==== Solution 16 ====")

print(df["Age"].max())

"""17.

Find the average age of all people in the DataFrame."""

print("==== Solution 17 ====")

print(df["Age"].mean())

"""18.

Find the median salary."""

print("==== Solution 18 ====")

print(df["Salary"].median())

"""19.

Find the total of all salaries."""

print("==== Solution 19 ====")

print(df["Salary"].sum())

"""20.

Find how many non-missing values exist in the Age column."""

print("==== Solution 20 ====")


print(df["Age"].count())

"""21.

Display all unique cities present in the City column."""

print("==== Solution 21 ====")

print(df["City"].unique())

"""22.

Find the total number of unique cities."""

print("==== Solution 22 ====")

print(df["City"].nunique())

"""23.

Find how many times each city appears in the DataFrame."""

print("==== Solution 23 ====")

print(df["City"].value_counts())

"""24.

Display statistical information specifically for text/object columns."""

print("==== Solution 24 ====")

print(df.describe(include="object"))

"""25.

Generate a summary that includes both numerical and text columns."""

print("==== Solution 25 ====")

print(df.describe(include="all"))

"""For the next questions, create this DataFrame:

data = {
    "Name": ["Aisha", "Rahul", "John", "Sara", "Rahul"],
    "Age": [25, 32, None, 35, 32],
    "City": ["Delhi", "Mumbai", None, "Pune", "Mumbai"],
    "Salary": [40000, 60000, 50000, None, 60000]
}

df = pd.DataFrame(data)"""

data = {
    "Name": ["Aisha", "Rahul", "John", "Sara", "Rahul"],
    "Age": [25, 32, None, 35, 32],
    "City": ["Delhi", "Mumbai", None, "Pune", "Mumbai"],
    "Salary": [40000, 60000, 50000, None, 60000]
}

df = pd.DataFrame(data)

"""26.

Check which values in the DataFrame are missing."""

print("==== Solution 26 ====")

print(df.isna().any())

"""27.

Find the number of missing values in each column."""

print("==== Solution 27 ====")

print(df.isna().sum())

"""28.

Calculate the percentage of missing values in each column."""

print("==== Solution 28 ====")

print(df.isna().sum()/len(df) * 100)

"""29.

Check which rows are duplicates."""

print("==== Solution 29 ====")

print(df[df.duplicated()])

"""30.

Find the total number of duplicate rows in the DataFrame."""

print("==== Solution 30 ====")

print(df.duplicated().sum())