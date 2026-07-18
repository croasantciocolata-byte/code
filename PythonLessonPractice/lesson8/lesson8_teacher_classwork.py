# num = 2

# for i in range(0,4):
#     num += 1
#     line = []
#     for j in range(1,num):
#         line.append("*")
#     print(line)


# for i in range(0,4):
#     line = ""
#     for j in range(0,4):
#         line = line + "* "
#     print(line)

# num = 0
# num1 = 1
# for i in range(0,4):
#     line = []
#     num += 1
#     num1 += 1m
#     for j in range(0,3):
#         line.append(num1)
#     print(line)


# def greet(name):
#     print(f"Hello , {name}")

# get_name = str(input("rite your name: "))
# greet(get_name)
# greet(get_name)
# greet(get_name)
# greet(get_name)
# greet(get_name)
# greet(get_name)
# greet(get_name)


# def add(a, b): 
#     return a + b

# plus = add(3, 4)
# print(plus)
# for i in range(1,plus):
#     print(i)

# def multiply(x, y):
#     """
#     Multiplies two numbers and returns the result.
#     """
#     return x * y
# result = multiply(3,4)
# print(result)


# Define your first function:
# def say_hello():
#     print("Hello, Python world!")
# Call it a few times. Change the message. Add a parameter.

# def say_hello(name):
#     print(f"Hello, {name} world!")

# # say_hello("Alex")
# # say_hello("mihail")
# # say_hello("cristi")
# # say_hello("humb")
# # say_hello("bomb")
# # say_hello("Aassd")
# # say_hello("asdasd")

# my_list = ["mihail","crigan","vasea"]
# for i in my_list:
#     say_hello(i)


# Define a function square that receives a number 
# and returns its square. Display the result using print().


# def square(number):
#     return number

# result = square(5)
# print(result)

# for i in range(1,result):
#     print(i)



# Modify the square function 
# to include a docstring that explains what it does. 
# Then, use the help() function to view the documentation.

# def square(number):
#     """
#     this function return the number
#     """
#     return number

# result = square(5)
# print(help(result))


# Write a function calculate_area that 
# calculates the area of a rectangle. It should receive the width 
# and height as parameters and return the result.

# def calculate_are( width , height):
#     result = ()

#     result = width * height
#     return result

# result = calculate_are(5, 6)
# print(type(result))

# Create a function temperature_message(temp) that:
# Receives a number as input
# Prints a message depending on whether it’s cold (<10), moderate (10–25), or hot (>25)
# Use comments to explain each step

# number = int(input("Give a number: "))

# def temperature_message(temp):
#     if temp < 10:
#         print("its cold")
#     elif temp > 10 and temp < 25:
#         print("Moderate")
#     elif temp > 25:
#         print("Hot")
#     else:
#         print("Wow")

# result = temperature_message(number)


# def mystery(x):
#     print(x * 2 + 1)

# # print(mystery(3))
# # print(mystery(5))
# mystery(5)
# mystery(7)


# def greet(name):
#     # var = "Hello, " + name
#     # return var
#     return  "Hello, " + name

# result = greet("Alex")
# print(result)
# for i in result:
#     print(i)

# def add_numbers(a, b):
#     sum = a + b
#     print(sum)

# add_numbers(3,5)

# Write a function that returns the bigger of two numbers:
# larger(3, 8) → 8  
# larger(10, 4) → 10

# def the_bigger(num ,num2):
#     result = []
#     for i in num:
#         for j in num:
#             if i > j:
#                 result.append(i)
#                 print(result)
#     for i in num2:
#         for j in num2:
#             if i > j:
#                 result.append(i)
#                 print(result)
#     return result
                



# def say_hi():
#     my_tuple = (3,8)
#     my_tuple1 = (10,4)
#     result = the_bigger(my_tuple, my_tuple1)
#     print(result)
#     print("Hi!")

# say_hi()


# def outer():
#     print("Outer start")
#     inner()
#     print("Outer end")

# def inner():
#     print("Inner")

# outer()

# def step_one():
#     step_two()
#     print("First")

# def step_two():
#     print("Second")



# step_one()



# def parametrs_default(name = None):
#     print(f"hello: {name}")

# parametrs_default()
# parametrs_default("mihail")


# Define a function power(base, exponent=2) 
# that returns the result of raising base to the power of exponent.

# Call it:
# once with one argument
# once with both arguments


# def power(base, exponent=2):
#     return base + exponent

# result = power(2)
# result1 = power(2,3)
# print(result)
# print(result1)

# #Create a function order(drink="Water", size="Small") that prints an order message.


# def order(drink="Water", size="Small"):
#     return f"Drink: {drink} , Size: {size}"

# result = order("Vodka")
# print(result)


def setup(name="crigan",greeting="Hello"):
    print(f"{greeting}, {name}!")

result = setup(greeting="hello")


# def describe(item="apple", colour="red"):
#     print(f"This is a {colour} {item}.")

# describe(colour="green")


# def is_positive(n):
#     return n > 0

# result = is_positive(1)
# print(result)
# message = "Hello"

# def greet():
#     print(message)

# greet()  
# print(message)
# # Error: message is not defined


# message = "Hello"  # Global

# def greet():
#     message = "Hi"  # Local variable with the same name
#     print("Inside function:", message)

# greet()
# print("Outside function:", message)


# count = 0  # Global

# def increment():
#     # print(count)
#     count = 1  # Error: Python thinks this is a local variable, but it's unassigned
#     print(count)

# increment()


# count = 0

# def increment():
#     global count
#     count += 1

# increment()
# print(count)  # Output: 1





# 1 
# def simple_function():
#     print("asdasd")

# 2
# def other_function(param,params):
#     print(F"name {param} {params}")
# 3
# def another_function(a,g):
#     return a + b

# 4
# def step_one():
#     step_two()
#     print("asdasd")

# def step_two():
#     print("hi")

# 5 
# def param_default(param=1,params=2):
#     print()

