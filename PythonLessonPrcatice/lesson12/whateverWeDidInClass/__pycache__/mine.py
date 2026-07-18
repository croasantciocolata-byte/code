import tkinter as tk
import page1

def open_page1():
    root.destroy()
    page1.show_page()

root = tk.Tk()
root.title("Main menu")

root.geometry("600x550")
root.resizable(False, False)

frame = tk.Frame(root, padx=30, pady=30)
frame.pack()

label = tk.Label(frame, text="Main menu", font=("Helvetica", 16))
label.pack(pady=10)

btn1 = tk.Button(frame, text="Go to Page 1", width=20, command = open_page1)
btn1.pack(pady=5)

root.mainloop()
