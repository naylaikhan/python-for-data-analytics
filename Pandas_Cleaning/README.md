# 🧹 Pandas Cleaning – 50 Practice Questions

This section contains **50 hands-on practice questions on Pandas Data Cleaning**.

The purpose of these exercises is to build a strong understanding of how to identify, clean, transform, and validate messy datasets using the Pandas library.

The questions focus on practical scenarios commonly encountered in **Data Analysis** and real-world datasets.

---

## 📚 Topics Covered

The practice questions cover the following Pandas Data Cleaning concepts:

* Missing Values
* `isna()` and `isnull()`
* Counting Missing Values
* `dropna()`
* `fillna()`
* Mean and Median Imputation
* Mode Imputation
* Forward Fill (`ffill()`)
* Backward Fill (`bfill()`)
* Duplicate Detection
* `duplicated()`
* `drop_duplicates()`
* Cleaning Text Data
* `str.strip()`
* `str.lower()`
* `str.upper()`
* `str.title()`
* `replace()`
* Standardizing Categories
* Cleaning Column Names
* Data Type Conversion
* `astype()`
* `pd.to_numeric()`
* `pd.to_datetime()`
* Handling Invalid Numerical Values
* Cleaning Currency Values
* Handling Invalid Dates
* Data Validation

---

# 📋 Practice Questions

## Part 1: Missing Values

1. Create a DataFrame with columns `Name`, `Age`, and `Salary`, where at least 3 values are missing. Find the missing values in the entire DataFrame.

2. Using the same DataFrame, count the number of missing values in each column.

3. Find all rows that contain at least one missing value.

4. Find all rows where the `Age` column has a missing value.

5. Remove all rows containing at least one missing value.

6. Remove only the rows where all values are missing.

7. Remove columns that contain at least one missing value.

8. Fill all missing values in the `Age` column with `0`.

9. Fill missing values in the `Age` column using the mean age.

10. Fill missing values in the `Salary` column using the median salary.

11. Create a `City` column containing missing values and fill them using the most frequently occurring city.

12. Fill missing values in a `Sales` column using forward fill.

13. Fill missing values in a `Sales` column using backward fill.

14. Count how many missing values exist in each row.

15. Remove rows where the `Salary` column is missing, but keep rows that have missing values in other columns.

---

## Part 2: Duplicate Data

16. Create a DataFrame containing at least 3 duplicate rows. Find all duplicate rows.

17. Count the total number of duplicate rows in a DataFrame.

18. Remove duplicate rows while keeping the first occurrence.

19. Remove duplicate rows while keeping the last occurrence.

20. Remove all occurrences of duplicated rows.

21. Find duplicate records based only on the `Name` column.

22. Remove duplicates based on both `Name` and `City`.

23. Create a DataFrame where two employees have the same name but different salaries. Remove duplicates based only on `Name`.

24. Display all rows that are duplicates, including the first occurrence of each duplicate group.

---

## Part 3: Text Cleaning

Assume you have a DataFrame containing a `City` column with values like:

```text
" Delhi "
"delhi"
"DELHI"
" Mumbai "
"mUMBAI"
```

25. Remove unnecessary spaces from the beginning and end of every value in the `City` column.

26. Convert every value in the `City` column to lowercase.

27. Convert every value in the `City` column to uppercase.

28. Convert every value in the `City` column to title case.

29. Clean the `City` column so that all values become consistently formatted like:

```text
Delhi
Mumbai
```

30. Replace `"Bangaluru"` with `"Bangalore"`.

31. Replace multiple incorrect city names using a dictionary.

```text
Bangaluru → Bangalore
Bombay → Mumbai
Madras → Chennai
```

32. A `Gender` column contains:

```text
Male
male
MALE
M
Female
female
F
```

Clean and standardize the values so that only `Male` and `Female` remain.

33. A `Status` column contains:

```text
YES
Yes
yes
Y
NO
No
N
```

Standardize the column so that only `Yes` and `No` remain.

34. Remove leading and trailing spaces from the `Name` column and convert all names to title case.

---

## Part 4: Cleaning Column Names

Assume your DataFrame has these columns:

```text
Customer Name
Customer Age
Monthly Salary
City Name
```

35. Convert all column names to lowercase.

36. Replace spaces in all column names with underscores.

37. Convert the column names into this format:

```text
customer_name
customer_age
monthly_salary
city_name
```

38. Rename only `Monthly Salary` to `monthly_salary`.

39. A DataFrame contains column names with extra spaces:

```text
" Name "
" Age "
" Salary "
```

Remove unnecessary spaces from all column names.

---

## Part 5: Data Type Cleaning

40. A column `Age` contains:

```text
"25"
"30"
"Unknown"
"35"
```

