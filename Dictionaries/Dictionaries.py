"""1.Create a dictionary called student with the following information:
Name: Naila
Age: 25
City: Delhi
Print the dictionary."""
print("Solution 1")
student = {
    "Name" : "Naila",
    "Age"  : 25 ,
    "City" : "Delhi"
}

print(student)

"""2. Access a value.Given:
student = {
    "name": "Naila",
    "age": 25,
    "city": "Delhi"
}
Print only the student's name."""
print("Solution 2")
student = {
    "Name" : "Naila",
    "Age"  : 25 ,
    "City" : "Delhi"
}

print(student["Name"])

"""3. Access another value.Using the same dictionary, print the student's age."""
print("Solution 3")
student = {
    "Name" : "Naila",
    "Age"  :  25,
    "City" : "Delhi"
}

print(student["Age"])

"""4. Add a new key-value pair.Given:
student = {
    "name": "Naila",
    "age": 25
}
Add:city → Delhi.Print the updated dictionary."""
print("Solution 4")
student = {
    "name": "Naila",
    "age": 25
}

student["City"] = "Delhi"
print(student)

"""5. Update a value.Given:
employee = {
    "name": "John",
    "salary": 50000
}
Update the salary to 60000."""
print("Solution 5")

employee = {
    "name" : "John",
    "salary":50000
}
print(employee)
employee["salary"] = 60000
print(employee)

"""6. Find the number of items.Given:
product = {
    "name": "Laptop",
    "price": 50000,
    "category": "Electronics"
}
Print the number of key-value pairs."""

print("Solution 6")

product = {
    "name" : "Laptop",
    "price" : 50000,
    "category" : "Electronics"
}
print(product)
print(len(product))

"""7. Check whether a key exists.Given:
student = {
    "name": "Naila",
    "age": 25
}
Check whether the key "age" exists.
Print:Age exists if it exists."""

print("Solution 7")

student = {
    "name": "Naila",
    "age": 25
}

if "age" in student:
    print("Age exists")

"""8. Check whether a key does not exist.Using the same dictionary, check whether "city" exists.
If it does not exist, print:City not found"""
print("Solution 8")
student = {
    "name": "Naila",
    "age": 25
}

print(student.get("city" , "City not found"))

"""9. Safely access a missing key.Given:
employee = {
    "name": "John",
    "salary": 50000
}
Try to get the value of "department" without causing a KeyError."""

print("Solution 9")
employee = {
    "name": "John",
    "salary": 50000
}

print(employee.get("department" , "not found"))

"""10. Use .get() with a default value.Using the same dictionary, get "department".
If it doesn't exist, return:Not Available"""

print("Solution 10")
employee = {
    "name": "John",
    "salary": 50000
}

print(employee.get("department" , "not found"))

"""11. Remove a specific item.Given:
student = {
    "name": "Naila",
    "age": 25,
    "city": "Delhi"
}
Remove "age" using pop()."""

print("Solution 11")
student = {
    "name": "Naila",
    "age": 25,
    "city": "Delhi"
}

print(student)
print(student.pop("age"))
print(student)

"""12. Store the removed value.Using:
employee = {
    "name": "John",
    "salary": 50000,
    "department": "Sales"
}
Remove "salary" using pop() and store the removed value in a variable called salary.Print the removed salary."""
print("Solution 12")
employee = {
    "name": "John",
    "salary": 50000,
    "department": "Sales"
}

print(employee)
salary = employee.pop("salary")
print(salary)
print(employee)

"""13. Remove the last inserted item.Given:
data = {
    "name": "Naila",
    "age": 25,
    "city": "Delhi"
}
Remove the last inserted item using popitem()."""
print("Solution 13")
data = {
    "name": "Naila",
    "age": 25,
    "city": "Delhi"
}

print(data)
print(data.popitem())
print(data)

"""14. Remove an item using del.Given:
student = {
    "name": "Naila",
    "age": 25,
    "city": "Delhi"
}
Delete "city" using del."""

print("Solution 14")

student = {
    "name": "Naila",
    "age": 25,
    "city": "Delhi"
}

print(student)
del student["city"]
print(student)

"""15. Clear a dictionary.Given:
data = {
    "a": 10,
    "b": 20,
    "c": 30
}
Remove all items but keep the dictionary variable."""

print("Solution 15")

data = {
    "a": 10,
    "b": 20,
    "c": 30
}

print(data)
data.clear()
print(data)

"""16.Given:
student = {
    "name": "Naila",
    "age": 25
}
Write code that changes "age" to 26 and adds "city" as "Delhi".Think about this:Does Python use different syntax for adding and updating?"""

