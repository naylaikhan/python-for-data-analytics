"""1. Create a set

Create a set called numbers containing:

10, 20, 30, 40, 50

Print the set.
"""
print("Solution 1")
numbers = {10,20,30,40,50}

print(numbers)

"""2. Create a set of names

Create a set called students containing:

Ali
Sara
Naila
John

Print the set."""
print("Solution 2")

students = {"Ali","Sara","Naila","John"}
print(students)

"""3. Remove duplicates automatically

Given:

numbers = [10, 20, 20, 30, 40, 40, 50]

Convert the list into a set and print the result."""

print("Solution 3")
numbers = [10, 20, 20, 30, 40, 40, 50]
numbers = set(numbers)
print(numbers)

"""4. Count unique values

Given:

numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]

Find how many unique numbers are present.

Expected result:

5"""

print("Solution 4")
numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]

unique_numbers = len(set(numbers))
print(unique_numbers)

"""5. Create an empty set

Create an empty set called data.

Then print its type using:

type()"""

print("Solution 5")
data = set()
print(type(data))

"""6. Create a set from a string

Given:

word = "programming"

Create a set containing all unique characters from the word."""

print("Solution 6")
word = "programming"

unique_characters = set(word)
print(unique_characters)

"""7. Count unique characters

Using:

word = "programming"

Find the number of unique characters."""

print("Solution 7")

word = "programming"
unique_characters_count = len(set(word))
print(unique_characters_count)

"""8. Check membership

Given:

numbers = {10, 20, 30, 40, 50}

Check whether 30 exists in the set.

Print:

30 exists

if it exists."""

print("Solution 8")
numbers = {10, 20, 30, 40, 50}

if 30 in numbers:
    print("30 exists")
else:
    print("Doesn't Exist")

"""9. Check if an item does not exist

Given:

numbers = {10, 20, 30, 40}

Check whether 100 is not present."""

print("Solution 9")

numbers = {10, 20, 30, 40}
print(100 not in numbers)

"""10. Compare two sets

Given:

A = {1, 2, 3}
B = {3, 2, 1}

Check whether both sets are equal."""
print("Solution 10")

A = {1, 2, 3}
B = {3, 2, 1}

print(A==B)

"""Level 2: Adding and Updating Sets"""

"""11. Add one item

Given:

numbers = {10, 20, 30}

Add 40 to the set."""

print("Solution 11")
numbers = {10, 20, 30}
print("Before Adding",numbers)
numbers.add(40)
print("After Adding",numbers)

"""12. Add a duplicate

Given:

numbers = {10, 20, 30}

Add 20 again.

Print the set and observe what happens."""

print("Solution 12")

numbers = {10, 20, 30}
print("Before Adding",numbers)
numbers = {10, 20, 30}
numbers.add(20)
print("After Adding",numbers)


"""13. Add multiple items

Given:

numbers = {1, 2, 3}

Add the following numbers using update():

4, 5, 6"""

print("Solution 13")

numbers = {1, 2, 3}
print("Before Adding",numbers)
numbers.update([4,5,6])
print("After Adding",numbers)


"""14. Add items from a list

Given:

numbers = {10, 20, 30}

new_numbers = [30, 40, 50, 60]

Add all values from new_numbers into numbers.

What should happen to the duplicate 30?"""

print("Solution 14")

numbers = {10, 20, 30}
new_numbers = [30, 40, 50, 60]
print("Before Adding",numbers)
numbers.update(new_numbers)
print("After Adding",numbers)

"""15. Add characters from a string

Given:

letters = {"a", "b", "c"}

Use update() to add all characters from:

"python"

Print the final set."""

print("Solution 15")

letters = {"a", "b", "c"}

letters.update("python")
print(letters)

"""16. User-entered unique numbers

Create an empty set.

Use a loop to take 5 numbers from the user and add them to the set.

Finally, print only the unique numbers."""

print("Solution 16")

empty_set = set()

for num in range(1,6):
    number = input("Enter the number")
    empty_set.add(number)

print(empty_set)

"""Level 3: Removing Elements"""
"""17. Remove an existing item

Given:

numbers = {10, 20, 30, 40}

Remove 20."""

