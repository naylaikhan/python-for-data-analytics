"""Level 1 — Class & Object Basics
1. Create a Simple Class

Create a class called Student.

The class does not need any attributes or methods.

Create one object from the class and print the object."""

print("Solution 1")
class Student:
    pass

student_1 = Student()
print(student_1)

"""2. Create Multiple Objects

Create a class called Car.

Create three objects:

car1
car2
car3

Print each object."""

print("Solution 2")

class Car:
    pass

car1 = Car()
car2 = Car()
car3 = Car()

print(car1)
print(car2)
print(car3)

"""3. Student Name

Create a Student class.

Create an object and add the following attribute:

name = "Naila"

Print the student's name."""

print("Solution 3")

class Student:

    def __init__(self,name):
        self.name = name


student = Student("Naila")
print(student.name)

"""4. Student Information

Create a Student class.

Create an object with these attributes:

name = "Naila"
age = 25
course = "Python"

Print all three values."""

print("Solution 4")

class Student:

    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course

student = Student("Naila",25,"Python")
print(student.name)
print(student.age)
print(student.course)

"""5. Employee Information

Create an Employee class.

Create an employee object with:

name = "Rahul"
department = "Analytics"
salary = 50000

Print the employee's information."""

print("Solution 5")

class Employee:

    def __init__(self,name,department,salary):
        self.name = name
        self.department = department
        self.salary = salary

employee = Employee("Rahul","Analytics",50000)
print(employee.name)
print(employee.department)
print(employee.salary)


"""6. Create Two Students

Create a Student class.

Create two objects:

student1
student2

Give them different:

names
ages
courses

Print the information of both students."""

print("Solution 6")

class Student:

    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course

student1 = Student("Naila",25,"Python")
student2 = Student("Rahul",26,"SQL")

print("Student 1")
print(student1.name)
print(student1.age)
print(student1.course)

print("Student 2")
print(student2.name)
print(student2.age)
print(student2.course)

"""7. Modify an Attribute

Create a Student class.

Create:

student = Student()

Give the student an attribute:

age = 20

Change the age to 21.

Print the updated age."""

print("Solution 7")

class Student:

    def __init__(self,age):
        self.age = age

student = Student(20)

student.age = 21
print(student.age)

"""8. Add a New Attribute

Create an Employee object with:

name
salary

After creating the object, add another attribute:

city

Print all three attributes."""

print("Solution 8")

class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

employee = Employee("Naila",50000)

employee.city = "Delhi"

print(employee.name)
print(employee.salary)
print(employee.city)

"""9. Delete an Attribute

Create a Student object with:

name
age
course

Delete the course attribute.

Try accessing the remaining attributes and print them."""

print("Solution 9")

class Student:
    pass

student = Student()
student.name = "Naila"
student.age = 25
student.course = "Python"

print(student.name)
print(student.age)
print(student.course)

del student.course

print("After Deletion")
print(student.name)
print(student.age)


"""10. Check Object Type

Create a class called:

Book

Create an object from it.

Use Python's built-in functionality to check whether the object is an instance of the Book class."""

print("Solution 10")

class Book:
    pass

book = Book()

print(book)
print(type(book))
print(isinstance(book,Book))

"""Level 2 — __init__() and self
11. Student Constructor

Create a Student class with an __init__() method.

The constructor should accept:

name
age

Create a student:

Naila, 25

Print the student's name and age."""

print("Solution 11")

class Student :

    def __init__(self ,name,age):
        self.name = name
        self.age = age

student = Student("Naila", 25)
print(student.name)
print(student.age)

"""12. Employee Constructor

Create an Employee class with:

name
department
salary

Initialize all three using __init__().

Create two employees with different information.

Print their details."""

print("Solution 12")

class Employee:

    def __init__(self,name,department,salary):
        self.name = name
        self.department = department
        self.salary = salary

employee_1 =Employee("Naila","Engineering",50000)
employee_2 = Employee("Rahul","Marketing",40000)

