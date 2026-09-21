# Customer Churn Analysis

## 📌 Project Overview

This project analyzes customer churn using Python and Pandas to understand **which customer, subscription, and support-related factors are associated with customer churn**.

The analysis combines customer, subscription, and support information, followed by data cleaning, feature engineering, exploratory data analysis, and visualization.

The project focuses on answering questions such as:

* Which customers are churning?
* How does churn vary by plan type and contract type?
* What customer characteristics are associated with churn?
* Is there a relationship between churn and customer support activity?
* What are the common reasons customers cancel their subscriptions?
* How do churn score and churn risk relate to actual churn?

---

## 🎯 Business Objective

Customer churn directly affects recurring revenue and customer lifetime value.

The objective of this analysis is to identify **patterns and characteristics associated with customer churn** so that a business can better understand potential retention issues and investigate areas such as:

* Subscription plans
* Contract types
* Customer tenure
* Monthly charges
* Customer lifetime value (CLTV)
* Customer satisfaction
* Complaints and escalations
* Churn score and churn risk
* Cancellation reasons

---

## 📂 Dataset

The project works with customer, subscription, and support-related data.

The final analytical dataset contains fields such as:

* `customerid`
* `subscription_start_date`
* `subscription_type`
* `renewal_date`
* `plan_type`
* `contract_type`
* `cancellation_date`
* `cancellation_reason`
* `monthly_charges`
* `cltv`
* `churn_score`
* `Churn_Flag`
* `customer_name`
* `country`
* `state`
* `gender`
* `dob`
* `complaint_date`
* `escalations`
* `csat_score`
* `complaint_count`
* `age`
* `tenure_days`
* `churn_risk`
* `cancellation_month`

These variables were used to analyze customer behavior, subscription characteristics, support interactions, and churn patterns.

---

## 🛠️ Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## 🔄 Project Workflow

### 1. Data Preparation

The project begins by working with separate customer, subscription, and support data.

The tables are combined using customer identifiers to create a consolidated dataset for analysis.

A `Churn_Flag` was also created based on whether a customer had a cancellation date:

```python
df_db_subscription['Churn_Flag'] = np.where(
    df_db_subscription['cancellation_date'].notna(),
    1,
    0
)
```

This converts the cancellation information into a binary churn indicator:

* `1` → Customer churned
* `0` → Customer did not churn

---

### 2. Data Cleaning

The data-cleaning process included:

* Renaming columns
* Removing unnecessary columns
* Converting date columns to appropriate date types
* Standardizing categorical values
* Handling missing values
* Checking country/state consistency
* Investigating discrepancies after joining tables

For example, unnecessary fields such as `interests` and `pincode` were removed from the customer table.

The project also identified a row-count discrepancy after joining the tables and investigated the underlying data rather than assuming the join was correct.

---

## 🧮 Feature Engineering

Additional analytical features were created to support the churn analysis.

### Churn Flag

A binary `Churn_Flag` was created from the cancellation date.

### Age

Customer age was derived from the date of birth.

### Tenure

Customer tenure was calculated using subscription-related dates.

### Churn Risk

Customers were categorized into:

* Low
* Medium
* High

The dataset contains these three churn-risk categories.

### Cancellation Month

Cancellation dates were transformed into a month-level field to support temporal churn analysis.

---

## 📊 Exploratory Data Analysis

The project uses visual analysis to investigate churn across different customer segments.

### Churn by Plan Type

The analysis calculates churn by:

* Basic
* Standard
* Premium

This helps compare churn behavior across subscription plans.

```python
churn_plan = df_visual.groupby('plan_type')['Churn_Flag'].mean()
```

### Churn by Contract Type

Contract type was also analyzed to compare churn behavior between:

* Monthly
* Annual

### Churn Risk Analysis

The analysis examines how the predefined churn-risk categories relate to actual churn.

### Customer Support Analysis

Support-related variables such as:

* `complaint_count`
* `escalations`
* `csat_score`

were included to investigate the relationship between customer experience and churn.

The support data also contained multiple records for the same customer, including different escalation statuses and CSAT scores, which required attention during data preparation.

---

## 🔥 Cancellation Reason Analysis

The dataset contains several cancellation reasons, including:

