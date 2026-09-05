import pandas as pd

df = pd.read_csv(r"C:\Users\knayl\Downloads\ecommerce_sales_34500.csv")
print(df.head(10))

print(df.shape)

print(df.columns)

print(df.info())

print(df.describe())

print(df.dtypes)

print(df.isna().sum())

print(df.duplicated().sum())

df["order_date"] = pd.to_datetime(df["order_date"])

print(df.dtypes)



# Part 1 — Understanding Numerical Data
# 1.

# Calculate the total number of orders in the dataset.

print("=====  Solution 1  =====")

print("total number of orders :",df["order_id"].count())

# 2.

# Calculate the total quantity of products sold.

print("=====  Solution 2  =====")

print("total quantity of products sold :",df["quantity"].sum())

# 3.

# Calculate the average product price.

print("=====  Solution 3  =====")

print("average product price :",df["price"].mean())

# 4.

# Calculate the median product price.

print("=====  Solution 4  =====")

print("median product price :",df["price"].median())

# 5.

# Find the minimum and maximum values of price.

print("=====  Solution 5  =====")

print("minimum price :",df["price"].min())
print("maximum price :",df["price"].max())

# 6.

# Calculate the average total_amount.

print("=====  Solution 6  =====")

print("average total_amount :",df["total_amount"].mean())

# 7.

# Calculate the median total_amount.

print("=====  Solution 7  =====")

print("median total_amount :",df["total_amount"].median())

# 8.

# Calculate the average shipping_cost.

print("=====  Solution 8  =====")

print("average shipping_cost :",df["shipping_cost"].mean())

# 9.

# Calculate the average profit_margin.

print("=====  Solution 9  =====")

print("average profit_margin :",df["profit_margin"].mean())

# 10.

# Use describe() to generate a statistical summary of the numerical columns.

print("=====  Solution 10  =====")

print(df.describe())

# Part 2 — Categorical Analysis
# 11.

# Find all unique product categories.

print("=====  Solution 11  =====")

print(df["category"].unique())

# 12.

# Find the number of unique categories.

print("=====  Solution 12  =====")

print("number of unique categories:",df["category"].nunique())


# 13.

# Count the number of orders in each category.

print("=====  Solution 13  =====")

print("number of orders in each category",df["category"].value_counts())

# 14.

# Calculate the percentage distribution of orders across categories.

print("=====  Solution 14  =====")

print("percentage distribution of orders across categories:", df["category"].value_counts(normalize=True) * 100)

# 15.

# Find all unique payment methods and count how many orders were made using each one.

print("=====  Solution 15  =====")

print(df["payment_method"].unique())

# 16.

# Calculate the percentage distribution of orders across payment methods.

print("=====  Solution 16  =====")

print("percentage distribution of orders across payment methods:",df["payment_method"].value_counts(normalize=True)*100)


# 17.

# Find all unique regions and calculate the number of orders from each region.

print("=====  Solution 17  =====")

print(df["region"].unique())

print("number of orders from each region:",df["region"].value_counts())

# 18.

# Find the number of unique customers.

print("=====  Solution 18  =====")

print("number of unique customers:",df["customer_id"].nunique())

# 19.

# Find the number of unique products.

print("=====  Solution 19  =====")

print("number of unique products",df["product_id"].nunique())

# 20.

# Calculate the number of orders for each customer_gender.

print("=====  Solution 20  =====")

print(df["customer_gender"].unique())

print("number of orders for each customer_gender:",df["customer_gender"].value_counts())

# Part 3 — Filtering
# 21.

# Display all orders where price is greater than 500.

print("=====  Solution 21  =====")

print(df[df["price"] > 500])

# 22.

# Display all orders where quantity is greater than 3.

print("=====  Solution 22  =====")

print(df[df["quantity"] > 3])

# 23.

# Display all orders where discount is greater than 0.10.

print("=====  Solution 23  =====")

print(df[df["discount"] > 0.10])

# 24.

# Display all orders where delivery_time_days is greater than 7.

print("=====  Solution 24  =====")

print(df[df["delivery_time_days"] > 7])

# 25.

# Display all orders where total_amount is greater than 1,000.

print("=====  Solution 25  =====")

print(df[df["total_amount"] > 1000])

# 26.

# Find all orders from the North region.

print("=====  Solution 26  =====")

print(df[df["region"]=="North"])

# 27.

# Find all orders where the customer is older than 40.

print("=====  Solution 27  =====")

print(df[df["customer_age"]>40])

# 28.

# Find all orders where:

# quantity >= 3
# AND
# total_amount > 500

