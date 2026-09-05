import numpy as np


# # ============================================================
# # LEVEL 1 — CREATING AND UNDERSTANDING ARRAYS
# # ============================================================

# # 1. Create a NumPy array
# # Create a NumPy array containing:
# # 10, 20, 30, 40, 50
# # Print the array.

print("=====  Solution 1  =====")

numbers = np.array([10, 20, 30, 40, 50])
print(numbers)


# # 2. Create an array of even numbers
# # Create a NumPy array containing:
# # 2, 4, 6, 8, 10, 12, 14, 16, 18, 20

print("=====  Solution 2  =====")

even_numbers = np.arange(2,21,2)
print(even_numbers)


# # 3. Create an array using arange()
# # Create an array containing numbers from 1 to 20 using NumPy.

print("=====  Solution 3  =====")

numbers = np.arange(1,21)
print(numbers)

# # 4. Create an array with a step
# # Create an array containing:
# # 5, 10, 15, 20, 25, 30, 35, 40
# # using NumPy.

print("=====  Solution 4  =====")

numbers = np.arange(5,41,5)
print(numbers)

# # 5. Create an array using linspace()
# # Create 10 evenly spaced numbers between 0 and 100.

print("=====  Solution 5  =====")

number = np.linspace(0,100,10)
print(number)

# # 6. Create an array of zeros
# # Create a NumPy array containing 10 zeros.


print("=====  Solution 6  =====")

number = np.zeros(10)
print(number)

# # 7. Create an array of ones
# # Create a NumPy array containing 8 ones.

print("=====  Solution 7  =====")

number = np.ones(8)
print(number)

# # 8. Create an array filled with a value
# # Create a NumPy array containing 7 values,
# # where every value is 25.

print("=====  Solution 8  =====")

number = np.full(7,25)
print(number)

# # 9. Check array information
# arr = np.array([10, 20, 30, 40, 50])

# # Print:
# # - Number of dimensions
# # - Shape
# # - Total number of elements
# # - Data type

print("=====  Solution 9  =====")

arr = np.array([10, 20, 30, 40, 50])

print("Number of dimensions :",arr.ndim)
print("Shape :", arr.shape)
print("Total number of elements:", arr.size)
print("Data type :", arr.dtype)


# # 10. Create a 2D array
# # Create the following NumPy array:
# #
# # 10 20 30
# # 40 50 60
# # 70 80 90
# #
# # Then print:
# # - Shape
# # - Number of dimensions
# # - Total number of elements

print("=====  Solution 10  =====")

arr = np.array([[10,20,30],[40,50,60],[70,80,90]])

print("Shape :", arr.shape)
print("Number of dimensions :",arr.ndim)
print("Total number of elements:", arr.size)

# # ============================================================
# # LEVEL 2 — INDEXING AND SLICING
# # ============================================================

# # 11. Access the first value
# arr = np.array([25, 40, 15, 60, 80])

# # Print the first value.

print("=====  Solution 11  =====")

arr = np.array([25, 40, 15, 60, 80])

print("first value",arr[0])


# # 12. Access the last value
# # Using the same array, print the last value.

print("=====  Solution 12  =====")

print("last value",arr[-1])

# # 13. Access a specific value
# arr = np.array([100, 200, 300, 400, 500])

# # Print the value 300 using indexing.

print("=====  Solution 13  =====")

arr = np.array([100, 200, 300, 400, 500])

print(arr[2])


# # 14. Extract the first three values
# arr = np.array([10, 20, 30, 40, 50, 60])

# # Extract:
# # 10, 20, 30

print("=====  Solution 14  =====")

arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[0:3])

# # 15. Extract the last three values
# # Using:
# # arr = np.array([10, 20, 30, 40, 50, 60])
# #
# # Extract:
# # 40, 50, 60

print("=====  Solution 15  =====")

arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[-3:])

# # 16. Extract values from the middle
# arr = np.array([5, 10, 15, 20, 25, 30, 35])

