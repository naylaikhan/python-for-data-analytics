"""1.Create a list called numbers containing:10, 20, 30, 40, 50.Print the entire list."""
print("Solution 1")
numbers = [10,20,30,40,50]
print(numbers)

"""2.Given:fruits = ["Apple", "Banana", "Mango", "Orange"].Print the first element."""
print("Solution 2")
fruits = ["Apple", "Banana","Mango","Orange"]
first_element = fruits[0]
print(first_element)

"""3.Using the same list:fruits = ["Apple", "Banana", "Mango", "Orange"].Print the last element using negative indexing."""
print("Solution 3")
fruits = ["Apple","Banana","Mango","Orange"]
last_element = fruits[-1]

print(last_element)

"""4.Given:numbers = [5, 10, 15, 20, 25].Print the element at index 2."""
print("Solution 4")
numbers = [5,10,15,20,25]
print(numbers[2])

"""5.Given:names = ["Ali", "Sara", "John"].Change "John" to "David".Print the updated list."""
print("Solution 5")
name = ["Ali","Sara","Jhon"]
name[2] = "David"
print(name)

"""6.Create an empty list called cities.Add the following cities one by one using append():
Delhi
Mumbai
Bangalore
Chennai
Print the final list."""

print("Solution 6")
city = []
city.append("Delhi")
city.append("Mumbai")
city.append("Bangalore")
city.append("Chennai")

print(city)

"""7.Given:numbers = [10, 20, 40, 50].Insert 30 at the correct position so the list becomes:[10, 20, 30, 40, 50]"""
print("Solution 7")
numbers = [10,20,40,50]
numbers.insert(2,30)
print(numbers)

"""8.Given:names = ["Ali", "Sara", "John", "Maya"]
Remove "Sara" using remove()."""
print("Solution 8")
names = ["Ali","Sara","John","Maya"]
names.remove("Sara")
print(names)

"""9.Given:numbers = [10, 20, 30, 40].Remove the element at index 2 using pop()."""
print("Solution 9")
numbers = [10,20,30,40]
numbers.pop(2)
print(numbers)

"""10.Given:colors = ["Red", "Blue", "Green"].Remove the last item without specifying an index.
Print both:The removed item.The updated list."""
print("Solution 10")
colors = ["Red","Blue","Green"]
colors.pop()
print(colors)

"""11.Given:numbers = [10, 20, 30, 20, 40, 20].Find how many times 20 appears in the list."""
print("Solution 11")
numbers = [10,20,30,20,40,20]
count= numbers.count(20)
print(count)

"""12.Given:names = ["Ali", "Sara", "John", "Maya"].Check whether "John" exists in the list.
Your output should be either:True or False"""
print("Solution 12")
names = ["Ali", "Sara", "John", "Maya"]
print("John" in names)

"""13.Given:employees = ["Ali", "Sara", "John"].Check whether "David" is not present in the list.Use not in."""
print("Solution 13")
employees = ["Ali", "Sara", "John"]

print("David" not in employees)

"""14.Given:numbers = [100, 200, 300, 400, 500].Find the index of 400."""
print("Solution 14")
numbers = [100, 200, 300, 400, 500]

position = numbers.index(400)
print("Index of 400 :", position)

"""15.Given:sales = [1200, 2500, 1800, 3200, 1500]
Find:
Total sales
Highest sale
Lowest sale
Number of sales"""
print("Solution 15")
sales = [1200, 2500, 1800, 3200, 1500]

total= sum(sales)
highest_sale = max(sales)
lowest_sale = min(sales)
num_of_sales = len(sales)

print("Total sales : ",total)
print("Highest sales : ",highest_sale)
print("Lowest sale : ",lowest_sale)
print("Number of sales : ",num_of_sales)

"""16.Given:numbers = [50, 10, 40, 20, 30]
Sort the list in ascending order."""
print("Solution 16")
numbers = [50, 10, 40, 20, 30]

numbers.sort()
print(numbers)

"""17.Using the same list:numbers = [50, 10, 40, 20, 30].Sort it in descending order."""
print("Solution 17")
numbers = [50, 10, 40, 20, 30]

numbers.sort(reverse=True)
print(numbers)

"""18.Given:names = ["John", "Ali", "Sara", "David"].Create a sorted version of the list without changing the original list.
Print both lists."""
print("Solution 18")
names = ["John", "Ali", "Sara", "David"]
new_list = names.copy()
new_list.sort()
print(names)
print(new_list)

