# ============================================================
# MATPLOTLIB INTRO — 40 PRACTICE QUESTIONS
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# LEVEL 1 — BASIC LINE CHARTS
# ============================================================

# Question 1
# Create a line chart using the following data.
# X-axis: months
# Y-axis: sales

print("=====  Solution 1  =====")

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 120, 180, 220]

plt.plot(months,sales)

plt.show()

# # # Question 2
# # # Create a line chart using the following data.
# # # Add a title: "Monthly Revenue"
# # # Label the X-axis as "Month"
# # # Label the Y-axis as "Revenue"

print("=====  Solution 2  =====")

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [20000, 25000, 22000, 30000, 35000, 40000]

plt.plot(months,revenue)

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.show()

# # # Question 3
# # # Create a line chart for the following website visitors data.
# # # Add a suitable title and labels for both axes.

print("=====  Solution 3  =====")

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
visitors = [120, 150, 180, 160, 220, 300, 280]


plt.plot(days , visitors)

plt.title("Weekly Visitors Frequency")
plt.xlabel("Days")
plt.ylabel("Visitors")

plt.show()

# # # Question 4
# # # Create a line chart for the following temperature data.
# # # Display gridlines on the chart.

print("=====  Solution 4  =====")

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
temperature = [28, 30, 32, 31, 29]

plt.plot(days,temperature)

plt.title("Daily Temperature Data")
plt.xlabel("Days")
plt.ylabel("Temperatue")

plt.show()

# # # Question 5
# # # Create a line chart for the following monthly expenses.
# # # Add:
# # # - Title
# # # - X-axis label
# # # - Y-axis label
# # # - Gridlines

print("=====  Solution 5  =====")

months = ["Jan", "Feb", "Mar", "Apr", "May"]
expenses = [15000, 18000, 16000, 20000, 17000]

plt.plot(months,expenses)

plt.title("Monthly Expenses")
plt.xlabel("Month")
plt.ylabel("Expenses")
plt.grid()

plt.show()

# # # ============================================================
# # # LEVEL 2 — LINE CHART CUSTOMIZATION
# # # ============================================================

# # # Question 6
# # # Create a line chart for the following sales data.
# # # Make the line red.

print("=====  Solution 6  =====")

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 140, 120, 180]

plt.plot(months,sales,color="red")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()

plt.show()

# # # Question 7
# # # Create a line chart for the following data.
# # # Add circular markers to every data point.

print("=====  Solution 7  =====")

months = ["Jan", "Feb", "Mar", "Apr", "May"]
orders = [50, 75, 60, 90, 120]

plt.plot(months,orders,color="red",marker="o")

plt.title("Monthly Orders")
plt.xlabel("Months")
plt.ylabel("Orders")
plt.grid()

plt.show()

# # # Question 8
# # # Create a line chart for the following data.
# # # Make the line thicker using an appropriate linewidth.

print("=====  Solution 8  =====")

months = ["Jan", "Feb", "Mar", "Apr", "May"]
profit = [10000, 12000, 9000, 15000, 18000]

plt.plot(months,profit,color="red",marker="o",linewidth=4)

plt.title("Monthly Profit")
plt.xlabel("Months")
plt.ylabel("Profit")
plt.grid()

plt.show()

# # # Question 9
# # # Create a line chart for the following data.
# # # Use a dashed line and circular markers.

print("=====  Solution 9  =====")

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 130, 110, 160, 200]

plt.plot(months,sales,color="red",marker="o",linewidth=4,linestyle="--")

plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid()

plt.show()

# # # Question 10
# # # Create a line chart for the following data.
# # # Customize the chart using:
# # # - A title
# # # - Axis labels
# # # - Circular markers
# # # - A thicker line
# # # - Gridlines

print("=====  Solution 10  =====")

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
customers = [200, 250, 230, 300, 350, 400]

plt.plot(months,customers,marker="o",linewidth = 5)

plt.title("Monthly Customers")
plt.xlabel("Months")
plt.ylabel("Customers")
plt.grid()

plt.show()

# # ============================================================
# # LEVEL 3 — BAR CHARTS
# # ============================================================

# # Question 11
# # Create a bar chart showing sales for each product.

print("=====  Solution 11  =====")

products = ["Laptop", "Phone", "Tablet", "Monitor"]
sales = [500, 800, 300, 450]

plt.bar(products,sales)

plt.show()

# # Question 12
# # Create a bar chart using the following data.
# # Add a suitable title and axis labels.

print("=====  Solution 12  =====")