* Switched to competitor
* Too expensive
* Not enough content
* Poor streaming quality
* Forgot to cancel trial

These categories were analyzed to understand the reasons behind customer cancellations.

---

## 📈 Correlation Analysis

A correlation heatmap was created to examine relationships between numerical variables and appropriately encoded categorical variables.

The analysis initially used automatic categorical encoding:

```python
df_encode[col] = df_encode[col].astype('category').cat.codes
```

This was then improved by explicitly defining category order:

```python
order_mappings = {
    'plan_type': ['Basic', 'Standard', 'Premium'],
    'contract_type': ['Monthly', 'Annual'],
    'churn_risk': ['Low', 'Medium', 'High']
}
```

This ensures that ordinal categories such as churn risk are represented according to their intended business order rather than relying on automatically assigned category codes.

### Important analytical consideration

Categorical encoding should not automatically be interpreted as a numerical measurement.

For example, assigning:

```text
Low → 0
Medium → 1
High → 2
```

is meaningful when the categories have an inherent order.

However, converting a nominal category into numbers does not automatically make Pearson correlation statistically appropriate. Therefore, the heatmap is treated as an exploratory analysis rather than definitive evidence of causation.

---

## 🔍 Key Analytical Areas

The project investigates relationships between churn and:

| Area                | Variables                                         |
| ------------------- | ------------------------------------------------- |
| Subscription        | `plan_type`, `contract_type`, `subscription_type` |
| Customer Value      | `monthly_charges`, `cltv`                         |
| Customer Profile    | `age`, `gender`, `state`, `country`               |
| Engagement          | `tenure_days`                                     |
| Customer Experience | `csat_score`, `complaint_count`                   |
| Support             | `escalations`                                     |
| Churn               | `Churn_Flag`, `churn_score`, `churn_risk`         |
| Cancellation        | `cancellation_reason`, `cancellation_month`       |

---

## 💡 Business Questions Answered

The analysis is structured around practical business questions:

1. What proportion of customers have churned?
2. How does churn vary across subscription plans?
3. How does churn differ between monthly and annual contracts?
4. Which cancellation reasons appear most frequently?
5. How does customer tenure relate to churn?
6. Is customer satisfaction associated with churn?
7. Are complaints and escalations associated with churn?
8. How does the existing churn-risk classification compare with the actual churn flag?
9. What customer characteristics should be investigated further for retention analysis?

---

## 🧠 Key Learning Outcomes

This project helped strengthen practical Data Analyst skills in:

* Data cleaning with Pandas
* Working with multiple related tables
* Investigating join discrepancies
* Handling missing values
* Date transformation
* Feature engineering
* GroupBy analysis
* Churn-rate calculation
* Categorical encoding
* Exploratory Data Analysis
* Correlation analysis
* Data visualization
* Translating analytical results into business questions

---

## ⚠️ Analytical Limitations

This project is an **exploratory churn analysis**, not a production churn prediction model.

Correlation does not establish causation.

Also, converting categorical variables into numeric codes solely to calculate a correlation matrix can introduce assumptions about category order and spacing. For future analysis, categorical-specific statistical methods could be used where appropriate.

The results should therefore be interpreted as **patterns and associations in the dataset**, rather than proof that a particular factor causes customer churn.

---

## 🚀 Future Improvements

Possible next steps include:

* Building a Power BI churn dashboard
* Creating customer-segment level churn analysis
* Performing statistical tests for categorical variables
* Building a churn prediction model
* Comparing model performance using precision, recall, and ROC-AUC
* Identifying high-value customers at risk of churn
* Developing a customer retention strategy based on analytical findings

---

## 📁 Project Structure

```text
Customer-Churn-Analysis/
│
├── Customer_Churn.ipynb
├── README.md
├── data/
│   └── customer_churn_data.csv
│
└── images/
    ├── churn_by_plan.png
    ├── churn_by_contract.png
    ├── churn_by_risk.png
    └── correlation_heatmap.png
```

---

## 👩‍💻 Skills Demonstrated

**Python | Pandas | NumPy | Matplotlib | Seaborn | Data Cleaning | Feature Engineering | EDA | Data Visualization | Business Analysis | Customer Churn Analysis**
