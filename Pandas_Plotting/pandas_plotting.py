# ============================================================
# MATPLOTLIB LABELLING + PANDAS PLOTTING
# 40 PRACTICE QUESTIONS
# ============================================================


import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# LEVEL 1 — MATPLOTLIB LABELLING
# ============================================================


# 1. Create two lists:
#    months = ["Jan", "Feb", "Mar", "Apr", "May"]
#    sales = [100, 150, 120, 180, 220]
#
#    Create a line plot of sales.
#    Add the title "Monthly Sales".
#    Add "Month" as the X-axis label.
#    Add "Sales" as the Y-axis label.

print("=====  Solution 1  =====")

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 120, 180, 220]

plt.figure(figsize=(10,5))

plt.plot(months,sales,marker="o",color="red")

plt.title("Sales by Month")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()

# 2. Using the same sales data, add a grid to the chart.

print("=====  Solution 2  =====")

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 120, 180, 220]

plt.figure(figsize=(10,5))

plt.plot(months,sales,marker="o",color="red")

plt.title("Sales by Month")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()

plt.show()

# 3. Create a line plot using:
#    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
#    visitors = [120, 150, 100, 180, 200]
#
#    Add:
#    Title: "Daily Website Visitors"
#    X-axis label: "Day"
#    Y-axis label: "Visitors"

print("=====  Solution 3  =====")

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
visitors = [120, 150, 100, 180, 200]

plt.figure(figsize=(10,5))

plt.plot(days,visitors,marker="o")

plt.title("Daily Website Visitors")
plt.xlabel("Day")
plt.ylabel("Visitors")
plt.grid()

plt.show()

# 4. Create a bar chart using:
#    products = ["Laptop", "Phone", "Tablet", "Watch"]
#    sales = [50, 120, 80, 40]
#
#    Add a title and appropriate X-axis and Y-axis labels.

print("=====  Solution 4  =====")

products = ["Laptop", "Phone", "Tablet", "Watch"]
sales = [50, 120, 80, 40]

plt.figure(figsize=(10,5))

plt.bar(products,sales)

plt.title("Sales by Products")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.show()

# 5. Create a line plot using:
#    months = ["Jan", "Feb", "Mar", "Apr", "May"]
#    profit = [20, 30, 25, 40, 50]
#
#    Set the title font size to 20.
#    Set the X-axis and Y-axis label font size to 14.

print("=====  Solution 5  =====")

months = ["Jan", "Feb", "Mar", "Apr", "May"]
profit = [20, 30, 25, 40, 50]

plt.figure(figsize=(10,5))

plt.plot(months,profit,marker="o")

plt.title("Monthly Profit",fontsize=20)
plt.xlabel("Months",fontsize=14)
plt.ylabel("Profit",fontsize=14)

plt.show()


# 6. Create a bar chart using:
#    departments = ["HR", "IT", "Sales", "Finance"]
#    employees = [20, 45, 60, 30]
#
#    Set the title to "Employees by Department".
#    Place the title on the left side of the chart.

print("=====  Solution 6  =====")

departments = ["HR", "IT", "Sales", "Finance"]
employees = [20, 45, 60, 30]

plt.figure(figsize=(10,5))

plt.bar(departments,employees)

plt.title("Employees by Department",loc="left")
plt.xlabel("Departments")
plt.ylabel("Employees")

plt.show()


# 7. Create a bar chart using:
#    cities = ["Delhi", "Mumbai", "Pune", "Chennai", "Kolkata"]
#    orders = [450, 380, 320, 290, 250]
#
#    Add a title, X-axis label, Y-axis label and grid.

print("=====  Solution 7  =====")

cities = ["Delhi", "Mumbai", "Pune", "Chennai", "Kolkata"]
orders = [450, 380, 320, 290, 250]


plt.figure(figsize=(10,5))

plt.bar(cities,orders)