cities = ["Delhi", "Mumbai", "Pune", "Chennai"]
customers = [500, 700, 450, 600]

plt.bar(cities,customers)

plt.title("Customers by City")
plt.xlabel("City")
plt.ylabel("Customers")

plt.show()


# # Question 13
# # Create a bar chart showing the number of employees
# # in each department.

print("=====  Solution 13  =====")

departments = ["HR", "IT", "Sales", "Finance", "Marketing"]
employees = [20, 50, 40, 25, 30]

plt.bar(departments,employees)

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")

plt.show()


# # Question 14
# # Create a bar chart for the following product quantities.
# # Add gridlines to the chart.

print("=====  Solution 14  =====")

products = ["Pen", "Notebook", "Bag", "Bottle", "Pencil"]
quantity = [120, 200, 80, 150, 250]

plt.bar(products,quantity)

plt.title("Total Quantity by Products")
plt.xlabel("Products")
plt.ylabel("Total Quantity")
plt.grid()

plt.show()

# # Question 15
# # Create a bar chart showing revenue generated by each category.
# # Add:
# # - Title
# # - X-axis label
# # - Y-axis label
# # - Gridlines

print("=====  Solution 15  =====")

categories = ["Electronics", "Clothing", "Books", "Furniture"]
revenue = [50000, 35000, 20000, 40000]

plt.bar(categories,revenue)
plt.title("Revenue by Category")
plt.xlabel("Categories")
plt.ylabel("Revenue")
plt.grid()

plt.show()

# # ============================================================
# # LEVEL 4 — SCATTER PLOTS
# # ============================================================

# # Question 16
# # Create a scatter plot showing the relationship between
# # age and salary.

print("=====  Solution 16  =====")

age = [22, 25, 28, 30, 32, 35, 40]
salary = [25000, 28000, 32000, 35000, 40000, 48000, 60000]

plt.scatter(age,salary)

plt.show()


# # Question 17
# # Create a scatter plot showing the relationship between
# # hours studied and exam scores.

print("=====  Solution 17  =====")

hours_studied = [1, 2, 3, 4, 5, 6, 7]
exam_scores = [45, 50, 55, 65, 70, 80, 90]

plt.scatter(hours_studied,exam_scores)

plt.title("Hours Studies Vs Score")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Scores")

plt.show()

# # Question 18
# # Create a scatter plot showing the relationship between
# # advertising spend and sales.

print("=====  Solution 18  =====")

advertising = [10, 20, 30, 40, 50, 60]
sales = [100, 150, 180, 220, 260, 300]

plt.scatter(advertising,sales)

plt.title("Advertising Spend Vs Sales")
plt.xlabel("Advertising Spend")
plt.ylabel("Sales")

plt.show()


# # Question 19
# # Create a scatter plot for the following data.
# # Add a title and labels for both axes.

print("=====  Solution 19  =====")

experience = [1, 2, 3, 4, 5, 6, 7]
salary = [25000, 28000, 32000, 37000, 42000, 50000, 60000]

plt.scatter(experience,salary)

plt.title("Experience Vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")

plt.show()

# # Question 20
# # Create a scatter plot showing the relationship between
# # number of hours worked and productivity score.
# # Add:
# # - Title
# # - X-axis label
# # - Y-axis label
# # - Gridlines

print("=====  Solution 20  =====")

hours_worked = [4, 5, 6, 7, 8, 9, 10]
productivity = [50, 55, 60, 68, 72, 80, 85]

plt.scatter(hours_worked,productivity)

plt.title("Hours Worked Vs Productivity")
plt.xlabel("Hours Worked")
plt.ylabel("Productivity")
plt.grid()

plt.show()


# # ============================================================
# # LEVEL 5 — HISTOGRAMS
# # ============================================================

# # Question 21
# # Create a histogram showing the distribution of ages.

print("=====  Solution 21  =====")

ages = [18, 20, 21, 22, 22, 23, 25, 25, 26, 27,
        28, 29, 30, 30, 31, 32, 34, 35, 36, 40]

plt.hist(ages,bins=5)

plt.show()


# # Question 22
# # Create a histogram showing the distribution of salaries.

print("=====  Solution 22  =====")

salaries = [
    25000, 28000, 30000, 32000, 35000,
    35000, 37000, 40000, 42000, 45000,
    45000, 48000, 50000, 55000, 60000
]

plt.hist(salaries,bins=5)

plt.title("Distribution of Salaries")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.show()

# # Question 23
# # Create a histogram showing the distribution of exam scores.
# # Add a suitable title and axis labels.

