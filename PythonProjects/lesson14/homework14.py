import datetime
# Write a Python program that asks the user to
#  enter their birthdate in the format YYYY-MM-DD.
try:
    dateBirth = input("Enter your birthdate (YYYY-MM-DD): ")
#  Your program should:
#  Convert the input into a datetime object using
#  strptime().
    obj = datetime.datetime.strptime(dateBirth, "%Y-%m-%d")
#  Calculate how many days old the user is using
#  timedelta.
    now = datetime.datetime.now()
    delta = now - obj
#  Print a message like: "You are 6,780 days
#  old!"
    print(f"You are {delta.days} days old!")
#  Show what day of the week they were born
#  (Monday, Friday...).
    print("You were born on a" + obj.strftime("%A"))
except ValueError:
    print("Invalid format. Write as in the example 2025-07-30")