print("Solution 16")

student = {
    "name": "Naila",
    "age": 25
}

print(student)
student["age"] = 26
student["city"] = "Delhi"
print(student)

"""17. Print all keys.Given:
employee = {
    "name": "John",
    "age": 30,
    "department": "HR"
}
Print all the keys."""

print("Solution 17")
employee = {
    "name": "John",
    "age": 30,
    "department": "HR"
}

for key in employee.keys():
    print(key)

"""18. Print all values.Using the same dictionary, print all the values."""
print("Solution 18")
employee = {
    "name": "John",
    "age": 30,
    "department": "HR"
}

for value in employee.values():
    print(value)

"""19. Print all key-value pairs.Print all items using .items().
Expected style:
name John
age 30
department HR"""

print("Solution 19")
employee = {
    "name": "John",
    "age": 30,
    "department": "HR"
}

for key , value in employee.items():
    print(key , value)

"""20. Loop through keys.Given:
student = {
    "name": "Naila",
    "age": 25,
    "city": "Delhi"
}
Use a loop to print only the keys."""

print("Solution 20")

student = {
    "name": "Naila",
    "age": 25,
    "city": "Delhi"
}

for key in student.keys():
    print(key)

"""21. Loop through values.Use a loop to print only the values."""

print("Solution 21")

student = {
    "name": "Naila",
    "age": 25,
    "city": "Delhi"
}

for value in student.values():
    print(value)

"""22. Loop through both keys and values.Use .items() and print:
name : Naila
age : 25
city : Delhi"""

print("Solution 22")

student = {
    "name": "Naila",
    "age": 25,
    "city": "Delhi"
}

for key , value in student.items():
    print(key , value)

"""23. Check whether a value exists.Given:
student = {
    "name": "Naila",
    "city": "Delhi"
}
Check whether "Delhi" exists as a value."""
print("Solution 23")
student = {
    "name": "Naila",
    "city": "Delhi"
}

print("Delhi" in student.values())

"""24.What will this print?
student = {
    "name": "Naila",
    "city": "Delhi"
}
print("Delhi" in student)
First predict the answer, then run it.
Explain why.
Solution - It will through key error because "Delhi" is a value not a key"""
print("Solution 24")
print("It will through key error because Delhi is a value not a key")

"""25.Given:
student1 = {
    "name": "Naila",
    "age": 25
}
student2 = student1
student2["age"] = 30
Print student1.
Then answer:
Why did student1 also change? 
Solution : Age will change is student1 as well because both student1 and student2 are
the object referencing the same dictionary"""
print("Solution 25")
student1 = {
    "name": "Naila",
    "age": 25
}
student2 = student1
student2["age"] = 30
print(student1)
print("Age will change is student1 as well because both student1 and student2 are" \
"the object referencing the same dictionary")

"""26.Solve the previous problem using .copy() so that changing student2 does not change student1."""
print("Solution 26")
student1 = {
    "name": "Naila",
    "age": 25
}

student2 = student1.copy()
student2["age"] = 30
print(student1)
print(student2)

"""27.Create a copy of:using dict().
data = {
    "name": "Laptop",
    "price": 50000
}"""

print("Solution 27")
data= {
    "name" : "Laptop",
    "price" : 50000
}

data1 = dict(data)
print(data)
print(data1)

"""28.Given:
student = {
    "name": "Naila",
    "age": 25
}
Using .update():
Change age to 26
Add city as "Delhi" """
print("Solution 28")
student = {
    "name": "Naila",
    "age": 25
}
print(student)

student.update({
    "age" : 26,
    "city" : "Delhi"
})
print(student)

"""29.Given:
personal_info = {
    "name": "Naila",
    "age": 25
}
location_info = {
    "city": "Delhi",
    "country": "India"
}
Merge location_info into personal_info."""
print("Solution 29")
personal_info = {
    "name": "Naila",
    "age": 25
}

location_info = {
    "city": "Delhi",
    "country": "India"
}

personal_info.update(location_info)
print(personal_info)

"""30.Given:
data1 = {
    "name": "Naila",
    "age": 25
}

data2 = {
    "age": 30,
    "city": "Delhi"
}
Merge data2 into data1.What will happen to "age"?"""
print("Solution 30")

data1 = {
    "name": "Naila",
    "age": 25
}

data2 = {
    "age": 30,
    "city": "Delhi"
}

data1.update(data2)
print(data1)
print("The Last recent age used will be picked by python")

"""31.Given:
student = {
    "name": "Naila",
    "address": {
        "city": "Delhi",
        "country": "India"
    }
}
Print "Delhi"."""
print("Solution 31")
student = {
    "name": "Naila",
    "address": {
        "city": "Delhi",
        "country": "India"
    }
}

