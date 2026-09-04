import pandas as pd
import numpy as np

data = {
    "Order_ID": [
        "ORD1001", "ORD1002", "ORD1003", "ORD1004", "ORD1005",
        "ORD1006", "ORD1007", "ORD1008", "ORD1009", "ORD1010",
        "ORD1011", "ORD1012", "ORD1013", "ORD1014", "ORD1015",
        "ORD1016", "ORD1017", "ORD1018", "ORD1019", "ORD1020",
        "ORD1021", "ORD1022", "ORD1023", "ORD1024", "ORD1025",
        "ORD1026", "ORD1027", "ORD1028", "ORD1029", "ORD1030"
    ],

    "Customer_Name": [
        " Rahul Sharma ", "Priya Mehta", "AMIT KUMAR", "Neha Singh",
        "rohit verma", "Anjali Gupta", None, "Vikas Rao",
        " Sneha Patel", "Arjun Malhotra", "Pooja Nair", "Karan Shah",
        "Meena Joshi", "Ravi Kapoor", "Simran Kaur", "Aakash Jain",
        "Nisha Roy", "Manish Sethi", "Rahul Sharma ", "Divya Menon",
        "Sahil Khan", "Priti Das", "Vivek Mishra", "Komal Arora",
        "Rohan Bhat", "Isha Kapoor", "Dev Mehta", "Tanya Singh",
        "Aditya Rao", "Neha Singh"
    ],

    "Age": [
        "28", "34", "Unknown", "29", "41", "17", None, "38",
        "31", "45", "27", "150", "36", "abc", "24", "39",
        "42", "28", "28", "33", "-5", "30", "26", None,
        "37", "29", "200", "35", "40", "29"
    ],

    "Gender": [
        "Male", "female", "M", "Female", "male", "F", "Female", None,
        "FEMALE", "Male", "Female", "M", "female", "Male", "F",
        "Male", "Female", "MALE", "male", "Female", "M", "female",
        "Male", "F", "Male", "Female", "M", "female", "Male", "F"
    ],

    "City": [
        "Delhi", "Mumbai", "delhi", "Bangalore ", "Mumbai",
        "Delhi ", "Pune", "MUMBAI", "Bengaluru", "Delhi",
        "Pune", None, "Delhi", "Mumbai", "pune", "Delhi",
        "Bangalore", "Delhi", "Delhi", "Mumbai", "Delhi",
        "Pune", "Mumbai", "Delhi", "Bengaluru ", "Delhi",
        "Mumbai", "pune", "DELHI", "Mumbai"
    ],

    "Order_Date": [
        "2026-01-05", "05/01/2026", "2026-01-07", "08-01-2026",
        "2026/01/10", "2026-01-12", None, "15/01/2026",
        "2026-01-17", "18-01-2026", "2026-01-20", "2026-01-22",
        "25/01/2026", "2026-01-27", "invalid", "2026-01-30",
        "02/02/2026", "2026-02-04", "2026-02-05", None,
        "2026/02/08", "10-02-2026", "2026-02-12", "13/02/2026",
        "2026-02-15", "16/02/2026", "2026-02-18", "19/02/2026",
        "2026-02-20", "21/02/2026"
    ],

    "Product_Category": [
        "Electronics", "electronics", "Home & Kitchen", "Fashion",
        "fashion ", "Electronics", "Beauty", "HOME & KITCHEN",
        "Fashion", None, "Beauty", "Electronics", "electronics",
        "Home & Kitchen", "Fashion", "BEAUTY", "Electronics",
        "Home & Kitchen", "electronics", "Fashion", "Beauty",
        "Electronics", "home & kitchen", "Fashion", "Electronics",
        "Beauty", "fashion", "Electronics", "Home & Kitchen", "electronics"
    ],

    "Quantity": [
        "2", "1", "3", "2", "1", "5", "2", None, "1", "2",
        "4", "-1", "2", "three", "1", "3", "2", "10", "2", "1",
        "0", "2", "4", None, "2", "1", "2", "3", "1", "2"
    ],

    "Unit_Price": [
        "₹25,000", "45000", "₹1,200", "2500", "₹3,499",
        "₹18,000", "999", "₹2,500", "3499", "₹55,000",
        "₹899", "12000", "₹22,500", "₹1,499", "2999",
        "₹75,000", "₹1,999", "3500", "₹25,000", "₹4,500",
        "₹799", "15000", "₹2,200", "₹5,999", None,
        "₹1,299", "₹35,000", "2499", "₹8,500", "₹25,000"
    ],

    "Discount": [
        "10%", "5%", "0%", None, "15%", "20%", "5%", "10%",
        "0%", "25%", "10%", "5%", "15%", "0%", "10%", "20%",
        "5%", "10%", "10%", "15%", "0%", "5%", "10%", "20%",
        "5%", None, "15%", "10%", "0%", "5%"
    ],

    "Payment_Method": [
        "Credit Card", "UPI", "credit card", "Debit Card", "UPI",
        "Cash on Delivery", "COD", "UPI", "Credit Card", None,
        "upi", "Debit card", "Credit Card", "COD", "UPI",
        "Credit Card", "debit card", "UPI", "Credit Card",
        "Cash On Delivery", "COD", "upi", "Credit Card",
        "Debit Card", "UPI", "Credit Card", "COD", "UPI",
        "Debit card", "Credit Card"
    ],

    "Order_Status": [
        "Delivered", "delivered", "Shipped", "Cancelled", "Delivered",
        "DELIVERED", "Pending", "Delivered", "returned", "Delivered",
        "Shipped", "Cancelled", "Delivered", "Pending", "Returned",
        "Delivered", "Shipped", "delivered", "Delivered", "Cancelled",
        "Pending", "Delivered", "Shipped", "Returned", "Delivered",
        "Cancelled", "Delivered", "pending", "Delivered", "Delivered"
    ],

    "Customer_Rating": [
        5, 4, None, 3, 5, 2, 4, 5, 1, None,
        4, 2, 5, 3, 4, 5, None, 3, 5, 2,
        4, 5, 3, 1, None, 4, 5, 3, 4, 5
    ]
}