plt.title("Orders by Cities")
plt.xlabel("Cities")
plt.ylabel("Orders")
plt.grid()

plt.show()


# 8. Create a line chart using:
#    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
#    revenue = [10000, 12000, 11000, 15000, 17000, 19000]
#
#    Add:
#    Title: "Monthly Revenue"
#    X-axis: "Month"
#    Y-axis: "Revenue"
#
#    Rotate the X-axis labels by 45 degrees.

print("=====  Solution 8  =====")

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [10000, 12000, 11000, 15000, 17000, 19000]

plt.figure(figsize=(10,5))

plt.plot(months,revenue)

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.show()

# 9. Create a bar chart using:
#    categories = ["Electronics", "Clothing", "Groceries", "Furniture"]
#    sales = [50000, 35000, 42000, 28000]
#
#    Add a title and axis labels.
#    Rotate the X-axis labels by 45 degrees.

print("=====  Solution 9  =====")

categories = ["Electronics", "Clothing", "Groceries", "Furniture"]
sales = [50000, 35000, 42000, 28000]

plt.figure(figsize=(10,5))

plt.bar(categories,sales)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=45)

plt.show()


# 10. Create a line chart using:
#     months = ["Jan", "Feb", "Mar", "Apr", "May"]
#     sales = [100, 150, 130, 180, 220]
#
#     Add an annotation pointing to the highest sales value.
#     The annotation should say "Highest Sales".

print("=====  Solution 10  =====")

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 130, 180, 220]

plt.figure(figsize=(10,5))

plt.plot(months,sales)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.annotate("Highest Sales",xy=("May",220))

plt.show()

# ============================================================
# LEVEL 2 — LEGENDS AND MULTIPLE DATA SERIES
# ============================================================


# 11. Create two lines using:
#     months = ["Jan", "Feb", "Mar", "Apr", "May"]
#     sales_2025 = [100, 120, 150, 140, 180]
#     sales_2026 = [110, 140, 160, 170, 210]
#
#     Give the two lines labels "2025" and "2026".
#     Display the legend.
#     Add a suitable title and axis labels.

print("=====  Solution 11  =====")

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales_2025 = [100, 120, 150, 140, 180]
sales_2026 = [110, 140, 160, 170, 210]

plt.figure(figsize=(10,5))

plt.plot(months,sales_2025,label="2025",marker="o")
plt.plot(months,sales_2026,label="2026",marker="s")

plt.legend(loc='upper left')

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()


# 12. Using the data from Question 11, move the legend to the upper right.

print("=====  Solution 12  =====")

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales_2025 = [100, 120, 150, 140, 180]
sales_2026 = [110, 140, 160, 170, 210]

plt.figure(figsize=(10,5))

plt.plot(months,sales_2025,label="2025",marker="o")
plt.plot(months,sales_2026,label="2026",marker="s")

plt.legend(loc='upper right')

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()


# 13. Create three lines:
#
    # months = ["Jan", "Feb", "Mar", "Apr"]
    # product_a = [100, 120, 140, 160]
    # product_b = [80, 110, 130, 150]
    # product_c = [60, 90, 120, 140]
#
#     Give each line an appropriate label.
#     Display a legend.
#     Add title and axis labels.

print("=====  Solution 13  =====")

months = ["Jan", "Feb", "Mar", "Apr"]
product_a = [100, 120, 140, 160]
product_b = [80, 110, 130, 150]
product_c = [60, 90, 120, 140]

plt.figure(figsize=(10,5))

plt.plot(months,product_a,label="Product A",marker="o")
plt.plot(months,product_b,label="Product B",marker="s")
plt.plot(months,product_c,label="Product C",marker="*")

plt.legend()

plt.title("Monthly Product Sold")
plt.xlabel("Month")
plt.ylabel("Product Sold")

plt.show()

