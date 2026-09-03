# ====== OPERATORS IN PYTHON ======#

# 1. ARITHMETIC OPERATORS

# Addition (+)
a = 5
b = 2
print(a + b)
#---O/P----#
#---7----#

# Boolean example for addition
print(True + True)
#---O/P----#
#---2----#

# String addition example
x = "10"
y = "20"
print(x + y)
#---O/P----#
#---1020----#

# Subtraction (-)
a = 10
b = 3
print(a - b)
#---O/P----#
#---7----#

# Boolean example for subtraction
print(True - False)
#---O/P----#
#---1----#

# Multiplication (*)
a = 4
b = 3
print(a * b)
#---O/P----#
#---12----#

# Boolean example for multiplication
print(True * 5)
#---O/P----#
#---5----#

# String multiplication example
word = "Python"
print(word * 3)
#---O/P----#
#---PythonPythonPython----#

# Division (/)
a = 10
b = 2
print(a / b)
#---O/P----#
#---5.0----#

# Boolean example for division
print(True / True)
#---O/P----#
#---1.0----#

# Floor division (//)
#example 1
a = 15
b = 2
print(a // b)
#---O/P----#
#---7----#

#example 2
a="10"
b=2
print(a/b)
#-----o/p-----#
""" print(a/b)
          ~^~
TypeError: unsupported operand type(s) for /: 'str' and 'int"""

#example 3
a='10'
b='2'
print(a/b)
"""    print(a/b)
          ~^~
TypeError: unsupported operand type(s) for /: 'str' and 'str'"""

# Modulus (%)
#example 1

a = 10
b = 3
print(a % b)
#---O/P----#
#---1----#

#example 2
a=10.32
b=3.2
print(a%b)
#----o/p---#
#----0.7199999999999998-----#

#example 3
a=12
b=True
print(a%b)
#-----o/p-----#
#------0-----#
#example 3
a='10'
b=2
print(a%b)

#---o/p---#
"""print(a%b)
          ~^~
TypeError: not all arguments converted during string formatting"""

a='10'
b='10'
print(a%b)
#-----o/p----#
""" print(a%b)
          ~^~
TypeError: not all arguments converted during string formatting"""

# Exponentiation (**)
a = 2
b = 5
print(a ** b)
#---O/P----#
#---32----#

# Boolean example for exponentiation
print(True ** 3)
#---O/P----#
#---1----#

#example 2
a='10'
b=2
print(a**2)
#----o/p----#
"""" print(a**2)
          ~^^~
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'"""

#example 3
a='10'
b='2'
print(a**b)

#----o/p-----#
""" print(a**b)
          ~^^~
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'str'"""


# 2. COMPARISON OPERATORS

# Equal to (==)
print(5 == 5)
#---O/P----#
#---True----#

# Boolean example
print(True == 1)
#---O/P----#
#---True----#

# Not equal to (!=)
print(5 != 3)
#---O/P----#
#---True----#

# Greater than (>)
print(10 > 7)
#---O/P----#
#---True----#

# Less than (<)
print(3 < 8)
#---O/P----#
#---True----#

# Greater than or equal to (>=)
print(10 >= 10)
#---O/P----#
#---True----#

# Less than or equal to (<=)
print(4 <= 6)
#---O/P----#
#---True----#

# Boolean result example
flag1 = True
flag2 = False
print(flag1 == flag2)
#---O/P----#
#---False----#


# 3. LOGICAL OPERATORS

# AND (and)
print(True and True)
#---O/P----#
#---True----#

print(True and False)
#---O/P----#
#---False----#

# OR (or)
print(True or False)
#---O/P----#
#---True----#

print(False or False)
#---O/P----#
#---False----#

# NOT (not)
print(not True)
#---O/P----#
#---False----#

print(not False)
#---O/P----#
#---True----#

# Example with conditions
age = 20
print(age >= 18 and age <= 25)
#---O/P----#
#---True----#


# 4. ASSIGNMENT OPERATORS

# Simple assignment (=)
value = 10
print(value)
#---O/P----#
#---10----#

# Add and assign (+=)
value = 5
value += 3
print(value)
#---O/P----#
#---8----#

# Subtract and assign (-=)
value = 10
value -= 4
print(value)
#---O/P----#
#---6----#

# Multiply and assign (*=)
value = 4
value *= 2
print(value)
#---O/P----#
#---8----#

# Divide and assign (/=)
value = 10
value /= 2
print(value)
#---O/P----#
#---5.0----#

# Boolean assignment example
flag = True
flag = not flag
print(flag)
#---O/P----#
#---False----#


# 5. BITWISE OPERATORS

# example for AND (&)
print(5 & 3)
#---O/P----#
#---1----#
#example 2
a="shashank"
b="rama"
print(a&b)
#---o/p---#
"""   print(a&b)
          ~^~
TypeError: unsupported operand type(s) for &: 'str' and 'str'"""


# example boolean
print(True & False)
#---O/P----#
#---False----#

# example OR (|)
print(5 | 3)
#---O/P----#
#---7----#

print(True | False)
#---O/P----#
#---True----#

#example for XOR (^)
print(5 ^ 3)
#---O/P----#
#---6----#

#example for NOT (~)
print(~5)
#---O/P----#
#----6----#

#example for Left shift (<<)
print(5 << 1)
#---O/P----#
#---10----#

# example for Right shift (>>)
print(8 >> 1)
#---O/P----#
#---4----#

#  example boolean
print(True ^ True)
#---O/P----#
#---False----#


# 6. MEMBERSHIP OPERATORS


# example for IN
name = "shashank"
print("s" in name)
#---O/P----#
#---True----#

# Example 2
name = "shashank"
print("z" in name)
#---O/P----#
#---False----#

# example for  List
numbers = [10, 20, 30, 40]
print(20 in numbers)
#---O/P----#
#---True----#

# example 1
name = input("Enter your name: ")
print("a" in name)
#---O/P----#
# """Enter your name: rama
# True"""

# example for  NOT IN
name = "shashank"
print("z" not in name)
#---O/P----#
#---True----#

# Example 2
numbers = [10, 20, 30, 40]
print(50 not in numbers)
#---O/P----#
#---True----#

# example for dictionary.
student = {"name": "Rama", "age": 22}
print("name" in student)
#---O/P----#
#---True----#

print("Rama" in student)
#---O/P----#
#---False----#


# 7. IDENTITY OPERATORS


#  example for IS
a = 10
b = a
print(a is b)
#---O/P----#
#---True----#

# Example 2
a = 10
b = 20
print(a is b)
#---O/P----#
#---False----#

# example forIS NOT
a = 10
b = 20
print(a is not b)
#---O/P----#
#---True----#

# example for difference: == vs is
a = [10, 20, 30]
b = [10, 20, 30]
print(a == b)
print(a is b)
#---O/P----#
# """True
# False"""

# example1
a = [10, 20, 30]
b = a
print(a == b)
print(a is b)
#---O/P----#
# """True
# True"""



# some problems on operators#

"""Chocolate Distribution
Problem
A teacher has some chocolates and wants to distribute them equally among students.
Find:
Number of chocolates each student receives.
Number of chocolates left over.
Example
Input
Chocolates = 95

Students = 12
Output
Each student gets 7 chocolates.

Remaining chocolates = 11"""

chocolate=int(input("enter the number of chocolates:"))
students=int(input("enter the number of students:"))
chocolates_per_student=chocolate//students
remaining_chocolates=chocolate%students
print(f"chocolates per student:{chocolates_per_student}")
print(f"remaining chocolates:{remaining_chocolates}")


"""Remove the Last Digit
Problem
Remove the last digit from a given number.
Example
Input
9876
Output
987"""

num=int(input("enter the number:"))
num=num//10
print(num)


"""Append a Digit
Problem
Given a number and another single digit, append the digit to the end of the number.
Example
Input
Number = 245

Digit = 8
Output
2458"""

num=int(input("enter the number:"))
digit=int(input("enter the number:"))
new_number=0
new_number=new_number+(num*10+digit)
print(f"appended last digit number is:{new_number}")


"""Check Whether Two Numbers Have Opposite Signs
Write a Python program that accepts two integers from the user and determines whether they have opposite signs.
Note: Do not use if or else statements.
Example:
Input:
Enter first number: 8
Enter second number: -5

Output:
True"""

num=int(input("enter the number:"))
num1=int(input("enter the number:"))

print((num>0 and num1<0) or (num<0 and num1>0))
