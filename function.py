# What is Function?
# A function is a block of code that runs only when it is called.

# Why use Functions?

# 1.Avoid repeating code
# 2. Makes program clean & organized
# 3. Easy to debug and reuse

# Syntax:
# def function_name():
#   # code

#Example:

def greet():
    print("Hello Students")

# ------------------------------------------------------- #

# Functions with parameters
# Used to pass values

def greet(name="Students"):
    print(f"Hello{name}")

greet()
greet("Shreyarth")
greet("AICW")



# ---------------------------------------------------------#


# Function with Return Value 
# USed when we want to send result back

def add(a,b):
    return a + b 

result = add(2 , 3)
print(result)


# ----------------------------------------------------------- #

#Task 1: Create a function to calculate and return result  

def calculate(a, b):
    return a + b

a = int(input())
b = int(input())

print(calculate(a, b))


# Task 2: create a function to check if a number is even or odd

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = 4
print(check_even_odd(num))


# Alternative

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = input()
print(check_even_odd(num))






# Task 3: Create a function to find factorial of a number

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

num = int(input("Enter number: "))
print(factorial(num))





# Task 4: Create a function to find maximum of three numbers.

def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

result = find_max(x, y, z)
print("Maximum number is:", result)




# Task 5: create a function to check if a string is Palindrome

def is_palindrome(s):
    s = s.lower()  
    return s == s[::-1]

text = input("Enter a string: ")

if is_palindrome(text):
    print("It is a Palindrome")
else:
    print("It is NOT a Palindrome")



# Task 6: Create a function to calculate the area pf circle

def aoc(radius):
    pi = 3.14  
    area = pi * radius * radius
    return area

r = float(input("Enter radius: "))
print("Area of circle =", aoc(r))