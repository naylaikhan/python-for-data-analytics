"""Create a string variable city = "New Delhi" and print its length using len()."""
city = "New Delhi"

print(len(city))

"""Print the first character and the last character of city using indexing."""
print(city[0])
print(city[-1])

"""Print the string "Hello" in all uppercase and all lowercase."""
text="Hello"
upper= text.upper()
lower = text.lower()
print(upper)
print(lower)

"""Given text = "  Data Analyst  ", remove the extra spaces from both sides and print the result."""
text = "  Data Analyst  "
formated_text=text.strip()
print(formated_text)

"""Create two strings first = "Data" and second = "Science", and join them (with a space in between) to print "Data Science"."""
first = "Data"
second = "Science"
full_name = first + " " +second
print(full_name)
print(f"The Full Course name is {first} {second}")

"""Given word = "Python", print characters from index 1 to 3 (using slicing)."""
word = "Python"
print(word[1:3])

"""Given sentence = "I love data", split it into a list of words."""
sentence = "I love data"
splitted_words = sentence.split(" ")
print(splitted_words)

"""Print the string "Analyst" reversed (hint: think about slicing with a negative step)."""
text = "Analyst"
print(text[::-1])

"""Given name = "rahul", print it with the first letter capitalized (hint: look for a method, don't do it manually)."""
name = "rahul"
lower_name = name.lower()
proper_name = lower_name.capitalize()
print(proper_name)

"""Check whether the word "data" is present inside the sentence "I love data analysis" (hint: use the in keyword)."""
sentence = "I love data analysis"
print("data" in sentence)

"""Given email = "rahul.sharma@gmail.com", extract and print only the username part (before the @)."""
email = "rahul.sharma@gmail.com"
splitted_email = email.split("@")
print(splitted_email[0])

"""Given email = "rahul.sharma@gmail.com", extract and print only the "gmail" part (after the @)."""
email = "rahul.sharma@gmail.com"
splitted_email = email.split("@")
print(splitted_email[1].split(".")[0])

"""Given date = "2024-08-20", extract the year, month, and day separately using slicing."""
date = "2024-08-20"
year=date.split("-")[0]
print(year)
month = date.split("-")[1]
print(month)
day = date.split("-")[2]
print(day)

"""Given phrase = "data,analysis,python", split it into a list using , as the separator."""
phrase = "data,analysis,python"
splitted_phrase = phrase.split(",")
print(splitted_phrase)

"""Given full_name = "Rahul Sharma", print only the first name and only the last name separately."""
full_name = "Rahul Sharma"
first_name = full_name.split(" ")[0]
last_name = full_name.split(" ")[1]
print(first_name)
print(last_name)

"""Given sentence = "Data is the new oil", count how many times the letter "a" appears (hint: look for a counting method)."""
sentence = "Data is the new oil"
a_occurance = sentence.count("a")
print(a_occurance)

"""Given messy = "   Hello World   ", remove the spaces and then replace "World" with "Python"."""
messy = "   Hello World   "
stripped_text = messy.strip()
final_text = stripped_text.replace("World","Python")
print(final_text)

"""Given price = "₹1,20,000", remove the ₹ symbol and the commas so it becomes a clean number-like string "120000"."""
price = "₹1,20,000"
new_price = price.replace(",","")
clean_amount = new_price[1:]
print(clean_amount)

"""Given text = "Data Analyst", check whether it starts with "Data" and whether it ends with "Analyst" (hint: two different string methods)."""
text = "Data Analyst"
print(text.startswith("Data"))
print(text.endswith("Analyst"))

"""Given csv_row = "John,25,Delhi", split it into three separate variables: name, age, city."""
csv_row = "John,25,Delhi"
name = csv_row.split(",")[0]
print(name)
age = csv_row.split(",")[1]
print(age)
city = csv_row.split(",")[2]
print(city)

"""Write logic (using string methods, no loops needed) to check if the string "Madam" reads the same forward and backward (a palindrome check), ignoring case."""
text="Madam"
cleaned_text = text.lower()
reversed_text = cleaned_text[::-1]
print(cleaned_text)
print(reversed_text)

"""Given full_name = "Rahul Kumar Sharma", extract only the middle name without knowing its exact position (hint: split first, then use indexing on the result)."""
full_name = "Rahul Kumar Sharma"
middle_name = full_name.split(" ")[1]
print(middle_name)

"""Given a messy email "  RAHUL.SHARMA@GMAIL.COM  ", clean it so it becomes "rahul.sharma@gmail.com" (remove spaces + lowercase — chain multiple methods together)."""
email = "  RAHUL.SHARMA@GMAIL.COM  "
cleaned_email = email.strip().lower()
print(cleaned_email)

"""Given id_code = "INV-2024-0567", extract just the invoice number 0567 without hardcoding its position by using .split("-")."""
id_code = "INV-2024-0567"
invoice_number = id_code.split("-")[2]
print(invoice_number)

"""Given sentence = "the quick brown fox", convert it to Title Case ("The Quick Brown Fox") without hardcoding — find the right method."""
sentence = "the quick brown fox"
title_case_sentence = sentence.title()
print(title_case_sentence)

"""Given text = "apple,banana,,grape,", split it by commas and figure out why you might get empty strings in the result — describe what's happening (conceptual, then verify with code)."""
text = "apple,banana,,grape,"
splitted_text = text.split(",")
print(splitted_text)

"""Given path = "C:/Users/Rahul/Documents/report.xlsx", extract just the filename report.xlsx using string methods (hint: think about what character separates folders)."""
path = "C:/Users/Rahul/Documents/report.xlsx"
file_name = path.split("/")[-1]
print(file_name)

"""Given path = "C:/Users/Rahul/Documents/report.xlsx", now extract only the file extension xlsx (hint: two different characters can help you split this)."""
path = "C:/Users/Rahul/Documents/report.xlsx"
file_extention_name = path.split("/")[-1].split(".")[1]
print(file_extention_name)

"""Given sentence = "Data Analysts use Python and Excel and SQL", count how many words are there in total without manually counting by eye."""
sentence = "Data Analysts use Python and Excel and SQL"
splitted_sentence = sentence.split(" ")
print(len(splitted_sentence))

