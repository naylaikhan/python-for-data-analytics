# Seaborn Practice — 60 Data Visualization Exercises

This repository contains **60 hands-on Seaborn practice questions** designed to build practical visualization skills for **Data Analysis**.

The exercises use the **IBM HR Analytics Employee Attrition & Performance** dataset from Kaggle. The dataset contains employee demographics, job information, compensation, satisfaction scores, work-life information, and attrition data.

The goal is not just to learn Seaborn syntax, but to develop the ability to look at a dataset, understand the analytical question, and choose an appropriate visualization.

---

## 📊 Dataset

### IBM HR Analytics Employee Attrition & Performance

**Source:** Kaggle

**Dataset Link:**

https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset

The dataset contains **1,470 employee records and 35 columns**.

Some important columns include:

```text
Age
Attrition
BusinessTravel
DailyRate
Department
DistanceFromHome
Education
EducationField
EmployeeNumber
EnvironmentSatisfaction
Gender
JobInvolvement
JobLevel
JobRole
JobSatisfaction
MaritalStatus
MonthlyIncome
MonthlyRate
NumCompaniesWorked
OverTime
PercentSalaryHike
PerformanceRating
RelationshipSatisfaction
StockOptionLevel
TotalWorkingYears
TrainingTimesLastYear
WorkLifeBalance
YearsAtCompany
YearsInCurrentRole
YearsSinceLastPromotion
YearsWithCurrManager
```

---

# 🎯 Learning Objectives

By completing these exercises, I aim to develop the ability to:

* Create different types of Seaborn visualizations
* Work with Pandas DataFrames and Seaborn
* Understand numerical and categorical variables
* Compare categories using visualizations
* Analyze distributions
* Identify potential outliers
* Analyze relationships between numerical variables
* Use `hue` for group comparisons
* Understand correlation
* Create correlation heatmaps
* Use pair plots
* Create regression plots
* Use Seaborn for Exploratory Data Analysis (EDA)
* Select an appropriate visualization based on an analytical question
* Translate visual patterns into business insights

---

# 🛠️ Technologies Used

* Python
* Pandas
* Seaborn
* Matplotlib
* Jupyter Notebook / VS Code

---

# 📚 Topics Covered

### Basic Seaborn

* Importing Seaborn
* Working with Pandas DataFrames
* `data=`
* `x=`
* `y=`
* Seaborn themes

### Statistical Visualizations

* Line plots
* Scatter plots
* Bar plots
* Count plots
* Histograms
* KDE
* Box plots
* Violin plots
* Strip plots
* Swarm plots

### Advanced Visualization

* `hue`
* `size`
* `style`
* `palette`
* Category ordering
* Faceting
* Pair plots
* Regression plots
* Heatmaps
* Correlation matrices

### Data Analysis

* Distribution analysis
* Group comparison
* Outlier detection
* Correlation analysis
* Relationship analysis
* Exploratory Data Analysis
* Business-oriented visualization

---

# 📁 Suggested Repository Structure

```text
seaborn-practice/
│
├── README.md
│
├── dataset/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
│
├── notebooks/
│   └── seaborn_practice.ipynb
│
└── solutions/
    └── seaborn_solutions.py
```

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone <your-repository-url>
```

## 2. Install Required Libraries

```bash
pip install pandas seaborn matplotlib
```

## 3. Import the Libraries

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
```

## 4. Load the Dataset

```python
df = pd.read_csv("dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv")
```

## 5. Inspect the Dataset

```python
print(df.head())
print(df.shape)
print(df.info())
```

---

# 📝 Practice Questions

## Level 1 — Getting Comfortable with Seaborn

### 1.

Create a count plot showing the number of employees in each `Department`.

### 2.

Create a count plot showing the number of employees in each `JobRole`.

### 3.

Create a histogram showing the distribution of employee `Age`.

### 4.

Create a histogram showing the distribution of `MonthlyIncome`.

### 5.

Create a histogram of `TotalWorkingYears`.

### 6.

Create a histogram of `DistanceFromHome`.

### 7.

Create a count plot showing the number of employees who stayed and left the company based on `Attrition`.

### 8.

Create a count plot showing the number of employees in each `BusinessTravel` category.

### 9.

Create a count plot showing the number of employees in each `MaritalStatus` category.

### 10.

Create a count plot showing the number of employees in each `EducationField`.

---

# Level 2 — Comparing Numerical Data

### 11.

