def even_or_odd():
    numb = 422
    if numb % 2 == 0:
        print(f"{numb} is Even")
    else:
        print(f"{numb} is Odd")


num = 21
if num % 2 == 0:
    print(f"{num} is even")
else: 
    print(f"{num} is odd")



# Write a function that takes three required parameters 
# and two optional parameters.

def f(x=2):
    return x**x
def z(y=4):
    return y**y
print(f())
print(z())
print(f(2))
print(f(23))
print(z(8))

num1 = int(input("Please enter a number between 1 and 25: "))
squared_num = num1 ** num1
print(squared_num)

def squared(x):
    return x**2
print(squared(2))

def print_string(string):
    print(type(string))
print_string("Testing: 1, 2, 3.")

def add_mult(a,b,c,x=100,z=1000):
    return a + b + c * x * z

result = add_mult(10, 15, 25)
print(result)

# Write a program with two functions. The first function 
# should take an integer as a parameter and return the result 
# of the integer divided by 2. The second function should take 
# an integer as a parameter and return the result of the integer 
# mulitplied by 4. Call the first function, save the result as a 
# variable, and pass it as a parameter to the second function. 

def divide(x):
    return x//2
def multiply(x):
    return x * 4
y = divide(4)
z = multiply(y)
print(z)


# Write a function that converts a string to a float and returns 
# the result. Use exception handling to catch the exception that could occur.

def convert(string):
    try:
        return float(string)
    except ValueError:
        print("Could not convert the string to a float.")
c = convert("495.2")
print(c)

# Add a docstring to all of the functions you wrote in challenges 1-5.



#I created this function to add five to any number that was passed 
# in to it and return the new value. It doesn't throw any errors 
# but it returns the wrong number.
# Can you help me fix the function?

import random
def add_five(num):
    total = random.randint(num + 5)
    return num

chosen_num = int(input("Enter any whole number: "))
add_num = int(chosen_num + 5)
print(add_num)


# Concatenation (bring multiple strings together) of strings
greeting = "Why hello"
name = "George"
full_greeting = greeting + ", " + name + "!"
print("\nConcatenation:")
print(full_greeting)

health = int(input("Enter your health (0-100): "))
energy = int(input("Enter your energy (0-100): "))
has_sword = input("Do you have a sword? (y or n): ").strip().lower()

def add_five(num):
    total = num + 5
    return num

def greet(Greg, Daniel):
    return(f"Well, hello {Greg} and {Daniel}.")
greeting = "Well, hello, Greg and Daniel."
print(greeting)