print(student["address"]["city"])

"""32. Access deeper nested data
Given:
company = {
    "employee": {
        "name": "John",
        "details": {
            "age": 30,
            "city": "Delhi"
        }
    }
}

Print John's city."""

print("Solution 32")
company = {
    "employee": {
        "name": "John",
        "details": {
            "age": 30,
            "city": "Delhi"
        }
    }
}

print("John's city is : ", company["employee"]["details"]["city"])

"""33. Update nested data

Using the previous dictionary, change John's age from 30 to 31."""

print("Solution 33")

company = {
    "employee": {
        "name": "John",
        "details": {
            "age": 30,
            "city": "Delhi"
        }
    }
}
print(company)
company["employee"]["details"]["age"] = 31
print(company)

"""34. Given:
student = {
    "name": "Naila",
    "address": {
        "city": "Delhi"
    }
}
Add:country → India inside "address"."""

print("Solution 34")
student = {
    "name": "Naila",
    "address": {
        "city": "Delhi"
    }
}

print(student)
student["address"]["country"] = "India"
print(student)

"""35. Access an item from a list inside a dictionary

Given:

student = {
    "name": "Naila",
    "skills": ["Python", "SQL", "Excel"]
}

Print "SQL"."""

print("Solution 35")

student = {
    "name": "Naila",
    "skills": ["Python", "SQL", "Excel"]
}

print(student["skills"][1])

"""36. Using the same dictionary, add "Power BI" to the skills list."""

print("Solution 36")
student = {
    "name": "Naila",
    "skills": ["Python", "SQL", "Excel"]
}

print(student)
student["skills"].append("Power BI")
print(student)

"""37.Given:
employees = [
    {
        "name": "Naila",
        "salary": 50000
    },
    {
        "name": "John",
        "salary": 60000
    }
]
Print John's salary."""

print("Solution 37")
employees = [
    {
        "name": "Naila",
        "salary": 50000
    },
    {
        "name": "John",
        "salary": 60000
    }
]

print("John's salary is :",employees[1]["salary"])

"""38. Calculate total salary

Using the same employees list, calculate the total salary of all employees.

Use a loop."""

print("Solution 38")

employees = [
    {
        "name": "Naila",
        "salary": 50000
    },
    {
        "name": "John",
        "salary": 60000
    }
]

total = 0

for employee in employees:
    total = total + employee["salary"]

print(f"Total Salary is {total}")

"""39. Find employees earning above 50,000
Given:
employees = [
    {"name": "Naila", "salary": 50000},
    {"name": "John", "salary": 60000},
    {"name": "Sara", "salary": 70000},
    {"name": "Mike", "salary": 45000}
]
Print the names of employees whose salary is greater than 50000."""

print("Solution 39")
employees = [
    {"name": "Naila", "salary": 50000},
    {"name": "John", "salary": 60000},
    {"name": "Sara", "salary": 70000},
    {"name": "Mike", "salary": 45000}
]

name_list = []
for employee in employees:
    if employee["salary"] > 50000:
        name_list.append(employee["name"])

print(name_list)

"""40. Count the frequency of numbers

Given:

numbers = [1, 2, 3, 1, 2, 1, 4, 3, 2, 1]

Create a dictionary that counts how many times each number appears.

Expected result:

{
    1: 4,
    2: 3,
    3: 2,
    4: 1
} """

print("Solution 40")

numbers = [1, 2, 3, 1, 2, 1, 4, 3, 2, 1]

data ={}

for num in numbers:
    if num in data:
        data[num] = data[num] + 1

    else:
        data[num] =1

print(data)

"""41. Frequency count using .get()

Solve Question 40 again, but this time use:

dictionary.get(key, default)"""

print("Solution 41")

numbers = [1, 2, 3, 1, 2, 1, 4, 3, 2, 1]

frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

print(frequency)

"""42. Count words

Given:

words = [
    "python",
    "sql",
    "python",
    "excel",
    "sql",
    "python"
]

Create a dictionary showing the frequency of each word.

Expected:

{
    "python": 3,
    "sql": 2,
    "excel": 1
}"""

print("Solution 42")
words = [
    "python",
    "sql",
    "python",
    "excel",
    "sql",
    "python"
]

data = {}

for word in words:
    if word in data:
        data[word] = data[word] + 1
    else:
        data[word] = 1

print(data)

"""43. Find the highest value

Given:

sales = {
    "January": 50000,
    "February": 75000,
    "March": 60000
}

Find the month with the highest sales.

Do not just print the maximum number. Print the month name.

Expected:

February"""