print("Employee 1")
print(employee_1.name)
print(employee_1.department)
print(employee_1.salary)

print("Employee 2")
print(employee_2.name)
print(employee_2.department)
print(employee_2.salary)

"""13. Product Class

Create a Product class.

The constructor should accept:

name
price
quantity

Create:

Laptop
50000
2

Print all the information."""

print("Solution 13")

class Product :

     def __init__(self,name,price,quantity):
         self.name = name
         self.price = price
         self.quantity = quantity

product = Product("Laptop",50000,2)

print(product.name)
print(product.price)
print(product.quantity)

"""14. Book Class

Create a Book class with:

title
author
price

Create three different book objects.

Print the information of each book."""

print("Solution 14")

class Book:

    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

book_1 = Book("Python Crash Course", "Eric Matthes", 2500)
book_2 = Book("Atomic Habits", "James Clear", 1200)
book_3 = Book("The Alchemist", "Paulo Coelho", 800)

print("==== Book 1 ====")
print(book_1.title)
print(book_1.author)
print(book_1.price)

print("==== Book 2 ====")
print(book_2.title)
print(book_2.author)
print(book_2.price)

print("==== Book 3 ====")
print(book_3.title)
print(book_3.author)
print(book_3.price)


"""15. Bank Account

Create a BankAccount class.

The constructor should accept:

account_holder
balance

Create an account for:

Naila
10000

Print the account holder and balance."""

print("Solution 15")

class BankAccount:

    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance

account = BankAccount("Naila",10000)
print(account.account_holder)
print(account.balance)

"""16. Rectangle

Create a Rectangle class.

The constructor should accept:

length
width

Create a rectangle with:

length = 10
width = 5

Print both values."""

print("Solution 16")

class Rectangle :

    def __init__(self,length,width):
        self.length = length
        self.width = width

rectangle = Rectangle(10,5)
print(rectangle.length)
print(rectangle.width)

"""17. Circle

Create a Circle class.

The constructor should accept:

radius

Create a circle with radius 7.

Print the radius."""

print("Solution 17")

class Circle :

    def __init__(self,radius):
        self.radius = radius
        

Circle = Circle(7)
print(Circle.radius)

"""18. Movie

Create a Movie class.

The constructor should accept:

title
genre
rating

Create two movie objects with different values.

Print their information."""

print("Solution 18")

class Movie:

    def __init__(self,title,genre,rating):
        self.title =title
        self.genre =genre
        self.rating =rating

movie_1 = Movie("Inception", "Sci-Fi", 8.8)
movie_2 = Movie("The Dark Knight", "Action", 9.0)

print("==== Movie 1 ====")
print(movie_1.title)
print(movie_1.genre)
print(movie_1.rating)

print("==== Movie 2 ====")
print(movie_2.title)
print(movie_2.genre)
print(movie_2.rating)

"""19. Mobile Phone

Create a MobilePhone class.

The constructor should accept:

brand
model
price

Create three phone objects.

Print the details of each phone."""

print("Solution 19")

class MobilePhone:

    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

mobile_1 = MobilePhone("Apple", "iPhone 15", 65000)
mobile_2 = MobilePhone("Samsung", "Galaxy S24", 70000)
mobile_3 = MobilePhone("OnePlus", "12", 60000)

print("==== Mobile 1 ====")
print(mobile_1.brand)
print(mobile_1.model)
print(mobile_1.price)

print("==== Mobile 2 ====")
print(mobile_2.brand)
print(mobile_2.model)
print(mobile_2.price)

print("==== Mobile 3 ====")
print(mobile_3.brand)
print(mobile_3.model)
print(mobile_3.price)

"""20. Employee ID

Create an Employee class.

The constructor should accept:

name
employee_id
department

Create two employees.

Print their information."""

print("Solution 20")

class Employee:

    def __init__(self,name,employee_id,department):
        self.name = name
        self.employee_id = employee_id
        self.department = department

employee_1 = Employee("Naila",101,"Sales")
employee_2 = Employee("Rahul",302,"IT")