print("Solution 17")

numbers = {10, 20, 30, 40}

print(numbers)
numbers.remove(20)
print(numbers)

"""18. Use discard()

Given:

numbers = {10, 20, 30}

Try to discard 50.

Does the program produce an error?
"""

print("Solution 18")
numbers = {10, 20, 30}

print(numbers)
numbers.discard(18)
print(numbers)

"""19. remove() vs discard()

Given:

numbers = {10, 20, 30}

Try both:

numbers.remove(50)

and:

numbers.discard(50)

Observe and explain the difference."""

print("Solution 19")
numbers = {10, 20, 30}
# numbers.remove(50)
print("Removing an item which is not present in set using remove will through error")
print(numbers)
numbers.discard(50)
print(numbers)
print("Removing an item which is not present in set using discard will not through any error")

"""20. Remove an arbitrary item

Given:

numbers = {10, 20, 30, 40}

Use pop() to remove one item.

Print:

The removed item
The remaining set"""

print("Solution 20")
numbers = {10, 20, 30, 40}

print(numbers)
numbers.pop()
print(numbers)

"""21. Empty a set

Given:

numbers = {10, 20, 30, 40}

Remove all elements but keep the set variable."""

print("Solution 21")

numbers = {10, 20, 30, 40}
print(numbers)
numbers.clear()
print(numbers)

"""22. Remove values conditionally

Given:

numbers = {10, 15, 20, 25, 30}

Remove 15 only if it exists in the set.

Your program should not produce an error if the value is missing."""

print("Solution 22")
numbers = {10, 15, 20, 25, 30}
print(numbers)
numbers.discard(15)
print(numbers)

"""Level 4: Looping and Conditions"""
"""23. Print all elements

Given:

numbers = {10, 20, 30, 40, 50}

Use a for loop to print every number."""

print("Solution 23")

numbers = {10, 20, 30, 40, 50}

for num in numbers:
    print(num)

"""24. Print only even numbers

Given:

numbers = {10, 15, 20, 25, 30, 35}

Print only the even numbers."""

print("Solution 24")

numbers = {10, 15, 20, 25, 30, 35}

for num in numbers:
    if num % 2 == 0:
        print(num)

"""25. Print only numbers greater than 20

Given:

numbers = {10, 15, 20, 25, 30, 35, 40}

Use a loop and conditional statement to print numbers greater than 20."""

print("Solution 25")

numbers = {10, 15, 20, 25, 30, 35, 40}

for num in numbers:
    if num > 20 :
        print(num)

"""26. Find the sum manually

Given:

numbers = {10, 20, 30, 40}

Use a loop to calculate the sum.

Do not use sum() for this question."""

print("Solution 26")

numbers = {10, 20, 30, 40}

total = 0
for num in numbers:
    total+=num

print("Total :",total)

"""27. Count even numbers

Given:

numbers = {10, 15, 20, 25, 30, 35, 40}

Count how many even numbers exist."""

print("Solution 27")

numbers = {10, 15, 20, 25, 30, 35, 40}

count = 0

for num in numbers:
    if num % 2 == 0:
        count+=1

print("total Even numbers :" , count)

"""28. Find the largest number manually

Given:

numbers = {15, 8, 25, 3, 40, 12}

Find the largest number using a loop.

Do not use max()."""

print("Solution 28")

numbers = {15, 8, 25, 3, 40, 12}

new_list = list(numbers)
largest_number = new_list[0]

for num in numbers:
    if num > largest_number:
        largest_number = num

print("Largest Number :" ,largest_number)

"""29. Find the smallest number manually

Given:

numbers = {15, 8, 25, 3, 40, 12}

Find the smallest number using a loop.

Do not use min()."""

print("Solution 29")
numbers = {15, 8, 25, 3, 40, 12}

new_list = list(numbers)
smallest_number = new_list[0]

for num in numbers:
    if num < smallest_number:
        smallest_number = num

print(smallest_number)

"""Level 5: Union, Intersection, and Difference

For the following questions, use:

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
30. Union

Find all unique values from both sets.
"""

print("Solution 30")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

