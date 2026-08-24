"""1.Write a for loop to print numbers from 1 to 10."""
print("Solution 1")
for num in range(1,11):
    print(num)

"""2.Write a for loop to print numbers from 0 to 20."""
print("Solution 2")
for num in range(0,21):
    print(num)

"""3.Write a program to print numbers from 1 to 20, but print only the even numbers."""
print("Solution 3")
for num in range(1,21):
    if(num % 2==0):
        print(num)

"""4.Write a program to print all odd numbers from 1 to 20."""
print("Solution 4")
for num in range(1,21):
    if(num % 2 != 0):
        print(num)

"""5.Given:numbers = [10, 20, 30, 40, 50].Use a for loop to print every number."""
print("Solution 5")
numbers = [10, 20, 30, 40, 50]
for num in numbers:
    print(num)

"""6.Given:names = ["Aman", "Riya", "Rahul", "Sara"].Use a loop to print each name."""
print("Solution 6")
names = ["Aman", "Riya", "Rahul", "Sara"]
for name in names:
    print(name)

"""7.Given:name = "Python"
Use a for loop to print each character separately. 
Expected output:
P
y
t
h
o
n """
print("Solution 7")
name = "Python"
for n in name:
    print(n)

"""8.Use range() to print numbers from 5 to 15."""
print("Solution 8")
for n in range(5,16):
    print(n)

"""9.Use range() to print numbers from 10 to 100 with a step of 10.
Expected output:
10
20
30
40
50
60
70
80
90
100  """
print("Solution 9")
for n in range(10,101,10):
    print(n)

"""10.Write a loop to print numbers from 20 to 1 in reverse order."""
print("Solution 10")
for n in range(20,0,-1):
    print(n)

"""11.Given:numbers = [10, 15, 20, 25, 30, 35].Print only the even numbers."""
print("Solution 11")
numbers = [10, 15, 20, 25, 30, 35]

for num in numbers:
    if num % 2 == 0 :
        print(num)

"""12.Given:numbers = [10, -5, 20, -10, 0, 15].Print only the positive numbers."""
print("Solution 12")
numbers = [10, -5, 20, -10, 0, 15]
for num in numbers:
    if num > 0:
        print(num)

"""13.Given:numbers = [10, -5, 20, -10, 0, 15].Print whether each number is:
Positive
Negative
Zero"""
print("Solution 13")
numbers = [10, -5, 20, -10, 0, 15]

for num in numbers:
    if num > 0:
        print(num , "Positive")
    elif num < 0 :
        print(num , "Negative")
    else:
        print(num,"Zero")


"""14.Given:marks = [45, 80, 32, 90, 50, 28].Print only the marks where the student has passed.Assume passing marks are 40 or above."""
print("Solution 14")
marks = [45, 80, 32, 90, 50, 28]

for n in marks:
    if n >= 40:
        print(n , "Passed")
    else:
        print(n, "Failed")

"""15.Given:numbers = [12, 15, 18, 21, 24, 27].Print only numbers divisible by 3."""
print("Solution 15")
numbers = [12, 15, 18, 21, 24, 27]

for num in numbers:
    if num % 3 ==0 :
        print(num , "divisible by 3")
    else:
        print(num ,"Not divisible by 3")

"""16.Given:numbers = [10, 25, 30, 45, 50, 75].Print numbers that are divisible by 5 but not by 10."""
print("Solution 16")
numbers = [10, 25, 30, 45, 50, 75]

for num in numbers:
    if num % 5 == 0 and num % 10 != 0 :
        print(num , "divisible by 5 but not by 10")


"""17.Given:numbers = [10, 20, 30, 40, 50].Use a loop to calculate the sum of all numbers.Do not use:sum()"""
print("Solution 17")
numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers :
    total+=num

print(total)

"""18.Given:numbers = [5, 10, 15, 20, 25].Calculate the product of all numbers.Expected result:375000"""
print("Solution 18")
numbers = [5, 10, 15, 20, 25]

product = 1

for num in numbers:
    product = product * num

print(product)

"""19.Given:numbers = [10, -5, 20, -8, 30, 0].Count how many numbers are positive.Do not use:len() for the answer."""
print("Solution 19")
numbers = [10, -5, 20, -8, 30, 0]

count = 0

for num in numbers:
    if num > 0:
        count += 1

print(count , "Positive numbers")

"""20.Given:numbers = [10, 15, 20, 25, 30, 35].Count how many numbers are even."""
print("Solution 20")
numbers = [10, 15, 20, 25, 30, 35]

count = 0

for num in numbers : 
    if num % 2 == 0:
        count +=1

print(count , "numbers are even")

"""21.Given:marks = [45, 80, 32, 90, 50, 28].Count how many students passed.Passing marks are 40 or above."""
print("Solution 21")
marks = [45, 80, 32, 90, 50, 28]
count = 0

for num in numbers:
    if num >= 40:
        count += 1

"""22.Given:sales = [100, 250, 300, 150, 400].Calculate the total sales using a loop."""
print("Solution 22")
sales = [100, 250, 300, 150, 400]

total=0

for sale in sales :
    total+=sale

print(total , "Total Sale")

"""23.Given:numbers = [25, 10, 50, 40, 80, 30].Find the largest number using a loop.Do not use:max()"""
print("Solution 23")

numbers = [25, 10, 50, 40, 80, 30]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(largest , "is the largest number")

