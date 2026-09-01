"""Part 1: Creating Series and DataFrames"""

"""1. Import the Pandas library using the standard alias pd."""

import pandas as pd

"""2. Create a Pandas Series containing the numbers:

10, 20, 30, 40, 50"""

print("====== Solution 2 ======")
numbers = pd.Series([10, 20, 30, 40, 50])
print(numbers)

"""3. Create a Pandas Series containing the names:

John, Sarah, Alex, Emma, David"""

print("====== Solution 3 ======")
names = pd.Series(["John","Sarah","Alex","Emma","David"])
print(names)

"""4. Create a Pandas Series containing:

True, False, True, True, False"""

print("====== Solution 4 ======")
boolean_value = pd.Series([True, False, True, True, False])
print(boolean_value)

"""5. Create a Series containing the ages:

25, 30, 22, 35, 28

and assign custom indexes:

A, B, C, D, E"""

print("====== Solution 5 ======")
ages = pd.Series([25, 30, 22, 35, 28], index =["A","B","C","D","E"])
print(ages)

"""6. Create a DataFrame using a dictionary with the following data:

Name	Age	City
John	25	Delhi
Sarah	30	Mumbai
Alex	28	Bangalore
Emma	35	Pune"""

print("====== Solution 6 ======")

data = {
    "Name" : ["John","Sarah","Alex","Emma"],
    "Age"  : [25,30,28,35],
    "city" : ["Delhi","Mumbai","Bangalore","Pune"]
}

df = pd.DataFrame(data)
print(df)

"""7. Create a DataFrame containing the following employee data:

Employee	Department	Salary
John	IT	50000
Sarah	HR	60000
Alex	Finance	55000
Emma	IT	70000"""

print("====== Solution 7 ======")

df = pd.DataFrame(data={
    "Employee" : ["John","Sarah","Alex","Emma"],
    "Department" : ["IT","HR","Finance","IT"],
    "Salary"  : [50000,60000,55000,70000]
})

print(df)

"""8. Create a DataFrame from a list of dictionaries containing information about 4 students with:

Name
Age
Marks"""

print("====== Solution 8 ======")

data = [{"Name":"John" ,"Age":25,"Marks":85},
        {"Name":"Sarah" ,"Age":30,"Marks":75},
        {"Name":"Alex" ,"Age":28,"Marks":65},
        {"Name":"Emma" ,"Age":22,"Marks":95}]

df = pd.DataFrame(data)
print(df)

"""9. Create a DataFrame from the following list of lists:

John, 25, Delhi
Sarah, 30, Mumbai
Alex, 28, Pune

Use the column names:

Name, Age, City"""

print("====== Solution 9 ======")

data = [["John", 25, "Delhi"],["Sarah", 30, "Mumbai"],["Alex", 28, "Pune"]]
df = pd.DataFrame(data,columns=["Name","Age","City"])
print(df)

"""10. Create a DataFrame with the following columns:

Product
Category
Price
Quantity

Add at least 5 rows of data."""

print("====== Solution 10 ======")

data = []
df = pd.DataFrame(data ,index=[0,1,2,3,4],columns=["Product","Category","Price","Quantity"])
df["Product"] = ["Laptop","Mobile","Tv","Camera","PC"]
df["Category"] =["Electronics","Electronics","Electronics","Electronics","Electronics"]
df["Price"] = [85000,55000,88000,65000,87000]
df["Quantity"] = [2,4,1,3,2]
print(df)

"""Part 2: Inspecting DataFrames

For Questions 11–20, use the following DataFrame:

data = {
    "Name": ["John", "Sarah", "Alex", "Emma", "David", "Lisa"],
    "Age": [25, 30, 28, 35, 22, 40],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Delhi"],
    "Salary": [40000, 55000, 48000, 70000, 35000, 80000]
}"""

data = {
    "Name": ["John", "Sarah", "Alex", "Emma", "David", "Lisa"],
    "Age": [25, 30, 28, 35, 22, 40],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Delhi"],
    "Salary": [40000, 55000, 48000, 70000, 35000, 80000]
}

