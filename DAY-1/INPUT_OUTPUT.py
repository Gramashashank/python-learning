#------INPUT/OUTPUT------#

#examples for output concept

#example1
print("Hello, World!")
#---O/P----#
#---Hello, World!---#

#example2
name="shashank"
print("Hello, " + name + "!")
#---O/P----#
#---Hello, shashank!----#

#example3
age=18
print("I am " + str(age) + " years old.")
#---O/P----#
#---I am 18 years old.----#

#example4
height=5.9
print("my height is", height, "feet.")
#---O/P----#
#---my height is 5.9 feet.----#

#example5
name="shashank"
age=18
height=5.9
print("Hello, my name is", name + ", I am", age, "years old and my height is", height, "feet.")
#---O/P----#
#---Hello, my name is shashank, I am 18 years old and my height is 5.9 feet.----#

#example for the input concept

#example 1
name = input("What is your name? ")
print ("my name is",name)
#---O/P----#
""" What is your name? ramashashank
my name is ramashashank"""

#example2
age = input("What is your age? ")
print ("my age is",age)
print (type(age))
#---O/P----#
""" What is your age? 22
my age is 22
<class 'str'> """

#example3
height = input("What is your height? ")
print ("my height is",height)
print (type(height))
#---O/P----#
""" What is your height? 5.9
my height is 5.9
<class 'str'> """

#example 4
age=int(input("What is your age? "))
print ("my age is",age)
print (type(age))
#---O/P----#
""" What is your age? 22
my age is 22
<class 'int'> """

#example 5
height=float(input("What is your height? "))
print ("my height is",height)
print (type(height))
#---O/P----#
""" What is your height? 5.79
my height is 5.79
<class 'float'> """

#example 6
name=input("What is your name? ")
age=int(input("What is your age? "))
salary=float(input("What is your salary? "))
phone_number=int(input("What is your phone number? "))
print ("my name is",name)
print ("my age is",age)
print ("my salary is",salary)
print ("my phone number is",phone_number)
#---O/P----#

"""INPUT
What is your name? raghu
What is your age? 22 
What is your salary? 50000.50
What is your phone number? 1234567890
OUTPUT
my name is raghu
my age is 22
my salary is 50000.5
my phone number is 1234567890 """