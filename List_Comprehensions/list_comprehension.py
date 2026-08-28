"""Level 1 — Basic List Comprehension
1. Double Every Number

Given:

numbers = [1, 2, 3, 4, 5]

Create a new list containing every number multiplied by 2.

Expected output:

[2, 4, 6, 8, 10]"""

print("Solution 1")

numbers = [1, 2, 3, 4, 5]

new_list = [ number * 2 for number in numbers]
print(new_list)

"""2. Square Every Number

Given:

numbers = [1, 2, 3, 4, 5]

Create a new list containing the square of every number.

Expected output:

[1, 4, 9, 16, 25]"""

print("Solution 2")
numbers = [1, 2, 3, 4, 5]

new_list = [ number **2 for number in numbers]
print(new_list)

"""3. Create a List of Numbers

Using range() and list comprehension, create a list containing numbers from 1 to 10.

Expected output:

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"""

print("Solution 3")

numbers = [number for number in range(1,11)]
print(numbers)

"""4. Create Cubes

Given:

numbers = [1, 2, 3, 4, 5]

Create a new list containing the cube of each number.

Expected output:

[1, 8, 27, 64, 125]"""

print("Solution 4")
numbers = [1, 2, 3, 4, 5]

new_list = [number ** 3 for number in numbers]
print(new_list)

"""5. Convert Words to Uppercase

Given:

words = ["python", "sql", "excel", "power bi"]

Create a new list where every word is converted to uppercase.

Expected output:

["PYTHON", "SQL", "EXCEL", "POWER BI"]"""

print("Solution 5")

words = ["python", "sql", "excel", "power bi"]

new_list = [word.upper() for word in words]
print(new_list)

"""6. Find Length of Each Word

Given:

words = ["python", "sql", "excel", "tableau"]

Create a list containing the length of every word.

Expected output:

[6, 3, 5, 7]"""

print("Solution 6")

words = ["python", "sql", "excel", "tableau"]

new_list = [len(word) for word in words]
print(new_list)

"""7. Add 10 to Every Number

Given:

numbers = [5, 10, 15, 20, 25]

Create a new list by adding 10 to every number.

Expected output:

[15, 20, 25, 30, 35]"""

print("Solution 7")

numbers = [5, 10, 15, 20, 25]

new_list = [number + 10 for number in numbers]
print(new_list)

"""8. Convert Strings to Integers

Given:

numbers = ["10", "20", "30", "40", "50"]

Create a new list containing these values as integers.

Expected output:

[10, 20, 30, 40, 50]"""

print("Solution 8")

numbers = ["10", "20", "30", "40", "50"]

new_list = [int(number) for number in numbers]
print(new_list)

"""Level 2 — Filtering With if
9. Find Even Numbers

Given:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Create a new list containing only the even numbers.

Expected output:

[2, 4, 6, 8, 10]"""

print("Solution 9")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = [ number for number in numbers if number % 2 == 0 ]
print(new_list)

"""10. Find Odd Numbers

Given:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Create a new list containing only the odd numbers.

Expected output:

[1, 3, 5, 7, 9]"""

print("Solution 10")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = [number for number in numbers if number % 2 != 0]
print(new_list)

"""11. Numbers Greater Than 50

Given:

numbers = [10, 65, 32, 89, 45, 72, 12, 100]

Create a new list containing only numbers greater than 50.

Expected output:

[65, 89, 72, 100]"""

print("Solution 11")

numbers = [10, 65, 32, 89, 45, 72, 12, 100]

new_list = [number for number in numbers if number > 50]
print(new_list)


"""12. Numbers Less Than 20

Given:

numbers = [5, 25, 10, 40, 15, 30, 8]

Create a new list containing only numbers less than 20.

Expected output:

[5, 10, 15, 8]"""

print("Solution 12")

numbers = [5, 25, 10, 40, 15, 30, 8]

new_list = [number for number in numbers if number < 20]
print(new_list)

"""13. Find Positive Numbers

Given:

numbers = [-5, 10, -3, 8, 0, -1, 7, 12]

Create a new list containing only positive numbers.

Expected output:

[10, 8, 7, 12]"""

print("Solution 13")
numbers = [-5, 10, -3, 8, 0, -1, 7, 12]

new_list = [number for number in numbers if number > 0]
print(new_list)

"""14. Find Numbers Divisible by 5

Given:

numbers = [10, 12, 15, 23, 25, 31, 40, 42]

Create a new list containing only numbers divisible by 5.

Expected output:

[10, 15, 25, 40]"""

print("Solution 14")

numbers = [10, 12, 15, 23, 25, 31, 40, 42]

new_list = [number for number in numbers if number % 5 == 0]
print(new_list)

"""15. Find Long Words

Given:

words = ["cat", "elephant", "dog", "python", "hi", "computer"]

Create a new list containing only words whose length is greater than 5.

Expected output:

["elephant", "python", "computer"]
Level 3 — Filtering + Transformation"""

print("Solution 15")
words = ["cat", "elephant", "dog", "python", "hi", "computer"]

new_list = [word for word in words if len(word) > 5]
print(new_list)

"""16. Square Only Even Numbers

Given:

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

Create a new list containing the squares of only the even numbers.

Expected output:

[4, 16, 36, 64]"""

print("Solution 16")
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

new_list = [number **2 for number in numbers if number % 2 == 0]
print(new_list)

"""17. Double Only Numbers Greater Than 10

Given:

numbers = [5, 12, 8, 20, 15, 3, 25]

Create a new list containing numbers greater than 10, with each selected number multiplied by 2.

Expected output:

[24, 40, 30, 50]"""

