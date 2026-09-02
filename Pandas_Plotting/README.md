## 📊 Matplotlib Labelling & Pandas Plotting — Python Practice

This section is part of my **Python for Data Analytics** learning journey.

The purpose of these exercises is to build practical understanding of **Matplotlib labelling** and **Pandas plotting**, with a focus on creating clear and meaningful data visualizations.

---

## 📚 Topics Covered

### Matplotlib Labelling

* `plt.title()`
* `plt.xlabel()`
* `plt.ylabel()`
* `plt.legend()`
* `plt.grid()`
* `plt.annotate()`
* `plt.xticks()`
* Title positioning
* Font size customization
* Axis label customization
* Legend positioning
* Data-point annotations
* Rotating axis labels

### Pandas Plotting

* `df.plot()`
* `df.plot(x=..., y=...)`
* Line plots
* Bar charts
* Horizontal bar charts
* Histograms
* Box plots
* Scatter plots
* Pie charts
* Area charts
* Plotting multiple columns
* Figure size customization

### Combining Pandas and Matplotlib

The exercises also demonstrate how Pandas and Matplotlib work together:

```text
Pandas DataFrame
       ↓
   df.plot()
       ↓
   Matplotlib
       ↓
Customize the chart
       ↓
   Final Visualization
```

---

# 🎯 Learning Objectives

After completing these exercises, I should be able to:

* Create basic visualizations using Matplotlib.
* Add meaningful titles to charts.
* Label X and Y axes correctly.
* Add and position legends.
* Add grids to improve readability.
* Annotate important data points.
* Rotate axis labels.
* Control figure size.
* Create visualizations directly from Pandas DataFrames.
* Select specific DataFrame columns for visualization.
* Choose appropriate chart types for different analytical situations.
* Plot multiple data series.
* Combine Pandas plotting with Matplotlib customization.
* Create charts similar to those used in real-world Data Analyst projects.

---

# 🧠 Visualization Logic

Creating a chart is not just about knowing Python syntax.

The basic thought process is:

```text
What question am I trying to answer?
              ↓
Which columns contain the required information?
              ↓
Which chart type is appropriate?
              ↓
Which column belongs on the X-axis?
              ↓
Which column belongs on the Y-axis?
              ↓
What title and labels explain the chart?
              ↓
Are there important points that should be highlighted?
              ↓
Final Visualization
```

For example:

If the question is:

> How are sales changing every month?

The thought process would be:

```text
Question
   ↓
Monthly Sales Trend
   ↓
Columns → Month + Sales
   ↓
Chart → Line Chart
   ↓
X-axis → Month
Y-axis → Sales
   ↓
Add title, labels and grid
```

---

# 📝 Practice Questions

This section contains **40 hands-on coding exercises**.

The questions progress from beginner-level Matplotlib labelling to practical Data Analyst-style visualization tasks.

### Level 1 — Matplotlib Labelling

**Questions 1–10**

Practice:

* Titles
* X-axis labels
* Y-axis labels
* Grid
* Font sizes
* Title positioning
* Rotating labels
* Annotations

### Level 2 — Legends & Multiple Data Series

**Questions 11–15**

Practice:

* Multiple lines
* `label`
* `plt.legend()`
* Legend positioning
* Comparing multiple data series

### Level 3 — Pandas Plotting Basics

**Questions 16–20**

Practice:

* Creating DataFrames
* `df.plot()`
* Line plots
* Bar charts
* Horizontal bar charts

### Level 4 — Pandas Plotting + Labelling

**Questions 21–27**

Practice:

* Pandas plots with Matplotlib labels
* Multiple columns
* Figure size
* Grid
* Rotated labels
* Sales and revenue visualizations

### Level 5 — Distribution Visualizations

**Questions 28–30**

Practice:

* Histograms
* Box plots
* Understanding numerical distributions

### Level 6 — Scatter Plots

**Questions 31–33**

Practice:

* Scatter plots
* Relationships between variables
* Adding titles and labels
* Using grids

### Level 7 — Real Data Analyst-Style Problems

**Questions 34–40**

Practice:

* Sales analysis
* Revenue analysis
* Regional performance
* Website visitors
* Orders
* Profit
* Expenses
* Year-over-year comparison
* Highlighting important business values

---

# 🛠️ Technologies Used

```text
Python
Pandas
Matplotlib
```

Import libraries:

```python
import pandas as pd
import matplotlib.pyplot as plt
```

---

# 📌 Important Matplotlib Commands

## Title

```python
plt.title("Monthly Sales")
```

## X-axis Label

```python
plt.xlabel("Month")
```

## Y-axis Label

```python
plt.ylabel("Sales")
```

## Grid

```python
plt.grid()
```

## Legend

```python
plt.legend()
```

## Annotation

```python
plt.annotate("Highest Sales", xy=(x, y))
```

## Rotate X-axis Labels

```python
plt.xticks(rotation=45)
```

---

# 📌 Important Pandas Plotting Commands

### Line Plot

```python
df.plot(
    x="Month",
    y="Sales",
    kind="line"
)
```

### Bar Chart

```python
df.plot(
    x="Month",
    y="Sales",
    kind="bar"
)
```

### Horizontal Bar Chart

```python
df.plot(
    x="Month",
    y="Sales",
    kind="barh"
)
```

### Histogram

```python
df["Sales"].plot(
    kind="hist"
)
```

### Box Plot

```python
df["Sales"].plot(
    kind="box"
)
```

### Scatter Plot

```python
df.plot(
    x="Advertising",
    y="Sales",
    kind="scatter"
)
```

### Pie Chart

```python
df["Sales"].plot(
    kind="pie"
)
```

### Area Chart

```python
df.plot(
    x="Month",
    y="Sales",
    kind="area"
)
```

---

# 🔗 Pandas + Matplotlib Workflow

A common Data Analyst workflow is:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

df.plot(
    x="Month",
    y="Sales",
    kind="line",
    figsize=(10, 5)
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()

plt.show()
```

Here:

* **Pandas** handles the DataFrame and plotting setup.
* **Matplotlib** helps customize the visualization.
* The final chart communicates the pattern in the data.

---

# 📈 Why This Matters for Data Analytics

Data Analysts frequently work with datasets containing thousands or millions of records.

Looking at raw numbers is often difficult.

Visualization makes patterns easier to identify.

For example:

```text
January     10,000
February    12,000
March       11,000
April       15,000
May         18,000
```

A line chart can make the overall trend immediately visible.

This can help identify:

* Growth
* Decline
* Seasonality
* Sudden changes
* Outliers
* Performance differences
* Relationships between variables

The ultimate objective is not simply to create a graph.

It is to use visualization to **find and communicate meaningful insights from data**.

---

# 🚀 Learning Progress

This practice set is part of my broader **Python for Data Analytics** learning path.

Current visualization skills:

* [x] Matplotlib Introduction
* [x] Matplotlib Plotting
* [x] Matplotlib Labelling
* [x] Pandas Plotting
* [ ] Advanced Matplotlib
* [ ] Seaborn
* [ ] Advanced Data Visualization
* [ ] Data Visualization Projects

---

# 📂 Suggested Folder Structure

```text
python-for-data-analytics/
│
├── Matplotlib/
│   │
│   ├── 01_Matplotlib_Introduction/
│   ├── 02_Matplotlib_Plotting/
│   ├── 03_Matplotlib_Labelling/
│   └── 04_Pandas_Plotting/
│
└── README.md
```

---

# 🎯 Goal

The goal of these exercises is to move from:

```text
Learning Syntax
      ↓
Understanding Logic
      ↓
Writing Code
      ↓
Creating Visualizations
      ↓
Interpreting Data
      ↓
Communicating Business Insights
```

This is an important step toward using Python effectively as a **Data Analyst**.
