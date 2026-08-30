## Python Classes - 50 Practice Questions

This section contains **50 Python practice questions on Classes**, designed to build understanding gradually from basic class/object concepts to more advanced Object-Oriented Programming (OOP) concepts.

The questions are arranged in increasing difficulty so that you can strengthen your logic step by step.

---

## 📚 Topics Covered

These exercises cover:

* Classes
* Objects
* Instances
* `__init__()`
* `self`
* Instance attributes
* Class attributes
* Methods
* Modifying attributes
* Deleting attributes
* Method parameters
* Returning values from methods
* Conditional logic inside classes
* Encapsulation
* Inheritance
* Method overriding
* `super()`
* Composition
* Polymorphism
* Basic OOP design
* Practical data-oriented examples

---

# 🟢 Level 1 — Class & Object Basics

### 1. Create a Simple Class

Create a class called `Student`.

The class does not need any attributes or methods.

Create one object from the class and print the object.

---

### 2. Create Multiple Objects

Create a class called `Car`.

Create three objects:

```python
car1
car2
car3
```

Print each object.

---

### 3. Student Name

Create a `Student` class.

Create an object and add the following attribute:

```python
name = "Naila"
```

Print the student's name.

---

### 4. Student Information

Create a `Student` class.

Create an object with these attributes:

```python
name = "Naila"
age = 25
course = "Python"
```

Print all three values.

---

### 5. Employee Information

Create an `Employee` class.

Create an employee object with:

```python
name = "Rahul"
department = "Analytics"
salary = 50000
```

Print the employee's information.

---

### 6. Create Two Students

Create a `Student` class.

Create two objects:

```python
student1
student2
```

Give them different:

* names
* ages
* courses

Print the information of both students.

---

### 7. Modify an Attribute

Create a `Student` class.

Create:

```python
student = Student()
```

Give the student an attribute:

```python
age = 20
```

Change the age to `21`.

Print the updated age.

---

### 8. Add a New Attribute

Create an `Employee` object with:

```python
name
salary
```

After creating the object, add another attribute:

```python
city
```

Print all three attributes.

---

### 9. Delete an Attribute

Create a `Student` object with:

```python
name
age
course
```

Delete the `course` attribute.

Print the remaining attributes.

---

### 10. Check Object Type

Create a class called:

```python
Book
```

Create an object from it.

Use Python's built-in functionality to check whether the object is an instance of the `Book` class.

---

# 🟡 Level 2 — `__init__()` and `self`

### 11. Student Constructor

Create a `Student` class with an `__init__()` method.

The constructor should accept:

```text
name
age
```

Create a student:

```text
Naila, 25
```

Print the student's name and age.

---

### 12. Employee Constructor

Create an `Employee` class with:

```text
name
department
salary
```

Initialize all three using `__init__()`.

Create two employees with different information.

Print their details.

---

### 13. Product Class

Create a `Product` class.

The constructor should accept:

```text
name
price
quantity
```

Create:

```text
Laptop
50000
2
```

Print all the information.

---

### 14. Book Class

Create a `Book` class with:

```text
title
author
price
```

Create three different book objects.

Print the information of each book.

---

### 15. Bank Account

Create a `BankAccount` class.

The constructor should accept:

```text
account_holder
balance
```

Create an account for:

```text
Naila
10000
```

Print the account holder and balance.

---

### 16. Rectangle

Create a `Rectangle` class.

The constructor should accept:

```text
length
width
```

Create a rectangle with:

```text
length = 10
width = 5
```

Print both values.

---

### 17. Circle

Create a `Circle` class.

The constructor should accept:

```text
radius
```

Create a circle with radius `7`.

Print the radius.

---

### 18. Movie

Create a `Movie` class.

The constructor should accept:

```text
title
genre
rating
```

Create two movie objects with different values.

Print their information.

---

### 19. Mobile Phone

Create a `MobilePhone` class.

The constructor should accept:

```text
brand
model
price
```

Create three phone objects.

Print the details of each phone.

---

### 20. Employee ID

Create an `Employee` class.

The constructor should accept:

```text
name
employee_id
department
```

Create two employees.

Print their information.

---

# 🟠 Level 3 — Methods

### 21. Greeting Method

Create a `Person` class with:

```text
name
```

Create a method:

```python
greet()
```

The method should print:

