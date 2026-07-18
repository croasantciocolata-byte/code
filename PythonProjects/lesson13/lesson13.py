# import math
# num = int(input("Enter a number: "))

# try:
#     if num >= 0:
#         print(math.sqrt(num))
#     else:
#         raise ValueError("Cannot compute square root of a negative number.")
# except ValueError as e:
#     print(e)

# # Task 1
# import math
# num = int(input("Enter a number: "))
# try:
#     if num >= 0:
#         print(math.sqrt(num))
#     else:
#         raise ValueError("Cannot compute square root of a negative number.")
# except ValueError as e:
#     print(e)

# import math
# print(math.pow(2,3)) # 2 la puterea 3
# print(math.sqrt(16)) # radical din 16 - float
# print(math.isqrt(25)) # radical din 25 - int
# print(math.ceil(4.2)) # rotunjeste in sus - 2
# print(math.floor(4.7)) # rotunjeste in jos - 4
# print(round(4.6)) # rotunjeste la cel mai apropiat intreg - 5
# print(math.fabs(-10)) # valoare absoluta - 10. 0
# print(math.fabs(10.0))  # valoare absoluta - 10. 0
# print(math.factorial(5)) # factorial - 120`)



# import math
# radius = 5
# area = math.pi * math.pow(radius, 2)
# print("Area of circle:", area)

# import math   
# x = 2
# exp_value = math.e ** x
# print("e raised to the power of", x, "is:", exp_value)

# Task 2
# Develop a Python script that:
# Imports the math module.
# Displays the values of math.pi and math.e.
# Calculates:
# The area of a circle with a user-provided radius using math.pi.
# The result of math.e raised to a user-provided power.
# Prints both results.

# import math
# print("Value of pi:", math.pi)
# print("Value of e:", math.e)
# radius = int(input("Enter the radius of the circle: "))
# area = math.pi * math.pow(radius, 2)
# power = int(input("Enter the power: "))
# e_power = math.e ** power
# print(area, e_power)

# import math
# print(math.floor(-4.9)) # -5
# print(math.ceil(-4.1))  # -4

# print(math.trunc(4.9)) # 4
# print(math.trunc(-4.1)) # -4

# print(math.exp(5))
# print(math.exp(1))
# print(math.exp(0))
# print(math.exp(-1))


import math
print(math.log(7))  # Natural logarithm (base e) of 7
print(math.log(2, 4)) #  Logarithm of 10 by base 4
print(math.log2(4))