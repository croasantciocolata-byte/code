# Write two functions:
# print_intro() prints: "This is the beginning of the story."
# start_story() calls print_intro() and then prints: "Once upon a time..."
# Call start_story().
def print_intro():
    print("This is the beggining of the story.")

def start_story():
    print_intro()
    print("Once upon a time...")

start_story()

print("************")
# Create the following three functions:
# step_one() prints "Step 1: Open the box"
# step_two() prints "Step 2: Take out the object"
# begin_process() calls both step_one() and step_two()
# Call begin_process() and observe the full process.
def step_one():
    print("Step 1: Open the box")

def step_two():
    print("Step 2: Take out the object")

def beggin_process():
    step_one()
    step_two()

beggin_process()
print("*****************")
# Create a function called thank_you() that prints "Thank you!".
# Now create two other functions:
# end_lesson() prints "The lesson is finished.", then calls thank_you()
# end_game() prints "The game has ended.", then calls thank_you()
# Call both end_lesson() and end_game().
def thank_you():
    print("Thank you!")
def end_lesson():
    print("The lesson is finished.")
    thank_you()
def end_game():
    print("The game has ended.")
    thank_you()

end_lesson()
end_game()
print("*********************")
# Write a function final_message() that prints "You’ve completed all levels!"
def final_message():
    print("You’ve completed all levels!")
# Then:
# level_two() calls final_message()
# level_one() calls level_two()
def level_two():
    final_message()

def level_one():
    level_two()
# Call level_one().
level_one()
print("*********************")

# Define a function is_positive(n) that returns True if the number
# is greater than 0, and False otherwise. Test it with several inputs.
def is_positive(nmb):
    if nmb > 0:
        return True, ("The number is positive")
    else:
        return False, ("The number is negative")

print(is_positive(-7))
print("***********")
# Write a function is_even(n) that returns True if the number is even, and False otherwise.
def is_even(nmb):
    if nmb % 2 == 0:
        return True, ("The number is even")
    else:
        return False, ("The number is odd")

print(is_even(5))
print("***********")
#  Define a function can_vote(age) that returns True if age is 18 or older.
def can_vote(age):
    if age > 18:
        return True
    else:
        return False
print(can_vote(17))
print("************")
# Define a function is_short(text) that returns True if the text has fewer than 5 characters.
def is_short(text):
    if len(text) < 5:
        return True, ("The word is shorter than 5 characters")
    else:
        return False, ("The word is greater than 5 characters")
print(is_short("her"))
print("**********")
# Challenge
# Write four separate functions: add(a, b), subtract(a, b), multiply(a, b), and divide(a, b).
# Then, ask the user to:
# input two numbers
# select an operation (+, -, *, /)
# call the correct function
# Bonus: Handle division by zero.

# def add(a, b):
#     print(a + b)

# def substract(a, b):
#     print(a - b)

# def multiply(a, b):
#     print(a * b)

# def divide(a, b):
#     if b == 0:
#         print("It can't be divided by 0, choose another number")
#     else:
#         print(a / b)

# nmb1 = input("Print number 1: ")
# nmb2 = input("Print number 2:")
# multiply(int(nmb1), int(nmb2))
# divide(int(nmb1), int(nmb2))
# print("******************")




# Write a program with three functions:
# def area_of_rectangle(width, height):
#     area = width * height
#     return area

# a = input("Enter width:")
# b = input("Enter height:")
# print(area_of_rectangle(int(a), int(b)))
# print("***************")

# def area_of_triangle(base, height):
#     area = (1/2) * base * height
#     return area

# a = input("Enter base:")
# b = input("Enter height:")
# print(area_of_triangle(int(a), int(b))) 
# print("*****************")


# def area_of_circle(radius):
#     area = 2 * 3.14 * radius
#     return area

# radius = input("Enter radius:")
# print(area_of_circle(float(radius)))
# Let the user choose the shape, input the values, and print the correct area using the corresponding function. Use π = 3.14 for simplicity.


# Create a function analyse_text(text) that:
# returns the number of characters
# the number of words
# and the number of vowels
# Bonus: Add a print_report() function that displays the result in a nice format.
def analyse_text(text):
    return len(text)

user = input("Enter a short text: ")
print("Number of characters: ", analyse_text(user)) 
"""am stat mult timp sa analizez cum sa fac aici la nr de cuvinte...si m-am enervat si nu am facut nici nmr de vocale
imi este greu sa inteleg cum sa aplic logica. codul in minte il am, dar nu pot sa il aplic - imi dau o multime de erori"""


# Write a program with three functions:
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         False
# def is_prime(n):
#     #HEEEEEEEELLPPPPPPPPPPPPP MEEEEEEEEEEEEEEEEEEEE
#         return True
#     else:
#         False
# def is_perfect_square(n):
#     i = 1
#     while i * i <= n:  # găsim dacă există un număr a cărui pătratul = n
#         if i * i == n:
#             return True
#         i += 1
#     return False
# # Ask the user to input a number, then print which of these properties it has.
# user = input("Enter a number: ")
# if is_even == True:
#     print("The number is even")
# elif is_prime == True:
#     print("The number is prime")
# elif is_perfect_square == True:
#     print("The number is perfect square")
# else: print("The number is neither even, prime, nor perfect square")