# 14. Create a chart using:
#     months = ["Jan", "Feb", "Mar", "Apr", "May"]
#     revenue = [100, 120, 150, 170, 200]
#     expenses = [70, 80, 100, 110, 130]
#
#     Plot both lines.
#     Add a legend.
#     Add a grid.
#     Add appropriate title and axis labels.

print("=====  Solution 14  =====")

months = ["Jan", "Feb", "Mar", "Apr", "May"]
revenue = [100, 120, 150, 170, 200]
expenses = [70, 80, 100, 110, 130]


plt.figure(figsize=(10,5))

plt.plot(months,revenue,label="Revenue",marker="o")
plt.plot(months,expenses,label="Expenses",marker="s")

plt.legend()

plt.title("Monthly Revenue vs Monthly Expenses")
plt.xlabel("Months")
plt.ylabel("Revenue & Expense")
plt.grid()

plt.show()


# 15. Create a chart using:
#     months = ["Jan", "Feb", "Mar", "Apr", "May"]
#     orders = [100, 130, 160, 150, 200]
#     returns = [5, 8, 10, 7, 12]
#
#     Plot both lines.
#     Label them "Orders" and "Returns".
#     Display the legend.
#     Add title and axis labels.

print("=====  Solution 15  =====")

months = ["Jan", "Feb", "Mar", "Apr", "May"]
orders = [100, 130, 160, 150, 200]
returns = [5, 8, 10, 7, 12]

plt.figure(figsize=(10,5))

plt.plot(months,orders,label="Orders",marker="o")
plt.plot(months,returns,label="Returns",marker="s")

plt.legend()

plt.title("Monthly Order bs Monthly Returns")
plt.xlabel("Months")
plt.ylabel("Orders & Returns")

plt.show()

# ============================================================
# LEVEL 3 — PANDAS PLOTTING BASICS
# ============================================================


# 16. Create the following DataFrame:
#
#     Month    Sales
#     Jan      100
#     Feb      150
#     Mar      120
#     Apr      180
#     May      220
#
#     Use Pandas plotting to create a line chart.
#     Use Month on the X-axis and Sales on the Y-axis.

print("=====  Solution 16  =====")

data = {"Month":["Jan","Feb","Mar","Apr","May"],"Sales":[100,150,120,180,220]}

df = pd.DataFrame(data)

plt.figure(figsize=(10,5))

df.plot(x="Month",y="Sales",kind="line",marker="o")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()


# 17. Using the DataFrame from Question 16,
#     create a bar chart instead of a line chart.

print("=====  Solution 17  =====")

data = {"Month":["Jan","Feb","Mar","Apr","May"],"Sales":[100,150,120,180,220]}

df = pd.DataFrame(data)


df.plot(x="Month",y="Sales",kind="bar",figsize=(10,5))

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()

# 18. Using the DataFrame from Question 16,
#     create a horizontal bar chart.

print("=====  Solution 18  =====")

data = {"Month":["Jan","Feb","Mar","Apr","May"],"Sales":[100,150,120,180,220]}

df = pd.DataFrame(data)


df.plot(x="Month",y="Sales",kind="barh",figsize=(10,5))

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()

# 19. Create this DataFrame:
#
#     Product       Quantity
#     Laptop        25
#     Phone         60
#     Tablet        40
#     Headphones    80
#
#     Create a Pandas bar chart showing product quantity.

print("=====  Solution 19  =====")

data = {
    "Product":["Laptop","Phone","Tablet","Headphones"],
    "Quantity" : [25,60,40,80]
}

df=pd.DataFrame(data)

df.plot(x="Product",y="Quantity",kind="bar",figsize=(10,5))

plt.title("Quantity by Products")
plt.xlabel("Product")
plt.ylabel("Quantity")

plt.show()

# 20. Create this DataFrame:
#
#     Department    Employees
#     HR            25
#     IT            50
#     Sales         75
#     Finance       35
#
#     Create a horizontal bar chart using Pandas.

print("=====  Solution 20  =====")

