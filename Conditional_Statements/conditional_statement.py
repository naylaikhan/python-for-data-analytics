"""1. Given age = 20, write a program that prints "Adult" if the age is 18 or above."""
age = 20

if age >=18:
    print("Adult")

"""2. Given number = 15, check whether the number is positive. Print "Positive" if it is greater than 0."""
number = 15
if number > 0 :
    print("Number is Positive")

"""3. Given number = -5, print "Negative" if the number is less than 0."""
number = -5
if number < 0 :
    print("Number is Negative")

"""4. Given marks = 65, check whether the student has passed. A student passes if marks are 40 or above."""
marks = 65
if marks >= 40:
    print("Student has Passed")

"""5. Given number = 12, check whether the number is even or odd using %."""
number =12
if number % 2 == 0:
    print("The number is Even")
else:
    print("The Number is Odd")

"""6. Given temperature = 35, print "Hot" if the temperature is greater than 30; otherwise print "Normal"."""
temperature = 35
if temperature > 30 :
    print("Hot")
else:
    print("Normal")

"""7. Given age = 17, print "Eligible" if the person is 18 or older; otherwise print "Not Eligible"."""
age = 17
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

"""8. Given password = "python123", check whether the password is "python123". Print "Correct Password" or "Wrong Password"."""
password = "python123"
if password == "python123":
    print("Correct Password")
else:
    print("Wrong Password")

"""9. Given number = 10, check whether the number is greater than 5. Print an appropriate message for both cases."""
number = 10
if number > 5:
    print("Greater than 5")
else:
    print("Less than 5")

"""10. Given sales = 45000, check whether the sales target of 50000 has been achieved."""
sales = 45000
target = 50000
if sales >= target:
    print("Target Achieved")
else:
    print("Target Not Achieved")

"""11. Given marks = 82, classify the result:
90 or above → "Excellent"
75–89 → "Good"
40–74 → "Pass"
Below 40 → "Fail" """

marks = 82
if marks >=90:
    print("Excellent")
elif marks >=75:
    print("Good")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")

"""12. Given age = 25, classify the person:
Below 13 → "Child"
13–19 → "Teenager"
20–59 → "Adult"
60 or above → "Senior" """

age = 25
if age>=60:
    print("Senior")
elif age>=20:
    print("Adult")
elif age>=13:
    print("Teenager")
else:
    print("Child")

"""13. Given number = 0, determine whether the number is:
Positive
Negative
Zero """

number = 0
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

"""14. Given salary = 65000, classify the salary:
Below 30000 → "Low"
30000–59999 → "Medium"
60000 or above → "High" """

salary = 55000
if salary >= 60000:
    print("High")
elif salary >=30000:
    print("Medium")
else:
    print("Low")

"""15. Given experience = 4, print:
Less than 1 → "Fresher"
1–3 → "Junior"
4–7 → "Mid-Level"
8 or above → "Senior" """

experience = 4
if experience >=8:
    print("Senior")
elif experience >=4:
    print("Mid-Level")
elif experience >=1:
    print("Junior")
else:
    print("Fresher")

"""16. Given purchase = 75000, classify the customer:
100000 or more → "High Value"
50000–99999 → "Medium Value"
Below 50000 → "Low Value" """

purchase = 75000
if purchase >= 100000:
    print("High Value")
elif purchase >= 50000:
    print("Medium Value")
else:
    print("Low Value")

"""17. Given num = 25, check whether the number is divisible by both 5 and 3."""
num = 25
if num % 5==0 and num % 3 == 0 :
    print("divisible by both 5 and 3")
else:
    print("Not divisible by both 5 and 3")

"""18. Given age = 25 and has_id = True, allow entry only when the person is at least 18 and has an ID."""
age = 25
has_id = True

if age >= 18 and has_id:
    print("Entry Allowed")
else:
    print("Entry Not Allowed")

"""19. Given day = "Sunday", print "Weekend" if the day is Saturday or Sunday. Otherwise print "Weekday"."""
day = "Sunday"