# # Extract:
# # 15, 20, 25

print("=====  Solution 16  =====")

arr = np.array([5, 10, 15, 20, 25, 30, 35])

print(arr[2:5])

# # 17. Reverse an array
# arr = np.array([10, 20, 30, 40, 50])

# # Create a reversed version:
# # 50, 40, 30, 20, 10

print("=====  Solution 17  =====")

arr = np.array([10, 20, 30, 40, 50])

print(arr[::-1])

# # 18. Access a value from a 2D array
# arr = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])

# # Extract the value 50.

print("=====  Solution 18  =====")

arr = np.array([
     [10, 20, 30],
     [40, 50, 60],
     [70, 80, 90]
 ])

print(arr[1][1])


# # 19. Extract the first row
# # Using the same 2D array, extract:
# # 10, 20, 30

print("=====  Solution 19  =====")

print(arr[0][:])

# # 20. Extract the second column
# # Using the same 2D array, extract:
# # 20
# # 50
# # 80

print("=====  Solution 20  =====")

print(arr[1][:])


# # ============================================================
# # LEVEL 3 — ARITHMETIC OPERATIONS
# # ============================================================

# # 21. Increase every value
# sales = np.array([100, 200, 300, 400, 500])
# # Increase every sales value by 50.
# # Expected:
# # 150, 250, 350, 450, 550

print("=====  Solution 21  =====")

sales = np.array([100, 200, 300, 400, 500])

print(sales + 50)


# # 22. Apply a discount
# prices = np.array([100, 200, 300, 400, 500])

# # Apply a 10% discount to every price.

print("=====  Solution 22  =====")

prices = np.array([100, 200, 300, 400, 500])

discounted_price = prices - (prices * 0.1)
print(discounted_price)

# # 23. Increase prices by 20%
# prices = np.array([500, 1000, 1500, 2000])

# # Increase every price by 20%.

print("=====  Solution 23  =====")

prices = np.array([500, 1000, 1500, 2000])

Increased_price = prices + (prices * 0.2)
print(Increased_price)


# # 24. Calculate profit
# sales = np.array([1000, 2000, 3000, 4000])
# cost = np.array([600, 1200, 1800, 2500])

# # Calculate the profit for each item.

print("=====  Solution 24  =====")

sales = np.array([1000, 2000, 3000, 4000])
cost = np.array([600, 1200, 1800, 2500])

profit = sales - cost

print(profit)

# # 25. Calculate remaining inventory
# stock = np.array([100, 200, 150, 300])
# sold = np.array([20, 50, 40, 100])

# # Calculate the remaining stock for each product.

print("=====  Solution 25  =====")

stock = np.array([100, 200, 150, 300])
sold = np.array([20, 50, 40, 100])

remaining_stock = stock - sold

print(remaining_stock)

# # 26. Calculate tax
# salary = np.array([30000, 40000, 50000, 60000])

# # Calculate 10% tax on each salary.

print("=====  Solution 26  =====")

salary = np.array([30000, 40000, 50000, 60000])

tax = 0.1 * salary

print(tax)


# # 27. Calculate percentage scores
# marks = np.array([45, 80, 70, 90, 60])

# # Assume each exam is out of 100.
# # Convert the marks into percentages.

print("=====  Solution 27  =====")

marks = np.array([45, 80, 70, 90, 60])

marks_percentage = marks/100 * 100

print(marks_percentage)


# # 28. Add two arrays
# sales_january = np.array([100, 200, 300, 400])
# sales_february = np.array([150, 250, 350, 450])

# # Calculate the combined sales for each position.

print("=====  Solution 28  =====")

sales_january = np.array([100, 200, 300, 400])
sales_february = np.array([150, 250, 350, 450])

combined_sales = sales_january + sales_february

print(combined_sales)

# # 29. Calculate month-wise growth
# previous_sales = np.array([1000, 1500, 2000, 2500])
# current_sales = np.array([1200, 1600, 2400, 3000])