print("==== Employee 1 ====")
print(employee_1.name)
print(employee_1.employee_id)
print(employee_1.department)

print("==== Employee 2 ====")
print(employee_2.name)
print(employee_2.employee_id)
print(employee_2.department)

"""Level 3 — Methods
21. Greeting Method

Create a Person class with:

name

Create a method:

greet()

The method should print:

Hello, my name is <name>

Create an object and call the method."""

print("Solution 21")

class Person:

    def __init__(self,name):
        self.name = name

    def greet(self):
        print("Hello, my name is",self.name)

person = Person("Naila")
person.greet()

"""22. Student Study Method

Create a Student class with:

name
course

Create a method:

study()

It should print:

Naila is studying Python

using the object's attributes.
"""
print("Solution 22")

class Student:

    def __init__(self , name ,course):
        self.name = name 
        self.course = course

    def study(self):
        print(self.name ,"is studying",self.course)

student = Student("Naila","Python")
student.study()


"""23. Employee Work Method

Create an Employee class with:

name
department

Create a method:

work()

It should print a sentence containing the employee's name and department."""

print("Solution 23")

class Employee:

    def __init__(self , name , department):
        self.name = name
        self.department = department

    def work(self):
        print(f"{self.name} works in the {self.department} department.")

employee = Employee("Naila","Analytics")
employee.work()

"""24. Rectangle Area

Create a Rectangle class with:

length
width

Create a method:

area()

The method should return the area of the rectangle.

Test it using:

length = 10
width = 5"""

print("Solution 24")

class Rectangle :

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle = Rectangle(10,5)
rectangle_area = rectangle.area()
print(rectangle_area)


"""25. Rectangle Perimeter

Using the Rectangle class, create a method:

perimeter()

It should return:

2 × (length + width)

Test the method with different rectangles."""

print("Solution 25")

class Rectangle :

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rectangle = Rectangle(15,10)
rectangle_area = rectangle.area()
rectangle_perimeter = rectangle.perimeter()
print("Area",rectangle_area)
print("Perimeter",rectangle_perimeter)


"""26. Circle Area

Create a Circle class with:

radius

Create a method:

area()

Return the area of the circle.

Use:

π = 3.14"""

print("Solution 26")

class Circle :

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius

circle = Circle(7)
print("Area of the Circle",circle.area())

"""27. Employee Annual Salary

Create an Employee class with:

name
monthly_salary

Create a method:

annual_salary()

It should return the employee's annual salary.

For example:

monthly salary = 50,000
annual salary = 600,000"""

print("Solution 27")