df = pd.DataFrame(data)

print(df)

# ============================================================
# LEVEL 1 — INSPECT AND UNDERSTAND THE DATASET
# ============================================================

# 1. Display the first 5 rows of the DataFrame.

print(" ===== Solution 1 =====")
print(df.head(5))

# 2. Display the last 5 rows of the DataFrame.

print(" ===== Solution 2 =====")

print(df.tail(5))

# 3. Find the number of rows and columns in the DataFrame.

print(" ===== Solution 3 =====")
print("number of rows and columns in the DataFrame:",df.shape)

# 4. Display the names of all columns.

print(" ===== Solution 4 =====")

print("names of all columns : ",df.columns)

# 5. Check the data type of every column.

print(" ===== Solution 5 =====")

print(df.dtypes)

# 6. Find the total number of missing values in each column.

print(" ===== Solution 6 =====")

print(df.isna().sum())

# 7. Find the total number of missing values in the entire DataFrame.

print(" ===== Solution 7 =====")

print("total number of missing values in the entire DataFrame:",df.isna().sum().sum())


# 8. Display all rows that contain at least one missing value.

print(" ===== Solution 8 =====")
print(df[df.isna().any(axis=1)])

# 9. Find the number of duplicate rows in the DataFrame.

print(" ===== Solution 9 =====")

print(df.duplicated().sum())

# 10. Display all duplicate rows.

print(" ===== Solution 10 =====")

print(df[df.duplicated()])

# ============================================================
# LEVEL 2 — MISSING VALUES
# ============================================================

# 11. Fill all missing values in the Customer_Rating column with 0.

print(" ===== Solution 11 =====")
df1 = pd.DataFrame(data)
print(df1["Customer_Rating"].fillna(0))
print(df1)

# 12. Fill missing values in the Age column with the median age
#     after converting valid age values to numeric values.

print(" ===== Solution 12 =====")

df1["Age"] = pd.to_numeric(df1["Age"],errors="coerce")
df1["Age"] = df1["Age"].fillna(df1["Age"].median())
print(df1)

# 13. Fill missing values in the Gender column with the
#     most frequently occurring gender.

print(" ===== Solution 13 =====")

print(df1["Gender"].fillna(df1["Gender"].mode()[0]))
print(df1.head(5))



# 14. Fill missing values in the City column with the
#     most frequently occurring city after standardizing
#     the city names.

print(" ===== Solution 14 =====")

df1["City"] = df1["City"].str.lower()
print(df1["City"].fillna(df1["City"].mode()[0]))


# 15. Find how many missing values exist in the Order_Date column.

print(" ===== Solution 15 =====")

print(df1["Order_Date"].isna().sum())


# 16. Convert invalid values in Order_Date into missing
#     datetime values.

print(" ===== Solution 16 =====")

