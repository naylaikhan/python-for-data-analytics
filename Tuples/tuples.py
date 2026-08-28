"""Level 1: Basic Tuple Operations
1. Create a tuple

Create a tuple called fruits containing:

apple, banana, mango, orange

Print the tuple."""

print("Solution 1")

fruits = ("apple","banana","mango","orange")
print(fruits)

"""2. Check the data type

Create:

numbers = (10, 20, 30)

Print the data type of numbers."""

print("Solution 2")

numbers = (10,20,30)
print(type(numbers))

"""3. Create an empty tuple

Create an empty tuple called empty_tuple.

Print it."""

print("Solution 3")
empty_tuple = ()
print(empty_tuple)

"""4. Create a single-item tuple

Create a tuple containing only:

Python

Store it in a variable called language.

Check and print its data type."""

print("Solution 4")
language = ("Python",)
print(language)
print(type(language))

print("Solution 4")

"""5. Access the first item

Given:

colors = ("red", "blue", "green", "yellow")

Print the first item."""

print("Solution 5")

colors = ("red", "blue", "green", "yellow")

first_item = colors[0]
print(first_item)

"""6. Access the last item

Given:

colors = ("red", "blue", "green", "yellow")

Print the last item using negative indexing."""

print("Solution 6")
colors = ("red", "blue", "green", "yellow")

last_item = colors[-1]
print(last_item)

"""7. Access a specific item

Given:

numbers = (10, 20, 30, 40, 50)

Print 30 using its index."""

print("Solution 7")

numbers = (10, 20, 30, 40, 50)

print(numbers.index(30))

"""8. Find the length

Given:

cities = ("Delhi", "Mumbai", "Chennai", "Bangalore")

Find and print the total number of cities."""

print("Solution 8")

cities = ("Delhi", "Mumbai", "Chennai", "Bangalore")

print("Total number of cities :",len(cities))

"""9. Check whether an item exists

Given:

fruits = ("apple", "banana", "mango")

Check whether "banana" exists in the tuple.

Print the result."""

print("Solution 9")

fruits = ("apple", "banana", "mango")

print("banana" in fruits)

"""10. Check whether an item does not exist

Given:

fruits = ("apple", "banana", "mango")

Check whether "orange" does not exist in the tuple.

Print the result."""

print("Solution 10")

fruits = ("apple", "banana", "mango")

print("orange" not in fruits)

"""Level 2: Indexing and Slicing
11. Extract the first three items

Given:

numbers = (10, 20, 30, 40, 50, 60)

Create and print a new tuple containing:

10, 20, 30

using slicing."""

print("Solution 11")

numbers = (10, 20, 30, 40, 50, 60)

first_three = numbers[0:3]
print(first_three)
print(type(first_three))

"""12. Extract the last three items

Given:

numbers = (10, 20, 30, 40, 50, 60)

Use slicing to get:

40, 50, 60"""

print("Solution 12")

numbers = (10, 20, 30, 40, 50, 60)
last_three = numbers[3:]
print(last_three)

"""13. Extract items from the middle

Given:

letters = ("a", "b", "c", "d", "e", "f")

Use slicing to extract:

c, d, e"""

print("Solution 13")
letters = ("a", "b", "c", "d", "e", "f")

sliced_letters = letters[2:5]
print(sliced_letters)

"""14. Get every second item

Given:

numbers = (1, 2, 3, 4, 5, 6, 7, 8)

Create a new tuple containing every second item.

Expected result:

(1, 3, 5, 7)"""

print("Solution 14")

numbers = (1, 2, 3, 4, 5, 6, 7, 8)

new_numbers = numbers[0::2]
print(new_numbers)


"""15. Reverse a tuple

Given:

numbers = (10, 20, 30, 40, 50)

Reverse the tuple using slicing.

Level 3: Tuple Methods"""

print("Solution 15")
numbers = (10, 20, 30, 40, 50)
reversed_tuple = numbers[::-1]
print(reversed_tuple)

"""16. Count occurrences

Given:

numbers = (10, 20, 10, 30, 10, 40)

Find how many times 10 appears."""

print("Solution 16")
numbers = (10, 20, 10, 30, 10, 40)
apperances_count = numbers.count(10)
print(apperances_count)

"""17. Find the index

Given:

fruits = ("apple", "banana", "mango", "orange")

Find the index of "mango"."""

print("Solution 17")

fruits = ("apple", "banana", "mango", "orange")
mango_index = fruits.index("mango")
print(mango_index)

"""18. Find the first occurrence

Given:

numbers = (5, 10, 15, 10, 20, 10)

Find the index of the first occurrence of 10."""

print("Solution 18")

numbers = (5, 10, 15, 10, 20, 10)

