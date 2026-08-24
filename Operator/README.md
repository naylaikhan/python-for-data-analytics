Operators

What it covers: The "verbs" of Python - how to perform calculations, comparisons, and logical checks.

Core Concepts
Arithmetic operators: + - * / // % **
Comparison operators: > < == != >= <= → always return a Boolean
Logical operators: and, or, not — combining multiple conditions
Assignment operators: += -= *= — shortcuts for updating variables
Membership operator: in / not in
Why It Matters for Data Analysis

Operators are the direct equivalent of:

Calculated columns (profit = revenue - cost)
Row filtering (df["sales"] > 1000)
Combined filter conditions (age >= 18 and city == "Delhi")

This is the exact logic used later in Pandas boolean filtering (with &, |, ~).

Common Mistakes
Confusing = (assignment) with == (comparison)
Expecting / to return a whole number
Ignoring operator precedence (BODMAS rules)
Forgetting % is a general-purpose "remainder" tool, not just for even/odd checks

📝 Practice: 30 questions covering arithmetic logic, chained comparisons, leap-year logic, and edge cases (like division by zero).
