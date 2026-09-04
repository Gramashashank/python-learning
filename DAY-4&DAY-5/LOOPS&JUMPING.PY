#Loops and Jumping statement

# example 1

n=int(input("enter the number:"))

for i in range(n):
    print(i)

#---o/p---#

"""enter the number:10
0
1
2
3
4
5
6
7
8
9"""
#example 2
for i in range(0,n+1,1):
    print(i)

#--o/p-#

"""enter the number:10
0
1
2
3
4
5
6
7"""

#example3
for i in range(1,n+1,2):
    print(i)

#---o/p---#

"""enter the number:20
1
3
5
7
9
11
13
15
17
19"""

#example for jumping statement

#example1
for i in range(n):
    if i==5:
        break
    print(i)

#-----o/p---#
"""enter the number:10
0
1
2
3
4"""

#example 2
for i in range(0,n):
    if i==5:
        continue
    print(i)
#---o/p---#

"""enter the number:10
0
1
2
3
4
6
7
8
9
"""
#example 3
for i in range(0,n):
    if i==8:
        pass
    print(i)

#---o/p---#
"""enter the number:10
0
1
2
3
4
5
6
7
8
9"""

#Example for while

#Example 1
sum=0
i=0
while n!=0:
    if i>n:
        break
    sum=sum+i
    i+=1
print(sum) 

#---o/p---#
"""enter the number:10
55
"""
# some problem questions oN LOOPS AND JUMPING Statements
"""Print First N Prime Numbers
Example
Input:
10
Output:
2 3 5 7 11 13 17 19 23 29
"""
count=0
n1=2
while count < n:
    factors =0
    for i in range(1,n1+1):
        if n1%i==0:
            factors+=1
    if factors ==2:
        print(n1,end=" ")
        count+=1
    n1+=1

"""Armstrong Number
Problem Statement
Write a program to check whether a given number is an Armstrong Number or not.
Example:
153
Number of digits = 3
1³ + 5³ + 3³
1 + 125 + 27
153

Example 1
Input:
153
Output:
Armstrong Number
Example 2
Input:
123
Output:
Not an Armstrong Number
"""

temp=n
result=0
if n>=1000:
    power=4
else:
    power=3
while n>0:
    digit=n%10
    result=result+digit**power
    n=n//10        
if temp ==result:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")


"""Problem Statement
Write a program to check whether a given number is a Spy Number or not.
Example 1
Input
123
Step 1: Separate the digits
1
2
3
Step 2: Find the Sum
1 + 2 + 3 = 6
Step 3: Find the Product
1 × 2 × 3 = 6
Step 4: Compare
Sum = 6

Product = 6
Since both are equal,
✅ 123 is a Spy Number

Example 2
Input
145
Digits
1
4
5
Sum=1 + 4 + 5 = 10
Product
1 × 4 × 5 = 20
10 ≠ 20
❌ Not a Spy Number
"""
sum=0
prod=1
temp=n
while n>0:
    digit=n%10
    sum=sum+digit
    prod=prod*digit
    n=n//10
if sum==prod:
    print(f"{temp} is a Spy NUmber")
else:
    print(f"{temp} is not a Spy number")



"""Strong Number
Problem Statement
Write a program to check whether a given number is a Strong Number or not.
Example
Input
145
Step 1: Separate the Digits
The digits of 145 are:
1
4
5

Step 2: Find the Factorial of Each Digit
Factorial of 1
1! = 1
Factorial of 4
4! = 4 × 3 × 2 × 1
= 24
Factorial of 5
5! = 5 × 4 × 3 × 2 × 1
= 120

Step 3: Add All the Factorials
1! + 4! + 5!

= 1 + 24 + 120

= 145

Step 4: Compare with the Original Number
Original Number = 145
Calculated Sum = 145
145 == 145
Since both are equal,
145 is a Strong Number.
Example 2
Input
123
Digits
1
2
3
Factorials
1! = 1
2! = 2
3! = 6
Sum
1 + 2 + 6 = 9
Compare
Original Number = 123
Calculated Sum = 9
9 ≠ 123
Output: Not a Strong Number
"""

sum=0
temp=n
while n>0:
    digit=n%10
    fact=1
    for i in range(1,digit+1):
        fact=fact*i
    sum=sum+fact
    n=n//10
if sum==temp:
    print(f"{temp} is a strong number")
else :
    print(f"{temp} is not a strong number")


# some problems on pattern

"""1. Right-Angled Triangle
Question: Print a right-angled triangle using *.
Input:
 Number of rows
Output:
 Print the triangle.
Example:
Input: 5

Output:
*
**
***
****
*****
"""

for row in range(n):
    for column in range(row+1):
        print("*",end=" ")
    print()

"""Inverted Triangle
Question: Print an inverted right-angled triangle using *.
Input:
 Number of rows
Output:
 Print the inverted triangle.
Example:
Input: 5

Output:
*****
****
***
**
*
"""
for row in range(n):
    for column in range(n-row):
        print("*",end=" ")
    print()

"""Number Triangle
Question: Print numbers in a triangular pattern.
Input:
 Number of rows
Output:
 Print numbers starting from 1 in every row.
Example:
Input: 5

Output:
1
12
123
1234
12345
"""
for row in range(1,n+1):
    for column in range(1,row+1):
        print(column,end=" ")
    print()

"""Continuous Number Pattern
Question: Print numbers continuously in a triangular pattern.
Input:
 Number of rows
Output:
 Print continuously increasing numbers.
Example:
Input: 4

Output:
1
23
456
78910
"""
num = 1
for row in range(1, n + 1):
    for column in range(1, row):
        print(num, end=" ")
        num += 1
    print()

"""Pyramid Pattern
Question: Print a pyramid using *.
Input:
 Number of rows
Output:
 Print a centered pyramid.
Example:
Input: 5

Output:
    *
   ***
  *****
 *******
*********
"""
for row in range(n):
    for space in range(n-row):
        print(" ",end=" ")
    for star in range(2*row+1):
        print("*",end=" ")
    print()

"""Diamond Pattern
Question: Print a diamond using *.
Input:
 Number of rows for the upper half
Output:
 Print a complete diamond.
Example:
Input: 3

Output:
  *
 ***
*****
 ***
  *
"""

for row in range(1,n+1):
    for space in range(n-row):
        print(" ",end=" ")
    for star in range(2*row-1):
        print("*",end=" ")
    print()
for row in range(n-1,0,-1):
    for space in range(n-row):
        print(" ",end=" ")
    for star in range(2*row-1):
        print("*",end=" ")
    print()

""" Hollow Square
Question: Print a hollow square using *.
Input:
 Size of the square
Output:
 Print stars only on the boundary.
Example:
Input: 5

Output:
*****
*   *
*   *
*   *
*****
"""
for row in range(n):
    for column in range(n):
        if row==0 or row==n-1 or column==0 or column==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()


"""Alphabet Triangle
Question: Print alphabets in a triangular pattern.
Input:
 Number of rows
Output:
 Print alphabets starting from A.
Example:
Input: 5

Output:
A
AB
ABC
ABCD
ABCDE
"""
for row in range(n+1):
    a=65
    for colunm in range(1,row+1):
        print(chr(a),end=" ")
        a+=1
    print()


""" Palindrome Number Pattern
Question: Print a palindrome number pattern.
Input:
 Number of rows
Output:
 Print numbers increasing and then decreasing in each row.
Example:
Input: 5

Output:
1
121
12321
1234321
123454321
"""
for row in range(n+1):
    for column in range(1,row+1):
        print(column,end="")
    for column in range(row-1,0,-1):
        print(column,end="")
    print()