# # Calculate the difference between current sales
# # and previous sales.

print("=====  Solution 29  =====")

previous_sales = np.array([1000, 1500, 2000, 2500])
current_sales = np.array([1200, 1600, 2400, 3000])

difference = current_sales - previous_sales

print(difference)

# # 30. Calculate percentage growth
# # Using:
# #
# # previous_sales = np.array([1000, 1500, 2000, 2500])
# # current_sales = np.array([1200, 1600, 2400, 3000])
# #
# # Calculate the percentage growth for each value.

print("=====  Solution 30  =====")

previous_sales = np.array([1000, 1500, 2000, 2500])
current_sales = np.array([1200, 1600, 2400, 3000])

percent_growth = (current_sales - previous_sales)/previous_sales * 100

print(percent_growth)


# # ============================================================
# # LEVEL 4 — STATISTICAL OPERATIONS
# # ============================================================

# # 31. Calculate total sales
# sales = np.array([1200, 1500, 900, 1800, 2200, 1700])

# # Find the total sales.

print("=====  Solution 31  =====")

sales = np.array([1200, 1500, 900, 1800, 2200, 1700])

print("total sales:",sales.sum())

# # 32. Calculate average sales
# # Using the same sales array, calculate the average sales.

print("=====  Solution 32  =====")

print("average sales:",sales.mean())

# # 33. Find minimum and maximum
# sales = np.array([1200, 1500, 900, 1800, 2200, 1700])

# # Find:
# # - Minimum sales
# # - Maximum sales

print("=====  Solution 33  =====")

sales = np.array([1200, 1500, 900, 1800, 2200, 1700])

print("Minimum sales:",sales.min())
print("Maximum sales:",sales.max())

# # 34. Find the median
# sales = np.array([500, 200, 800, 300, 1000, 400, 600])

# # Calculate the median.

print("=====  Solution 34  =====")

sales = np.array([500, 200, 800, 300, 1000, 400, 600])

print("median:",np.median(sales))

# # 35. Calculate standard deviation
# sales = np.array([100, 120, 110, 105, 115, 108])

# # Calculate the standard deviation.

print("=====  Solution 35  =====")

sales = np.array([100, 120, 110, 105, 115, 108])

print(np.std(sales))

# # 36. Calculate variance
# sales = np.array([100, 120, 110, 105, 115, 108])

# # Calculate the variance.

print("=====  Solution 36  =====")

sales = np.array([100, 120, 110, 105, 115, 108])

print(np.var(sales))

# # 37. Analyze employee salaries
# salary = np.array([30000, 45000, 50000, 35000, 60000, 55000, 40000])

# # Calculate:
# # - Total salary
# # - Average salary
# # - Median salary
# # - Minimum salary
# # - Maximum salary
# # - Standard deviation

print("=====  Solution 37  =====")

salary = np.array([30000, 45000, 50000, 35000, 60000, 55000, 40000])

print("Total salary:",salary.sum())
print("Average salary:",salary.mean())
print("Median salary:",np.median(salary))
print("Minimum salary:",salary.min())
print("Maximum salary:",salary.max())
print("Standard deviation:",np.std(salary))


# # 38. Analyze customer ages
# ages = np.array([22, 35, 41, 28, 19, 52, 31, 45, 27])

# # Calculate:
# # - Average age
# # - Youngest age
# # - Oldest age
# # - Median age

print("=====  Solution 38  =====")

ages = np.array([22, 35, 41, 28, 19, 52, 31, 45, 27])

print("Average age:",ages.mean())
print("Youngest age:",ages.min())
print("Oldest age:",ages.max())
print("Median age:",np.median(ages))


# # ============================================================
# # LEVEL 5 — FILTERING AND CONDITIONS
# # ============================================================

# # 39. Find sales above 500
# sales = np.array([100, 750, 300, 900, 450, 1200, 600])

# # Extract only the sales values greater than 500.

print("=====  Solution 39  =====")

sales = np.array([100, 750, 300, 900, 450, 1200, 600])