unique_values = A.union(B)
print(unique_values)

"""31. Intersection

Find the values that exist in both sets."""

print("Solution 31")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

common_values = A.intersection(B)
print(common_values)

"""32. Difference: A − B

Find values that exist in A but not in B."""

print("Solution 32")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

not_in_b = A - B
print(not_in_b)

"""33. Difference: B − A

Find values that exist in B but not in A.

Notice how this differs from Question 32."""

print("Solution 33")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

not_in_a = B - A

print(not_in_a)

"""34. Symmetric difference

Find values that exist in either A or B, but not in both."""

print("Solution 34")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

not_in_either = A.symmetric_difference(B)
print(not_in_either)

"""35. Use methods instead of operators

Solve the following using set methods instead of symbols:

Union
Intersection
Difference
Symmetric difference

For example:

A.union(B)"""

"""Level 6: Subsets, Supersets, and Disjoint Sets
36. Check subset

Given:

A = {1, 2, 3, 4, 5}
B = {2, 3, 4}

Check whether B is a subset of A."""

print("Solution 36")
A = {1, 2, 3, 4, 5}
B = {2, 3, 4}

print(B.issubset(A))

"""37. Check superset

Using the same sets:

A = {1, 2, 3, 4, 5}
B = {2, 3, 4}

Check whether A is a superset of B."""

print("Solution 37")

print(A.issuperset(B))

"""38. Check disjoint sets

Given:

A = {1, 2, 3}
B = {4, 5, 6}

Check whether the sets have no common values."""

print("Solution 38")

A = {1, 2, 3}
B = {4, 5, 6}

print(A.isdisjoint(B))

"""39. Check another disjoint example

Given:

A = {1, 2, 3}
B = {3, 4, 5}

Check whether they are disjoint.

Explain why the result is different from Question 38."""

print("Solution 39")

A = {1, 2, 3}
B = {3, 4, 5}

print(A.isdisjoint(B))
print("Because 3 is common in both sets")

"""Level 7: Set Comprehension
40. Create a set of squares

Given:

numbers = [1, 2, 3, 4, 5]

Use set comprehension to create:

{1, 4, 9, 16, 25}"""

print("Solution 40")

numbers = [1, 2, 3, 4, 5]

new_numbers = {number **2 for number in numbers}
print(new_numbers)

"""41. Create a set of even numbers

Using set comprehension, create a set containing even numbers from 1 to 20."""

print("Solution 41")
new_numbers = {number for number in range(1,21) if number % 2 == 0}
print(new_numbers)

"""42. Squares of even numbers only

Given:

numbers = [1, 2, 3, 4, 5, 6]

Create a set containing the squares of only even numbers.

Expected values:

4, 16, 36"""

print("Solution 42")
numbers = [1, 2, 3, 4, 5, 6]

new_numbers = { number ** 2 for number in numbers if number % 2 == 0}
print(new_numbers)

"""43. Unique first letters

Given:

names = ["Ali", "Aman", "Sara", "John", "Naila", "Sam"]

Create a set containing the first letter of every name.

What happens to duplicate letters?"""

print("Solution 43")

names = ["Ali", "Aman", "Sara", "John", "Naila", "Sam"]

name_letters_list = [name[0] for name in names]
print(name_letters_list)
print(set(name_letters_list))

"""Level 8: Logic-Building Problems


44. Find duplicate values

Given:

numbers = [10, 20, 30, 20, 40, 50, 30, 60]

Find which numbers appear more than once.

Hint: Use two sets.

Example logic:

First time seeing number → add to one set

Already seen → add to duplicates set

Expected result:

{20, 30}"""

print("Solution 44")

numbers = [10, 20, 30, 20, 40, 50, 30, 60]

seen = set()
duplicates = set()

for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print(duplicates)

"""45. Find unique values between two lists

Given:

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

Find values that appear in only one of the lists.

Expected concept:

Symmetric Difference"""

print("Solution 45")

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

unique_values = set(list1)^set(list2)
print(unique_values)


"""46. Find common students

Given:

python_students = {
    "Ali",
    "Sara",
    "Naila",
    "John"
}

sql_students = {
    "Sara",
    "Naila",
    "David",
    "Rahul"
}

Find students learning both Python and SQL."""