print("=====  Solution 23  =====")

scores = [
    45, 50, 52, 55, 60, 62, 65, 67,
    70, 72, 75, 78, 80, 82, 85, 90, 92, 95
]

plt.hist(scores)

plt.title("Distribution of Scores")
plt.xlabel("Scores")
plt.ylabel("Frequency")

plt.show()

# # Question 24
# # Create a histogram showing the distribution of order values.

print("=====  Solution 24  =====")

order_values = [
    200, 250, 300, 350, 400, 450, 500,
    500, 550, 600, 650, 700, 750, 800,
    850, 900, 1000
]

plt.hist(order_values)

plt.title("Distribution of Order Value")
plt.xlabel("Order Value")
plt.ylabel("Frequency")

plt.show()


# # Question 25
# # Create a histogram for the following customer ages.
# # Add:
# # - Title
# # - X-axis label
# # - Y-axis label
# # - Gridlines

print("=====  Solution 25  =====")

customer_ages = [
    18, 19, 20, 21, 21, 22, 23, 24, 24,
    25, 26, 27, 28, 28, 29, 30, 32, 35,
    36, 40, 42, 45, 50
]

plt.hist(customer_ages)

plt.title("Distribution of Customer Age")
plt.xlabel("Customer Age")
plt.ylabel("Frequency")
plt.grid()

plt.show()


# # ============================================================
# # LEVEL 6 — PIE CHARTS
# # ============================================================

# # Question 26
# # Create a pie chart showing sales distribution by category.

print("=====  Solution 26  =====")

categories = ["Electronics", "Clothing", "Books", "Furniture"]
sales = [400, 300, 150, 150]

plt.pie(sales,labels=categories)

plt.show()


# # Question 27
# # Create a pie chart showing the distribution of expenses.
# # Display category names on the chart.

print("=====  Solution 27  =====")

categories = ["Rent", "Food", "Transport", "Entertainment"]
expenses = [30000, 10000, 5000, 5000]

plt.pie(expenses,labels=categories)

plt.title("Expenses by Category")
plt.show()


# # Question 28
# # Create a pie chart showing market share.
# # Display percentages on the chart.

print("=====  Solution 28  =====")

companies = ["Company A", "Company B", "Company C", "Company D"]
market_share = [40, 30, 20, 10]

plt.pie(market_share,labels=companies,autopct="%1.1f%%")

plt.title("Market Share by Companies")

plt.show()

# # Question 29
# # Create a pie chart showing the number of customers
# # from different cities.
# # Display both labels and percentages.

print("=====  Solution 29  =====")

cities = ["Delhi", "Mumbai", "Bangalore", "Chennai"]
customers = [400, 300, 200, 100]

plt.pie(customers,labels=cities,autopct="%1.1f%%")

plt.title("Customers by Cities")

plt.show()

# # Question 30
# # Create a pie chart showing sales by product category.
# # Display:
# # - Category names
# # - Percentages

print("=====  Solution 30  =====")

categories = ["Laptop", "Mobile", "Tablet", "Accessories"]
sales = [500, 700, 300, 200]

plt.pie(sales,labels=categories,autopct="%1.1f%%")

plt.title("Sales by Customers")

plt.show()

# # ============================================================
# # LEVEL 7 — MULTIPLE LINES AND LEGENDS
# # ============================================================

# # Question 31
# # Create two line charts on the same graph.
# # Compare sales for 2025 and 2026.
# # Add a legend.

print("=====  Solution 31  =====")

months = ["Jan", "Feb", "Mar", "Apr", "May"]

sales_2025 = [100, 120, 140, 130, 160]
sales_2026 = [110, 130, 150, 170, 190]

plt.plot(months,sales_2025,label="2025")
plt.plot(months,sales_2026,label="2026")

plt.legend()

plt.title("Sales by Months")
plt.xlabel("Month")
plt.ylabel("Sale")

plt.show()


# # Question 32
# # Compare the monthly revenue of two companies
# # using two lines on the same chart.
# # Add:
# # - Title
# # - Axis labels
# # - Legend

print("=====  Solution 32  =====")

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

company_a = [20000, 25000, 23000, 28000, 30000, 35000]
company_b = [18000, 22000, 24000, 26000, 32000, 34000]

plt.plot(months,company_a,marker="o",label="Company A")
plt.plot(months,company_b,marker="o",label="Company A")

plt.legend()

plt.title("Companies Revenue by Months")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.show()


