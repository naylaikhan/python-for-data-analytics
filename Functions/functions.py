"""🟢 Level 1 — Function Basics
1. Create a Simple Function

Create a function called greet() that prints:

Hello, Python!

Call the function."""

print("Solution 1")

def greet():
    print("Hello , Python")

greet()

"""2. Welcome Message

Create a function called welcome() that prints:

Welcome to Python Programming

Call it three times."""

print("Solution 2")

def welcome():
    print("Welcome to Python Programming")

welcome()
welcome()
welcome()

"""3. Print Your Name

Create a function called show_name() that prints your name.

Call the function."""

print("Solution 3")

def show_name():
    print("Naila")

show_name()

"""4. Print Numbers

Create a function called print_numbers() that prints the numbers:

1
2
3
4
5

Call the function."""

print("Solution 4")

def print_numbers():
    for num in range(1,6):
        print(num)

print_numbers()       

"""5. Function With One Parameter

Create a function called greet_user(name).

It should print:

Hello Naila

when called as:

greet_user("Naila")"""

print("Solution 5")

def greet_user(name):
    print("Hello",name)

greet_user("Naila")

"""6. Square of a Number

Create a function called square(number).

It should return the square of the given number.

Example:

square(5)

Expected result:

25"""

print("Solution 6")

def square(number):
    return number ** 2

square_number = square(5)
print(square_number)

"""7. Cube of a Number

Create a function called cube(number).

It should return the cube of the number.

Example:

cube(3)

Expected result:

27"""

print("Solution 7")

def cube(number):
    return number ** 3

print(cube(3))

"""8. Add Two Numbers

Create a function called add(a, b).

It should return the sum of two numbers.

Example:

add(10, 20)

Expected result:

30"""

print("Solution 8")

def add(a,b):
    return a + b

print(add(10,20))

"""9. Subtract Two Numbers

Create a function called subtract(a, b).

It should return:

a - b

Test it with:

subtract(20, 8)"""

print("Solution 9")

def subtract(a,b):
    return a - b 

print(subtract(20,8))

"""10. Multiply Two Numbers

Create a function called multiply(a, b).

It should return the multiplication of two numbers.

Test:

multiply(6, 7)"""

print("Solution 10")

def multiply(a,b):
    return a * b

print(multiply(6,7))

"""🟢 Level 2 — Parameters and Return Values
11. Divide Two Numbers

Create a function called divide(a, b) that returns the result of:

a / b

Test it with:

divide(20, 5)"""

print("Solution 11")

def divide(a,b):
    return a / b

print(divide(20,5))

"""12. Calculate Rectangle Area

Create a function:

rectangle_area(length, width)

Return the area of the rectangle.

Formula:

length × width"""

print("Solution 12")

def rectangle_area(length,width):
    return length * width

print("Area of the Rectangle:" ,rectangle_area(12,10))

"""13. Calculate Rectangle Perimeter

Create:

rectangle_perimeter(length, width)

Return the perimeter.

Formula:

2 × (length + width)"""

print("Solution 13")

def rectangle_perimeter(length,width):
    perimeter = 2 * (length + width)
    return perimeter

print("Perimeter:" , rectangle_perimeter(10,12) )

"""14. Calculate Circle Area

Create:

circle_area(radius)

Use:

π × radius²

You may use 3.14 for π."""

print("Solution 14")

def circle_area(radius):
    return 3.14 * radius ** 2

print("Area of Circle:",circle_area(8))

"""15. Check Even Number

Create:

is_even(number)

The function should return:

True

if the number is even and:

False

if it is odd."""

print("Solution 15")

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))
print(is_even(7))

"""16. Check Positive Number

Create:

is_positive(number)

Return True if the number is positive and False otherwise.

Test it with positive, negative, and zero values."""

print("Solution 16")

def is_positive(number):
    if number > 0:
        return True
    elif number < 0:
        return False
    else:
        return False

print(is_positive(3))
print(is_positive(-3))
print(is_positive(0))

"""17. Check Adult

Create:

is_adult(age)

Return True if age is 18 or above.

Otherwise return False."""

print("Solution 17")

def is_adult(age):
    if age >= 18:
        return True
    else:
        return False

print(is_adult(20))
print(is_adult(10))

"""18. Find the Larger Number

Create:

find_larger(a, b)

Return whichever number is larger.

Example:

find_larger(10, 25)

Expected result:

25"""

print("Solution 18")

def find_larger(a, b):
    if a > b :
        return a
    else:
        return b

print(find_larger(10,20))
print(find_larger(20,10))

"""19. Find the Smaller Number

Create:

find_smaller(a, b)

Return whichever number is smaller."""

print("Solution 19")

def find_smaller(a, b):
    if a > b:
        return b
    else:
        return a

