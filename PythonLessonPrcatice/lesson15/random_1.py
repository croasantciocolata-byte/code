# # import random

# # print(random.randint(1,1000))
# # print(random.random())
# # print(random.randint(1000 ,10999))
# # mu_list = ["green", "apple", "melon", "watermelon"]
# # print(random.choice(mu_list))
# # mu_list = ["green", "apple", "melon", "watermelon"]

# # my_list = ["green", "apple", "melon", "watermelon"]
# # random.shuffle(my_list)
# # print(my_list)

# # my_tuple = "green", "apple", "melon","melon", "watermelon", "watermelon"
# # group = random.sample(my_tuple, 3)
# # print(group)
# import random




# # Write a program that generates and prints a random floating-point number between 0.0 and 1.0.
# # # import random
# # from random import random
# # print(random())

# # Simulate rolling a six-sided die by printing a random integer from 1 to 6.
# # import random
# # num = int(input("Guees a number: "))

# # if random.randint(1,6) == num :
# #     print(num)
# # else:
# #     print("Lol")

# random.seed(2)
# print(random.randint(1,99))
# print(random.random())


import tkinter as tk
import random

coin_colours = ["#139b33","#160989","#a8d8b3","#ded370","#dc305b","#d4d421",]

colour_index = 0
def toss_coin():
    global colour_index
    result = random.choice(["Heads", "Tails"])
    canvas.itemconfig(text_item,text=result)
    canvas.itemconfig(coin, fill=coin_colours[colour_index])
    colour_index = (colour_index + 1) % len(coin_colours)

window = tk.Tk()
window.title("Coin Toss simulator")
window.geometry("400x350")

canvas = tk.Canvas(window, width=200 , height=200)
canvas.pack(pady=10)

coin = canvas.create_oval(25,25,175,175, fill="green", outline="black" ,  width=3)
text_item  = canvas.create_text(100,100,text="", font=("Arial", 20 , "bold"))

button = tk.Button(window, text="Toss Coin")
button.config(command=toss_coin)
button.pack(pady=10)



window.mainloop()
