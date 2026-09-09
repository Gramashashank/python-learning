# Example for Lambda Function

#Example 1: simple example

square = lambda x: x * x
n=int(input("enter the number:"))
res=square(n)
print(res)
#---o/p---#
"""enter the number:5
25"""

#Example 2: Example for map()

student_name=input("enter the student name:").split(" ")
student_upper_case=list(map(lambda name:name.upper(),student_name))
print(f"student name in upper case:{student_upper_case}")
#---o/p---#
"""enter the student name:shashank
student name in upper case:['SHASHANK']"""

#Example 3: Example for filter()

salary=input("enter the 5 salary:").split()
salary=list(map(lambda x:float(x),salary))
f_salary=list(filter(lambda x:x>30000,salary))
print(f"salary greater than 30000:{f_salary}")
#---o/p---#
"""enter the 5 salary:25000 50000 60000 75000 10000
salary greater than 30000:[50000.0, 60000.0, 75000.0]"""

#Example 4: Example for reduce()

from functools import reduce
n=[1,2,3,4,5]
r=reduce(lambda x,y:x+y,n)
print(f"sum of digits:{r}")
#---o/p---#
"sum of digits:15"

#Example 5: Example for sort()

salaries=[23000,30100,62000,27000,31000,18000]
total_salaries=reduce(lambda x,y:x+y,salaries)
print(f"company providing total salary amount to employees:{total_salaries}")

s=sorted(salaries,key=lambda x:x,reverse=False)
print(s)
#---o/p---#
"""company providing total salary amount to employees:191100
[18000, 23000, 27000, 30100, 31000, 62000]"""

fruits=input("enter the fruits:").split()
fruits_sorted=sorted(fruits,key=lambda x:len(x),reverse=True)
print(f"fruits_sorted based on the length: {fruits_sorted}")
#---o/p---#
"""enter the fruits:apple mango banana kiwi watermelon
fruits_sorted based on the length: ['watermelon', 'banana', 'apple', 'mango', 'kiwi']"""