ten_index = numbers.index(10)
print(ten_index)

"""Level 4: Looping Through Tuples
19. Print every item

Given:

fruits = ("apple", "banana", "mango", "orange")

Use a for loop to print every fruit."""

print("Solution 19")

fruits = ("apple", "banana", "mango", "orange")

for fruit in fruits:
    print(fruit)

"""20. Print items with their indexes

Given:

languages = ("Python", "SQL", "Excel", "Power BI")

Print the index and value of every item.

Expected format:

0 Python
1 SQL
2 Excel
3 Power BI"""

print("Solution 20")
languages = ("Python", "SQL", "Excel", "Power BI")

for i , language in enumerate(languages):
    print(i,language)

"""21. Print only even numbers

Given:

numbers = (10, 15, 20, 25, 30, 35, 40)

Use a loop and conditional statement to print only the even numbers."""

print("Solution 21")

numbers = (10, 15, 20, 25, 30, 35, 40)

for num in numbers :
    if num % 2 == 0:
        print(num)

"""22. Find numbers greater than 50

Given:

numbers = (25, 60, 45, 80, 30, 90, 50)

Print only the numbers greater than 50."""
print("Solution 22")

numbers = (25, 60, 45, 80, 30, 90, 50)

for num in numbers :
    if num > 50:
        print(num)

"""Level 5: Tuple Packing and Unpacking"""
"""23. Unpack a tuple

Given:

person = ("Naila", 25, "Delhi")

Unpack the tuple into three variables:

name
age
city

Then print all three variables."""

print("Solution 23")
person = ("Naila", 25, "Delhi")

name ,age ,city = person
print(name)
print(age)
print(city)

"""24. Swap two variables

Given:

a = 10
b = 20

Swap the values of a and b using tuple unpacking.

Expected result:

a = 20
b = 10"""
print("Solution 24")
a = 10
b = 20

b,a =a,b
print(a)
print(b)

"""25. Use extended unpacking

Given:

numbers = (10, 20, 30, 40, 50, 60)

Unpack the tuple so that:

first contains 10
last contains 60
middle contains all remaining values

Print all three variables."""

print("Solution 25")
numbers = (10, 20, 30, 40, 50, 60)

first,*middle,last = numbers
print(first)
print(middle)
print(last)

"""Level 6: Modifying Tuples Indirectly
26. Add an item to a tuple

Given:

fruits = ("apple", "banana", "mango")

Add "orange" to the tuple.

Print the updated tuple."""

print("Solution 26")
fruits = ("apple", "banana", "mango")
fruits = list(fruits)
fruits.append("orange")
fruits = tuple(fruits)
print(fruits)

"""27. Remove an item from a tuple

Given:

numbers = (10, 20, 30, 40, 50)

Remove 30 from the tuple.

Do this by creating a new tuple."""

print("Solution 27")

numbers = (10, 20, 30, 40, 50)

numbers = numbers[0:2]+numbers[3:]
print(numbers)

"""28. Convert, modify, and convert back

Given:

fruits = ("apple", "banana", "mango")

Perform the following steps:

Convert the tuple into a list.
Add "orange".
Remove "banana".
Convert the list back into a tuple.
Print the final tuple."""

print("Solution 28")
fruits = ("apple", "banana", "mango")
fruits = list(fruits)
fruits.append("orange")
fruits.remove("banana")
fruits = tuple(fruits)
print(fruits)

"""Level 7: Logic-Building Questions
29. Find the maximum and minimum values

Given:

sales = (45000, 60000, 35000, 80000, 55000)

Find and print:

The highest sales value
The lowest sales value"""

print("Solution 29")

sales = (45000, 60000, 35000, 80000, 55000)

highest_sales = max(sales)
lowest_sales = min(sales)

print("The highest sales value :" , highest_sales)
print("The lowest sales value :" , lowest_sales)

"""30. Analyze student marks

Given:

students = (
    ("Ali", 85),
    ("Sara", 72),
    ("Naila", 91),
    ("John", 65),
    ("Maya", 78)
)

Write a program that:

Uses a loop to go through each student's tuple.
Unpacks the student's name and marks.
Prints the student's name and marks.
Prints "Passed with distinction" if marks are 80 or above.
Prints "Passed" if marks are 50 or above but less than 80.
Prints "Failed" if marks are below 50."""

print("Solution 30")

students = (
    ("Ali", 85),
    ("Sara", 72),
    ("Naila", 91),
    ("John", 65),
    ("Maya", 78)
)

for items in students:
    name , marks = items
    print(name , marks)

    if marks >=80:
        print("Passed with distinction")
    elif marks >=50:
        print("Passed")
    else:
        print("Failed")

    