print("=====  Solution 28  =====")

print(df[(df["quantity"]>=3) & (df["total_amount"] > 500)])

# 29.

# Find all orders where:

# category = Electronics
# AND
# returned = True

print("=====  Solution 29  =====")

print(df[(df["category"]=="Electronics") & (df["returned"] == "Yes")])

# 30.

# Find all orders where the payment method is either Credit Card or UPI.

print("=====  Solution 30  =====")

print(df[(df["payment_method"]=="Credit Card") | (df["payment_method"] == "UPI")])

# Part 4 — Business Calculations

# Now start creating analytical columns.

# 31.

# Create a new column called calculated_amount using:

# price × quantity

# Compare it with the existing total_amount column.

print("=====  Solution 31  =====")


df["Calculated_Amount"] = df["price"] * df["quantity"]

print(df.head(5))

print(df["total_amount"] > df["Calculated_Amount"])

# 32.

# Calculate the difference between calculated_amount and total_amount.

# Create a column called:

# amount_difference

print("=====  Solution 32  =====")

df["Amount_Difference"] = df["Calculated_Amount"] - df["total_amount"]

print(df.head(5))

# 33.

# Find how many orders have a difference between calculated_amount and total_amount.

print("=====  Solution 33  =====")

print((df["Calculated_Amount"] != df["total_amount"]).sum())

# 34.

# Calculate the total value of all orders using the total_amount column.

print("=====  Solution 34  =====")

print(df["total_amount"].sum())

# 35.

# Calculate the total shipping cost across all orders.

print("=====  Solution 35  =====")

print("total shipping cost across all orders",df["shipping_cost"].sum())

# 36.

# Calculate the average shipping cost per order.

print("=====  Solution 36  =====")

print("average shipping cost per order",df["shipping_cost"].mean())

# 37.

# Find the order with the highest total_amount and display the complete row.

print("=====  Solution 37  =====")

print(df.nlargest(1,"total_amount"))


# 38.

# Find the order with the lowest total_amount and display the complete row.


print("=====  Solution 38  =====")

print(df.nsmallest(1,"total_amount"))

# 39.

# Find the top 10 orders based on total_amount.

print("=====  Solution 39  =====")

print(df.nlargest(10,"total_amount"))

# 40.

# Find the 10 orders with the highest shipping costs.

print("=====  Solution 40  =====")

print(df.nlargest(10,"shipping_cost"))

# Part 5 — GroupBy Analysis
# 41.

# Calculate the total total_amount for each category.

print("=====  Solution 41  =====")

print(df.groupby("category")["total_amount"].sum())

# 42.

# Calculate the average total_amount for each category.

print("=====  Solution 42  =====")

print(df.groupby("category")["total_amount"].mean())

# 43.

# Calculate the total quantity sold for each category.

print("=====  Solution 43  =====")

print(df.groupby("category")["quantity"].sum())

# 44.

# Calculate the average profit_margin for each category.

print("=====  Solution 44  =====")

print(df.groupby("category")["profit_margin"].mean())

# 45.

# Calculate the average delivery time for each category.

print("=====  Solution 45  =====")

print(df.groupby("category")["delivery_time_days"].mean())
print(df.columns)

# 46.

# Calculate total sales for each region.

print("=====  Solution 46  =====")

print(df.groupby("region")["total_amount"].sum())

# 47.

# Calculate the average order value for each region.

print("=====  Solution 47  =====")

print(df.groupby("region")["price"].mean())

# 48.

# Calculate the total shipping cost for each region.

print("=====  Solution 48  =====")

print(df.groupby("region")["shipping_cost"].sum())

# 49.

# For each payment method, calculate:

# Number of orders
# Total sales
# Average order value
# Average shipping cost

# Return the result as a single DataFrame.

print("=====  Solution 49  =====")

print(df.groupby("payment_method").agg(
    Number_of_orders = ("order_id","count"),
    Total_sales = ("total_amount","sum"),
    Average_order_value = ("total_amount","mean"),
    Average_shipping_cost = ("shipping_cost","mean"),
))

# 50.

# For each customer gender, calculate:

# Number of orders
# Total sales
# Average order value
# Average quantity purchased

# Return the result as a single DataFrame.

print("=====  Solution 50  =====")

print(df.groupby("customer_gender").agg(
    Number_of_orders = ("order_id","count"),
    Total_sales = ("total_amount","sum"),
    Average_order_value = ("total_amount","mean"),
    Average_quantity_purchased = ("quantity","mean")
))

# Part 6 — Advanced Pandas Analysis
# 51.

