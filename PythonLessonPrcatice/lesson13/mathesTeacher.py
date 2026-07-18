# import math

# # print(math.sqrt(25))
# # math.sqrt(-25)

# print(math.sqrt(16))
# print(math.sqrt(2))
# print(math.sqrt(0))

# Write a Python script that performs the following steps:
# Import the math module from the standard library.
# import math
# # Prompt the user to enter a non-negative number.
# num = int(input("Enter non-negative number: "))
# # Calculate the square root of the input value using the math.sqrt() function.
# try:
#     if num >=0:
#         print(math.sqrt(num))
#     else:
#         raise ValueError("math domain error")
# except ValueError as e:
#     print(e)
# # Display the result in a clear and formatted message.
# # Validate the input:
# # If the number is negative, print an appropriate error message.
# # Otherwise, proceed with the calculation.


# import math 

# # print(math.isqrt(25))
# # # print(math.isqrt(-25))

# print(math.isqrt(49))
# print(math.isqrt(48))
# print(math.isqrt(50))
# print(math.isqrt(2))

# print("---------------")
# print(math.isqrt(49))
# print(math.isqrt(50))
# print(math.sqrt(49))
# print(math.sqrt(50))



# Write a Python script that:
# Imports the math module.
# Accepts user input as an integer.
# num = int(input("Enter a number: "))
# # Validates that the number is non-negative.
# try:
#     if num >=0:
#         print(math.isqrt(num))
#     else:
#         raise ValueError("math domain error")
# except ValueError as e:
#     print(e)
# # Uses math.isqrt() to compute the integer square root.
# # Displays the result with a clear explanatory message.



# print(math.pow(2,8))
# print(2 ** 8)

# print(math.floor(4.7))
# print(math.floor(4.9))
# print(math.floor(-4.9))
# print(math.floor(49))

# print(math.ceil(4.7))
# print(math.ceil(4.1))
# print(math.ceil(4.05))
# print(math.ceil(-4.05))


# print(round(4.5))
# print(round(6.5))
# print(round(4.6))

# print(round(5.5))
# print(round(7.5))
# print(math.pi)
# print(math.e)

# radius = 5
# print(math.pi * radius ** 2)

# x = 2
# print(math.e ** x)

# Develop a Python script that:
# Imports the math module.
# Displays the values of math.pi and math.e.
# Calculates:
# The area of a circle with a user-provided radius using math.pi.
# The result of math.e raised to a user-provided power.
# Prints both results.


# import math
# # num = int(input("Enter a number: "))

# # print(math.pi * num ** 2)
# # print(math.e ** num)

# print(math.fabs(-45))
# print(math.fabs(-9))
# print(math.fabs(-45.0))
# print(math.fabs(-9.0))
# print("-------------------")
# print(abs(-45))
# print(abs(-9))
# print(abs(-45.0))
# print(abs(-9.0))

# 1 * 2 = 2 * 3 = 6 * 4 = 24
# import math
# x = [1,2,3,4]
# j = []
# f = 1
# for i in x:
#     j = x[f] * i
#     f+=1
#     print(j)
#     if f == len(x):
#         break

# num =7 
# fact = 1
# if num <=0:


# print(math.factorial(5))
# print(math.factorial(7))
# print(math.factorial(10))
# # print(math.factorial(-5))

# print(math.trunc(5.9))
# print(math.trunc(4.5))
# print(math.trunc(-4.5))
# print(math.trunc(-5.9))

# print(math.floor(-5.9))
# print(math.ceil(-4.7))


# print(math.exp(5))
# print(math.exp(1))
# print(math.exp(0))
# print(math.exp(-1))
# print(math.e)


# Develop a Python script that:
# Imports the math module.
# Prompts the user to enter a real number x.
# Computes e^x using math.exp(x).
# Displays the result clearly.

# import math
# num = int(input("Enter a number: "))
# print(math.exp(num))


# import math 
# print(math.log(2))
# # print(math.log(10,1))
# print(math.log(100,10))
# print(math.log(74,8))

# Develop a Python script that:
# Asks the user to input a positive number.
# Calculates and displays:
# Natural logarithm using math.log(x)
# Base-10 logarithm using math.log10(x)
# Base-2 logarithm using math.log2(x)
# Logarithm of x in a user-specified base using math.log(x, base)
# Prints results.
# print(math.log(math.e))

# num =  int(input("Enter a number positive: "))
# print(math.log2(num))
# print(math.log10(num))
# print(math.log(num))
# print(math.log(10,num))


# num = 4
# fact = 1
# for i in range(1,num+1):
#     fact *= i
# print(fact)

# print(math.factorial(4))

# my_list = [1,2,3,4,5,6,7,8,9]

# check_stop =  my_list / 2

# temp = i[j]
# i[j] = j[i]
# j[i] = temp[i]

