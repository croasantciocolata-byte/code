import tkinter as tk

def show_page():
    root = tk.Tk()
    root.title("page1")
    root.geometry("600x550")
    root.resizable(False, False)

    frame - tk.Frame(root, padx=30, pady=30)
    frame.pack()

    label = tk.Label(frame, text="Page 1", font=("Helvetica", 16))
    label.pack(pady=10)

    def go_back()
        root.destroy()
        mine
    btn1 = tk.Button(frame, text="Go to Page 1", width=20, command = open_page1)
    btn1.pack(pady=5)