Create a box plot showing the distribution of `MonthlyIncome`.

### 12.

Create a box plot showing the distribution of `Age`.

### 13.

Create a box plot showing the distribution of `DistanceFromHome`.

### 14.

Create a box plot comparing `MonthlyIncome` across different `Departments`.

### 15.

Create a box plot comparing `MonthlyIncome` across different `JobRoles`.

### 16.

Create a box plot comparing `Age` across different `JobRoles`.

### 17.

Create a box plot comparing `TotalWorkingYears` across different `Departments`.

### 18.

Create a box plot comparing `YearsAtCompany` across different `JobRoles`.

### 19.

Create a box plot comparing `MonthlyIncome` between employees who stayed and employees who left.

### 20.

Create a box plot comparing `YearsAtCompany` between employees who stayed and employees who left.

---

# Level 3 — Scatter Plots and Relationships

### 21.

Create a scatter plot showing the relationship between `Age` and `MonthlyIncome`.

### 22.

Create a scatter plot showing the relationship between `TotalWorkingYears` and `MonthlyIncome`.

### 23.

Create a scatter plot showing the relationship between `YearsAtCompany` and `MonthlyIncome`.

### 24.

Create a scatter plot showing the relationship between `DistanceFromHome` and `MonthlyIncome`.

### 25.

Create a scatter plot showing the relationship between `YearsInCurrentRole` and `MonthlyIncome`.

### 26.

Create a scatter plot showing the relationship between `YearsSinceLastPromotion` and `MonthlyIncome`.

### 27.

Create a scatter plot showing the relationship between `YearsWithCurrManager` and `MonthlyIncome`.

### 28.

Create a scatter plot between `TotalWorkingYears` and `YearsAtCompany`.

### 29.

Create a scatter plot showing `Age` against `MonthlyIncome`, while visually separating employees according to `Attrition`.

### 30.

Create a scatter plot showing `TotalWorkingYears` against `MonthlyIncome`, while visually separating employees according to `JobLevel`.

---

# Level 4 — Using `hue` for Group Comparisons

### 31.

Create a box plot of `MonthlyIncome` by `Department`, while separating the employees according to `Attrition`.

### 32.

Create a box plot of `MonthlyIncome` by `JobRole`, while separating employees according to `Attrition`.

### 33.

Create a box plot of `Age` by `JobRole`, while separating employees according to `Attrition`.

### 34.

Create a box plot of `DistanceFromHome` by `Department`, while separating employees according to `Attrition`.

### 35.

Create a count plot showing `JobRole`, with the bars separated according to `Attrition`.

### 36.

Create a count plot showing `BusinessTravel`, with the bars separated according to `Attrition`.

### 37.

Create a count plot showing `OverTime`, with the bars separated according to `Attrition`.

### 38.

Create a count plot showing `JobSatisfaction`, with the bars separated according to `Attrition`.

### 39.

Create a count plot showing `WorkLifeBalance`, with the bars separated according to `Attrition`.

### 40.

Create a count plot showing `JobInvolvement`, with the bars separated according to `Attrition`.

---

# Level 5 — Distribution Analysis

### 41.

Create a distribution plot of `MonthlyIncome` and display a smooth density curve along with the histogram.

### 42.

Create a distribution plot of `Age` and display a smooth density curve.

### 43.

Create separate salary distributions for employees who stayed and employees who left, using `Attrition` to distinguish the groups.

### 44.

Compare the distributions of `TotalWorkingYears` between employees who stayed and employees who left.

### 45.

Compare the distributions of `DistanceFromHome` between employees who stayed and employees who left.

### 46.

Create separate distributions of `MonthlyIncome` for each `Department`.

### 47.

Create separate distributions of `Age` for each `Department`.

### 48.

Create separate distributions of `MonthlyIncome` for each `JobLevel`.

### 49.

Create a violin plot comparing `MonthlyIncome` across the different `JobLevels`.

### 50.

Create a violin plot comparing `MonthlyIncome` across `JobRoles`, while distinguishing employees according to `Attrition`.

---

# Level 6 — Correlation and Heatmaps

### 51.

Select the numerical columns from the dataset and create a correlation matrix.

Visualize the correlation matrix using a Seaborn heatmap.

### 52.

Create a heatmap of the numerical correlation matrix and display the correlation values inside the cells.

### 53.

Create a correlation heatmap containing only:

