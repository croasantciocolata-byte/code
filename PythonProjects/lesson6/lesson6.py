'''# Task 1
number = 7
if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

print("-------")

# Task 2
x = -10
if x > 0:
    print("Positive")
else:
    print("Non-positive")

print("-------")
# Task 3
temperature = 10
if temperature > 20:
    print("Warm")
elif temperature > 0:
    print("Chilly")
else:
    print("Freezing")

print("-------")

# Task 4
weather = "rainy"
if weather == "sunny":
    print("Wear sunglasses")
elif weather == "rainy":
    print("Take an umbrella")
else:
    print("Stay inside")    
print("-------")

number = 0
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
print("-------")

# Task 5
pet = "cat"
if pet == "dog":
    print("Woof")
elif pet == "cat":
    print("Meow")
else:
    print("Unknown pet sound")
print("-------")

# Task 6
fruit = "pear"
if fruit == "apple":
    print("Red")
elif fruit == "banana":
    print("Yellow")
else:
    print("Unknown fruit color")
print("-------")

# Task 7
weather = "snowy"
if weather == "rainy":
    print("Take umbrella")
elif weather == "sunny":
    print("Wear sunglasses")
else:
    print("Check the forecast")
print("-------")

# Task 8
is_number = True
if is_number:
    print("It's a number")
else:
    print("It's not a number")
print("-------")

# Task 9
name = "Nico"
if name == "Nico":
    print("Hello buddy")
else:
    print("We are waiting for Nico")
print("-------")
 
 # Task madfe by teacher
fruit = "apple"
fresh = ("apple")
if fruit is fresh:
    print("Right")
elif fruit in fresh:
    print("Wrong")
else:
    print("Incorrect")
print("-------")

# Task 10
my_list = ["friends", "trips", "skyDiving"]
myOther = ["work", "money", "value"]
if my_list[0] <= myOther[0]:
    print("Priority")
else:
    print("Not priority")
print("-------")

# Task 11
print("How do you feel today, sir/madam?")
mood = "chill"
if mood == "sleepy":
    print("It's aftrenoon")
elif mood == "chill":
    print("It's evening")
else:
    print("It's morning")

print("-------")

# Task 12
time_of_day = "morning"
if time_of_day == "morning":
    print("You wake up to the sound of birds chirping.")
elif time_of_day == "afternoon":
    print("You decide to go for a walk in the park.")
else:
    print("You prepare for a cozy evening at home.")
print("-------")

# Task 13
x = 10
y = 20
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
print("-------")

# Task 14
username = "Nico"
password = "12345"

if username == username:
    if password == password:
        print("Access granted")
    else:
        print("Incorrect password try again")
else:
    print("Unknown user, try again")
    
import random

secret = random.randint(1, 10)
guess = int(input("Guess the secret number between 1 and 10: "))

match guess:
    case 7:
        print("Correct! You've guessed the secret number.")
    case _:
        print("Invalid input. Please enter a number between 1 and 10.")

'''
