# ============================================================
# PYTHON DAY 1 - FUNDAMENTALS
# Topics: Python basics, Variables, Data Types, Type Conversion,
#         Input and Output


# ------------------------------------------------------------
# 1. WHAT IS PYTHON?
# ------------------------------------------------------------
# Definition:
# Python is a high-level, interpreted, general-purpose programming
# language. It is popular because its syntax is simple and readable.
#
# Python is commonly used for:
# - Web development
# - Data Science
# - Artificial Intelligence / Machine Learning
# - Automation
# - Backend development
# - Testing
#
# Example:
print("Hello Python")


# ------------------------------------------------------------
# 2. VARIABLES
# ------------------------------------------------------------
# Definition:
# A variable is a name used to store a value.
#
# Python does not require us to specify the data type while creating
# a variable. Python automatically determines the data type.
#
# Syntax:
# variable_name = value

name = "Rama"
age = 22
salary = 25000.50

print(name)
print(age)
print(salary)


# ------------------------------------------------------------
# 3. DATA TYPES
# ------------------------------------------------------------
# Definition:
# A data type tells us what kind of value a variable contains.
#
# Main data types for Day 1:
#
# int   -> Whole numbers
# float -> Decimal numbers
# str   -> Text / characters
# bool  -> True or False
#
# Examples:

# int
age = 22

# float
percentage = 85.5

# str
student_name = "Rama"

# bool
is_student = True

print(age)
print(percentage)
print(student_name)
print(is_student)


# ------------------------------------------------------------
# 4. type()
# ------------------------------------------------------------
# Definition:
# type() is a built-in function used to find the data type
# of a value or variable.
#
# Example:

print(type(age))
print(type(percentage))
print(type(student_name))
print(type(is_student))


# ------------------------------------------------------------
# 5. TYPE CONVERSION
# ------------------------------------------------------------
# Definition:
# Type conversion means changing a value from one data type
# to another data type.
#
# Common type conversion functions:
#
# int()   -> Converts a value to integer
# float() -> Converts a value to float
# str()   -> Converts a value to string
# bool()  -> Converts a value to boolean


# String -> Integer
age_text = "22"
age_number = int(age_text)

print(age_number)
print(type(age_number))


# Integer -> String
number = 22
number_text = str(number)

print(number_text)
print(type(number_text))


# Integer -> Float
number = 10
decimal_number = float(number)

print(decimal_number)
print(type(decimal_number))


# Float -> Integer
decimal_number = 10.5
whole_number = int(decimal_number)

print(whole_number)
print(type(whole_number))


# ------------------------------------------------------------
# 6. OUTPUT - print()
# ------------------------------------------------------------
# Definition:
# print() is used to display information on the screen.
#
# Examples:

print("Hello")
print("Python")
print(100)
print(True)

name = "Rama"
age = 22

print(name)
print(age)

# Printing a label with a variable:
print("My name is", name)
print("My age is", age)


# ------------------------------------------------------------
# 7. INPUT - input()
# ------------------------------------------------------------
# Definition:
# input() is used to take data from the user through the keyboard.
#
# IMPORTANT:
# input() always returns the entered value as a STRING.
#
# Example:

user_name = input("Enter your name: ")
print("Your name is", user_name)


# ------------------------------------------------------------
# 8. INPUT WITH TYPE CONVERSION
# ------------------------------------------------------------
# Since input() returns a string, we can use type conversion when
# we need another data type.
#
# Example:
#
# age = int(input("Enter your age: "))
#
# Here:
# input() -> takes the user's input as a string
# int()   -> converts that string into an integer
# age     -> stores the converted integer


# ============================================================
# DAY 1 PRACTICE TASKS
# ============================================================


# ------------------------------------------------------------
# TASK 1 - Variables and Output
# ------------------------------------------------------------
# Create variables for:
# name, age, city, course
# Then print all of them.

name = "Rama"
age = 22
city = "Hyderabad"
course = "Python"

print("Name:", name)
print("Age:", age)
print("City:", city)
print("Course:", course)


# ------------------------------------------------------------
# TASK 2 - Data Types
# ------------------------------------------------------------
# Create the following variables and print their types:
# name, age, percentage, is_student

name = "Rama"
age = 22
percentage = 85.5
is_student = True

print(type(name))
print(type(age))
print(type(percentage))
print(type(is_student))


# ------------------------------------------------------------
# TASK 3 - User Input
# ------------------------------------------------------------
# Take the following values from the user:
# Name, Age, City, Course
# Then display them.
#
# Note:
# Age is taken using input(), so it will initially be a string.

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
course = input("Enter your course: ")

print("Name:", name)
print("Age:", age)
print("City:", city)
print("Course:", course)


# ------------------------------------------------------------
# TASK 4 - Student Details
# ------------------------------------------------------------
# Take Name, Age and Course from the user.
# Display them in the following format:
#
# ----- Student Details -----
# Name: ...
# Age: ...
# Course: ...

name = input("Enter your name: ")
age = input("Enter your age: ")
course = input("Enter your course: ")

print()
print("----- Student Details -----")
print("Name:", name)
print("Age:", age)
print("Course:", course)


# ------------------------------------------------------------
# TASK 5 - String to Integer
# ------------------------------------------------------------
# Take a number as input.
# Convert it to an integer.
# Print the value and its type.

num = input("Enter a number: ")
num = int(num)

print(num)
print(type(num))


# ------------------------------------------------------------
# TASK 6 - Type Conversion Practice
# ------------------------------------------------------------
# Write and understand these conversions:
#
# String -> Integer
# Integer -> String
# Integer -> Float
# Float -> Integer
#
# Print the value and type after each conversion.


# String -> Integer
value1 = "100"
value1 = int(value1)
print("String to Integer:", value1)
print(type(value1))


# Integer -> String
value2 = 100
value2 = str(value2)
print("Integer to String:", value2)
print(type(value2))


# Integer -> Float
value3 = 100
value3 = float(value3)
print("Integer to Float:", value3)
print(type(value3))


# Float -> Integer
value4 = 100.5
value4 = int(value4)
print("Float to Integer:", value4)
print(type(value4))


# ============================================================
# DAY 1 FINAL PRACTICE
# ============================================================
# Take the following details from the user:
# Name
# Age
# City
# Course
#
# Then display the student information.
#
# Do not use operators, conditions, loops, functions, lists, etc.
# ============================================================

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
course = input("Enter your course: ")

print()
print("----- Student Information -----")
print("Name:", name)
print("Age:", age)
print("City:", city)
print("Course:", course)

# IMPORTANT:
# input() always returns a string.
# ============================================================