print(sales[sales > 500])

# # 40. Find customers older than 30
# ages = np.array([22, 35, 41, 28, 19, 52, 31, 25])

# # Extract all ages greater than 30.

print("=====  Solution 40  =====")

ages = np.array([22, 35, 41, 28, 19, 52, 31, 25])

print("all ages greater than 30 :\n" ,ages[ages > 30])

# # 41. Find failed students
# marks = np.array([85, 42, 76, 33, 90, 28, 65, 49])

# # Assume the passing mark is 50.
# # Extract the marks of students who failed.

print("=====  Solution 41  =====")

marks = np.array([85, 42, 76, 33, 90, 28, 65, 49])

print("marks of students who failed :\n" ,marks[marks < 50])

# # 42. Find high-value transactions
# transactions = np.array([
#     500,
#     1200,
#     350,
#     5000,
#     800,
#     2500,
#     150,
#     7000
# ])

# # Extract transactions greater than 2000.

print("=====  Solution 42  =====")

transactions = np.array([
    500,
    1200,
    350,
    5000,
    800,
    2500,
    150,
    7000
])

print("transactions greater than 2000 :\n" ,transactions[transactions > 2000])

# # 43. Find values between two limits
# sales = np.array([100, 250, 400, 550, 700, 850, 1000])

# # Extract values between 300 and 800.

print("=====  Solution 42  =====")

sales = np.array([100, 250, 400, 550, 700, 850, 1000])

result = sales[(sales >= 300) & (sales <= 800)]

print("values between 300 and 800 :\n" ,result)

# # 44. Count high-value sales
# sales = np.array([100, 750, 300, 900, 450, 1200, 600, 2000])

# # Find how many sales values are greater than 500.

print("=====  Solution 44  =====")

sales = np.array([100, 750, 300, 900, 450, 1200, 600, 2000])

result = sales[sales > 500]

print(len(result))

# # 45. Replace values using where
# sales = np.array([100, 600, 300, 800, 450, 1200])

# # Create a new array where:
# # - Sales greater than 500 become "High"
# # - All other sales become "Low"

print("=====  Solution 45  =====")

sales = np.array([100, 600, 300, 800, 450, 1200])

result = np.where(sales>500,"High","Low")
print(result)

# # ============================================================
# # LEVEL 6 — RESHAPING, AXIS AND PRACTICAL ANALYSIS
# # ============================================================

# # 46. Reshape an array
# arr = np.arange(1, 13)

# # Reshape it into:
# #
# # 1   2   3   4
# # 5   6   7   8
# # 9  10  11  12
# #
# # Then print its shape.

print("=====  Solution 46  =====")
arr = np.arange(1, 13)

result = arr.reshape(3,4)

print(result)

print("Shape:", result.shape)

# # 47. Calculate row totals
# sales = np.array([
#     [100, 200, 300],
#     [400, 500, 600],
#     [700, 800, 900]
# ])

# # Calculate the total sales for each row.
# #
# # Expected:
# # 600
# # 1500
# # 2400

print("=====  Solution 47  =====")

sales = np.array([
    [100, 200, 300],
    [400, 500, 600],
    [700, 800, 900]
])

print("total sales for each row : \n" , np.sum(sales,axis=1))


# # 48. Calculate column totals
# sales = np.array([
#     [100, 200, 300],
#     [400, 500, 600],
#     [700, 800, 900]
# ])

# # Calculate the total for each column.
# #
# # Expected:
# # 1200
# # 1500
# # 1800

print("=====  Solution 48  =====")

sales = np.array([
    [100, 200, 300],
    [400, 500, 600],
    [700, 800, 900]
])

print("total for each column : \n" , np.sum(sales,axis=0))


# # 49. Analyze branch sales
# #
# # Three branches over four months.
# # Each row represents one branch.

# sales = np.array([
#     [1000, 1200, 1100, 1300],
#     [1500, 1600, 1400, 1700],
#     [900, 1000, 950, 1200]
# ])

