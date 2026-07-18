# Develop a Python script that:
# Imports the math module.
import math
# Requests two numbers from the user:
# Base value (x)
# Exponent value (y)
base = float(input("Enter value x: "))
exponent = float(input("Enter value y: "))
# Calculates the result of xʸ using math.pow(x, y).
mathResult = math.pow(base, exponent)
# Prints the result in a readable format.
print("Result is:", mathResult)
# Optionally, compares it to the result of x ** y.
print("Camparation: ", base ** exponent)

# Develop a Python script that:
# Imports the math module.
# Accepts a float input from the user.
userInput = float(input("Enter a number: "))
# Applies math.trunc() to the input
result = math.trunc(userInput)
# Prints the result.
print("Nmb truncated", result)
# Compares it to the result of math.floor() and math.ceil().
print("Nmb floor", math.floor(userInput))
print("Nmb ceil", math.ceil(userInput))
