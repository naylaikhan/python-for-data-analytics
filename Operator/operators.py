# x=7
# y=10

# print(x>y)
# print(x<y)
# print(x==y)
# print(x!=y)
# print(x>=y)
# print(x<=y)

# age = 25
# has_id = True

# print(age >=18 and has_id)
# print(age <=18 or has_id)
# print(not has_id)


"""
1. Given a = 15 and b = 4, print the result of:
- Addition
- Subtraction
- Multiplication
- Division
"""

a = 15
b = 4

add = a + b
sub = a - b
mul = a * b
div = a / b

print(f"Addition : {add}")
print(f"Subtraction : {sub}")
print(f"Multiplication : {mul}")
print(f"Division : {div}")

"""
2. Given a = 15 and b = 4:

- Print the result of floor division (//).
- Print the result of modulus (%).
- Explain in one line what each operator represents.
"""

a = 15
b = 4
floor_div = a // b
mod = a % b

print(f"Floor Division: {floor_div}")
print(f"Modulus : {mod}")


"""
3. Calculate and print 2 raised to the power of 5
using the exponent operator (**).
"""

powered_number = 2 ** 5
print(f"2 raise to the power 5 : {powered_number}")

"""
4. Given x = 10, write a comparison expression to check
whether x is greater than 5.

Print the result.
"""

x = 10

print(x>5)

"""
5. Given x = 8:

1. Check whether x is equal to 8.
2. Print the result.
3. Check whether x is not equal to 8.
4. Print that result too.
"""

x = 8

print(x==8)
print(x!=8)

"""
6. Given age = 20, write a single expression using 'and'
to check whether age is:

- Greater than 18
- Less than 30

Print the result.
"""
age = 20
print(age > 18 and age < 30)

"""
7. Given:

has_ticket = True
has_id = False

Use the 'or' operator to check whether the person can enter.

Assume having either a ticket OR an ID is enough.

Print the result.
"""

has_ticket = True
has_id = False

print(has_ticket or has_id)


"""
8. Given is_raining = True, use the 'not' operator
to print the opposite Boolean value.
"""

is_raining = True

print(not is_raining)


"""
9. Given count = 5:

Use the += operator to increase count by 3.

Print the updated value.
"""

count = 5
count +=3
print(count)


"""
10. Given:

fruits = "apple,mango,banana"

Check whether "mango" is present in the string
using the 'in' operator.

Print the result.
"""

fruits = "apple,mango,banana"
print("mango" in fruits)

"""
11. Given n = 27, use the modulus operator (%)
to check the remainder when n is divided by 2.

Do NOT return True or False.

Just print the result of the modulus operation.
"""

n = 27
print(n % 2 == 0)

"""
12. Given price = 999, use floor division (//)
to find how many complete hundreds fit into the price.

Example:
How many ₹100 notes can fit into ₹999?

Print the result.
"""

price = 999
complete_hundreds = price // 100
print(complete_hundreds)

"""
13. Given:

total_items = 47
items_per_box = 6

Calculate:

1. How many full boxes can be made using //.
2. How many items will be left over using %.

Print both results.
"""

total_items = 47
items_per_box = 6

full_boxes = total_items // items_per_box
left_over = total_items % items_per_box

print(full_boxes)
print(left_over)

"""
14. Given marks = 82, write one expression using
a chained comparison to check whether marks are
between 80 and 90, inclusive.

Use:

80 <= marks <= 90

Print the result.
"""

marks = 82

print(80<=marks<=90)

"""
15. Given salary = 50000, use the 'and' operator
to check whether salary is:

- Greater than 40000
- Less than 60000

Print True or False.
"""

salary = 50000

print(salary>40000 and salary<60000)

# Write your code below

"""
16. Given city = "Delhi", use the 'or' operator
to check whether the city is:

- "Delhi"
OR
- "Mumbai"

Print the result.
"""

city = "Delhi"