# # Calculate:
# #
# # 1. Total sales for each branch.
# # 2. Average sales for each branch.
# # 3. Total sales for each month.
# # 4. Which branch has the highest total sales?
# # 5. Which month has the highest total sales?


print("===== Solution 49 =====")

sales = np.array([
    [1000, 1200, 1100, 1300],
    [1500, 1600, 1400, 1700],
    [900, 1000, 950, 1200]
])

branch_totals = np.sum(sales, axis=1)
branch_averages = np.mean(sales, axis=1)
month_totals = np.sum(sales, axis=0)

print("Total sales for each branch:", branch_totals)
print("Average sales for each branch:", branch_averages)
print("Total sales for each month:", month_totals)

print("Branch with highest total sales:", np.argmax(branch_totals) + 1)
print("Month with highest total sales:", np.argmax(month_totals) + 1)

# # 50. MINI DATA ANALYSIS CHALLENGE

# transactions = np.array([
#     1200, 450, 2300, 800, 1500,
#     3200, 700, 1800, 950, 4200,
#     600, 2750, 1100, 3500, 900
# ])

# # Perform the following analysis:
# #
# # 1. Find the total number of transactions.
# #
# # 2. Find the total transaction value.
# #
# # 3. Find the average transaction value.
# #
# # 4. Find the median transaction value.
# #
# # 5. Find the minimum transaction value.
# #
# # 6. Find the maximum transaction value.
# #
# # 7. Find the standard deviation.
# #
# # 8. Extract transactions greater than 2000.
# #
# # 9. Count how many transactions are greater than 2000.
# #
# # 10. Extract transactions between 1000 and 3000.
# #
# # 11. Calculate what percentage of transactions
# #     are greater than 2000.
# #
# # 12. Increase every transaction value by 5%.
# #
# # 13. Find the total value of the transactions
# #     after the 5% increase.
# #
# # 14. Create a new array that labels every transaction
# #     as "High" if it is greater than 2000,
# #     otherwise "Low".

print("===== Solution 50 =====")

transactions = np.array([
    1200, 450, 2300, 800, 1500,
    3200, 700, 1800, 950, 4200,
    600, 2750, 1100, 3500, 900
])

# 1. Find the total number of transactions.

print("total number of transactions :" , transactions.size)

# # 2. Find the total transaction value.

print("total transaction value :" , transactions.sum())

# # 3. Find the average transaction value.

print("average transaction value :" , transactions.mean())

# # 4. Find the median transaction value.

print("median transaction value :" , np.median(transactions))

# # 5. Find the minimum transaction value.

print("minimum transaction value :" , transactions.min())

# # 6. Find the maximum transaction value.

print("maximum transaction value :" , transactions.max())

# # 7. Find the standard deviation.

print("standard deviation :" , np.std(transactions))

# # 8. Extract transactions greater than 2000.

print("transactions greater than 2000 :" , transactions[transactions > 2000])

# # 9. Count how many transactions are greater than 2000.

print("count of transactions greater than 2000 :" , len(transactions[transactions > 2000]))

# # 10. Extract transactions between 1000 and 3000.

print("transactions between 1000 and 3000 :" , transactions[(transactions >= 1000) & (transactions <= 3000)])

# # 11. Calculate what percentage of transactions
# #     are greater than 2000.

result = len(transactions[transactions > 2000])/len(transactions) * 100
print("percentage of transactions greater than 2000 :" ,result)

# # 12. Increase every transaction value by 5%.

result = transactions + (transactions * 0.05)
print("transaction Increase value by 5% :" , result)

# # 13. Find the total value of the transactions
# #     after the 5% increase.

result = transactions + (transactions * 0.05)
print("total value of the transactions after Increase value by 5% :" , result.sum())

# # 14. Create a new array that labels every transaction
# #     as "High" if it is greater than 2000,
# #     otherwise "Low".

result = np.where(transactions > 2000 ,"High","Low")
print(result)