print(find_smaller(10,30))
print(find_smaller(30,10))


"""20. Positive, Negative, or Zero

Create:

check_number(number)

Return:

"Positive"

if the number is positive,

"Negative"

if negative, and

"Zero"

if it is zero.
"""
print("Solution 20")

def check_number(number):
    if number > 0:
        print("Positive") 
    elif number < 0:
        print("Negative")  
    else:
        print("Zero")   

check_number(6)
check_number(-6)
check_number(0)

"""🟡 Level 3 — Default and Multiple Parameters
21. Greeting With Default Name

Create:

greet(name="Guest")

If a name is provided, greet that person.

If no name is provided, print:

Hello Guest

Test both cases."""

print("Solution 21")

def greet(name = "Guest"):
    print("Hello",name)

greet()
greet("Naila")

"""22. Calculate Discount

Create:

calculate_discount(price, discount=10)

The default discount should be 10%.

For example:

calculate_discount(1000)

should calculate the final price after a 10% discount.

Also test it with a different discount."""

print("Solution 22")

def calculate_discount(price, discount = 10):
    discounted_price = price - (price * 0.1)
    return discounted_price

print(calculate_discount(1000))
print(calculate_discount(2000))

"""23. Calculate Final Price With Tax

Create:

final_price(price, tax=18)

Calculate the price after adding the given percentage of tax.

Test the function using the default tax and a different tax percentage."""

print("Solution 23")

def final_price(price, tax=18):
    price_after_discount = price + (price * tax/100)
    return price_after_discount

default_tax = final_price(1000)
different_tax = final_price(1000,20)

print(default_tax)
print(different_tax)

"""24. Student Information

Create:

student_info(name, age, city)

The function should print:

Name: ...
Age: ...
City: ...

Test it using different students."""

print("Solution 24")

def student_info(name, age, city):
    print("Name:",name)
    print("Age:",age)
    print("City:",city)

student_info("Naila",25,"Delhi")
student_info("John",29,"Mumbai")

"""25. Employee Salary

Create:

calculate_salary(basic_salary, bonus)

Return:

basic salary + bonus

Test the function with at least three employees."""

print("Solution 25")

def calculate_salary(basic_salary, bonus):
    return basic_salary + bonus

print(calculate_salary(620000,50000))
print(calculate_salary(520000,40000))
print(calculate_salary(350000,20000))


"""26. Calculate Profit

Create:

calculate_profit(revenue, cost)

Return:

revenue - cost

Test:

calculate_profit(50000, 32000)"""

print("Solution 26")

def calculate_profit(revenue, cost):
    return revenue - cost

print(calculate_profit(50000,36000))
print(calculate_profit(50000,66000))

"""27. Calculate Percentage

Create:

calculate_percentage(obtained, total)

Return the percentage obtained.

For example:

calculate_percentage(450, 500)

should return:

90.0"""

print("Solution 27")

def calculate_percentage(obtained, total):
    return obtained/total * 100

print(calculate_percentage(450,500))

"""28. Convert Celsius to Fahrenheit

Create:

celsius_to_fahrenheit(celsius)

Use the formula:

F = (C × 9/5) + 32"""

print("Solution 28")

def celsius_to_fahrenheit(celsius):
    F = (celsius * 9/5) + 32
    return F

print(celsius_to_fahrenheit(33))


"""29. Convert Kilometers to Miles

Create:

km_to_miles(km)

Use:

1 kilometer = 0.621371 miles"""

print("Solution 29")

def km_to_miles(km):
    return km * 0.621371

print(km_to_miles(10))

"""30. Calculate Average of Three Numbers

Create:

average(a, b, c)

Return the average of the three numbers."""
print("Solution 30")

def average(a,b,c):
    result = (a+b+c)/3
    return result

print(average(2,4,6))

"""🟡 Level 4 — Functions + Lists"""
"""31. Sum of List

Given:

numbers = [10, 20, 30, 40, 50]

Create:

calculate_sum(numbers)

Return the sum of all numbers in the list."""

print("Solution 31")

numbers = [10, 20, 30, 40, 50]


def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total+=num

    return total

print(calculate_sum(numbers))


"""32. Average of List

Given:

numbers = [10, 20, 30, 40, 50]

Create:

calculate_average(numbers)

Return the average.
"""
print("Solution 32")

numbers = [10, 20, 30, 40, 50]

def calculate_average(numbers):
    final_result = sum(numbers)/len(numbers)
    return final_result

print(calculate_average(numbers))


"""33. Find Maximum

Create:

find_maximum(numbers)

Given:

numbers = [12, 45, 7, 89, 23]

Return the largest number."""

print("Solution 33")

numbers = [12, 45, 7, 89, 23]
def find_maximum(numbers):
    maximum_number = numbers[0]
    for num in numbers:
        if num > maximum_number:
            maximum_number = num

    return maximum_number