data = {
    "Department":["HR","IT","Sales","Finance"],
    "Quantity" : [25,50,75,35]
}

df=pd.DataFrame(data)

df.plot(x="Department",y="Quantity",kind="barh",figsize=(10,5))

plt.title("Quantity by Department")
plt.xlabel("Department")
plt.ylabel("Quantity")

plt.show()


# ============================================================
# LEVEL 4 — PANDAS PLOTTING + LABELLING
# ============================================================


# 21. Create a DataFrame:
#
#     Month    Revenue
#     Jan      10000
#     Feb      12000
#     Mar      15000
#     Apr      14000
#     May      18000
#
#     Create a Pandas line plot.
#     Add:
#     Title: "Monthly Revenue"
#     X-axis label: "Month"
#     Y-axis label: "Revenue"
#     Grid

print("=====  Solution 21  =====")

data = {
    "Month":["Jan","Feb","Mar","Apr","May"],
    "Revenue" : [10000,12000,15000,14000,18000]
}

df = pd.DataFrame(data)
print(df)

df.plot(x="Month",y="Revenue",kind="line",marker="o")

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid()

plt.show()

# 22. Create a DataFrame:
#
#     City       Sales
#     Delhi      50000
#     Mumbai     45000
#     Pune       35000
#     Chennai    35000
#
#     Create a Pandas bar chart.
#     Add a suitable title and axis labels.
#     Rotate the X-axis labels by 45 degrees.

print("=====  Solution 22  =====")

data = {
    "City":["Delhi","Mumbai","Pune","Chennai"],
    "Sales":[50000,45000,35000,35000]
}

df= pd.DataFrame(data)
print(df)

df.plot(x="City",y="Sales",kind="bar",figsize=(10,5))

plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Sales")
plt.xticks(rotation=45)

plt.show()


# 23. Create a DataFrame:
#
#     Month    Sales    Profit
#     Jan      10000    2000
#     Feb      12000    2500
#     Mar      15000    3000
#     Apr      14000    2800
#     May      18000    4000
#
#     Plot Sales and Profit on the same line chart.
#     Use Month as the X-axis.
#     Add a legend.
#     Add title, axis labels and grid.

print("=====  Solution 23  =====")

data = {
    "Month" : ["Jan","Feb","Mar","Apr","May"],
    "Sales" : [10000,12000,15000,14000,18000],
    "Profit" :[2000,2500,3000,2800,4000]
}

df = pd.DataFrame(data)

df.plot(x="Month",y=["Sales","Profit"],kind="line",label=["Sales","Profit"],marker="o",figsize=(10,5))

plt.legend()

plt.title("Montly Sales vs Monthly Profit")
plt.xlabel("Month")
plt.ylabel("Sales & Profit")
plt.grid()

plt.show()


# 24. Using the DataFrame from Question 23,
#     create a bar chart comparing Sales and Profit.

print("=====  Solution 24  =====")

data = {
    "Month" : ["Jan","Feb","Mar","Apr","May"],
    "Sales" : [10000,12000,15000,14000,18000],
    "Profit" :[2000,2500,3000,2800,4000]
}

df = pd.DataFrame(data)

df.plot(x="Month",y=["Sales","Profit"],kind="bar",label=["Sales","Profit"],figsize=(10,5))

plt.legend()

plt.title("Montly Sales vs Monthly Profit")
plt.xlabel("Month")
plt.ylabel("Sales & Profit")
plt.grid()

plt.show()


# 25. Create a DataFrame:
#
#     Month       Customers
#     Jan         100
#     Feb         120
#     Mar         150
#     Apr         180
#     May         210
#
#     Create a line plot.
#     Set the figure size to 10 x 5.
#     Add title and axis labels.

print("=====  Solution 25  =====")

data = {
    "Month" : ["Jan","Feb","Mar","Apr","May"],
    "Customers" : [100,120,150,180,210],
}

df = pd.DataFrame(data)

