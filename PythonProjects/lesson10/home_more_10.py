# Try to open a file named info.txt in read mode.
# If the file is found, read and print its contents.
# If the file is missing, display: "File not found."
# Always display: "File check complete."
# Use: try, except, finally.

# import os
# try:
#       with open("info.txt", "r") as f:
#          content = f.read()
#          print(content)
# except FileNotFoundError as e:
#    print("File not found")
#    print("Message: ", e)
# finally: print("File check complete")



# Ask the user to enter their age. Convert the input into an integer.
# If the value is valid, use if/else to print:"You are an adult." (18 or older), "You are a minor." (under 18)
# If the value is invalid, print: "Age must be a number."
# Always print: "Age check done." at the end.
# Use: try, except, finally, if/else.

# age = int(input("Enter your age: "))
# try:
#     if age >= 18:
#         print("You are an adult")
#     else:
#         print("You are a minor")
# except ValueError as e:
#     print("Message: ", e)
# finally: print("Age check done.")

# Create a program that asks the user to enter a number repeatedly.
# If the number is 0, print: "Stopping the loop." and stop the program using break.
# If the number is not 0, print: "You entered something else."
# If input is not a number, print: "Invalid input."
# Always print: "Attempt complete." after each input.
# Use: loop + try, except, finally.

# while True:
#     user = input("Enter a number: ")
#     try:
#         if int(user) == 0:
#             print("Stopping the loop.")
#             break
#         else:
#             print("You print something else.")
#     except ValueError:
#         print("Invalid input")
#     finally: print("Attempt complete")


# Ask the user for two filenames: one to read from, one to rename to. Use:
# FileNotFoundError if the original file doesn't exist
# PermissionError if renaming is not allowed
# Print a final message regardless of success.
# with open("file1.txt", "r") as f:
#     content = f.read()
#     print(content)

# import os
# import time
#     # time.sleep(100)
# try:
#     file1 = input("Enter name of first file (don't forget about .txt): ")
#     file2 = input("Enter name of second file (don't forget about .txt): ")
#     with open(file1, "r") as f:
#         print("File content:\n")
#         content = f.read()
#         print(content)
#     # with open(file2) as f:


# except FileExistsError:
#     # os.rename(file2, "renamed.txt")
# except FileNotFoundError:
#     with open(file1, "x") as f:
#         f.write("File 1 created succesfully")
#     print("File 1 has been created")
#     with open(file2, "x") as f:
#         f.write("File 2 created succesfully")
#     print("File 2 has been created")
#     print("File were not found. They are created now")
# except PermissionError:
#     print("Renaming is not allowed")
# finally:
#     print("Whatever you do with file - is cool")




# Create a dictionary of menu items:
# {"1": "Start", "2": "Settings", "3": "Exit"}
# Ask the user to choose an option. Try to print the corresponding value using the input as a key. If the key is invalid, print "Invalid menu option."
# smth = {"1":"Start", "2":"Settings", "3": "Exit"}
# option = input("Option: ")
# try:
#     print(smth[option])
# except KeyError:
#     print("Invalid menu option.")