"""19.Given:numbers = [10, 30, 20, 50, 40].Reverse the current order of the list.Do not sort it."""
print("Solution 19")
numbers = [10, 30, 20, 50, 40]
numbers.reverse()
print(numbers)

"""20.Given:numbers = [10, 20, 30, 40, 50, 60, 70]
Print:[20, 30, 40]."""
print("Solution 20")
numbers = [10, 20, 30, 40, 50, 60, 70]
sliced_numbers = numbers[1:4]
print(sliced_numbers)

"""21.Using the same list:numbers = [10, 20, 30, 40, 50, 60, 70].Print the first four elements using slicing."""
print("Solution 21")
numbers = [10, 20, 30, 40, 50, 60, 70]
first_four_number = numbers[:4]
print(first_four_number)

"""22.Using the same list, print the last three elements using slicing."""
print("Solution 22")
numbers = [10, 20, 30, 40, 50, 60, 70]
last_three_elements = numbers[-1:-4:-1]
print(last_three_elements)

"""23.Given:numbers = [10, 20, 30, 40, 50, 60].Print every second element using slicing.
Expected output:[10, 30, 50]"""
print("Solution 23")
numbers = [10, 20, 30, 40, 50, 60]
sliced_numbers = numbers[::2]
print(sliced_numbers)

"""24.Given:numbers = [10, 20, 30, 40, 50].Create a reversed version using slicing.
Expected output:[50, 40, 30, 20, 10]"""
print("Solution 24")
numbers = [10, 20, 30, 40, 50]
numbers.reverse()
print(numbers)

"""25.Given:numbers = [10, 15, 20, 25, 30, 35].Use a for loop to print only the even numbers."""
print("Solution 25")
numbers = [10, 15, 20, 25, 30, 35]
new_list = []

for num in numbers:
    if num % 2 == 0 :
        new_list.append(num)

print(new_list)

"""26.Given:sales = [500, 1200, 800, 2500, 3000, 900].Print only the sales greater than 1000."""
print("Solution 26")
sales = [500, 1200, 800, 2500, 3000, 900]
new_list = []

for sale in sales :
    if sale > 1000:
        new_list.append(sale)

print(new_list)

"""27.Given:numbers = [10, 20, 30, 40, 50].Create a new empty list called doubled.
Using a loop, add the double of every number to doubled.
Expected result:[20, 40, 60, 80, 100]"""
print("Solution 27")
numbers = [10, 20, 30, 40, 50]
doubled = []

for num in numbers:
    num = num * 2
    doubled.append(num)

print(doubled)

"""28.Given:marks = [45, 78, 32, 90, 55, 28, 67].Create an empty list called passed_students_marks.
Using a loop and an if condition, add only marks that are 40 or above.
Expected result:[45, 78, 90, 55, 67]"""
print("Solution 28")
marks = [45, 78, 32, 90, 55, 28, 67]
passed_students_marks = []

for mark in marks:
    if mark >= 40 :
        passed_students_marks.append(mark)

print(passed_students_marks)

"""29.Given:numbers = [10, 15, 20, 25, 30, 35, 40].Find the sum of only the even numbers.
Do not manually write:10 + 20 + 30 + 40"""
print("Solution 29")
numbers = [10, 15, 20, 25, 30, 35, 40]
total = 0

for num in numbers:
    if num % 2 == 0:
        total+=num

print(total)

"""30.Given daily sales:sales = [1200, 800, 1500, 2200, 500, 3000, 1800]
Write a program that finds:
Total sales
Average sales
Highest sale
Lowest sale
Number of days where sales were greater than 1000
Create a new list containing only sales greater than 1000
Expected final filtered list:[1200, 1500, 2200, 3000, 1800]"""
print("Solution 30")
sales = [1200, 800, 1500, 2200, 500, 3000, 1800]
new_list = []
total_sales = sum(sales)
average_sales = sum(sales)/len(sales)
highest_sale = max(sales)
lowest_sale = min(sales)
count = 0
for sale in sales :
    if sale > 1000:
        new_list.append(sale)
        count +=1

print(f"Total sales : {total_sales}")
print(f"Average sales : {average_sales}")
print(f"Highest sale : {highest_sale}")
print(f"Lowest sale : {lowest_sale}")
print(f"days where sales were greater than 1000 : {count}")
print(f"filtered list : {new_list}")