df.plot(x="Month",y="Customers",kind="line",figsize=(10,5))

plt.title("Monthly Customers")
plt.xlabel("Month")
plt.ylabel("Customers")

plt.show()


# 26. Create a DataFrame:
#
#     Category       Sales
#     Electronics    50000
#     Clothing       30000
#     Groceries      40000
#     Furniture      25000
#
#     Create a Pandas bar chart.
#     Add a suitable title.
#     Add X-axis and Y-axis labels.
#     Add a grid.

print("=====  Solution 26  =====")

data = {
    "Category" : ["Electronics","Clothing","Groceries","Furniture"],
    "Sales" : [50000,30000,40000,25000],
}

df = pd.DataFrame(data)

df.plot(x="Category",y="Sales",kind="bar",figsize=(10,5))

plt.title("Category vs Sales")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid()

plt.show()


# 27. Create a DataFrame:
#
#     Month       Sales
#     January     10000
#     February    12000
#     March       15000
#     April       14000
#     May         18000
#     June        20000
#
#     Create a bar chart.
#     Rotate the X-axis labels by 45 degrees.
#     Add a title and appropriate axis labels.

print("=====  Solution 27  =====")

data = {
    "Month" : ["January","February","March","April","May","June"],
    "Sales" : [10000,12000,15000,14000,18000,20000],
}

df = pd.DataFrame(data)

df.plot(x="Month",y="Sales",kind="bar",figsize=(10,5))

plt.title("Monthly Saless")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)

plt.show()


# ============================================================
# LEVEL 5 — HISTOGRAMS, BOX PLOTS AND DISTRIBUTION
# ============================================================


# 28. Create a DataFrame containing:
#
#     Customer_Age = [18, 21, 25, 25, 28, 30, 32, 35,
#                     36, 40, 42, 45, 50, 55, 60]
#
#     Create a histogram using Pandas.
#     Add an appropriate title.
#     Label the X-axis "Age".
#     Label the Y-axis "Number of Customers".

print("=====  Solution 28  =====")

Customer_Age = [18, 21, 25, 25, 28, 30, 32, 35,
                    36, 40, 42, 45, 50, 55, 60]


data = {"age":Customer_Age}

df = pd.DataFrame(data)

df["age"].plot(kind="hist")

plt.show()

# 29. Create a DataFrame containing:
#
#     Salary = [25000, 30000, 35000, 40000, 42000,
#               45000, 50000, 55000, 60000, 70000,
#               80000, 100000]
#
#     Create a histogram.
#     Add a suitable title and axis labels.

print("=====  Solution 29  =====")

Salary = [25000, 30000, 35000, 40000, 42000,
              45000, 50000, 55000, 60000, 70000,
              80000, 100000]

data = {"Salary":Salary}

df = pd.DataFrame(data)

df["Salary"].plot(kind="hist")

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.show()

# 30. Create a DataFrame containing:
#
#     Sales = [100, 120, 150, 130, 180, 200,
#              220, 190, 250, 300, 500]
#
#     Create a box plot using Pandas.
#     Add a suitable title and Y-axis label.

print("=====  Solution 30  =====")

Sales = [100, 120, 150, 130, 180, 200,
             220, 190, 250, 300, 500]

data = {"Sales":Sales}

df = pd.DataFrame(data)

df["Sales"].plot(kind="box")

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Salary")

plt.show()


# ============================================================
# LEVEL 6 — SCATTER PLOTS
# ============================================================


# 31. Create this DataFrame:
#
#     Advertising    Sales
#     10             100
#     20             120
#     30             150
#     40             180
#     50             220
#     60             250
#
#     Create a scatter plot using Pandas.
#     Put Advertising on the X-axis.
#     Put Sales on the Y-axis.
#     Add title and axis labels.

print("=====  Solution 31  =====")

data = { 
    "Advertising" : [10,20,30,40,50,60],
    "Sales" : [100,120,150,180,220,250]
}