print("Solution 46")
python_students = {
    "Ali",
    "Sara",
    "Naila",
    "John"
}

sql_students = {
    "Sara",
    "Naila",
    "David",
    "Rahul"
}

learning_both = python_students.intersection(sql_students)
print(learning_both)

"""47. Find students learning only Python

Using the same sets:

python_students = {
    "Ali",
    "Sara",
    "Naila",
    "John"
}

sql_students = {
    "Sara",
    "Naila",
    "David",
    "Rahul"
}

Find students learning Python but not SQL."""

print("Solution 47")

python_students = {
    "Ali",
    "Sara",
    "Naila",
    "John"
}

sql_students = {
    "Sara",
    "Naila",
    "David",
    "Rahul"
}

learning_python  = python_students - sql_students
print(learning_python)

"""48. Find students learning at least one skill

Using the same data, find every student learning:

Python
SQL
or both

Make sure there are no duplicates."""
print("Solution 48")
python_students = {
    "Ali",
    "Sara",
    "Naila",
    "John"
}

sql_students = {
    "Sara",
    "Naila",
    "David",
    "Rahul"
}

python_sql_both = python_students | sql_students
print(python_sql_both)

"""Level 9: Data Analyst Style Problems"""

"""49. Returning and new customers

You have customer IDs from two months:

january = {
    "C101",
    "C102",
    "C103",
    "C104",
    "C105"
}

february = {
    "C103",
    "C104",
    "C105",
    "C106",
    "C107"
}

Write a program to find:

Returning customers
Customers who were present only in January
New customers in February
All unique customers across both months
Customers who appear in only one month

This question combines multiple set operations."""

print("Solution 49")

january = {
    "C101",
    "C102",
    "C103",
    "C104",
    "C105"
}

february = {
    "C103",
    "C104",
    "C105",
    "C106",
    "C107"
}

Returning_customers = january.intersection(february)
Customers_only_in_January = january - february
New_customers_in_February = february - january
unique_both_months = january | february
Customers_only_in_one_month = january.symmetric_difference(february)


print("Returning Customers are :",Returning_customers)
print("Customers who were present only in January are :", Customers_only_in_January)
print("New customers in February are :", New_customers_in_February)
print("All unique customers across both months are :",unique_both_months)
print("Customers who appear in only one month are :",Customers_only_in_one_month)


"""50. Advanced: Website Visitors Analysis

You have visitors from three different days:

monday = {
    "U101",
    "U102",
    "U103",
    "U104"
}

tuesday = {
    "U103",
    "U104",
    "U105",
    "U106"
}

wednesday = {
    "U104",
    "U105",
    "U107"
}

Find:

All unique visitors across the three days.
Visitors who visited on all three days.
Visitors who visited Monday and Tuesday.
Visitors who visited Tuesday and Wednesday.
Visitors who visited Monday but not Tuesday.
Visitors who visited exactly one day.
"""
print("Solution 50")
monday = {
    "U101",
    "U102",
    "U103",
    "U104"
}

tuesday = {
    "U103",
    "U104",
    "U105",
    "U106"
}

wednesday = {
    "U104",
    "U105",
    "U107"
}

unique_visitors_three_days = monday | tuesday | wednesday
visited_all_days = monday & tuesday & wednesday
visited_mon_tues = monday & tuesday
visited_tues_wed = tuesday & wednesday
visited_mon_not_tues = monday - tuesday
monday_only = monday - tuesday - wednesday
tuesday_only = tuesday - monday - wednesday
wednesday_only = wednesday - monday - tuesday
visited_exactly_one_day = monday_only | tuesday_only | wednesday_only

print("All unique visitors across the three days.",unique_visitors_three_days)
print("Visitors who visited on all three days.",visited_all_days)
print("Visitors who visited Monday and Tuesday.",visited_mon_tues)
print("Visitors who visited Tuesday and Wednesday.",visited_tues_wed)
print("Visitors who visited Monday but not Tuesday.",visited_mon_not_tues)
print("Visitors who visited exactly one day.", visited_exactly_one_day)
