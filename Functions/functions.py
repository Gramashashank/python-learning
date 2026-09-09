# Examples of Functions in python
#Example 1: Simple function

def greet():
    print("Hello, Shashank")
greet()
#----o/p---#
"Hello, Shashank"

#Example 2: Function with parameter
def greet_name(name):
    print("Hello", name)
greet_name("Shashank")
greet_name("Rahul")
#----o/p----#
"""Hello Shashank
Hello Rahul"""


#Example 3: Function with multiple parameters

def add(a, b):
    print(a + b)

add(10, 20)
add(50, 30)
#-----o/p----#
"""30
80"""

#Example 4: Function with return value

def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print("Result:", result)
#---o/p--#
"""Result: 30"""

#Example 5: Positional and keyword arguments

def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Shashank", 22)
student(age=22, name="Shashank")
#---o/p--#
"""Name: Shashank
Age: 22
Name: Shashank
Age: 22"""

#Example 6: Default arguments

def greet_user(name="User"):
    print("Hello", name)

greet_user()
greet_user("Shashank")
#---o/p--#
"""Hello User
Hello Shashank"""


#Example 7: Function with user input

def square(n):
    return n * n

num = int(input("Enter number: "))
print("Square =", square(num))
#---o/p---#
"""Enter number: 5
Square = 25"""


#Example 8: Function returning multiple values

def calculations(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    return addition, subtraction, multiplication
x, y, z = calculations(10, 5)
print("Addition:", x)
print("Subtraction:", y)
print("Multiplication:", z)
#---o/p--#
"""Addition: 15
Subtraction: 5
Multiplication: 50"""


#Example 9: *args: multiple positional arguments
def add_many(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(add_many(10, 20))
print(add_many(10, 20, 30))
print(add_many(1, 2, 3, 4, 5))
#---o/p---#
"""30
60
15 """

#Example 10: **kwargs: multiple keyword arguments

def student_details(**details):
    print(details)


student_details(name="Shashank", age=22, city="Hyderabad")
#---o/p---#
"{'name': 'Shashank', 'age': 22, 'city': 'Hyderabad'}"


#Example 11: Local and global variables
x = 100
def test():
    local_x = 10
    print("Local variable:", local_x)
    print("Global variable:", x)

test()


#Example 12: Example of function call inside another function

def square_of_number(n):
    return n * n

def show_square(num):
    ans = square_of_number(num)
    print("Square of", num, "is", ans)
show_square(7)

#Example 13: Local Variable

def my_function():
    x = 10
    print(x)

my_function()
#---o/p---#
"""10"""

#Example 14: Global Variable
x = 100

def my_function_global():
    print(x)

my_function_global()
#---o/p---#
"""100"""

#Example 15: Changing global variable using global keyword
x = 10

def change():
    global x
    x = 20

change()
print(x)
#---o/p---#
"""20"""

#Example 16: Non-local variable

def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20

    inner()
    print(x)

outer()
#---o/p---#
"""20"""

#Example 17: Nested function

def outer_function():
    print("Outer function")

    def inner_function():
        print("Inner function")

    inner_function()

outer_function()
#---o/p---#
"""Outer function
Inner function"""

#Example 18: Nested function with parameters

def outer(a):
    def inner(b):
        return a + b

    return inner(20)

result = outer(10)
print(result)
#---o/p---#
"""30"""

#Example 19: Nested function + nonlocal

def counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        print(count)

    increment()
    increment()
    increment()

counter()
#---o/p---#
"""1
2
3"""