df1["Order_Date"] = pd.to_datetime(
    df1["Order_Date"],
    format="mixed",
    errors="coerce"
)

print(df1["Order_Date"])

# 17. Find all rows where Unit_Price is missing.

print(" ===== Solution 17 =====")

print(df1[df1["Unit_Price"].isna()])


# 18. Find all rows where Quantity is missing.

print(" ===== Solution 18 =====")

print(df1[df1["Quantity"].isna()])

# 19. Remove rows where Order_ID is missing.

print(" ===== Solution 19 =====")

print(df1.dropna(subset=["Order_ID"]))

# 20. Remove columns that contain at least one missing value.

print(" ===== Solution 20 =====")

print(df1.dropna(axis=1))

# ============================================================
# LEVEL 3 — DATA TYPE CLEANING
# ============================================================

# 21. Convert the Age column into a numeric data type.
#     Any value that cannot be converted should become
#     a missing value.

print(" ===== Solution 21 =====")

print(df1.dtypes)


# 22. After converting Age to numeric, identify all rows
#     where the age is missing.

print(" ===== Solution 22 =====")

print(df1[df1["Age"].isna()])

# 23. Convert the Quantity column into a numeric data type.
#     Any non-numeric value should become a missing value.

print(" ===== Solution 23 =====")

df1["Quantity"] = pd.to_numeric(df1["Quantity"], errors="coerce")
print(df1["Quantity"])
print(df1.dtypes)

# 24. After converting Quantity, identify all rows where
#     the quantity is missing.

print(" ===== Solution 24 =====")

print(df1[df1["Quantity"].isna()])

# 25. Convert the Unit_Price column into a numeric column
#     by removing the ₹ symbol and commas.

print(" ===== Solution 25 =====")

df1["Unit_Price"] = pd.to_numeric(df1["Unit_Price"],errors="coerce")
print(df1.dtypes)

# 26. Convert the Discount column into a numeric percentage value.
#
#     Examples:
#     10% → 10
#     5%  → 5

print(" ===== Solution 26 =====")

df1["Discount"] = pd.to_numeric(
    df1["Discount"].str.replace("%", "", regex=False),
    errors="coerce"
)

print(df1)

# 27. Convert Order_Date into a proper Pandas datetime column.
#     Invalid dates should become missing datetime values.

print(" ===== Solution 27 =====")

print("Already  Done Above")

# 28. Check the data types again after completing the
#     conversions in Questions 21, 23, 25, 26, and 27.

print(" ===== Solution 28 =====")

print(df1.dtypes)

# ============================================================
# LEVEL 4 — TEXT CLEANING
# ============================================================

# 29. Remove unnecessary leading and trailing spaces
#     from the Customer_Name column.

print(" ===== Solution 29 =====")

df1["Customer_Name"] = df1["Customer_Name"].str.strip()

print(df1["Customer_Name"].unique())

# 30. Standardize the capitalization of all customer names
#     so that names follow title-case formatting.
#
#     Examples:
#     rahul sharma → Rahul Sharma
#     AMIT KUMAR   → Amit Kumar

print(" ===== Solution 30 =====")

df1["Customer_Name"] = df1["Customer_Name"].str.title()
print(df1["Customer_Name"].unique())

# 31. Remove unnecessary spaces from the City column.

print(" ===== Solution 31 =====")

df1["City"] = df1["City"].str.strip()
print(df1["City"].unique())

# 32. Standardize the capitalization of the City column.

print(" ===== Solution 32 =====")

df1["City"] = df1["City"].str.title()
df1["City"] = df1["City"].str.replace("Bangalore","Bengaluru")
print(df1["City"].unique())

# 33. Standardize the Gender column so that values use only:
#
#     Male
#     Female
#
#     Convert:
#     M      → Male
#     F      → Female
#     male   → Male
#     female → Female


print(" ===== Solution 33 =====")

df1["Gender"] = df1["Gender"].str.lower().replace({
    "m" : "Male",
    "male" : "Male",
    "f"  : "Female",
    "female" : "Female"
})

print(df1["Gender"].unique())

# 34. Standardize the Payment_Method column so that equivalent
#     values are represented consistently.
#
#     Examples:
#     upi              → UPI
#     credit card      → Credit Card
#     debit card       → Debit Card
#     COD              → Cash on Delivery
#     Cash On Delivery → Cash on Delivery


print(" ===== Solution 34 =====")

df1["Payment_Method"] = df["Payment_Method"]

