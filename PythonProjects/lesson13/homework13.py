import math
#  Write a Python program that asks the user to
#  enter a positive number. The program should:
user = float(input("Enter a positive number: "))
try:
#  Calculate and display the square root using
#  math.sqrt()
   
    if user < 0:
        raise ValueError("This nmb must be positive to solve the square root.")
    print("Square root:", math.sqrt(user))
except ValueError as e:
    print(e)
#  Calculate and display the factorial using
#  math.factorial() (only if the number is an
#  integer)
try:

    if user < 0 or not user.is_integer():
        raise ValueError("This number must be integer and positive.")
    print("Factorial:", math.factorial(int(user)))
except ValueError as e:
    print(e)
#  Calculate and display the natural logarithm
#  using math.log()
try:
    
    if user <= 0:
        raise ValueError("Logarithms work only when numers are positive.")
    print("Natural logarithm:", math.log(user))
except ValueError as e:
    print(e)
#  Round the number using math.floor(),
#  math.ceil(), and math.trunc()

print("Rounded down:", math.floor(user))
print("Rounded up:", math.ceil(user))  
print("Truncated:", math.trunc(user))
#  Display the value of math.e raised to the
#  input number using math.exp()
print("e raised to the number:", math.exp(user))
#  Make sure your program checks for valid input and
#  handles errors (e.g., negative numbers or non
# integer input for factorial)