df = pd.DataFrame(data)

df.plot(x="Advertising",y="Sales",kind="scatter")

plt.title("Advertising vs Salary")
plt.xlabel("Advertising")
plt.ylabel("Salary")

plt.show()

# 32. Create this DataFrame:
#
#     Study_Hours    Exam_Score
#     1              45
#     2              50
#     3              55
#     4              65
#     5              70
#     6              78
#     7              85
#     8              90
#
#     Create a scatter plot.
#     Add:
#     Title: "Study Hours vs Exam Score"
#     X-axis: "Study Hours"
#     Y-axis: "Exam Score"

print("=====  Solution 32  =====")

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Exam_Score": [45, 50, 55, 65, 70, 78, 85, 90]
}

df = pd.DataFrame(data)


df.plot(x="Study_Hours",y="Exam_Score",kind="scatter",figsize=(10,5))

plt.title("Study_Hours vs Exam_Score")
plt.xlabel("Study_Hours")
plt.ylabel("Exam_Score")

plt.show()

# 33. Create this DataFrame:
#
#     Experience    Salary
#     1             30000
#     2             35000
#     3             40000
#     4             48000
#     5             55000
#     7             70000
#     10            90000
#
#     Create a scatter plot.
#     Add title, axis labels and grid.

print("=====  Solution 33  =====")

data = {
    "Experience": [1, 2, 3, 4, 5, 7, 10],
    "Salary": [30000, 35000, 40000, 48000, 55000, 70000, 90000]
}

df = pd.DataFrame(data)

df.plot(x="Experience",y="Salary",kind="scatter",figsize=(10,5))

plt.title("Experience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.grid()

plt.show()


# ============================================================
# LEVEL 7 — REAL DATA ANALYST STYLE QUESTIONS
# ============================================================


# 34. Create this DataFrame:
#
#     Month    Sales    Profit    Expenses
#     Jan      10000    2000      8000
#     Feb      12000    2500      9500
#     Mar      11000    2200      8800
#     Apr      15000    3500      11500
#     May      18000    4500      13500
#     Jun      20000    5200      14800
#
#     Create a line chart showing Sales, Profit and Expenses.
#     Use Month on the X-axis.
#     Add a legend.
#     Add a title, axis labels and grid.

print("=====  Solution 34  =====")

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [10000, 12000, 11000, 15000, 18000, 20000],
    "Profit": [2000, 2500, 2200, 3500, 4500, 5200],
    "Expenses": [8000, 9500, 8800, 11500, 13500, 14800]
}

df = pd.DataFrame(data)

df.plot(x="Month",y=["Sales","Profit","Expenses"],kind="line",label=["Sales","Profit","Expenses"],marker="o")

plt.legend()

plt.title("Monthly Sales/Profit/Expenses")
plt.xlabel("Month")
plt.ylabel("Sales/Profit/Expenses")
plt.grid()

plt.show()


# 35. Using the DataFrame from Question 34,
#     create a bar chart showing only Sales for each month.
#     Add a suitable title and axis labels.

print("=====  Solution 35  =====")

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [10000, 12000, 11000, 15000, 18000, 20000],
    "Profit": [2000, 2500, 2200, 3500, 4500, 5200],
    "Expenses": [8000, 9500, 8800, 11500, 13500, 14800]
}

df = pd.DataFrame(data)

df.plot(x="Month",y=["Sales","Profit","Expenses"],kind="bar",label=["Sales","Profit","Expenses"])

plt.legend()

plt.title("Sales/Profit/Expenses by Month")
plt.xlabel("Month")
plt.ylabel("Sales/Profit/Expenses")
plt.grid()

plt.show()


# 36. Create this DataFrame:
#
#     Region    Orders    Revenue
#     North     500       100000
#     South     450       85000
#     East      600       120000
#     West      550       110000
#
#     Create a bar chart comparing Orders by Region.
#     Add title, X-axis label and Y-axis label.
#     Rotate the X-axis labels by 45 degrees.