df1["Payment_Method"] = df1["Payment_Method"].str.lower().replace({
    "upi": "UPI",
    "credit card": "Credit Card",
    "debit card": "Debit Card",
    "cod": "Cash on Delivery",
    "cash on delivery": "Cash on Delivery"
})

print(df1["Payment_Method"].unique())

# 35. Find all unique values in the Product_Category column
#     before cleaning it.

print(" ===== Solution 35 =====")

print(df["Product_Category"].unique())

# 36. Clean the Product_Category column so that equivalent
#     values are represented consistently.
#
#     Examples:
#     Electronics
#     electronics
#     Home & Kitchen
#     HOME & KITCHEN
#     Fashion
#     fashion
#     BEAUTY
#     Beauty


print(" ===== Solution 36 =====")

df1["Product_Category"] = df1["Product_Category"].str.strip().str.lower().str.title()

print(df1["Product_Category"].unique())

# 37. Find all unique values in the Order_Status column
#     before cleaning it.

print(" ===== Solution 37 =====")

print(df1["Order_Status"].unique())


# 38. Standardize Order_Status so that capitalization
#     is consistent.

print(" ===== Solution 38 =====")

df1["Order_Status"] = df1["Order_Status"].str.strip().str.lower().str.title()

print(df1["Order_Status"].unique())

# ============================================================
# LEVEL 5 — INVALID AND SUSPICIOUS DATA
# ============================================================

# 39. Find all customers whose age is below 18.

print(" ===== Solution 39 =====")

print(df1[df1["Age"] < 18])

# 40. Find all customers whose age is greater than 100.

print(" ===== Solution 40 =====")

print(df1[df1["Age"] > 100])

# 41. Replace invalid ages below 0 or above 100
#     with missing values.

print(" ===== Solution 41 =====")

df1.loc[(df1["Age"] < 18) | (df1["Age"] > 100),"Age"] = np.nan
print(df1["Age"].unique())

print(df["Age"])

# 42. Find all orders where Quantity is less than
#     or equal to 0.

print(" ===== Solution 42 =====")

print(df1[df1["Quantity"]<= 0])

# 43. Replace invalid quantities less than or equal to 0
#     with missing values.

print(" ===== Solution 43 =====")


df1.loc[df1["Quantity"]<= 0,"Quantity"] = np.nan

print(df1[df1["Quantity"].isna()])


# 44. Find all orders where Customer_Rating is outside
#     the valid range of 1–5.

print(" ===== Solution 44 =====")

df1.loc[(df1["Customer_Rating"] < 1) | (df1["Customer_Rating"] > 5) ,"Customer_Rating"] = np.nan

print(df1["Customer_Rating"].unique())

# 45. Find all rows where Order_Status is Cancelled.

print(" ===== Solution 45 =====")

print(df1[df1["Order_Status"] == "Cancelled"])

# ============================================================
# LEVEL 6 — DUPLICATE AND RECORD CLEANING
# ============================================================

# 46. Remove exact duplicate rows from the DataFrame.

print(" ===== Solution 46 =====")

print(df1.drop_duplicates())

# 47. Check whether duplicate Order_ID values exist
#     in the DataFrame.

print(" ===== Solution 47 =====")

print(df[df.duplicated(subset="Order_ID")])

# 48. Display all rows where the combination of
#     Customer_Name, City, and Unit_Price appears
#     more than once.

print(" ===== Solution 48 =====")

print(df[df.duplicated(subset=["Customer_Name", "City","Unit_Price"])])

# 49. After cleaning the relevant columns, check whether
#     duplicate customer/order records exist that should
#     be removed.

print(" ===== Solution 49 =====")

print(df.duplicated().sum())

# 50. Create a final cleaned DataFrame by applying all
#     necessary cleaning steps from Questions 11–49.
#
#     Then display:
#
#     - Number of rows
#     - Number of columns
#     - Missing values per column
#     - Duplicate row count
#     - Data types
#     - Unique values for categorical columns

print(" ===== Solution 50 =====")

print("\nNumber of rows:")
print(df1.shape[0])

print("\nNumber of columns:")
print(df1.shape[1])

print("\nMissing values per column:")
print(df1.isna().sum())

print("\nDuplicate row count:")
print(df1.duplicated().sum())

print("\nData types:")
print(df1.dtypes)

print("\nUnique values for categorical columns:")

categorical_columns = df1.select_dtypes(include="object").columns

for column in categorical_columns:
    print(f"\n{column}:")
    print(df1[column].unique())