if day == "Saturday" or day == "Sunday" :
    print("Weekend")
else:
   print("Not Weekend") 

"""20. Given username = "admin" and password = "1234", print "Login Successful" only if both are correct. Otherwise print "Login Failed"."""
username = "admin"
password = "1234"

if username == "admin" and password == "1234" :
    print("Login Successful")
else:
    print("Login Failed")

"""21. Given num = 17, determine whether the number is:
Positive even
Positive odd
Negative even
Negative odd
Zero """

num = -8
if num > 0:
    if num % 2 == 0 :
        print("Positive Even")
    else:
        print("Positive Odd")
elif num < 0:
    if num % 2 == 0 :
        print("Negative Even")
    else:
        print("Negative Odd")
else:
    print("Number is Zero")

"""22. Given marks = 78 and attendance = 82, print "Eligible" only if:
marks are at least 40 AND
attendance is at least 75.
Otherwise print "Not Eligible"."""

marks = 78
attendance = 82

if marks >= 40 and attendance >= 75:
    print("Eligible")
else:
    print("Not Eligible")

"""23. Given age = 22 and has_license = True, determine whether a person can drive.
They can drive only if they are at least 18 and have a license."""
age = 22
has_license = True

if age >= 18 and has_license:
    print("Can Drive")
else:
    print("Can't Drive")

"""24. Given salary = 55000 and experience = 3, determine whether an employee is eligible for a bonus.
Eligibility requires:
salary >= 50000 AND
experience >= 3."""
salary = 55000
experience = 3

if salary >= 50000 and experience >= 3 :
    print("employee is eligible for a bonus")
else:
    print("employee is not eligible for a bonus")


"""25. Given num = 30, check whether the number is divisible by 3, 5, both, or neither.
Expected possibilities:
Divisible by both
Divisible by 3
Divisible by 5
Neither"""
num = 30
if num % 5 == 0 and num % 3==0:
    print("divisible by both 3 and 5")
elif num % 5 == 0:
    print("divisible by 5")
elif num % 3==0:
    print("divisible by 3")
else:
    print("Neither")

"""26. Given:
username = "naila"
password = "python123"
Create a login system:
Correct username AND correct password → "Login Successful"
Otherwise → "Invalid Credentials" """
username = "naila"
password = "python123"

if username == "naila" and password == "python123":
    print("Login Successful")
else:
    print("Invalid Credentials")


"""27. Given age = 35 and salary = 70000, determine whether a person qualifies for a loan.
Rules:
Age must be between 21 and 60.
Salary must be at least 50000.
Print "Loan Approved" or "Loan Rejected"."""
age = 35
salary = 70000

if 21<=age<=60 and salary>=50000:
    print("Loan Approved")
else:
    print("Loan Rejected")

"""28. Given:
sales = 120000
customers = 150
A salesperson gets a "Bonus" if:
sales are at least 100000 OR
customers are at least 200.
Otherwise print "No Bonus".
Think carefully about OR vs AND."""

sales = 120000
customers = 150

if sales>=100000 or customers >= 200:
    print("Bonus")
else:
    print("No Bonus")

"""29. Given:
marks = 85
attendance = 72
A student gets "Scholarship" only if:
marks are at least 80 AND
attendance is at least 75.
Otherwise print "No Scholarship"."""

marks = 85
attendance = 72
if marks >= 80 and attendance >=75:
    print("Scholarship")
else:
    print("No Scholarship")

"""30. Build a simple employee performance classifier using:
performance = 87
Rules:
90–100 → "Outstanding"
80–89 → "Excellent"
70–79 → "Good"
50–69 → "Average"
Below 50 → "Poor" """

performance = 87
if performance >=90:
    print("Outstanding")
elif performance >=80:
    print("Excellent")
elif performance >=70:
    print("Good")
elif performance >=50:
    print("Average")
else:
    print("Poor")