Convert the column into numeric format. Invalid values should become missing values.

41. A `Salary` column contains:

```text
"50000"
"60000"
"Not Available"
"70000"
```

Convert the column to numeric values while handling invalid data.

42. A `Price` column contains:

```text
₹50,000
₹60,500
₹70,000
```

Remove the currency symbol and commas, then convert the column into numeric format.

43. A `Date` column contains:

```text
01/01/2026
15/02/2026
ABC
20/03/2026
```

Convert the column to datetime format while handling invalid values.

44. After converting a `Date` column into datetime format, create three new columns:

```text
Year
Month
Day
```

from the date.

---

## Part 6: Invalid and Incorrect Values

45. An `Age` column contains:

```text
25
30
-5
150
40
```

Identify the invalid age values.

46. Replace all ages below `0` and above `100` with missing values.

47. After replacing invalid ages with missing values, fill the missing ages using the median age.

48. A `Salary` column contains:

```text
50000
60000
0
-10000
75000
```

Identify the invalid salary values and remove those rows.

---

# 🚀 Real-World Cleaning Challenges

## Question 49

Create the following messy DataFrame:

| Name        | Age         | City          | Salary      |
| ----------- | ----------- | ------------- | ----------- |
| `" Rahul "` | `"25"`      | `"Delhi"`     | `"₹50,000"` |
| `"Priya"`   | `"28"`      | `" Mumbai "`  | `"₹60,000"` |
| `"Rahul"`   | `"25"`      | `"delhi"`     | `"₹50,000"` |
| `"Amit"`    | `"Unknown"` | `" Delhi "`   | `"₹55,000"` |
| `"Neha"`    | `"150"`     | `"Bangalore"` | `"₹70,000"` |

Perform the following cleaning tasks:

* Remove unnecessary spaces from `Name`
* Convert names to title case
* Clean and standardize `City`
* Convert `Age` to numeric
* Convert invalid age values to missing values
* Fill missing ages using the median
* Remove the ₹ symbol from `Salary`
* Remove commas from `Salary`
* Convert `Salary` to numeric
* Remove duplicate records
* Check the final data types
* Check missing values
* Check duplicates

---

## Question 50: Complete Pandas Cleaning Challenge

Create a messy employee dataset with at least **15 rows** containing all of the following problems:

* Missing values
* Duplicate rows
* Extra spaces
* Inconsistent capitalization
* Incorrect city names
* Incorrect gender values
* Age stored as text
* Invalid ages
* Salary stored as text
* Currency symbols
* Commas in salary
* Invalid salary values
* Invalid dates
* Messy column names

Then write a complete Pandas cleaning process that:

1. Inspects the DataFrame
2. Cleans column names
3. Checks missing values
4. Handles missing values appropriately
5. Finds duplicates
6. Removes duplicates
7. Cleans text columns
8. Standardizes categorical values
9. Fixes incorrect city names
10. Converts numerical columns
11. Handles invalid numerical values
12. Cleans salary values
13. Converts dates
14. Handles invalid dates
15. Removes unnecessary columns if present
16. Validates the final DataFrame using:

```python
df.shape
df.dtypes
df.isna().sum()
df.duplicated().sum()
df["column_name"].value_counts()
```

---

# 🎯 Learning Objective

After completing these 50 practice questions, you should be able to:

* Identify missing values in a dataset
* Handle missing data using different strategies
* Detect and remove duplicate records
* Clean messy text data
* Standardize categorical values
* Clean column names
* Convert incorrect data types
* Handle invalid numerical values
* Clean currency values
* Convert and validate date columns
* Identify suspicious or incorrect data
* Validate cleaned datasets
* Build a structured data-cleaning workflow

---

# 🧠 Data Cleaning Workflow

A useful workflow when working with a new dataset is:

```text
Load Data
    ↓
Inspect Data
    ↓
Check Data Types
    ↓
Check Missing Values
    ↓
Check Duplicates
    ↓
Clean Text
    ↓
Standardize Categories
    ↓
Fix Data Types
    ↓
Handle Invalid Values
    ↓
Handle Missing Data
    ↓
Remove Duplicates
    ↓
Validate Final Dataset
    ↓
Ready for Analysis
```

---

# 🛠️ Technologies Used

* Python
* Pandas
* Jupyter Notebook

---

# 📌 Important Note

Data cleaning is one of the most important steps in Data Analysis.

Incorrect, inconsistent, or missing data can produce misleading results even when the analysis code is correct.

The goal of these exercises is to develop the ability to inspect messy datasets, identify problems, apply appropriate cleaning techniques, and validate the final dataset before performing analysis.

---

⭐ **Practice consistently. Clean data leads to reliable analysis.**
