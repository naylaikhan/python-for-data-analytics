## Python Dictionaries - Practice Exercises

A hands-on Python practice set designed to build a strong understanding of Dictionaries through progressively challenging exercises.

This repository contains 50 practice questions, starting with basic dictionary operations and gradually moving toward logic-building and Data Analyst–style problems.

📚 Topics Covered

The exercises cover:

Creating dictionaries
Dictionary key-value pairs
Accessing values
Adding new key-value pairs
Updating existing values
Removing dictionary items
pop()
popitem()
del
clear()
len()
Checking whether keys exist
Using in and not in
.get()
.keys()
.values()
.items()
Dictionary loops
Copying dictionaries
.copy()
dict()
.update()
Nested dictionaries
Lists inside dictionaries
Dictionaries inside lists
Dictionary aggregation
Frequency counting
Finding maximum and minimum values
Separating data based on conditions
Character frequency
Data Analyst–style dictionary problems
🎯 Learning Objectives

By completing these exercises, you will learn how to:

Create and structure dictionaries.
Access information using keys.
Add and modify dictionary data.
Safely retrieve values using .get().
Remove dictionary elements.
Iterate through keys, values, and key-value pairs.
Work with nested data structures.
Combine dictionaries with lists.
Build dictionaries dynamically using loops.
Count frequencies using dictionaries.
Perform simple aggregations.
Find maximum and minimum values.
Filter dictionary data using conditions.
Develop problem-solving and programming logic.
Apply dictionaries to practical data-analysis scenarios.
📂 Practice Structure

The 50 exercises are organized into progressive levels.

Level 1 - Dictionary Basics

Questions 1–10

Focuses on:

Creating dictionaries
Accessing values
Adding data
Updating data
len()
Checking keys
.get()
Level 2 — Adding, Updating & Removing

Questions 11–16

Practice:

pop()
popitem()
del
clear()
Adding new keys
Updating existing keys
Level 3 — Keys, Values & Items

Questions 17–24

Practice:

.keys()
.values()
.items()

and:

in
not in

You will also practice looping through dictionaries.

Level 4 — Copying Dictionaries

Questions 25–27

Learn the difference between:

student2 = student1

and:

student2 = student1.copy()

You will also practice:

dict(student1)
Level 5 — Updating Dictionaries

Questions 28–30

Practice:

.update()

and learn what happens when dictionaries contain the same key.

Level 6 — Nested Dictionaries

Questions 31–34

Work with dictionaries inside dictionaries.

Example:

student = {
    "name": "Naila",
    "address": {
        "city": "Delhi",
        "country": "India"
    }
}
Level 7 — Lists + Dictionaries

Questions 35–39

Practice working with combinations such as:

student = {
    "name": "Naila",
    "skills": ["Python", "SQL", "Excel"]
}

and:

employees = [
    {"name": "Naila", "salary": 50000},
    {"name": "John", "salary": 60000}
]

These structures are particularly important when working with real-world data and JSON.

Level 8 — Dictionary Logic Building

Questions 40–45

This section introduces more programming logic.

You will practice:

Frequency counting
.get()
Aggregation
Maximum values
Minimum values
Total and average calculations

One important pattern introduced here is:

count[item] = count.get(item, 0) + 1
Level 9 — Advanced Logic Building

Questions 46–50

These exercises simulate more realistic data-analysis problems.

You will practice:

Filtering dictionary data
Separating data into categories
Finding the highest value
Character frequency
Product-level sales aggregation

The final exercise works with transaction data:

transactions = [
    {"product": "Laptop", "amount": 50000},
    {"product": "Mouse", "amount": 1000},
    {"product": "Laptop", "amount": 50000}
]

and requires you to produce a summarized result.

🧠 Important Dictionary Patterns

During these exercises, pay special attention to the following patterns.

Accessing a value
student["name"]
Safely accessing a value
student.get("name")
Adding or updating
student["age"] = 26
Checking a key
if "age" in student:
    print("Age exists")
Looping through keys and values
for key, value in student.items():
    print(key, value)
Frequency counting
count[item] = count.get(item, 0) + 1
Aggregating values
total[key] = total.get(key, 0) + value

These patterns are worth understanding rather than simply memorizing.

🔍 Logic-Building Approach

For each problem, try to follow this process:

1. Understand the input
        ↓
2. Identify what output is required
        ↓
