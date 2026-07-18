# Write a Python program that helps you decide what
#  to eat for lunch:
#  Create a list with at least 6 food options.
my_list = ["pizza", "sushi", "salad", "tacos", "meat and cheese"]
#  Use random.choice() to pick one at random.
import random
lunch = random.choice(my_list)
#  Add a fun message like: "Today's lunch is...
print("Today's lunch is...", lunch)
print("Enjoy!")
#  sushi! Enjoy!"
#  Add a button and display the result in a
#  Tkinter window

import tkinter as tk
import random

def pick_lunch():
    lunch = random.choice(my_list)
    canvas.itemconfig(text_item, text="Today's lunch is... " + lunch + "! \nEnjoy!")

window = tk.Tk()
window.title("Lunch Picker")
window.geometry("500x420")

canvas = tk.Canvas(window, width=300, height=200)  
canvas.pack(pady=10)

well = canvas.create_rectangle(10, 10, 300, 300, fill="#7600f4", outline="", width=3)
text_item = canvas.create_text(150, 150, text="Press button to see the choice \nfor today's lunch", font=("Georgia", 12), fill="#ffffff")

button = tk.Button(window, text="Random choice", font=("Georgia", 12), bg="#7600f4", fg="#ffffff")
button.config(command=pick_lunch)
button.pack(pady=10)

window.mainloop()