```text
Hello, my name is <name>
```

Create an object and call the method.

---

### 22. Student Study Method

Create a `Student` class with:

```text
name
course
```

Create a method:

```python
study()
```

It should print a sentence using the student's name and course.

---

### 23. Employee Work Method

Create an `Employee` class with:

```text
name
department
```

Create a method:

```python
work()
```

It should print a sentence containing the employee's name and department.

---

### 24. Rectangle Area

Create a `Rectangle` class with:

```text
length
width
```

Create a method:

```python
area()
```

The method should return the area of the rectangle.

Test it using:

```text
length = 10
width = 5
```

---

### 25. Rectangle Perimeter

Using the `Rectangle` class, create a method:

```python
perimeter()
```

It should return:

```text
2 × (length + width)
```

Test the method with different rectangles.

---

### 26. Circle Area

Create a `Circle` class with:

```text
radius
```

Create a method:

```python
area()
```

Return the area of the circle.

Use:

```text
π = 3.14
```

---

### 27. Employee Annual Salary

Create an `Employee` class with:

```text
name
monthly_salary
```

Create a method:

```python
annual_salary()
```

It should return the employee's annual salary.

---

### 28. Bank Deposit

Create a `BankAccount` class with:

```text
balance
```

Create a method:

```python
deposit(amount)
```

The method should add the deposited amount to the balance.

Create an account with:

```text
balance = 1000
```

Deposit:

```text
500
```

Print the new balance.

---

### 29. Bank Withdrawal

Add a method:

```python
withdraw(amount)
```

to the `BankAccount` class.

The method should subtract the amount from the balance.

Test it using:

```text
balance = 5000
withdraw = 1500
```

Print the remaining balance.

---

### 30. Temperature Converter

Create a `Temperature` class.

Store temperature in Celsius.

Create a method:

```python
to_fahrenheit()
```

Use:

```text
F = (C × 9/5) + 32
```

Create an object with:

```text
C = 25
```

Return the Fahrenheit value.

---

# 🔵 Level 4 — Logic Building With Classes

### 31. Student Pass or Fail

Create a `Student` class with:

```text
name
marks
```

Create a method:

```python
result()
```

If marks are `40` or above, return:

```text
Pass
```

Otherwise return:

```text
Fail
```

Create multiple student objects and test them.

---

### 32. Employee Bonus

Create an `Employee` class with:

```text
name
salary
```

Create a method:

```python
calculate_bonus()
```

If salary is greater than or equal to `50,000`, give a `10%` bonus.

Otherwise give a `5%` bonus.

Return the bonus amount.

---

### 33. Product Discount

Create a `Product` class with:

```text
name
price
```

Create a method:

```python
discounted_price()
```

If the price is greater than `1000`, apply a `10%` discount.

Otherwise apply no discount.

Return the final price.

---

### 34. Bank Withdrawal Validation

Create a `BankAccount` class with:

```text
balance
```

Create:

```python
withdraw(amount)
```

The method should:

* reject negative or zero withdrawal amounts
* reject withdrawals greater than the balance
* successfully withdraw valid amounts

Print an appropriate message for each situation.

---

### 35. Student Grade

Create a `Student` class with:

```text
name
marks
```

Create:

```python
grade()
```

Use these rules:

```text
90–100 → A
80–89  → B
70–79  → C
60–69  → D
Below 60 → F
```

Create several students and test the method.

---

### 36. Login System

Create a `User` class with:

```text
username
password
```

Create a method:

```python
login(password)
```

The method should check whether the provided password matches the stored password.

Print:

```text
Login successful
```

or:

```text
Incorrect password
```

---

### 37. Shopping Cart

Create a `ShoppingCart` class.

The object should maintain a list of products.

Create methods:

```python
add_product()
remove_product()
show_products()
```

Test the class by adding and removing several products.

---

### 38. Counter

Create a `Counter` class.

The object should start with:

```text
count = 0
```

Create methods:

```python
increment()
decrement()
reset()
```

Test the counter by calling the methods multiple times.

---

### 39. Even or Odd

Create a `Number` class with:

```text
value
```

Create a method:

```python
check_even_odd()
```

The method should determine whether the number is even or odd.

Create several objects with different numbers.

---

### 40. Largest of Two Numbers

Create a class called:

```python
NumberComparison
```

