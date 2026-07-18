# Write a function is_odd(n) that returns True if n is odd, and False otherwise.
# Write at least 4 assert statements to test the function with:
# A positive odd number 
# A positive even number
# Zero
# A negative odd number
def is_odd(n):
    if n % 2 != 0:
        return True
    else:
        return False
    
assert is_odd(5) == True, "The number must be odd"
assert is_odd(4) == False, "The numeber must be odd"
assert is_odd(0) == False, "The numeber must be odd"
assert is_odd(-3) == True, "The numeber must be odd"
# Write a function max_of_three(a, b, c) that returns the largest of three numbers.
# Write assert tests covering:
# All numbers positive
# Some numbers negative
# Two or more numbers equal
# All numbers equal


# Write at least 3 assert statements testing the behaviour of Python’s built-in abs() function with:
# A positive integer
# A negative integer
# Zero


# The following function should return True if a string is a palindrome (reads the same forwards and backwards), False otherwise:
# def is_palindrome(s):
#     return s == s[::-1]
# Write at least 3 assert statements testing is_palindrome() with:
# A palindrome string (e.g., "madam")
# A non-palindrome string (e.g., "hello")
# An empty string ("")


# Create a function add(a, b) that returns the sum of two numbers.
# Write a test case using assertEqual to verify that add(2, 3) returns 5.
# Add one more test to check that add(-1, 1) returns 0.


# Define a list of fruits: ["apple", "banana", "cherry"].
# Write a test to check with assertIn that "banana" is in the list.
# Add another test that fails by checking if "grape" is in the list.


# Create two variables that point to the same list object, and another variable that contains an identical copy.
# Use assertIs to prove that the first two are the same object.
# Use assertIs again to show that the copied list is not the same object.


# Define a class Car with attributes brand and year.
# Create an object my_car = Car("Toyota", 2020).
# Write a test with assertIsInstance to check that my_car is a Car.
# Write another test with assertIsInstance to check that my_car.year is an int.

# Define a function is_even(n) that returns True if n is even.
# Write a test with assertTrue to confirm that is_even(4) is true.
# Add a failing test to check that is_even(5) is true.