"""11. Create a DataFrame from the given dictionary and store it in a variable called df."""

print("====== Solution 11 ======")

df = pd.DataFrame(data)
print(df)

"""12. Display the complete DataFrame."""

print("====== Solution 12 ======")

print(df)

"""13. Display the first 5 rows of the DataFrame."""

print("====== Solution 13 ======")

print(df.head(5))

"""14. Display the first 3 rows of the DataFrame."""

print("====== Solution 14 ======")

print(df.head(3))

"""15. Display the last 5 rows of the DataFrame."""

print("====== Solution 15 ======")

print(df.tail(5))

"""16. Display the last 2 rows of the DataFrame."""

print("====== Solution 16 ======")

print(df.tail(2))

"""17. Find the number of rows and columns in the DataFrame."""

print("====== Solution 17 ======")

print("number of rows and columns in the DataFrame :",df.shape)

"""18. Display all column names."""

print("====== Solution 18 ======")

print(df.columns)

"""19. Display the data type of every column."""

print("====== Solution 19 ======")

print(df.dtypes)

"""20. Display complete information about the DataFrame using a Pandas method."""

print("====== Solution 20 ======")

print(df.info())

""""Part 3: Selecting Columns

Use the same DataFrame from Questions 11–20."""""

"""21. Select and display only the Name column."""

print("====== Solution 21 ======")

print(df["Name"])

"""22. Select and display only the Salary column."""

print("====== Solution 22 ======")

print(df["Salary"])

"""23. Select the Name and Age columns together."""

print("====== Solution 23 ======")

print(df[["Name","Age"]])

"""24. Select the Name, City, and Salary columns together."""

print("====== Solution 24 ======")

print(df[["Name","City","Salary"]])

"""25. Store the Age column in a variable called ages."""

print("====== Solution 25 ======")

ages = df["Age"]
print(ages)

"""26. Find the data type of the object returned when selecting a single column:

df["Name"]"""

print("====== Solution 26 ======")

print(type(df["Name"]))

"""27. Find the data type of the object returned when selecting multiple columns:

df[["Name", "Age"]]"""

print("====== Solution 27 ======")

print(type(df[["Name", "Age"]]))

"""Part 4: Basic Calculations and New Columns

Use the same DataFrame."""

"""28. Calculate the average salary of all employees."""

print("====== Solution 28 ======")

average_salary = df["Salary"].mean()
print(average_salary)

"""29. Find the highest salary."""

print("====== Solution 29 ======")

highest_salary = df["Salary"].max()
print(highest_salary)

"""30. Find the lowest salary."""

print("====== Solution 30 ======")

lowest_salary = df["Salary"].min()
print(lowest_salary)

"""31. Find the total salary of all employees."""

print("====== Solution 31 ======")

total_salary = df["Salary"].sum()
print(total_salary)

"""32. Count the number of non-missing values in the Salary column."""

print("====== Solution 32 ======")
non_missing_count = df["Salary"].count()
print(non_missing_count)

"""33. Create a new column called Annual Salary by multiplying the monthly Salary by 12."""

print("====== Solution 33 ======")

df["Annual_Salary"] = df["Salary"] * 12
print(df)

"""34. Create a new column called Bonus where every employee receives 10% of their salary."""

print("====== Solution 34 ======")

df["Bonus"] = df["Salary"] * 0.1
print(df)

"""35. Create a new column called Salary After Raise by increasing every employee's salary by 5%."""

print("====== Solution 34 ======")

df["Raised_Salary"] = df["Salary"] + ( df["Salary"] * 0.05 )
print(df)

"""Part 5: Filtering Data

Use the same DataFrame."""

"""36. Display all employees whose age is greater than 30."""

print("====== Solution 36 ======")

result  = df[df["Age"] > 30]
print(result)

"""37. Display all employees whose age is less than 30."""

print("====== Solution 37 ======")

result = df[df["Age"] < 30]
print(result)

"""38. Display all employees whose salary is greater than 50,000."""

print("====== Solution 38 ======")

employees = df[df["Salary"] > 50000]
print(employees)

"""39. Display all employees who live in Delhi."""

