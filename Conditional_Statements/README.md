Conditional Statements

What it covers: Decision-making in code - running different logic depending on data values.

Core Concepts
if, elif, else - the "fork in the road" model
Python checks conditions top-to-bottom and stops at the first True
Nested conditionals vs. combined conditions (and/or)
Why indentation defines code blocks in Python (no {})
Why It Matters for Data Analysis

This is the manual version of logic later automated with:

np.where()
pd.cut()
.apply() with custom functions

Used constantly for creating categories (grades, age groups, income tiers) and flagging data issues.

Common Mistakes
Using multiple separate if statements instead of elif (causes multiple blocks to run unintentionally)
Wrong order of overlapping elif conditions
Forgetting the colon : or messing up indentation
Adding unnecessary else blocks when not needed

📝 Practice: 30 questions covering grading systems, eligibility checks, tax slabs, leap years, and prime number logic.
