## Python List Comprehension - Practice Exercises

This repository contains 30 hands-on Python practice questions focused on List Comprehension.

The exercises are designed for beginners who want to understand not only the syntax of list comprehensions but also the logic behind them.

📌 What is List Comprehension?

List comprehension is a concise way to create a new list from an existing iterable such as a list, tuple, string, set, or range().

Basic Syntax
[expression for item in iterable]

Example:

numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)

Output:

[1, 4, 9, 16, 25]

The same logic using a traditional for loop:

numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number ** 2)

List comprehension simply provides a more compact way to express this kind of logic.

🎯 Objectives

By completing these exercises, you will practice:

Creating lists using list comprehension
Transforming values
Filtering values using if
Using if...else
Working with numbers
Working with strings
Using built-in functions inside comprehensions
Converting data types
Cleaning string data
Working with nested lists
Using nested for loops inside comprehensions
Combining filtering and transformation
Developing Python problem-solving logic
📚 Practice Questions

The exercises are divided into six levels.

Level 1 — Basic List Comprehension
#	Exercise	Concept
1	Double Every Number	Transformation
2	Square Every Number	Mathematical transformation
3	Create a List of Numbers	range()
4	Create Cubes	Mathematical transformation
5	Convert Words to Uppercase	String transformation
6	Find Length of Each Word	len()
7	Add 10 to Every Number	Mathematical transformation
8	Convert Strings to Integers	Type conversion
Level 2 — Filtering With if
#	Exercise	Concept
9	Find Even Numbers	Filtering
10	Find Odd Numbers	Filtering
11	Numbers Greater Than 50	Conditional filtering
12	Numbers Less Than 20	Conditional filtering
13	Find Positive Numbers	Conditional filtering
14	Numbers Divisible by 5	Modulo + filtering
15	Find Long Words	String length + filtering
Level 3 — Filtering + Transformation
#	Exercise	Concept
16	Square Only Even Numbers	Filtering + transformation
17	Double Numbers Greater Than 10	Filtering + transformation
18	Square Positive Numbers	Filtering + transformation
19	Uppercase Long Words	String filtering + transformation
20	Discounted Prices	Mathematical transformation
Level 4 — if...else
#	Exercise	Concept
21	Pass or Fail	if...else
22	Even or Odd	if...else
23	Positive, Negative or Zero	Multiple conditions
24	Adult or Minor	Conditional transformation
25	Replace Negative Numbers	Conditional transformation
Level 5 — Strings and Logic
#	Exercise	Concept
26	Extract Vowels	String filtering
27	Extract Uppercase Letters	String filtering
28	Clean Names	String transformation
Level 6 — Nested List Comprehension
#	Exercise	Concept
29	Flatten a Nested List	Nested comprehension
30	Flatten and Filter	Nested comprehension + filtering
🧠 Important Syntax Patterns
1. Transform Every Item
[expression for item in iterable]

Example:

[x * 2 for x in numbers]
2. Filter Items
[item for item in iterable if condition]

Example:

[x for x in numbers if x > 10]
3. Filter and Transform
[expression for item in iterable if condition]

Example:

[x ** 2 for x in numbers if x % 2 == 0]
4. Use if...else
[value_if_true if condition else value_if_false for item in iterable]

Example:

["Pass" if mark >= 40 else "Fail" for mark in marks]
5. Nested List Comprehension
[expression for outer_item in outer_iterable for inner_item in inner_iterable]

Example:

[number for row in numbers for number in row]
🔄 Normal Loop vs List Comprehension

Understanding this conversion is one of the most important skills in this topic.

Traditional for loop
numbers = [1, 2, 3, 4, 5]

result = []

for number in numbers:
    result.append(number * 2)
List comprehension
numbers = [1, 2, 3, 4, 5]

result = [number * 2 for number in numbers]

Both produce:

[2, 4, 6, 8, 10]
🔍 Recommended Problem-Solving Approach

When solving a list comprehension problem, identify these things:

1. What is the input?

Example:

numbers = [1, 2, 3, 4, 5]
2. What happens to each item?

For example:

number → number × 2
3. Do we need a condition?

For example:

Keep only even numbers
4. What should the new list contain?

For example:

[4, 16, 36]
5. Write the normal loop first if necessary

For example:

result = []

for number in numbers:
    if number % 2 == 0:
        result.append(number ** 2)

Then convert it into:

result = [number ** 2 for number in numbers if number % 2 == 0]
📊 Connection to Data Analytics

List comprehension is useful when performing simple data preparation and transformation tasks.

For example, converting string values into integers:

prices = ["100", "200", "300"]

prices = [int(price) for price in prices]

Cleaning text:

names = ["  Ali", "Sara  ", "  John  "]

clean_names = [name.strip() for name in names]

Filtering values:

sales = [100, 500, 250, 80, 900]

high_sales = [sale for sale in sales if sale > 300]

Transforming values:

prices = [100, 200, 300]

🚀 Learning Progression

The exercises intentionally increase in difficulty:

Basic Comprehension
        ↓
Transformation
        ↓
Filtering with if
        ↓
Filtering + Transformation
        ↓
if...else
        ↓
String Processing
        ↓
Nested Comprehension

The goal is not simply to memorize the syntax.

The goal is to develop the ability to look at a problem and identify:

INPUT
  ↓
LOOP
  ↓
CONDITION
  ↓
TRANSFORMATION
  ↓
OUTPUT
✅ Completion Checklist
 Complete Questions 1–8
 Complete Questions 9–15
 Complete Questions 16–20
 Complete Questions 21–25
 Complete Questions 26–28
 Complete Questions 29–30
 Convert traditional for loops into list comprehensions
 Understand filtering with if
 Understand if...else inside comprehensions
 Practice nested list comprehensions
 Review all solutions after completing the exercises
💡 Key Takeaway

List comprehension is essentially a compact way of expressing:

for
optionally:
if
optionally a transformation:
expression

to create a new list.

The most important patterns to master are:

[expression for item in iterable]
[item for item in iterable if condition]
[value_if_true if condition else value_if_false for item in iterable]

Once these patterns become comfortable, more advanced Python data-processing tasks become much easier.

🐍 Python Learning Journey

This practice set is part of a broader Python for Data Analytics learning journey, covering Python fundamentals through hands-on exercises and progressively more complex problems.
discounted_prices = [price * 0.9 for price in prices]

These kinds of operations are useful foundations for later Python data-analysis work with tools such as Pandas.