# # Question 33
# # Create two lines showing website traffic for
# # two different websites.
# # Add markers to the lines and display a legend.

print("=====  Solution 33  =====")

months = ["Jan", "Feb", "Mar", "Apr", "May"]

website_a = [1000, 1200, 1500, 1400, 1800]
website_b = [900, 1100, 1300, 1600, 1700]

plt.plot(months,website_a,marker="s",label="Website A")
plt.plot(months,website_b,marker="o",label="Website B")

plt.legend()

plt.title("Website Traffic by Months")
plt.xlabel("Month")
plt.ylabel("Website Traffic")

plt.show()


# # Question 34
# # Compare the number of orders for two products
# # over six months.
# # Add a title, axis labels, legend, and gridlines.

print("=====  Solution 34  =====")

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

product_a = [100, 120, 150, 140, 180, 200]
product_b = [80, 100, 130, 160, 170, 190]

plt.plot(months,product_a,marker="s",label="Product A")
plt.plot(months,product_b,marker="o",label="Product B")

plt.legend()

plt.title("Orders by Months")
plt.xlabel("Month")
plt.ylabel("Orders")
plt.grid()

plt.show()


# # Question 35
# # Create a chart comparing profits for 2025 and 2026.
# # Use different line styles for the two years.
# # Add markers and a legend.

print("=====  Solution 35  =====")

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

profit_2025 = [10000, 12000, 11000, 15000, 17000, 19000]
profit_2026 = [12000, 14000, 13000, 17000, 20000, 23000]

plt.plot(months,profit_2025,marker="s",label="2025",linestyle="--")
plt.plot(months,profit_2026,marker="o",label="2026",linestyle="-.")

plt.legend()

plt.title("Profit by Months")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.grid()

plt.show()

# # ============================================================
# # LEVEL 8 — FIGURE SIZE AND SAVING CHARTS
# # ============================================================

# # Question 36
# # Create a line chart using the following data.
# # Set the figure size to 10 inches wide and 5 inches high.

print("=====  Solution 36  =====")

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 130, 180, 220]

plt.figure(figsize=(10,5))

plt.plot(months,sales,color="red",marker="o")

plt.title("Sales by Months")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()

plt.show()


# # Question 37
# # Create a bar chart using the following data.
# # Set an appropriate figure size.
# # Add a title and axis labels.

print("=====  Solution 37  =====")

products = ["Laptop", "Phone", "Tablet", "Watch"]
sales = [500, 800, 300, 400]

plt.figure(figsize=(12,6))

plt.bar(products,sales)

plt.title("Sales by Products")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.show()


# # Question 38
# # Create a line chart for the following data.
# # Save the resulting chart as "monthly_sales.png".

print("=====  Solution 38  =====")

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 125, 180, 220]

plt.figure(figsize=(10,5))

plt.plot(months,sales,color="red",marker="o")

plt.title("Sales by Month")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.savefig("Sales_Charts.png")

plt.show()

# # ============================================================
# # LEVEL 9 — COMBINATION PRACTICE
# # ============================================================

# # Question 39
# # You are given monthly sales data.
# #
# # Create a professional-looking line chart that includes:
# # - Appropriate figure size
# # - Title
# # - X-axis label
# # - Y-axis label
# # - Circular markers
# # - Thicker line
# # - Gridlines
# # - Legend
# #
# # Finally, display the chart.

print("=====  Solution 39  =====")

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

sales = [
    120, 135, 150, 145, 170, 180,
    160, 190, 210, 230, 250, 280
]

plt.figure(figsize=(10,5))

plt.plot(months,sales,marker="o",linewidth=1,label="Sales")

plt.legend()

plt.title("Sales by Month")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()

plt.savefig("Sales_by_month_Charts.png")

plt.show()


# # Question 40
# # You are analyzing product performance.
# #
# # Create a visualization showing the sales of each product.
# #
# # Your chart should include:
# # - Appropriate figure size
# # - Bars for each product
# # - A suitable title
# # - X-axis label
# # - Y-axis label
# # - Gridlines
# #
# # Finally, display the chart.

print("=====  Solution 40  =====")

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor",
    "Keyboard",
    "Mouse"
]

sales = [850, 1200, 500, 650, 400, 550]

plt.figure(figsize=(10,5))

bars = plt.bar(products, sales)

# Add data labels
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        str(bar.get_height()),
        ha="center",
        va="bottom"
    )

plt.bar(products,sales)

plt.title("Sales by Product")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.grid()

plt.savefig("Sales_by_Products_Charts.png")

plt.show()