print("====== Solution 39 ======")

in_delhi = df[df["City"] == "Delhi"]
print(in_delhi)

"""40. Display all employees who live in Mumbai."""

print("====== Solution 40 ======")

in_mumbai = df[df["City"] == "Mumbai"]
print(in_mumbai)

"""41. Display employees whose salary is greater than 50,000 and whose age is greater than 30."""

print("====== Solution 41 ======")

employees = df[(df["Salary"] > 50000) & (df["Age"] > 30)]
print(employees)

"""42. Display employees who belong to Delhi or Mumbai."""

print("====== Solution 42 ======")

delhi_mumbai = df[(df["City"] == "Delhi") | (df["City"] == "Mumbai")]
print(delhi_mumbai)

"""43. Display employees whose age is between 25 and 35."""

print("====== Solution 43 ======")

result = df[(df["Age"] >= 25) & (df["Age"] <= 35)]
print(result)

"""44. Display employees whose salary is less than 50,000."""

print("====== Solution 44 ======")

result = df[df["Salary"] < 50000 ]
print(result)

"""45. Display the names and salaries of employees earning more than 50,000."""

print("====== Solution 45 ======")

result = df.loc[df["Salary"] > 50000, ["Name", "Salary"]]

print(result)

"""Part 6: Sorting Data

Use the same DataFrame."""

"""46. Sort the DataFrame by Age in ascending order."""

print("====== Solution 46 ======")

sorted_data = df.sort_values("Age")
print(sorted_data)

"""47. Sort the DataFrame by Age in descending order."""

print("====== Solution 47 ======")

sorted_data = df.sort_values("Age",ascending= False)
print(sorted_data)

"""48. Sort the DataFrame by Salary from lowest to highest."""

print("====== Solution 48 ======")

sorted_salary = df.sort_values("Salary")
print(sorted_salary)

"""49. Sort the DataFrame by Salary from highest to lowest."""

print("====== Solution 49 ======")

sorted_salary = df.sort_values("Salary" , ascending=False)
print(sorted_salary)

"""50. Sort the DataFrame first by City and then by Salary."""

print("====== Solution 50 ======")

sorted_salary = df.sort_values(["City","Salary"] , ascending=[True,True])
print(sorted_salary)

"""Part 7: Unique Values and Frequency

Use the same DataFrame."""

"""51. Find all unique cities in the DataFrame."""

print("====== Solution 51 ======")

unique_cities = df["City"].unique()
print(unique_cities)

"""52. Find the number of unique cities."""

print("====== Solution 52 ======")

unique_cities = df["City"].nunique()
print(unique_cities)

"""53. Count how many employees belong to each city."""

print("====== Solution 53 ======")

employees_count = df["City"].value_counts()
print(employees_count)

"""54. Find the city with the highest number of employees."""

print("====== Solution 54 ======")

highest_employees = df["City"].value_counts().head(1)
print(highest_employees)

"""55. Count how many employees have each age."""

print("====== Solution 55 ======")

emp_counts = df["Age"].value_counts()
print(emp_counts)

"""Part 8: Grouping Data

Use the same DataFrame."""

"""56. Find the average salary for each city."""

print("====== Solution 56 ======")

average_salary = df.groupby("City")["Salary"].mean()
print(average_salary)

"""57. Find the total salary for each city."""

print("====== Solution 57 ======")

total_salary = df.groupby("City")["Salary"].sum()
print(total_salary)

"""58. Find the maximum salary for each city."""

print("====== Solution 58 ======")

maximum_salary = df.groupby("City")["Salary"].max()
print(maximum_salary)

"""59. Find the minimum age for each city."""

print("====== Solution 59 ======")

minimum_age = df.groupby("City")["Age"].min()
print(minimum_age)

"""60. Create a summary showing, for each city:

Average salary
Maximum salary
Minimum salary
Number of employees"""

print("====== Solution 60 ======")

summary = df.groupby("City")["Salary"].agg(
    Average_Salary="mean",
    Maximum_Salary="max",
    Minimum_Salary="min",
    Number_of_Employees="count"
)

print(summary)