print("Solution 43")

sales = {
    "January": 50000,
    "February": 75000,
    "March": 60000
}

max_sales = max(sales.values())

for key , value in sales.items():
    if max_sales == value:
        print(f"the Month with the highest sales is {key} with {max_sales} sale")

"""44. Find the lowest value. Using the same sales dictionary, find the month with the lowest sales."""
print("Solution 44")
sales = {
    "January": 50000,
    "February": 75000,
    "March": 60000
}

min_sale = min(sales.values())
print(min_sale)

for key , value in sales.items():
    if min_sale == value:
        print(f"the Month with the Lowest sales is {key} with {min_sale} sale")


"""45. Calculate total and average

Given:

marks = {
    "Math": 80,
    "Science": 90,
    "English": 85,
    "Computer": 95
}

Calculate:

Total marks
Average marks"""

print("Solution 45")

marks = {
    "Math": 80,
    "Science": 90,
    "English": 85,
    "Computer": 95
}

total = sum(marks.values())
average_mark = sum(marks.values()) / len(marks)

print(f"Total marks is : {total}")
print(f"Average mark is : {average_mark}")

"""46. Find students who passed

Given:

students = {
    "Naila": 85,
    "John": 45,
    "Sara": 90,
    "Mike": 35,
    "Anna": 60
}

A student passes if marks are 50 or above.

Print the names of all students who passed."""

print("Solution 46")

students = {
    "Naila": 85,
    "John": 45,
    "Sara": 90,
    "Mike": 35,
    "Anna": 60
}

passed_students_lists = []

for key , value in students.items():
    if value >= 50:
        passed_students_lists.append(key)


print(passed_students_lists)



"""47. Separate pass and fail students

Using the same dictionary, create two new dictionaries:

passed = {}
failed = {}

Store students with marks:

50 or above → passed
Below 50 → failed

Expected:

passed = {
    "Naila": 85,
    "Sara": 90,
    "Anna": 60
}

failed = {
    "John": 45,
    "Mike": 35
} """

print("Solution 47")

students = {
    "Naila": 85,
    "John": 45,
    "Sara": 90,
    "Mike": 35,
    "Anna": 60
}

passed = {}
failed = {}

for key , value in students.items():
    if value >= 50:
        passed[key] = value
    else:
        failed[key] = value

print("Passed :" , passed)
print("Failed :" , failed)

"""48. Find the student with the highest marks

Using:

students = {
    "Naila": 85,
    "John": 45,
    "Sara": 90,
    "Mike": 35,
    "Anna": 60
}

Find the student with the highest marks."""

print("Solution 48")

highest_mark = max(students.values())

for key , value in students.items():
   if  highest_mark == value:
       print(f"{key} scored the Highest marks {highest_mark}")


"""49. Count character frequency

Given:

text = "programming"

Create a dictionary that counts how many times each character appears.

For example:

p → 1
r → 2
o → 1
g → 2
...

Ignore nothing for now—count every character exactly as it appears."""

print("Solution 49")

text = "programming"

count = {}

for n in text:
    count[n] = count.get(n,0) + 1

print(count)


"""50. Data Analyst Challenge — Sales Summary

You are given sales transactions:

transactions = [
    {"product": "Laptop", "amount": 50000},
    {"product": "Mouse", "amount": 1000},
    {"product": "Laptop", "amount": 50000},
    {"product": "Keyboard", "amount": 2000},
    {"product": "Mouse", "amount": 1000},
    {"product": "Laptop", "amount": 50000}
]

Create a dictionary that calculates the total sales amount for each product.

Expected result:

{
    "Laptop": 150000,
    "Mouse": 2000,
    "Keyboard": 2000
} """

print("Solution 50")

transactions = [
    {"product": "Laptop", "amount": 50000},
    {"product": "Mouse", "amount": 1000},
    {"product": "Laptop", "amount": 50000},
    {"product": "Keyboard", "amount": 2000},
    {"product": "Mouse", "amount": 1000},
    {"product": "Laptop", "amount": 50000}
]

total_sales = {}

for transaction in transactions:
    product = transaction["product"]
    amount = transaction["amount"]

    total_sales[product] = total_sales.get(product, 0) + amount

print(total_sales)

"""51. Count word frequency
Given:
words = ["apple", "banana", "apple", "orange", "banana", "apple"]"""

print("Solution 50")

words = ["apple", "banana", "apple", "orange", "banana", "apple"]

words_count = {}

for word in words:
    words_count[word]= words_count.get(word,0) + 1

print(words_count)