print("Solution 17")

numbers = [5, 12, 8, 20, 15, 3, 25]
new_list = [number * 2 for number in numbers if number > 10]
print(new_list)

"""18. Convert Only Positive Numbers

Given:

numbers = [-10, 20, -5, 30, 40, -2]

Create a new list containing the squares of only the positive numbers.

Expected output:

[400, 900, 1600]"""

print("Solution 18")

numbers = [-10, 20, -5, 30, 40, -2]

new_list = [number ** 2 for number in numbers if number > 0]
print(new_list)

"""19. Uppercase Long Words

Given:

words = ["cat", "elephant", "dog", "python", "computer", "sql"]

Create a new list containing only words whose length is greater than 4, and convert those words to uppercase.

Expected output:

["ELEPHANT", "PYTHON", "COMPUTER"]"""

print("Solution 19")

words = ["cat", "elephant", "dog", "python", "computer", "sql"]

new_list = [word.upper() for word in words if len(word) > 4]
print(new_list)


"""20. Discounted Prices

Given:

prices = [100, 250, 500, 750, 1000]

Create a new list containing prices after applying a 10% discount.

Expected output:

[90.0, 225.0, 450.0, 675.0, 900.0]"""

print("Solution 20")

prices = [100, 250, 500, 750, 1000]

new_list = [price - (price * 0.1) for price in prices]
print(new_list)


"""Level 4 — if...else Inside List Comprehension"""
"""21. Pass or Fail

Given:

marks = [85, 35, 72, 40, 28, 90]

Create a new list where:

marks >= 40 become "Pass"
marks < 40 become "Fail"

Expected output:

["Pass", "Fail", "Pass", "Pass", "Fail", "Pass"]"""

print("Solution 21")

marks = [85, 35, 72, 40, 28, 90]

new_list = ["Pass" if mark>= 40 else "Fail" for mark in marks]
print(new_list)

"""22. Even or Odd

Given:

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

Create a new list where each number is replaced with either "Even" or "Odd".

Expected output:

["Odd", "Even", "Odd", "Even", "Odd", "Even", "Odd", "Even"]"""

print("Solution 22")
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

new_list = ["Even" if number % 2 == 0 else "Odd" for number in numbers]
print(new_list)

"""23. Positive or Negative

Given:

numbers = [-5, 10, -2, 8, -7, 0, 12]

Create a new list where:

positive numbers become "Positive"
negative numbers become "Negative"
0 becomes "Zero"

Expected output:

["Negative", "Positive", "Negative", "Positive", "Negative", "Zero", "Positive"]"""

print("Solution 23")
numbers = [-5, 10, -2, 8, -7, 0, 12]

new_list = ["Positive" if number > 0 else "Negative" if number < 0  else "Zero" for number in numbers]
print(new_list)


"""24. Adult or Minor

Given:

ages = [12, 18, 25, 15, 30, 17, 40]

Create a new list where each age is replaced with:

"Adult" if age is 18 or above
"Minor" otherwise

Expected output:

["Minor", "Adult", "Adult", "Minor", "Adult", "Minor", "Adult"]"""

print("Solution 24")

ages = [12, 18, 25, 15, 30, 17, 40]

new_list = ["Adult" if age >= 18 else "Minor" for age in ages]
print(new_list)

"""25. Replace Negative Numbers

Given:

numbers = [10, -5, 20, -8, 30, -2, 40]

Create a new list where:

positive numbers remain unchanged
negative numbers are replaced with 0

Expected output:

[10, 0, 20, 0, 30, 0, 40]
Level 5 — Strings and More Logic"""

print("Solution 25")

numbers = [10, -5, 20, -8, 30, -2, 40]

new_list = [num if num > 0 else 0 for num in numbers ]
print(new_list)

"""26. Extract Vowels

Given:

text = "programming"

Create a list containing only the vowels present in the string.

Expected output:

["o", "a", "i"]"""

print("Solution 26")
text = "programming"

new_string = [char for char in text if char in "aeoiu"]
print(new_string)

"""27. Extract Uppercase Letters

Given:

text = "PyThOn Is FuN"

Create a list containing only the uppercase characters.

Expected output:

["P", "T", "O", "I", "F", "N"]"""

print("Solution 27")

text = "PyThOn Is FuN"

upcase_char = [char for char in text if char in (text.replace(" ","").upper())]
print(upcase_char)


"""28. Clean Names

Given:

names = ["  Ali", "Sara  ", "  John  ", "Naila", "  David"]

Create a new list where the unnecessary spaces at the beginning and end of every name are removed.

Expected output:

["Ali", "Sara", "John", "Naila", "David"]"""

print("Solution 28")

names = ["  Ali", "Sara  ", "  John  ", "Naila", "  David"]

new_names = [name.strip(" ") for name in names]
print(new_names)

"""Level 6 — Nested List Comprehension
29. Flatten a Nested List

Given:

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Create a single list containing all the numbers.

Expected output:

[1, 2, 3, 4, 5, 6, 7, 8, 9]"""

print("Solution 29")

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_list = [ num for row in numbers for num in row ]
print(new_list)

"""30. Flatten and Filter

Given:

numbers = [
    [1, 8, 3],
    [12, 5, 20],
    [7, 15, 2]
]

Using list comprehension, create a single list containing only numbers greater than 5.

Expected output:

[8, 12, 20, 7, 15]"""

print("Solution 30")

numbers = [
    [1, 8, 3],
    [12, 5, 20],
    [7, 15, 2]
]

new_list = [num for row in numbers for num in row if num > 5]
print(new_list)