print(city == "Delhi" or  city  == "Mumbai")

"""
17. Given:

x = 5
y = 10
z = 15

Write an expression using 'and' to check whether
all three values are greater than 0.

Print the result.
"""

x = 5
y = 10
z = 15

print( x > 0 and y > 0 and z > 0)

"""
18. Given balance = 1000:

1. Use -= to deduct 250.
2. Use += to add 500.

Print the final balance.
"""

balance = 1000
balance -= 250
balance +=500
print(balance)


"""
19. Given:

password = "abc123"

Check:

1. Whether "123" is present using 'in'.
2. Whether "xyz" is NOT present using 'not in'.

Print both results.
"""

password = "abc123"

print("123" in password)
print("xyz" not in password)

"""
20. Given:

a = 6
b = 3

Predict the results first.

Then print the results of:

a == b
a != b
a >= b
"""

a = 6
b = 3

print(a==b)
print(a!=b)
print(a>=b)

"""
21. Given n = 14, write a single expression using %
that returns:

True  -> if the number is even
False -> if the number is odd

Do NOT just print the remainder.

Create a proper Boolean expression.
"""

n = 14

print(n % 2 == 0)

"""
22. Given year = 2024, write logic to check
whether it is a leap year.

A year is a leap year if:

- It is divisible by 4
AND
- It is NOT divisible by 100
OR
- It is divisible by 400

Use %, and, and/or.

Print True or False.
"""

year = 2024

print( year%4==0 and  year%100!=0 or year%400==0  )

"""
23. Given marks = 45, check whether the student
has failed.

Passing marks = 40.

Do NOT directly write:

marks < 40

Instead, use the 'not' operator combined with
a comparison.

Print the result.
"""

marks = 45

print(marks < 40 )

"""
24. Given:

age = 25
income = 45000

A person is eligible for a loan if:

- Age is between 21 and 60
AND
- Income is greater than 30000

Combine all conditions using 'and'.

Print True or False.
"""

age = 25
income = 45000

print( 21<=age<=60 and income>30000)

"""
25. Given x = 10, without using an if statement,
write an expression that checks whether x is
a multiple of BOTH 2 and 5.

Use:

- Comparison operators
- %
- Logical operators

Print True or False.
"""

x = 10

print( x%2==0 and x%5==0)

"""
26. Given num = 0:

First explain in words:

Why does:

num % 2 == 0

correctly identify 0 as an even number?

Think about what the modulus operator does when
0 is divided by 2.

Then verify your explanation with code.
"""

num = 0

print(num % 2 == 0)

"""
27. Given:

a = 12
b = 18

Using the modulus operator (%), check:

1. Whether a is exactly divisible by b.
2. Whether b is exactly divisible by a.

Print both Boolean results.

Remember:
A number is exactly divisible if the remainder is 0.
"""

a = 12
b = 18

print(a%b==0)
print(b%a==0)

"""
28. Consider the following condition:

discount_eligible = (
    (purchase_amount > 500)
    and
    (is_member == True)
)

Given:

purchase_amount = 600
is_member = False

Before writing code:

1. Predict whether discount_eligible will be
   True or False.
2. Explain why.
3. Then verify your answer using Python code.
"""

purchase_amount = 600
is_member = False

print(purchase_amount > 500 and is_member==True)

"""
29. Given:

a = 5
b = 0

Before writing the code, predict what will happen
when you calculate:

a / b
a // b
a % b

Think carefully about division by zero.

Then verify what happens by running the code.

Important:
Test each operation carefully because Python will
raise an error.
"""

# a = 5
# b = 0

# print(a/b)
# print(a//b)
# print(a%b)

"""
30. Given:

grade_input = "A"

Without using the 'in' keyword, write an expression
using only:

- ==
- or

Check whether grade_input is either:

"A"
OR
"B"

Print True or False.
"""

grade_input = "A"

print(grade_input=="A" or grade_input=="B")