3. Decide what dictionary you need
        ↓
4. Decide what the KEY should represent
        ↓
5. Decide what the VALUE should represent
        ↓
6. Loop through the data if necessary
        ↓
7. Check whether the key already exists
        ↓
8. Add or update the value
        ↓
9. Print/check the final result

For example, in a frequency-counting problem:

Input
  ↓
apple
banana
apple
apple
  ↓
Dictionary
  ↓
apple → 3
banana → 1

The important question is:

What should my dictionary key represent, and what should my value represent?

This question will help you solve many dictionary problems independently.

📊 Data Analyst Connection

Dictionaries are particularly useful for understanding how structured data works.

Many real-world data sources use structures similar to:

{
    "customer_id": 101,
    "customer_name": "Naila",
    "age": 30,
    "city": "Delhi",
    "purchase_amount": 5000
}

Multiple records may then be stored in a list:

customers = [
    {
        "customer_id": 101,
        "customer_name": "Naila",
        "age": 30
    },
    {
        "customer_id": 102,
        "customer_name": "John",
        "age": 35
    }
]

This type of structure appears frequently when working with:

JSON
APIs
Web data
Python data processing
Automation
Pandas
Data pipelines
🚀 Recommended Practice Strategy

Don't immediately look at solutions.

For every question:

Step 1 — Predict

Before writing code, determine what the final output should look like.

Step 2 — Think about the data structure

Ask:

Do I need a dictionary?

If yes:

What should be my key?

What should be my value?

Step 3 — Write the simplest solution

Don't try to make your code short.

First make it correct and understandable.

Step 4 — Test

Use:

print()

to inspect intermediate results.

Step 5 — Improve

Once your solution works, ask:

Can I make this code cleaner?

📈 Difficulty Progression
Questions	Difficulty	Main Focus
1–10	🟢 Beginner	Basic dictionary operations
11–16	🟢 Beginner	Add, update, remove
17–24	🟢 Beginner	Keys, values, items, loops
25–27	🟡 Beginner+	Copying
28–30	🟡 Intermediate	Updating & merging
31–34	🟡 Intermediate	Nested dictionaries
35–39	🟡 Intermediate	Lists + dictionaries
40–45	🟠 Logic Building	Counting & aggregation
46–50	🔴 Advanced Practice	Data-analysis logic
💡 Key Takeaway

The goal of this practice set is not to memorize 50 solutions.

The goal is to develop the ability to look at a problem and think:

What information do I have?
        ↓
What information do I need?
        ↓
Should I use a dictionary?
        ↓
What should the key represent?
        ↓
What should the value represent?
        ↓
Do I need a loop?
        ↓
Do I need to check whether the key already exists?
        ↓
Should I add, update, count, or aggregate?

Once you can answer these questions, dictionaries become much easier.

🛠️ Skills Practiced

By the end of these exercises, you will have practiced:

Python Fundamentals

Variables
Dictionaries
Loops
Conditions
Lists
Nested structures
Functions/methods
Basic aggregation

Programming Logic

Searching
Counting
Filtering
Updating
Grouping
Aggregating
Comparing
Finding maximum/minimum

Data Analyst Foundations

Frequency analysis
Group-level aggregation
Transaction summaries
Filtering records
Working with semi-structured data
📌 Practice Rule

Don't memorize the code. Understand why the dictionary key and value are being used.

Especially master this pattern:

result[key] = result.get(key, 0) + value

It is one of the most useful dictionary patterns for building your Python logic and will appear repeatedly in data-processing and analytical problems.

⭐ Progress Tracker

You can use this checklist to track your progress:

 Questions 1–10 completed
 Questions 11–20 completed
 Questions 21–30 completed
 Questions 31–40 completed
 Questions 41–50 completed
 Re-solved difficult questions without looking at previous code
 Explained the logic behind frequency counting
 Explained the difference between adding and updating
 Explained .get() and why it is useful
 Solved the final sales aggregation problem independently
🏁 Goal

After completing all 50 exercises, you should be comfortable with:

dictionary[key]
dictionary.get(key)
dictionary.keys()
dictionary.values()
dictionary.items()
dictionary.update()
dictionary.pop()
dictionary.popitem()
dictionary.clear()
dictionary.copy()

and, more importantly, you should be able to build dictionary-based solutions from scratch instead of relying on memorized syntax.