print("=====  Solution 36  =====")

data = {
    "Region": ["North", "South", "East", "West"],
    "Orders": [500, 450, 600, 550],
    "Revenue": [100000, 85000, 120000, 110000]
}

df = pd.DataFrame(data)

df.plot(x="Region",y="Orders",kind="bar")

plt.title("Orders by Region")
plt.xlabel("Region")
plt.ylabel("Orders")
plt.xticks(rotation=45)

plt.show()

# 37. Using the DataFrame from Question 36,
#     create a separate bar chart showing Revenue by Region.
#     Add title and appropriate axis labels.

print("=====  Solution 37  =====")

data = {
    "Region": ["North", "South", "East", "West"],
    "Orders": [500, 450, 600, 550],
    "Revenue": [100000, 85000, 120000, 110000]
}

df = pd.DataFrame(data)

df.plot(x="Region",y="Revenue",kind="bar")

plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.show()

# 38. Create this DataFrame:
#
#     Month    Website_Visitors    Orders
#     Jan      10000               500
#     Feb      12000               600
#     Mar      15000               750
#     Apr      14000               700
#     May      18000               950
#     Jun      20000               1100
#
#     Create a line chart showing Website Visitors and Orders.
#     Use Month as the X-axis.
#     Add a legend.
#     Add title, axis labels and grid.

print("=====  Solution 38  =====")

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Website_Visitors": [10000, 12000, 15000, 14000, 18000, 20000],
    "Orders": [500, 600, 750, 700, 950, 1100]
}

df = pd.DataFrame(data)

df.plot(x="Month",y=["Website_Visitors","Orders"],kind="line",label=["Website_Visitors","Orders"],marker="o")

plt.legend()

plt.title("Monthly Website_Visitors & Monthly Orders")
plt.xlabel("Month")
plt.ylabel("Website_Visitors & Orders")
plt.grid()

plt.show()

# 39. Create this DataFrame:
#
#     Product       Sales
#     Laptop        120000
#     Mobile        90000
#     Tablet        60000
#     Headphones    40000
#     Smartwatch    50000
#
#     Create a Pandas bar chart.
#
#     Add:
#     - A suitable title
#     - X-axis label
#     - Y-axis label
#     - Grid
#     - Rotated X-axis labels
#
#     Then identify the product with the highest sales and
#     annotate that bar on the chart.

print("=====  Solution 39  =====")

data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Headphones", "Smartwatch"],
    "Sales": [120000, 90000, 60000, 40000, 50000]
}

df = pd.DataFrame(data)

df.plot(x="Product",y="Sales",kind="bar")

plt.title("Sales by Products")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.grid()
plt.xticks(rotation=45)

plt.show()

# 40. Create this DataFrame:
#
#     Month    Sales_2025    Sales_2026
#     Jan      10000         12000
#     Feb      12000         13500
#     Mar      11000         14000
#     Apr      15000         16500
#     May      18000         20000
#     Jun      17000         22000
#
#     Create a line chart comparing Sales in 2025 and 2026.
#
#     Your chart must contain:
#     - Both lines
#     - A legend
#     - A title
#     - X-axis label
#     - Y-axis label
#     - Grid
#     - Figure size of 10 x 5
#     - X-axis labels rotated by 45 degrees
#
#     Finally, annotate the highest Sales_2026 value.

print("=====  Solution 40  =====")

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales_2025": [10000, 12000, 11000, 15000, 18000, 17000],
    "Sales_2026": [12000, 13500, 14000, 16500, 20000, 22000]
}

df = pd.DataFrame(data)

df.plot(x="Month",y=["Sales_2025","Sales_2026"],kind="line",label=["Sales_2025","Sales_2026"],marker="o",figsize=(10,5))

plt.legend()

plt.title("Monthly Sales of 2025 & 2026")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()
plt.xticks(rotation=45)

plt.show()