class Employee:

    def __init__(self , name , monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return 12 * self.monthly_salary

employee = Employee("Naila",50000)
print(employee.name)
print("Annual Salary:",employee.annual_salary())

"""28. Bank Deposit

Create a BankAccount class with:

balance

Create a method:

deposit(amount)

The method should add the deposited amount to the balance.

Create an account with:

balance = 1000

Deposit:

500

Print the new balance."""

print("Solution 28")

class BankAccount:

    def __init__(self,balance):
        self.balance = balance

    def deposit(self,amount):
         self.balance += amount
         return self.balance

account = BankAccount(1000)
print(account.balance)
print(account.deposit(500))
print(account.balance)


"""29. Bank Withdrawal

Add a method:

withdraw(amount)

to the BankAccount class.

The method should subtract the amount from the balance.

Test it using:

balance = 5000
withdraw = 1500

Print the remaining balance."""

print("Solution 29")

class BankAccount:

    def __init__(self , balance):
        self.balance = balance

    def deposit(self,amount):
         self.balance += amount
         return self.balance

    def withdraw(self , amount):
        self.balance -= amount
        return self.balance

account = BankAccount(5000)
print(account.withdraw(1500))

"""30. Temperature Converter

Create a Temperature class.

Store temperature in Celsius.

Create a method:

to_fahrenheit()

Use:

F = (C × 9/5) + 32

Create an object with:

C = 25

Return the Fahrenheit value."""

print("Solution 30")

class Temperature:

    def __init__(self,c):
        self.c = c

    def to_fahrenheit(self):
        f = (self.c * 9/5) + 32
        return f

temp = Temperature(25)
print(temp.to_fahrenheit())

"""Level 4 — Logic Building With Classes"""
"""31. Student Pass or Fail

Create a Student class with:

name
marks

Create a method:

result()

If marks are 40 or above, return:

Pass

Otherwise return:

Fail

Create multiple student objects and test them."""

print("Solution 31")

class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"

student_1 = Student("John",35)
student_2 = Student("Kim",65)
print(student_1.result())
print(student_2.result())


"""32. Employee Bonus

Create an Employee class with:

name
salary

Create a method:

calculate_bonus()

If salary is greater than or equal to 50,000, give a 10% bonus.

Otherwise give a 5% bonus.

Return the bonus amount."""

print("Solution 32")

class Employee:

    def __init__(self, name , salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        if self.salary >= 50000:
            return 0.1 * self.salary
        else:
            return 0.05 * self.salary

employee_1 = Employee("Naila",65000)
employee_2 = Employee("Rahul",35000)

print(employee_1.calculate_bonus())
print(employee_2.calculate_bonus())


"""33. Product Discount

Create a Product class with:

name
price

Create a method:

discounted_price()

If the price is greater than 1000, apply a 10% discount.

Otherwise apply no discount.

Return the final price."""

print("Solution 33")

class Product:

    def __init__(self,name,price):
        self.name = name
        self.price = price

    def discounted_price(self):
        if self.price > 1000:
            return self.price - 0.1 * self.price
        else:
            return self.price

product_1 = Product("Laptop",65000)
product_2 = Product("Shirt",500)
print("Final Price",product_1.discounted_price())
print("Final Price",product_2.discounted_price())

"""34. Bank Withdrawal Validation

Create a BankAccount class with:

balance

Create:

withdraw(amount)

The method should:

reject negative or zero withdrawal amounts
reject withdrawals greater than the balance
successfully withdraw valid amounts

Print an appropriate message for each situation."""

print("Solution 34")

class BankAccount:

    def __init__(self,balance):
        self.balance = balance

    def withdraw(self , amount):
        if amount > self.balance:
            print("Transaction Unsuccessful! Insufficient balance ")
        elif amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. Remaining balance: {self.balance}")

account = BankAccount(5000)
account.withdraw(6000)
account.withdraw(-6000)
account.withdraw(0)
account.withdraw(600)

"""35. Student Grade

Create a Student class with:

name
marks

Create:

grade()

Use these rules:

90–100 → A
80–89  → B
70–79  → C
60–69  → D
Below 60 → F

Create several students and test the method."""

print("Solution 35")

class Student:

    def __init__(self , name , marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            print("Grade A")
        elif self.marks >=80:
            print("Grade B")
        elif self.marks >=70:
            print("Grade C")
        elif self.marks >=60:
            print("Grade D")
        else:
            print("Grade F")

student_1 = Student("John",95)
student_2 = Student("Kim",85)
student_3 = Student("Sara",75)
student_4 = Student("Nim",65)
student_5 = Student("Tim",55)
student_1.grade()
student_2.grade()
student_3.grade()
student_4.grade()
student_5.grade()


"""36. Login System

Create a User class with:

username
password

Create a method:

login(password)

The method should check whether the provided password matches the stored password.

Print:

Login successful

or:

Incorrect password"""

print("Solution 36")

class User:

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def login(self,user_password):
        if self.password == user_password:
            print("Login successful")
        else:
            print("Incorrect password")

user = User("john","xyz786")
user.login("xyz786")
user.login("abc123")


"""37. Shopping Cart

Create a ShoppingCart class.

The object should maintain a list of products.

Create methods:

add_product()
remove_product()
show_products()

Test the class by adding and removing several products."""

print("Solution 37")

class ShoppingCart:

    def __init__(self):
        self.products = []

    def add_product(self,product):
        self.products.append(product)

    def remove_product(self,product):
        self.products.remove(product)

    def show_products(self):
        print(self.products)

cart = ShoppingCart()
cart.add_product("Laptop")
cart.add_product("Battery")
cart.add_product("Mobile")
cart.show_products()
cart.remove_product("Battery")
cart.show_products()

"""38. Counter

Create a Counter class.

The object should start with:

count = 0

Create methods:

increment()
decrement()
reset()

Test the counter by calling the methods multiple times.
"""
print("Solution 38")

class Counter:

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count +=1
        return self.count

    def decrement(self):
        self.count -= 1
        return self.count
    

    def reset(self):
        self.count = 0
        return self.count

counter = Counter()
print(counter.increment())
print(counter.increment())
print(counter.increment())
print(counter.decrement())
print(counter.reset()) 

"""39. Even or Odd

Create a Number class with:

value

Create a method:

check_even_odd()

The method should determine whether the number is even or odd.

Create several objects with different numbers.
"""
print("Solution 39")

class Number:

    def __init__(self,value):
        self.value = value

    def check_even_odd(self):
        if self.value % 2 == 0:
            print("Number is Even")
        else:
            print("Number is Odd")

number_1 = Number(6)
number_2 = Number(7)
number_3 = Number(0)

number_1.check_even_odd()
number_2.check_even_odd()
number_3.check_even_odd()

"""40. Largest of Two Numbers

Create a class called:

NumberComparison

The constructor should accept two numbers.

Create a method:

largest()

Return the larger number.

Test it with multiple pairs of numbers."""

print("Solution 40")

class NumberComparison:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def largest(self):
        if self.num1 >= self.num2:
            return self.num1
        else:
            return self.num2

number1 = NumberComparison(10,20)
number2 = NumberComparison(30,20)
number3 = NumberComparison(10,10)

print(number1.largest())
print(number2.largest())
print(number3.largest())


"""Level 5 — Class Attributes, Inheritance & OOP"""
"""41. Class Attribute

Create an Employee class with a class attribute:

company = "ABC Ltd"

Create three employees.

Print the company name using each employee object."""

print("Solution 41")

class Employee:

    company = "ABC Ltd"

emp1 = Employee()
emp2 = Employee()
emp3 = Employee()

print(emp1.company)
print(emp2.company)
print(emp3.company)

"""42. Change Class Attribute

Using the Employee class from Question 41, change the company name from:

ABC Ltd

to:

XYZ Ltd

Print the company name for all employee objects."""

print("Solution 42")

class Employee:

    company = "ABC Ltd"


emp1 = Employee()
emp2 = Employee()
emp3 = Employee()

Employee.company = "XYZ Ltd"

print(emp1.company)
print(emp2.company)
print(emp3.company)

"""43. Instance vs Class Attribute

Create a class:

Student

with a class attribute:

school = "ABC School"

Each student should have an instance attribute:

name

Create three students.

Print:

each student's name
each student's school"""

print("Solution 43")

class Student:
    school = "ABC School"

    def __init__(self,name):
        self.name = name


student1 = Student("Naila")
student2 = Student("John")
student3 = Student("Rahul")

print(student1.name)
print(student1.school)
print(student2.name)
print(student2.school)
print(student3.name)
print(student3.school)


"""44. Animal Inheritance

Create a parent class:

Animal

with a method:

eat()

Create a child class:

Dog

that inherits from Animal.

Create a Dog object and call eat()."""

print("Solution 44")

class Animal:

    def eat(self):
        print(f"{self} is eating")

class Dog(Animal):
    pass

dog = Dog()
dog.eat()

"""45. Employee Inheritance

Create a parent class:

Employee

with:

work()

Create two child classes:

Developer
Tester

Both should inherit from Employee.

Give each child class its own additional method.

Create objects of both classes and call their methods."""

print("Solution 45")

class Employee:

    def work(self):
        print("Employee is working")


class Developer(Employee):

    def code(self):
        print("Developer is coding")


class Tester(Employee):

    def test(self):
        print("Tester is testing")


developer = Developer()
tester = Tester()

developer.work()
developer.code()

tester.work()
tester.test()

"""46. Method Overriding

Create a class:

Animal

with:

sound()

The method should print:

Animal makes a sound

Create:

Dog
Cat

that inherit from Animal.

Override sound() in both classes so that:

Dog → Bark
Cat → Meow

Create objects and test them."""


print("Solution 46")

class Animal:

    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):

    def sound(self):
        print("Dog makes a Bark sound")

class Cat(Animal):
    def sound(self):
        print("Cat makes a Meow sound")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


"""47. super()

Create a parent class:

Person

Its constructor should accept:

name
age

Create a child class:

Employee

The child should additionally have:

salary

Use super() to initialize the parent attributes.

Create an employee object and print all three values."""

print("Solution 47")

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

class Employee(Person):

    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary = salary


employee = Employee("Naila",23,50000)
print(employee.name)
print(employee.age)
print(employee.salary)

"""48. Composition

Create a class:

Engine

with a method:

start()

Create a class:

Car

that contains an Engine object.

Create a Car object and use the car to start its engine."""

print("Solution 48")

class Engine:

    def start(self):
        print("Engine is working")

class Car:

    def __init__(self):
        self.engine = Engine()

car = Car()
car.engine.start()

"""49. Polymorphism

Create three classes:

Dog
Cat
Cow

Each class should have a method:

sound()

The methods should produce different sounds.

Create a function:

make_sound(animal)

that calls the object's sound() method.

Pass objects of all three classes to the function."""

print("Solution 49")

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

class Cow:
    def sound(self):
        print("Moo")

def make_sound(animal):
    animal.sound()

dog = Dog()
cat = Cat()
cow = Cow()

make_sound(dog)
make_sound(cat)
make_sound(cow)

"""50. Complete Employee Management System

Create an Employee class with:

name
employee_id
department
monthly_salary

The class should contain methods to:

display employee details
calculate annual salary
calculate bonus

Use the following bonus rules:

salary >= 100000 → 15% bonus
salary >= 50000  → 10% bonus
salary < 50000   → 5% bonus

Create at least 5 employee objects belonging to different departments.

Display each employee's:

Name
Employee ID
Department
Monthly Salary
Annual Salary
Bonus

Then determine which employee has the highest annual salary."""

print("Solution 50")

class Employee:

    def __init__(self,name,employee_id,department,monthly_salary):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.monthly_salary = monthly_salary

    def display_employee_details(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Department:", self.department)
        print("Monthly Salary:", self.monthly_salary)

    def calculate_annual_salary(self):
        return self.monthly_salary * 12

    def calculate_bonus(self):
        if self.monthly_salary >= 100000 :
            return 0.15 * self.monthly_salary
        elif self.monthly_salary >= 50000 :
            return 0.1 * self.monthly_salary
        else:
            return 0.05 * self.monthly_salary


employee1 = Employee("Naila", "EMP001", "Analytics", 50000)
employee2 = Employee("Rahul", "EMP002", "Engineering", 65000)
employee3 = Employee("Priya", "EMP003", "HR", 45000)
employee4 = Employee("Amit", "EMP004", "Finance", 55000)
employee5 = Employee("Sara", "EMP005", "Marketing", 48000)

employees = [employee1, employee2, employee3, employee4, employee5]

for employee in employees:
    print("\n==== Employee ====")

    employee.display_employee_details()

    print("Annual Salary:", employee.calculate_annual_salary())

    print("Bonus:", employee.calculate_bonus())


highest_paid = max(
    employees,
    key=lambda employee: employee.calculate_annual_salary()
)


print("\n==== Highest Annual Salary ====")
print("Name:", highest_paid.name)
print("Annual Salary:", highest_paid.calculate_annual_salary())   