```text
Age
MonthlyIncome
TotalWorkingYears
YearsAtCompany
YearsInCurrentRole
YearsSinceLastPromotion
YearsWithCurrManager
DistanceFromHome
```

### 54.

Using the correlation matrix, identify the numerical variable that has the strongest positive correlation with `MonthlyIncome`.

Create an appropriate visualization to examine that relationship.

### 55.

Examine the relationship between `YearsAtCompany` and `YearsWithCurrManager`.

Create an appropriate Seaborn visualization to investigate the relationship.

---

# Level 7 — Advanced Seaborn Practice

### 56.

Create a pair plot using:

```text
Age
MonthlyIncome
TotalWorkingYears
YearsAtCompany
YearsInCurrentRole
```

Use `Attrition` to distinguish the employee groups.

### 57.

Create a pair plot using:

```text
Age
MonthlyIncome
JobLevel
TotalWorkingYears
YearsAtCompany
```

Visually separate observations according to `Attrition`.

### 58.

Create a regression plot showing the relationship between `TotalWorkingYears` and `MonthlyIncome`.

### 59.

Create a regression plot showing the relationship between `Age` and `MonthlyIncome`.

---

# Level 8 — Business Analysis Challenge

### 60.

The HR department wants to understand **why employees may be leaving the organization**.

Using Seaborn, create a visual analysis containing multiple appropriate charts that investigate the relationship between `Attrition` and:

```text
OverTime
JobSatisfaction
JobInvolvement
WorkLifeBalance
BusinessTravel
JobLevel
MonthlyIncome
DistanceFromHome
YearsAtCompany
JobRole
```

Your visual analysis should allow an HR manager to compare employees who stayed versus employees who left and identify potentially important patterns in the data.

---

# 🧠 Visualization Decision Framework

The main goal of this practice is not simply to memorize Seaborn functions.

Before creating a chart, ask:

```text
What question am I trying to answer?
            ↓
What type of variables do I have?
            ↓
Numerical / Categorical / Time
            ↓
What am I trying to understand?
            ↓
Count / Comparison / Distribution /
Relationship / Correlation
            ↓
Choose the appropriate visualization
            ↓
Look for patterns
            ↓
Convert patterns into insights
```

---

# 📊 Quick Visualization Reference

| Analytical Question                                       | Visualization   |
| --------------------------------------------------------- | --------------- |
| How many observations are in each category?               | Count Plot      |
| How does something change over time?                      | Line Plot       |
| What is the relationship between two numerical variables? | Scatter Plot    |
| How does a numerical value compare across categories?     | Bar Plot        |
| What is the distribution of a numerical variable?         | Histogram       |
| Are there potential outliers?                             | Box Plot        |
| How do distributions differ between groups?               | Violin Plot     |
| Show individual observations                              | Strip Plot      |
| Show individual observations with reduced overlap         | Swarm Plot      |
| How strongly are numerical variables related?             | Heatmap         |
| Explore relationships among many numerical variables      | Pair Plot       |
| Investigate a linear relationship                         | Regression Plot |

---

# 🔍 Skills Practiced

After completing these exercises, I should be comfortable with:

```python
sns.lineplot()
sns.scatterplot()
sns.barplot()
sns.countplot()
sns.histplot()
sns.boxplot()
sns.violinplot()
sns.stripplot()
sns.swarmplot()
sns.heatmap()
sns.pairplot()
sns.regplot()
sns.relplot()
sns.displot()
sns.catplot()
```

And important Seaborn parameters such as:

```python
data=
x=
y=
hue=
size=
style=
palette=
order=
col=
row=
bins=
kde=
annot=
```

---

# 💼 Data Analyst Perspective

The purpose of these exercises is to develop the following workflow:

```text
Dataset
   ↓
Understand the data
   ↓
Identify variables
   ↓
Ask an analytical question
   ↓
Select visualization
   ↓
Create visualization
   ↓
Identify patterns
   ↓
Investigate unusual findings
   ↓
Generate business insights
```

A good Data Analyst should not create visualizations simply because they are visually appealing.

Every visualization should answer a question or communicate something useful.

---

# 📌 Project Goal

This project is part of my **Python for Data Analytics** learning journey.

The focus is on developing practical skills in:

* Data Visualization
* Exploratory Data Analysis
* Statistical Thinking
* Business Analysis
* Python
* Seaborn
* Pandas
* Matplotlib

The ultimate objective is to become capable of taking a real-world dataset and independently performing meaningful exploratory analysis.
