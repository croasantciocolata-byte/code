import tkinter as tk
import app

def show_page():
    root = tk.Tk()
    root.title("Page 2")

    root.geometry("600x550")
    root.resizable(False, False)

    frame = tk.Frame(root, padx=30, pady=30)
    frame.pack()

    label = tk.Label(frame, text="This is Page 2", font=("Helvetica", 16))
    label.pack(pady=10)

    def go_back():
       root.destroy()
       app.show_menu()

    btn1 = tk.Button(frame, text="Go to Main menu", width=20, command=go_back)
    btn1.pack(pady=5)

    root.mainloop()