# Create a Python program that asks the user to enter their name and age: 1. If the user enters an empty name, 
# raise a ValueError with the message "Name cannot be empty." 
# 2. Try to convert the age to an integer. If this fails, display: "Age must be a number." 
# 3. If the age is below 0 or greater than 120, raise a ValueError with the message "Age must be between 0 and 120."
# 4. In all cases, display: "Input process completed." using a finally block. The program should not crash, 
# even if the user enters invalid data. All error messages must be clear and handled with try, except, and raise where needed
try:
    name = input("Enter your name:")  
    if not name:
        raise ValueError  
except ValueError as e:
    print("Name cannot be empty.", e) 
finally:
    print("Input process completed.")

try:
    age = input("Enter your age:")
    age = int(age)
except ValueError:
        print("Age must be a number.")
finally:
    print("Input process completed.")