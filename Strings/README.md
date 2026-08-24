Strings

What it covers: Text data handling - the foundation of almost every data-cleaning task an analyst performs.

Core Concepts
Strings as an ordered sequence of characters (indexing starts at 0)
Positive vs. negative indexing
Slicing (text[start:end]) — and why the end index is excluded
Immutability - strings can't be changed in place; operations return new strings
Common methods: .strip(), .upper(), .lower(), .split(), .replace()
String concatenation vs. f-strings
Why It Matters for Data Analysis

Real datasets are full of messy text - extra spaces, inconsistent casing, IDs that need splitting, dates stored as strings. String manipulation is the backbone of data cleaning before any analysis happens.

Common Mistakes
Assuming indexing starts at 1
Forgetting strings are immutable
Mixing string and numeric types without str() conversion
Misunderstanding .strip() (only trims edges, not internal spaces)

📝 Practice: 30 questions (10 Basic / 10 Intermediate / 10 Logic-building) covering indexing, slicing, cleaning, and text parsing (emails, dates, file paths, IDs).
