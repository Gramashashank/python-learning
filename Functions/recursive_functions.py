#Example for Recursive Functions
#Example 1: Countdown using recursion

def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)
countdown(5)
print()
#---o/p---#
"""5
4
3
2
1"""

#Example 2: Factorial using recursion

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print("Factorial of 5:", factorial(5))
#---o/p---#
"""Factorial of 5: 120"""

#Example3. Sum of numbers from 1 to n

def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)
print("Sum of 1 to 5:", sum_numbers(5))
#---o/p--#
"""Sum of 1 to 5: 15"""

#Example 4:Fibonacci sequence using recursion

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci sequence first 10 numbers:")
for i in range(10):
    print(fibonacci(i), end=" ")
print()
#---o/p--#
"""Fibonacci sequence first 10 numbers:
0 1 1 2 3 5 8 13 21 34 """

#Example 5. Example of base case and recursive case

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(power(2, 5))
#---o/p---#
"32"

#Example 6: Reverse a number using recursion
def reverse_number(num):
    if num == 0:
        return 0
    print(num % 10, end="")
    return reverse_number(num // 10)

print("\nReverse number using recursion:")
reverse_number(1234)
print()
#---o/p---#
"""Reverse number using recursion:
4321"""

#Example 7. Sum of digits using recursion

def sum_of_digits(num):
    if num == 0:
        return 0
    return num % 10 + sum_of_digits(num // 10)

print("Sum of digits of 1234:", sum_of_digits(1234))
#---o/p---#
"""Sum of digits of 1234: 10"""

#Example 8. Palindrome check using recursion

def is_palindrome(num, start=0):
    digits = [int(d) for d in str(num)]
    if start >= len(digits) // 2:
        return True
    if digits[start] != digits[-1 - start]:
        return False
    return is_palindrome(num, start + 1)
n=int(input("enter the number:"))
result=n
print(f"Is{n} palindrome?", is_palindrome(n))
#---o/p---#
"""enter the number:121
Is 121 palindrome? True"""