print(find_maximum(numbers))


"""34. Find Minimum

Create:

find_minimum(numbers)

Given:

numbers = [12, 45, 7, 89, 23]

Return the smallest number."""

print("Solution 34")
numbers = [12, 45, 7, 89, 23]

def find_minimum(numbers):
    minimum_number = numbers[0]
    for num in numbers:
        if num < minimum_number:
            minimum_number = num
    
    return minimum_number
    
print(find_minimum(numbers))

"""35. Count Even Numbers

Create:

count_even(numbers)

Given:

numbers = [1, 2, 4, 7, 8, 10, 13]

Return how many numbers are even.

Expected result:

4"""

print("Solution 35")
numbers = [1, 2, 4, 7, 8, 10, 13]

def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count+=1
            
    return count
print(count_even(numbers))

"""36. Count Positive Numbers

Create:

count_positive(numbers)

Given:

numbers = [-5, 10, -2, 8, -7, 0, 12]

Return the number of positive values."""

print("Solution 36")

numbers = [-5, 10, -2, 8, -7, 0, 12]
def count_positive(numbers):
    count = 0
    for num in numbers:
        if num > 0:
            count+=1

    return count

print(count_positive(numbers))

"""37. Find Sum of Positive Numbers

Create:

sum_positive(numbers)

Given:

numbers = [-5, 10, -2, 8, -7, 0, 12]

Return the sum of only the positive numbers."""

print("Solution 37")

numbers = [-5, 10, -2, 8, -7, 0, 12]

def sum_positive(numbers):
    total = 0
    for num in numbers:
        if num > 0:
            total+=num

    return total

print(sum_positive(numbers))       

"""38. Find Sum of Negative Numbers

Create:

sum_negative(numbers)

Given:

numbers = [-5, 10, -2, 8, -7, 0, 12]

Return the sum of only the negative numbers."""

print("Solution 38")

numbers = [-5, 10, -2, 8, -7, 0, 12]

def sum_negative(numbers):
    total = 0
    for num in numbers:
        if num < 0:
            total+=num

    return total

print(sum_negative(numbers))


"""39. Create a List of Squares

Create:

square_numbers(numbers)

Given:

numbers = [1, 2, 3, 4, 5]

Return:

[1, 4, 9, 16, 25]"""

print("Solution 39")

numbers = [1, 2, 3, 4, 5]

def square_numbers(numbers):
    new_numbers = []

    for num in numbers:
        result =  num ** 2
        new_numbers.append(result)

    return new_numbers

print(square_numbers(numbers))
    

"""40. Find Numbers Greater Than 50

Create:

greater_than_50(numbers)

Given:

numbers = [10, 65, 23, 78, 90, 45, 51]

Return a new list containing only numbers greater than 50.

Expected:

[65, 78, 90, 51]"""

print("Solution 40")

numbers = [10, 65, 23, 78, 90, 45, 51]
def greater_than_50(numbers):
    new_list = []

    for num in numbers:
        if num > 50:
            new_list.append(num)

    return new_list

print(greater_than_50(numbers))


"""🟠 Level 5 — Logic Building With Functions
41. Count Vowels

Create:

count_vowels(text)

Given:

text = "Python Programming"

Return the number of vowels in the string."""

print("Solution 41")
text = "Python Programming"

def count_vowels(text):
    count = 0
    for letter in text:
        if letter in "aeiou":
            count+=1

    return count

print(count_vowels(text))

"""42. Reverse a String

Create:

reverse_string(text)

Given:

"Python"

Return:

"nohtyP" """

print("Solution 42")

text = "Python"

def reverse_string(text):

    for letter in text:
        reversed_string = text[::-1]
        return reversed_string

print(reverse_string(text))

"""43. Check Palindrome

Create:

is_palindrome(text)

Return True if the word reads the same forward and backward.

For example:

is_palindrome("madam")

should return:

True

Test it with both palindrome and non-palindrome words."""

print("Solution 43")

def is_palindrome(text):
    reverse_string = text[::-1]
    if text == reverse_string:
        return True
    else:
        return False

print(is_palindrome("madam"))
print(is_palindrome("camel"))


"""44. Count Words

Create:

count_words(sentence)

Given:

sentence = "Python is easy to learn"

Return the number of words.

Expected:

5"""

print("Solution 44")
sentence = "Python is easy to learn"

def count_words(sentence):
    count = len(sentence.split(" "))
    return count

print(count_words(sentence))

"""45. Remove Duplicates

Create:

remove_duplicates(numbers)

Given:

numbers = [1, 2, 2, 3, 4, 4, 5, 5]

Return a collection containing only unique values.

Expected:

[1, 2, 3, 4, 5]"""