The constructor should accept two numbers.

Create a method:

```python
largest()
```

Return the larger number.

Test it with multiple pairs of numbers.

---

# 🔴 Level 5 — Class Attributes, Inheritance & OOP

### 41. Class Attribute

Create an `Employee` class with a class attribute:

```python
company = "ABC Ltd"
```

Create three employees.

Print the company name using each employee object.

---

### 42. Change Class Attribute

Using the `Employee` class from Question 41, change the company name from:

```text
ABC Ltd
```

to:

```text
XYZ Ltd
```

Print the company name for all employee objects.

---

### 43. Instance vs Class Attribute

Create a class:

```python
Student
```

with a class attribute:

```python
school = "ABC School"
```

Each student should have an instance attribute:

```python
name
```

Create three students.

Print:

* each student's name
* each student's school

---

### 44. Animal Inheritance

Create a parent class:

```python
Animal
```

with a method:

```python
eat()
```

Create a child class:

```python
Dog
```

that inherits from `Animal`.

Create a Dog object and call `eat()`.

---

### 45. Employee Inheritance

Create a parent class:

```python
Employee
```

with:

```python
work()
```

Create two child classes:

```python
Developer
Tester
```

Both should inherit from `Employee`.

Give each child class its own additional method.

Create objects of both classes and call their methods.

---

### 46. Method Overriding

Create a class:

```python
Animal
```

with:

```python
sound()
```

The method should print:

```text
Animal makes a sound
```

Create:

```python
Dog
Cat
```

that inherit from `Animal`.

Override `sound()` in both classes so that:

```text
Dog → Bark
Cat → Meow
```

Create objects and test them.

---

### 47. `super()`

Create a parent class:

```python
Person
```

Its constructor should accept:

```text
name
age
```

Create a child class:

```python
Employee
```

The child should additionally have:

```text
salary
```

Use `super()` to initialize the parent attributes.

Create an employee object and print all three values.

---

### 48. Composition

Create a class:

```python
Engine
```

with a method:

```python
start()
```

Create a class:

```python
Car
```

that contains an `Engine` object.

Create a `Car` object and use the car to start its engine.

---

### 49. Polymorphism

Create three classes:

```python
Dog
Cat
Cow
```

Each class should have a method:

```python
sound()
```

The methods should produce different sounds.

Create a function:

```python
make_sound(animal)
```

that calls the object's `sound()` method.

Pass objects of all three classes to the function.

---

### 50. Complete Employee Management System

Create an `Employee` class with:

```text
name
employee_id
department
monthly_salary
```

The class should contain methods to:

```text
display employee details
calculate annual salary
calculate bonus
```

Use the following bonus rules:

```text
salary >= 100000 → 15% bonus
salary >= 50000  → 10% bonus
salary < 50000   → 5% bonus
```

Create at least **5 employee objects** belonging to different departments.

Display each employee's:

```text
Name
Employee ID
Department
Monthly Salary
Annual Salary
Bonus
```

Then determine which employee has the **highest annual salary**.

---

# 🎯 Learning Progress

Use the questions in this order:

```text
01–10  → Classes & Objects
11–20  → __init__() & self
21–30  → Methods
31–40  → Logic Building
41–50  → OOP Concepts
```

The goal is not simply to finish all 50 questions.

The goal is to be able to look at a problem and independently decide:

```text
What should be a class?
        ↓
What attributes should it have?
        ↓
What should __init__() receive?
        ↓
What does self refer to?
        ↓
What methods should the class have?
        ↓
What objects should I create?
        ↓
How should the objects interact?
```

---

## 📝 Suggested Repository Structure

```text
python-for-data-analytics/
│
├── Classes/
│   │
│   ├── README.md
│   │
│   ├── 01_simple_class.py
│   ├── 02_multiple_objects.py
│   ├── 03_student_name.py
│   ├── 04_student_information.py
│   ├── 05_employee_information.py
│   ├── ...
│   ├── 49_polymorphism.py
│   └── 50_employee_management.py
│
└── README.md
```

---

## 🚀 Goal

By completing these 50 exercises, you should become comfortable with the fundamental Python class concepts required to read and write basic object-oriented Python code.

**Practice → Understand → Build → Repeat**

Do not rush through the questions. Focus on understanding **why** each class, attribute, method, and object is being created.
