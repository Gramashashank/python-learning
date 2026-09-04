#==========CONTROL STATEMENT=======#

name=input('enter the name:')
age=int(input("enter the number:"))

a=int(input("enter the number1:"))
b=int(input("enter the number2:"))
c=int(input("enter the number3:"))

#Simple IF

if name=="":
    print("name is empty")
else:
    print(f"my name is:{name}")

#-----o/p-----#
""" for if condition
enter the name:
name is empty
for else condition
enter the name:shashank
my name is:shashank"""

#example for if elif statememt

if name=="" and age== 0:
    print("name is empty and age is should be greater than zero")
elif name=="" and age<=18:
    print("name is empty and age should be greater than 18")
elif name =="" and age>18:
    print("name should not be empty and my age is above 18")
elif name!="" and age>18:
    print(f"my name is {name} and age is{age}")

#---o/p---#
"""enter the name:
enter the number:0 
name is empty and age is should be greater than zero

enter the name:
enter the number:17
name is empty and age should be greater than 18

enter the name:
enter the number:20
name should not be empty and my age is above 18

enter the name:raghu
enter the number:20
my name is raghu and age is20"""

#example for if elif else statement

if a>b and a>c:
    print(f"{a} is greater than {b} and {c}")
elif b>a and b>c:
    print(f"{b} is greater than {a} and {c}")
elif c>a and c>a:
    print(f"{c} is greater than {a} and {b}")
else:
    print(f"{a},{b} and {c} all are equal ")

#---o/p---#
"""enter the number1:10
enter the number2:1
enter the number3:2
10 is greater than 1 and 2

enter the number1:2
enter the number2:9
enter the number3:3
9 is greater than 2 and 3

enter the number1:22
enter the number2:23
enter the number3:25
25 is greater than 22 and 23

enter the number1:3
enter the number2:3
enter the number3:3
3,3 and 3 all are equal"""

#=====some more examples for control statememts====#


"""Write a Python program that accepts two integers and checks whether they have the same last digit.

If they do, display:

Same Last Digit

Otherwise, display:

Different Last Digit
Example 1
Input
27
97
Output
Same Last Digit
Example 2
Input
154
289
Output
Different Last Digit
"""
num1=int(input("enter the number:"))
num2=int(input("enter the number1:"))
res=0
res1=0
if num1<=0 and num2<=0:
    print("enter the numbers greater than zero")
else:
    res=num1%10
    res1=num2%10
    if res==res1:
        print(f"Same Last Digit ")
    else:
        print(" Different Last Digit ")


"""Write a Python program that accepts two integers.

Find their sum.

Display whether the sum is:

Even
Odd
"""

if num1<=0 and num2>=0:
    print("enter the numbers greater than zero")
else:
    sum=num1+num2
    if sum%2==0:
        print("sum is even")
    else:
        print("sum is odd")


"""Determine Whether Three Numbers are Consecutive or not"""

# if (
#     (b == a + 1 and c == b + 1) or      # a → b → c
#     (c == a + 1 and b == c + 1) or      # a → c → b
#     (a == b + 1 and c == a + 1) or      # b → a → c
#     (c == b + 1 and a == c + 1) or      # b → c → a
#     (a == c + 1 and b == a + 1) or      # c → a → b
#     (b == c + 1 and a == b + 1)         # c → b → a
# ):
#     print("Consecutive")
# else:
#     print("Not Consecutive")



"""Check Whether Three Numbers are in Ascending, Descending, or Random Order
Example:

5
10
20

Output: Ascending Order
"""

if a<b and b<c:
    print("Ascending order")
elif a>b and b>c:
    print("Descending order")
else:
    print("Random order")


