"""# Ask for a number.
# Convert it to int, and print whether it’s even or odd.
nmb = input("Enter a number: ")

if (int(nmb) % 2 == 0):
    print("Number is even")
else:
     print("Number is odd")

# Ask for two numbers.
# Convert both to float and print their sum.
nmb1 = input("Input first number: ")
nmb2 = input("Input second number: ")
print("Sum is: ", float(nmb1) + float(nmb2))


# Ask for age.
# If  it’s under 12, print "Child", otherwise "Older child".
age = input("Enter your age: ")
if int(age) < 12:
    print("child")
else:
    print("oldre child")

# Ask for temperature.
# Convert to float, and print if it’s above or below freezing.
temp = input("Enter the temperature: ")
if float(temp) < 0:
    print("Below freezing")
else:
    print("Above freezing")

# Ask the user for their birth year.
# Convert it and calculate their age using subtraction.
birth_year = input("Enter your birth year: ")
current_year = 2025
print("Your age is: ", current_year - int(birth_year))

# Ask for the number of items.
# If the number is 0, print "Nothing to do". If more, print "Let's go!"
nmb_items = input("Enter number of items: ")
if int(nmb_items) == 0:
    print("Nothing to do")
else:
    print("Let's go!")"""

# Ask the user for their favourite fruit.
# Use .strip().lower()
# Use match to print a comment about "apple", "banana", "grape"
# Use case _ for other fruits
favourite_fruit = input("Type your favourite fruit: ")

match favourite_fruit.strip().lower():
    case "apple":
        print("Wow, I like apples too!")
    case "banana":
        print("Bananas are great!")
    case "grape":
        print("Grapes are delicious!")
    case _:
        print("That's an interesting choice!")


# Ask the user for the day of the week.
# Use match to print:
# "Monday" → "Start of the week"
# "Friday" → "Weekend is near!"
# "Saturday"/"Sunday" → "Weekend!"
# _ → "Regular day"
day = input("Enter the day of the week: ")
match day.strip():
    case "Monday":
        print("Start of the week")
    case "Friday":
        print("Weekend is near!")
    case "Saturday" | "Sunday":
        print("Weekend!")
    case _:
        print("Regular day")




# Objective
# Create a simple game where the program has a secret number,
# and the user has to guess it. The program gives feedback until the user finds it.
# STEPS
# Read the user’s guess using input()
# Convert the input into an int
# Use if-else or match to check the guess
# Give feedback:
# If guess is too low → say “Too low!”
# If guess is too high → say “Too high!”
# If correct → say “You got it!”
# Use .strip() in case the input has spaces
# Use a fixed number that the user has to guess

# SOLUTION 1
# secret = 7
# guess = int(input("Guess the number (1 to 10): ").strip())

# if guess == secret:
#     print("You got it!")
# elif guess < secret:
#     print("Too low!")
# else:
#     print("Too high!")
# SOLUTION 2
# secret = 7
# guess = int(input("Guess the number (1 to 10): ").strip())

# match guess:
#     case 7:
#         print("You got it!")
#     case _:
#         print("Try again!")



# # #Тут пример не решение , Aiceai exemplu nu rezolvare
# #NEW Concept
# # import random

# # secret = random.randint(1, 10)
# # guess = int(input("Guess the number (1 to 10): ").strip())

# # match guess:
# #     case 7:
# #         print("You got it!")
# #     case _:
# #         print("Try again!")


# OBJECTIVE
# Create a game where the user guesses "heads" or "tails", 
# and the program randomly “tosses” the coin and checks if the user was right.
# STEPS
# Ask the user to guess: "heads" or "tails"
# Clean the input: use .strip().lower()
# Toss the coin using random.choice(["heads", "tails"])
# Compare user guess with result
# Print a win/lose message
# Optional: Use match to give custom feedback
# Optional: Handle invalid answers
# SOLUTION 1
# import random

# user_guess = input("Heads or tails? ").strip().lower()
# toss = random.choice(["heads", "tails"])

# if user_guess == toss:
#     print("You guessed right!")
# else:
#     print(f"Nope! It was {toss}.")
# SOLUTION 2
# import random

# user_guess = input("Heads or tails? ").strip().lower()
# toss = random.choice(["heads", "tails"])

# match toss:
#     case "heads":
#         print("Heads it is!")
#     case "tails":
#         print("Tails landed!")




# OBJECTIVE
# Create a game where the user picks rock, paper, 
# or scissors, the computer does the same, and the winner is announced based on classic rules.
# STEPS
# Ask for player’s choice
# Clean it with .strip().lower()
# Generate computer’s move using random.choice()
# Compare the moves and print:
# Tie
# Win
# Lose
# Optional: Use match for fun effects ("Rock crushes scissors!")
# Optional: Handle invalid inputs with an error message
# SOLUTION 1
# import random

# player = input("Rock, paper, or scissors? ").strip().lower()
# computer = random.choice(["rock", "paper", "scissors"])

# print("Computer chose:", computer)

# if player == computer:
#     print("It's a tie!")
# elif (player == "rock" and computer == "scissors") or \
#      (player == "scissors" and computer == "paper") or \
#      (player == "paper" and computer == "rock"):
#     print("You win!")
# else:
#     print("You lose!")
# SOLUTION 2
# import random

# player = input("Rock, paper, or scissors? ").strip().lower()
# computer = random.choice(["rock", "paper", "scissors"])

# print("Computer chose:", computer)

# match (player, computer):
#     case ("rock", "scissors"):
#         print("Rock crushes scissors! You win!")
#     case ("scissors", "paper"):
#         print("Scissors cuts paper! You win!")
#     case ("paper", "rock"):
#         print("Paper covers rock! You win!")
#     case (a, b) if a == b:
#         print("It's a tie!")
#     case _:
#         print("You lose!")
