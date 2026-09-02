## 📊 Matplotlib Intro — Practice Questions

This folder contains **40 hands-on practice questions** designed to build a strong foundation in **Matplotlib** for Data Analytics.

The exercises focus entirely on writing Python code and creating visualizations. No theoretical questions are included.

---

## 🎯 Objective

The purpose of these exercises is to develop practical skills in:

* Creating basic charts with Matplotlib
* Working with X-axis and Y-axis data
* Creating line charts
* Creating bar charts
* Creating scatter plots
* Creating histograms
* Creating pie charts
* Adding titles and axis labels
* Adding legends and gridlines
* Customizing lines and markers
* Changing figure size
* Saving charts as image files
* Visualizing multiple datasets on the same chart

---

## 🛠️ Requirements

Make sure Python and Matplotlib are installed.

### Install Matplotlib

```bash
pip install matplotlib
```

### Import Matplotlib

```python
import matplotlib.pyplot as plt
```

---

## 📚 Topics Covered

### 1. Basic Line Charts

Practice:

```python
plt.plot()
```

Exercises include:

* Monthly sales
* Monthly revenue
* Website visitors
* Temperature
* Monthly expenses

---

### 2. Line Chart Customization

Practice:

```python
plt.plot(
    x,
    y,
    color="red",
    marker="o",
    linewidth=2,
    linestyle="--"
)
```

Exercises cover:

* Line colors
* Markers
* Line width
* Line styles
* Gridlines
* Chart titles
* Axis labels

---

### 3. Bar Charts

Practice:

```python
plt.bar(x, y)
```

Exercises include:

* Product sales
* Customers by city
* Employees by department
* Product quantities
* Revenue by category

---

### 4. Scatter Plots

Practice:

```python
plt.scatter(x, y)
```

Exercises include relationships between:

* Age and salary
* Study hours and exam scores
* Advertising spend and sales
* Experience and salary
* Working hours and productivity

---

### 5. Histograms

Practice:

```python
plt.hist(data)
```

Exercises include distributions of:

* Ages
* Salaries
* Exam scores
* Order values
* Customer ages

---

### 6. Pie Charts

Practice:

```python
plt.pie(values, labels=labels)
```

Exercises include:

* Sales distribution
* Expense distribution
* Market share
* Customers by city
* Product sales

Percentage labels are also practiced using:

```python
autopct="%1.1f%%"
```

---

### 7. Multiple Lines

Practice plotting multiple datasets on the same chart:

```python
plt.plot(months, sales_2025, label="2025")
plt.plot(months, sales_2026, label="2026")

plt.legend()
```

Exercises include comparisons between:

* Sales in 2025 vs 2026
* Company revenue
* Website traffic
* Product orders
* Profit across years

---

### 8. Figure Size and Saving Charts

Practice:

```python
plt.figure(figsize=(10, 5))
```

and:

```python
plt.savefig("chart.png")
```

---

## 📈 Matplotlib Functions Practiced

| Function        | Purpose                 |
| --------------- | ----------------------- |
| `plt.plot()`    | Create a line chart     |
| `plt.bar()`     | Create a bar chart      |
| `plt.scatter()` | Create a scatter plot   |
| `plt.hist()`    | Create a histogram      |
| `plt.pie()`     | Create a pie chart      |
| `plt.title()`   | Add a chart title       |
| `plt.xlabel()`  | Label the X-axis        |
| `plt.ylabel()`  | Label the Y-axis        |
| `plt.legend()`  | Display a legend        |
| `plt.grid()`    | Add gridlines           |
| `plt.figure()`  | Control figure settings |
| `plt.savefig()` | Save a chart            |
| `plt.show()`    | Display a chart         |

---

## 🧠 Practice Structure

The 40 questions are divided into levels:

| Level   | Topic                       | Questions |
| ------- | --------------------------- | --------: |
| Level 1 | Basic Line Charts           |       1–5 |
| Level 2 | Line Chart Customization    |      6–10 |
| Level 3 | Bar Charts                  |     11–15 |
| Level 4 | Scatter Plots               |     16–20 |
| Level 5 | Histograms                  |     21–25 |
| Level 6 | Pie Charts                  |     26–30 |
| Level 7 | Multiple Lines & Legends    |     31–35 |
| Level 8 | Figure Size & Saving Charts |     36–38 |
| Level 9 | Combination Practice        |     39–40 |

---

## 📁 Suggested Folder Structure

```text
matplotlib-intro/
│
├── README.md
│
├── matplotlib_intro_practice.py
│
└── charts/
    ├── monthly_sales.png
    └── other_generated_charts.png
```

---

## 🚀 How to Practice

Open:

```text
matplotlib_intro_practice.py
```

The file contains all **40 questions**.

For each question:

1. Read the dataset.
2. Understand what visualization is required.
3. Write the Matplotlib code.
4. Run the code.
5. Inspect the resulting chart.
6. Move to the next question.

The goal is to **write the code yourself rather than simply copy a solution**.

---

## 💼 Data Analyst Connection

Matplotlib is particularly useful when you need to convert analytical results into visual insights.

A typical Data Analyst workflow can look like:

```text
Dataset
   ↓
Pandas
   ↓
Data Cleaning
   ↓
Data Analysis
   ↓
Business Questions
   ↓
Analytical Results
   ↓
Matplotlib
   ↓
Visualization
   ↓
Business Insights
```

For example:

```python
monthly_sales = df.groupby("Month")["Sales"].sum()
```

After calculating the monthly sales with Pandas, Matplotlib can be used to visualize the result:

```python
plt.plot(monthly_sales.index, monthly_sales.values)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()
```

This is how visualization becomes part of a real Data Analytics workflow.

---

## 📌 Key Mental Model

When deciding which chart to create, start with the **business question**, not the Matplotlib function.

```text
TIME → TREND
        ↓
    Line Chart
```

```text
CATEGORY → COMPARISON
             ↓
         Bar Chart
```

```text
NUMBER vs NUMBER → RELATIONSHIP
                     ↓
                Scatter Plot
```

```text
NUMBER → DISTRIBUTION
           ↓
       Histogram
```

```text
PART → WHOLE
        ↓
    Pie Chart
```

This mental model will help when you eventually work with real-world datasets.

---

## 🎓 Learning Goal

After completing these exercises, you should be comfortable with the basic Matplotlib workflow:

```python
import matplotlib.pyplot as plt

plt.figure()

plt.plot(x, y)

plt.title("Chart Title")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.grid()
plt.legend()

plt.show()
```

You should also be able to choose and create basic:

* Line charts
* Bar charts
* Scatter plots
* Histograms
* Pie charts

and customize them with titles, labels, markers, line styles, legends, gridlines, and figure sizes.

---

## 🔜 Next Step

After completing these 40 exercises, the next Matplotlib topics to practice are:

* Subplots
* Multiple charts
* Figure and Axes
* Tick customization
* Annotations
* Text on charts
* Advanced formatting
* Working with Pandas DataFrames
* Real-world Data Analyst visualizations
* Business-focused dashboards

---

## 📜 License

This practice material is intended for learning and educational purposes.
