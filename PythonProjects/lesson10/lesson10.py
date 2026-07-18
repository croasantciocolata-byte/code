# nmb = 10
# try:
#     result = nmb / 0
#     print(result)
# except ZeroDivisionError as e:
#     print("Message: ", e)

# try:
#     user = "abc"
#     nmb = int(user)
# except ValueError as e:
#     print("Message: ", e)

# try:
#     text = "Total: "
#     value = 5
#     print(text + value)
# except TypeError as e:
#     print("Error: ", e)

# try:
#     number  = 25
#     number.append(5)
# except ValueError as e:
#     print("Message: ", e)

# Atsk 1
# You have a list that contains both numbers and text:
# Write a program that goes through each item in the list and tries to multiply it by 2.
# If an error occurs, print:
# "Cannot multiply this item."
# data = [10, "five", 3]
# try:
#     for i in data:
#         i += 2
#         print(i)
# except TypeError as e:
#     print("Message: ", e)

# You are given a set:
# Try to remove "yellow" from the set using the remove() method.
# If the item is not in the set, print:
# "Item not found in the set."

# try:
#     colours = {"red", "green", "blue"}
#     colours.remove("yellow")
# except KeyError as e:
#     print("Message: ", e)
#     print("Item not found in the set")


# try: 
#     print("cool")
# except:
#     print("kids")
# finally:
#     print("that's kinda true")

# Define a function calculate_total(price, quantity) that multiplies the two values. Now call it like this:
# calculate_total("free", 3)
# Handle the error and print:
# "Cannot calculate total: one of the values is invalid."

# try:
#     with open("data.txt", "r") as f:
#         content = f.read()
#         print(content)
# except FileNotFoundError as e:
#     print("Message: ", e)
# finally: 
#     print("File")

# user_input = input("Enter a number: ")

# try:
#     number = int(user_input)
#     if number >= 0:
#         print("You entered a positive number.")
#     else:
#         print("You entered a negative number.")
# except ValueError:
#     print("Thatwas not a valid number")
# finally:
#     print("Thank you for using this program")

# while True:
#     try:
#         number = int(input("Enter 10 to stop: "))
#         if number == 10:
#             print("Program ending")
#             break
#     except ValueError as e:
#         print("Message: ", e)
#     finally:
#         print("Attempt completed")

# Ask the user to input two values. Try to:
# Convert both to int.
# Divide the first by the second.
# Handle both:
# ValueError if conversion fails.
# ZeroDivisionError if second value is 0.
# Also include a finally block that says: "Calculation complete."

# while True:
#     try:
#         nmb1 = input(int("Enter first nmb."))
#         nmb2 = input(int("Enter second nmb"))
#         divide = nmb1 / nmb2
#         print(divide)
#     except ValueError as e:
#         print("Message: ", e)
#     except ZeroDivisionError as o:
#         print("Message: ", o)
#     finally: 
#         print("Calculation complete")
        