"""24.Using the same list:numbers = [25, 10, 50, 40, 80, 30].Find the smallest number using a loop.Do not use:min()"""
print("Solution 24")
numbers = [25, 10, 50, 40, 80, 30]
smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print(smallest , "is the smallest number")


"""25.Given:numbers = [12, 45, 7, 89, 34, 56].Find the first number greater than 50 and stop the loop immediately after finding it.Use:break"""
print("Solution 25")
numbers = [12, 45, 7, 89, 34, 56]

for num in numbers:
    if num > 50:
        break

print(num)

"""26.Given:names = ["Aman", "Riya", "Rahul", "Sara", "John"]
Search for:
target = "Sara"
Print "Found" if the target exists.
Use a loop."""
print("Solution 26")

names = ["Aman", "Riya", "Rahul", "Sara", "John"]
target = "Sara"

for name in names:
    if target == name:
        print("Found")

"""27.Print numbers from 1 to 10, but stop the loop when the number becomes 7.Use break."""
print("Solution 27")

for num in range(1,11):
    print(num)
    if num == 7:
        break
    

"""28.Print numbers from 1 to 10, but skip 5.Use continue.
Expected output:
1
2
3
4
6
7
8
9
10"""
print("Solution 28")

for num in range(1,11):
    if num == 5:
        continue

    print(num)

"""29.Given:numbers = [10, 20, -1, 30, 40].Print the numbers until -1 appears.When -1 appears, stop the loop."""
print("Solution 29")

numbers = [10, 20, -1, 30, 40]

for num in numbers:
    if num == -1:
        break
    print(num)

"""30.Given:numbers = [10, -5, 20, -10, 30].Skip all negative numbers and print only the remaining values using continue."""
print("Solution 30")
numbers = [10, -5, 20, -10, 30]

for num in numbers:
    if num < 0 :
        continue
    print(num)

"""31.Given:numbers = [1, 2, 3, 4, 5].Create a new list containing the square of every number.
Expected result:[1, 4, 9, 16, 25]"""
print("Solution 31")
numbers = [1, 2, 3, 4, 5]
new_list = []

for num in numbers :
    new_list.append(num ** 2)

print(new_list)

"""32.Given:numbers = [10, 15, 20, 25, 30].Create a new list containing only the even numbers.
Expected result:[10, 20, 30]"""
print("Solution 32")
numbers = [10, 15, 20, 25, 30]
new_list = []

for num in numbers:
    if num % 2 == 0 :
        new_list.append(num)

print(new_list)

"""33.Given:names = ["aman", "riya", "rahul", "sara"].Create a new list where every name is converted to uppercase.
Expected result:["AMAN", "RIYA", "RAHUL", "SARA"]"""
print("Solution 33")
names = ["aman", "riya", "rahul", "sara"]
new_list =[]

for name in names :
    new_list.append(name.upper())

print(new_list)

"""34.Use a while loop to print numbers from 1 to 10."""
print("Solution 34")

number = 1 

while number <= 10:
    print(number)
    number +=1

"""35.Use a while loop to print even numbers from 2 to 20."""
print("Solution 35")

num = 2

while num <= 20:
    if num % 2 == 0:
        print(num)
    num+=1

"""36.Use a while loop to print numbers from 10 to 1."""
print("Solution 36")

num = 10

while num >= 1 :
    print(num)
    num=num -1

"""37.Use a while loop to calculate the sum of numbers from 1 to 100.Do not use:sum()"""
print("Solution 37")

num = 1
total = 0

while num <=100:
    total +=num
    num+=1

print(total,"is the sum")
"""38.Start with:number = 1.Use a while loop to calculate:1 + 2 + 3 + ... + 50.Print the final total."""
print("Solution 38")
num = 1
total = 0

while num <=50:
    total +=num
    num+=1

print(total,"is the sum")

"""39.Given:sales = [500, 1200, 800, 1500, 300, 2000]
Using a loop:
Count how many sales are greater than or equal to 1000.
Calculate the total of only those sales.
For example, the qualifying sales are:
1200
1500
2000
Your program should print:
Count: 3
Total: 4700"""
print("Solution 39")

sales = [500, 1200, 800, 1500, 300, 2000]

count = 0
total = 0

for sale in sales:
    if sale >= 1000:
        count+=1
        total+=sale

print("Count:" , count)
print("Total" , total)


"""40.Given:transactions = [500, -200, 1000, 0, -150, 750, 1200, -50]
Using one loop, calculate all of the following:
Total positive transaction amount.
Number of positive transactions.
Number of negative transactions.
Number of zero transactions.
Largest positive transaction.
Do not use:sum(),max(),filter()

Think about which variables you need to create before the loop.
A possible expected result:
Total Positive Amount: 3450
Positive Transactions: 4
Negative Transactions: 3
Zero Transactions: 1
Largest Positive Transaction: 1200 """
print("Solution 40")
transactions = [500, -200, 1000, 0, -150, 750, 1200, -50]

total = 0
positive_count = 0 
negative_count = 0
zero_count = 0
largest_positive_transaction = transactions[0]

for num in transactions :
    if num > 0 :
        total+=num
        positive_count+=1
        if num > largest_positive_transaction:
            largest_positive_transaction = num
    elif num < 0 :
        negative_count+=1
    
    else:
        zero_count+=1
    

print(f"Total Positive Amount: {total}")
print(f"Positive Transactions: {positive_count}")
print(f"Negative Transactions: {negative_count}")
print(f"Zero Transactionst: {zero_count}")
print(f"Largest Positive Transaction: {largest_positive_transaction}")