print("Solution 45")

numbers = [1, 2, 2, 3, 4, 4, 5, 5]

def remove_duplicates(numbers):
    new_number = set(numbers)
    return new_number

print(remove_duplicates(numbers))


"""46. Categorize Scores

Create:

categorize_score(score)

Return:

"Excellent" → 80 or above
"Good"      → 60–79
"Average"   → 40–59
"Fail"      → below 40

Test the function with different scores."""

print("Solution 46")

def categorize_score(score):
    if score >= 80:
        return "Excellent"
    elif score >=60:
        return "Good"
    elif score >=40:
        return "Average"
    else:
        return "Fail" 

print(categorize_score(89))
print(categorize_score(69))
print(categorize_score(49))
print(categorize_score(39))


"""47. Calculate Employee Performance

Create:

employee_performance(sales)

Rules:

sales >= 100000 → "Excellent"
sales >= 75000  → "Good"
sales >= 50000  → "Average"
sales < 50000   → "Needs Improvement"

Return the appropriate category."""

print("Solution 47")

def employee_performance(sales):
    if sales >= 100000:
        return "Excellent"
    elif sales >= 75000:
        return "Good"
    elif sales >= 50000:
        return "Average"
    else:
        return "Needs Improvement"

print(employee_performance(150000))
print(employee_performance(95000))
print(employee_performance(40000))
print(employee_performance(55000))

"""48. Calculate Statistics

Create a function:

calculate_statistics(numbers)

Given:

numbers = [10, 20, 30, 40, 50]

The function should calculate and return:

total
average
minimum
maximum

Store the returned results and print them separately."""

print("Solution 48")

numbers = [10, 20, 30, 40, 50]

def calculate_statistics(numbers):
    total = 0
    for num in numbers:
        total +=num

    average = total /len(numbers)
    minimum=min(numbers)
    maximum=max(numbers)
    return total ,average ,minimum ,maximum
    
total, average, minimum, maximum = calculate_statistics(numbers)

print("Total:", total)
print("Average:", average)
print("Minimum:", minimum)
print("Maximum:", maximum)

"""49. Analyze Sales Data

Given:

sales = [1200, 1500, 800, 2000, 1750, 950, 3000]

Create separate functions to calculate:

1. Total sales
2. Average sales
3. Highest sale
4. Lowest sale
5. Number of sales above 1000

Call all the functions and display the results."""

print("Solution 49")
sales = [1200, 1500, 800, 2000, 1750, 950, 3000]

def total_sales(sales):
    total = 0
    for sale in sales:
        total += sale
    return total

def average_sales(sales):
    average_sale = sum(sales)/len(sales)
    return average_sale

def highest_sale(sales):
    return max(sales)

def lowest_sale(sales):
    return min(sales)

def sales_above(sales):
    count =0
    for sale in sales:
        if sale > 1000:
            count+=1
    return count

print("Total sales:",total_sales(sales))
print("Average sales:",average_sales(sales))
print("Highest sale:",highest_sale(sales))
print("Lowest sale:",lowest_sale(sales))
print("Number of sales above 1000:",sales_above(sales))

"""🔴 Level 6 — Advanced Logic / Data Analytics
50. Website Visitors Analysis

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

Create separate functions to find:

All unique visitors across the three days.
Visitors who visited on all three days.
Visitors who visited on only one day.
Total number of unique visitors.
Visitors who visited on Monday and Tuesday but not Wednesday."""

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

def unique_visitors(monday,tuesday,wednesday):
    unique_visitors_all = monday | tuesday |wednesday
    total_unique_visitor = len(unique_visitors_all)
    return unique_visitors_all , total_unique_visitor

unique_visitors_all_days , total_unique_visitors = unique_visitors(monday,tuesday,wednesday)

def all_three_days(monday,tuesday,wednesday):
    visited_all_day = monday & tuesday & wednesday
    return visited_all_day

def Mon_Tue_not_Wed(monday,tuesday,wednesday):
    Mons_Tues_not_Weds = (monday & tuesday) - wednesday
    return Mons_Tues_not_Weds

def only_one_day(monday, tuesday, wednesday):

    monday_only = monday - tuesday - wednesday
    tuesday_only = tuesday - monday - wednesday
    wednesday_only = wednesday - monday - tuesday

    return monday_only | tuesday_only | wednesday_only

print("All unique visitors across the three days" , unique_visitors_all_days)
print("Visitors who visited on all three days",all_three_days(monday,tuesday,wednesday))
print("Visitors who visited on only one day:",only_one_day(monday, tuesday, wednesday))
print("Total number of unique visitors :", total_unique_visitors)
print("Visitors who visited on Monday and Tuesday but not Wednesday.",Mon_Tue_not_Wed(monday,tuesday,wednesday))

