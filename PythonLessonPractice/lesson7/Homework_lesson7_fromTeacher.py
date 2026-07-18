# Create a loop that keeps asking "Type 'stop' to end:" and ends only when the user types stop.

# while True:
#     user = input("Type 'stop' to end:")
#     if user.lower().strip() == "stop":
#        break

# Write a for loop that prints the numbers 1 to 5, but skips 4.
# for i in range(1, 6):
#     if i == 4:
#         continue
#     print(i)

#Write a while loop that starts at 1 and stops when the number is greater than 10.
# Use break to stop the loop when the number is 7.


#Keep asking the user for a password until they enter "python123".
# If they enter "quit", use break to exit the loop early.

# while True:
#     password = input("Password:")
#     if password.strip().lower() == "quit": 
#         break
#     elif password == "python123":
#         print("Logged in succesfully")
#         break
#     else:
#         print()
# print()
# You have a list of inputs:
# Write a loop that prints only the numbers (the ones that can be turned into int). Use continue to skip invalid ones.
# .isdigit() checks if a string contains only numbers (e.g., "5" is valid, "ten" is not).

inputs = ["5", "ten", "12", "hello", "7"]
for i in inputs:
    if not i.isdigit():
        continue
    else:
        print(i)

print()
# Given this list:
# Use a for loop and break to stop searching when you find "cherry".

fruits = ["apple", "banana", "cherry", "kiwi", "melon"]
for i in fruits:
    if i == "cherry":
        break
    else:
        print(i)
    
print()
#Use nested loops to print this 3×4 pattern:
# * * * *
# * * * *
# * * * *

for i in range(3):
    row = "" 
    for j in range(4):
        row += "* "
    print(row)
    

print()
# Write a loop that prints the row and column numbers in a grid of size 2×3:
# Row 0 Col 0  
# Row 0 Col 1  
# Row 0 Col 2  
# Row 1 Col 0  
# Row 1 Col 1  
# Row 1 Col 2

for i in range(2):
    for j in range(3):
        print("Row", i, "Col", j)

print()
# Use a nested loop to print:
# 1  
# 1 2  
# 1 2 3  
# 1 2 3 4

for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print()

# Write a loop that adds all numbers in the array and prints the total:
array = [
    [1, 2, 3],
    [4, 5, 6]
]

total = 0
for i in array:
    for nmb in i:
        total += nmb
print(total)

print()

# Print only even numbers from a 2D array:
numbers = [
    [3, 6, 1],
    [8, 2, 7]
]
for i in numbers:
    for nmb in i:
        if nmb % 2 == 0:
            print(nmb)

print()
# Write code to print both diagonals:
# grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ] 
"""Nu stiu"""