# Find the top 10 customers by total spending.

# Your result should contain:

# customer_id
# total_spending

print("=====  Solution 51  =====")

print(
    df[["customer_id", "total_amount"]]
    .groupby("customer_id", as_index=False)
    .sum()
    .rename(columns={"total_amount": "total_spending"})
    .nlargest(10, "total_spending")
)

# 52.

# Find the top 10 customers by number of orders.

print("===== Solution 52 =====")

print(
    df.groupby("customer_id")
      .size().nlargest(10)
)

# 53.

# For every customer, calculate:

# customer_id
# number_of_orders
# total_spending
# average_order_value
# total_quantity

# Return everything as one DataFrame.

print("===== Solution 53 =====")

result = df.groupby("customer_id").agg(
    number_of_orders = ("order_id","count"),
    total_spending = ("total_amount","sum"),
    average_order_value = ("total_amount","mean"),
    total_quantity = ("quantity","sum"),
)

print(result)

# 54.

# Find customers who have placed at least 5 orders.

print("===== Solution 54 =====")

print(
    df.groupby("customer_id")["order_id"]
      .count()
      .loc[lambda x: x >= 5]
)

# 55.

# Find the top 10 products based on total quantity sold.

print("===== Solution 55 =====")

print(
    df.groupby("product_id")["quantity"]
      .sum()
      .nlargest(10)
)

# 56.

# Find the top 10 products based on total sales (total_amount).

print("===== Solution 56 =====")

print(
    df.groupby("product_id")["total_amount"]
      .sum()
      .nlargest(10)
)

# 57.

# Calculate the percentage contribution of each region to total sales.

# Your result should contain:

# region
# total_sales
# sales_percentage

print("===== Solution 57 =====")

result = (
    df.groupby("region", as_index=False)
      .agg(total_sales=("total_amount", "sum"))
)

result["sales_percentage"] = (
    result["total_sales"] / result["total_sales"].sum() * 100
)

print(result)


# 58.

# Compare returned and non-returned orders.

# For each value of returned, calculate:

# Number of orders
# Total sales
# Average order value
# Average delivery time
# Average profit margin

print("===== Solution 58 =====")

print("returned :",df["returned"].value_counts())

result = df.groupby("returned").agg(
    number_of_orders = ("order_id","count"),
    total_spending = ("total_amount","sum"),
    average_order_value = ("total_amount","mean"),
    Average_delivery_time = ("delivery_time_days","mean"),
    Average_profit_margin = ("profit_margin","mean"),
)

print(result)

# 59.

# Analyze the relationship between these numerical columns:

# price
# discount
# quantity
# delivery_time_days
# total_amount
# shipping_cost
# profit_margin
# customer_age

# Create a correlation matrix and identify which variables have the strongest positive and negative relationships with total_amount.

print("===== Solution 59 =====")

# Create correlation matrix
corr_matrix = df.corr(numeric_only=True)

print(corr_matrix)

# Correlations with total_amount
total_amount_corr = corr_matrix["total_amount"].drop("total_amount")

# Strongest positive relationship
strongest_positive = total_amount_corr.idxmax()
positive_value = total_amount_corr.max()

# Strongest negative relationship
strongest_negative = total_amount_corr.idxmin()
negative_value = total_amount_corr.min()

print("\nStrongest positive relationship:")
print(strongest_positive, positive_value)

print("\nStrongest negative relationship:")
print(strongest_negative, negative_value)


# 60.

# Perform a complete monthly e-commerce sales analysis.

# First convert order_date into a proper datetime column.

# Then create a monthly summary containing:

# Month
# Number of orders
# Total quantity sold
# Total sales
# Average order value
# Total shipping cost
# Average delivery time
# Average profit margin
# Number of returned orders

# Finally, sort the result chronologically.

print("===== Solution 60 =====")

# Create Month
df["Month"] = df["order_date"].dt.to_period("M")

# Create returned flag
df["returned_flag"] = df["returned"].eq("Yes")

# Monthly summary
result = df.groupby("Month").agg(
    number_of_orders=("order_id", "count"),
    total_quantity_sold=("quantity", "sum"),
    total_sales=("total_amount", "sum"),
    average_order_value=("total_amount", "mean"),
    total_shipping_cost=("shipping_cost", "sum"),
    average_delivery_time=("delivery_time_days", "mean"),
    average_profit_margin=("profit_margin", "mean"),
    number_of_returned_orders=("returned_flag", "sum")
).reset_index()

# Sort chronologically
result = result.sort_values("Month")

print(result)