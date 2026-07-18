import random

# print(random.randint(1, 10)) # returns whatever numb between 1 and 10
# print(random.random())

# value = random.random()
# print(value)  # prints a random float between 0.0 and 1.0

# colors = ["red", "blue", "green", "yellow", "purple"]
# selected = random.choice(colors)
# print(selected)  # prints a random color from the list

# my_list = ["red", "blue", "green", "yellow", "purple"]
# random.shuffle(my_list)
# print(my_list)  # prints the list in a random order

# my_tuple = "green", "apple", "blue", "hanorac"
# group = random.sample(my_tuple, 2)
# print(group)  # prints 2 random elements from the tuple

# random.seed(103222)
# print(random.random())  # prints a random float based on the seed value

# import random

# random.seed(5) # fixeaza sa arate in continuare aceleasi numere aleatoare
# print(random.randint(1, 10))
# print(random.randint(1, 10))
# print(random.randint(1, 10))

# Task 1
# user = random.random()
# print(user)
# sau putem face asta

# from random import random
# print(random())

# Task 2
# n = random.randint(1, 6)
# print(n)

# sau ca o mica joaca

# num = int(input("Guess a number: "))

# if random.randint(1, 6) == num:
#     print("You guessed right!")
# else:
#     print("Try again!")

# Task 3
# students = ["Alice", "Ben", "Carla", "David"]
# random.shuffle(students)
# print(students)

# Task 4
# players = ["Alice", "Ben", "Carla", "David", "Eva", "Frank"]
# team = random.sample(players, 3)
# print(team)  # prints a random team of 3 players

# import tkinter as tk
# import random

# coin_colours = ["#f0c674", "#f28c8c",
#                 "#8cd0f2", "#8cf29e", 
#                 "#d58cf2", "#810bf0"]

# colour_index = 0

# def toss_coin():
#     global colour_index
#     result = random.choice(["Heads", "Tails"])
#     canvas.itemconfig(text_item, text=result)
#     canvas.itemconfig(coin, fill=coin_colours[colour_index])
#     colour_index = (colour_index + 1) % len(coin_colours)

                

# window = tk.Tk()
# window.title("Coin Toss Simulator")
# window.geometry("400x350")

# canvas = tk.Canvas(window, width=200, height=200)
# canvas.pack(pady=10)

# coin = canvas.create_oval(25, 25, 175, 175, fill="#f0c674", outline="black", width=3)
# text_item = canvas.create_text(100, 100, text="", font=("Arial", 24, "bold"))

# button = tk.Button(window, text="Toss Coin")
# button.config(command=toss_coin)
# button.pack(pady=10)

# window.mainloop()

# class Telefon:
#     def __init__(self, model, memorie):
#         self.model = model
#         self.memorie = memorie
#     def upgrate_memory(self, memorie):
#         return memorie + self.memorie
    
# telefon1 = Telefon("Samsung", 128)
# print(telefon1.upgrate_memory(64))

# import datetime
# now = datetime.datetime.today()
# next_year = now.year + 1
# year = datetime.datetime(next_year, 1, 1)
# print(year.strftime("%A"))  

# import datetime
# now = datetime.datetime.now()
# print(now.strftime("%H:%M:%S"))

# legume = {
#     "morcov" : 16,
#     "rosie" : 12,  
#     "castravete" : 8,
# }

# print(legume)
# legume["ardei"] = 10
# print(legume) 



