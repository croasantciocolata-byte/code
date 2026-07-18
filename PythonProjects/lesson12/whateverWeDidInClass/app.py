import tkinter as tk # tkinter useful to make apps
import page1 # import the page1 module

def show_menu(): # function to show the main menu
    def open_page1():
        root.destroy()
        page1.show_page()

    root = tk.Tk() # create the main window
    root.title("Main menu") # set the title of the window

    root.geometry("600x550") # set the size of the window
    root.resizable(False, False) # make the window non-resizable

    frame = tk.Frame(root, padx=30, pady=30)
    frame.pack()

    label = tk.Label(frame, text="Main menu", font=("Helvetica", 16))
    label.pack(pady=10)

    btn1 = tk.Button(frame, text="Go to Page 1", width=20, command=open_page1)
    btn1.pack(pady=5)

    btn2 = tk.Button(frame, text="Go to Page 2", width=20, command=open_page1)
    btn2.pack(pady=5)

    root.mainloop() # run the main loop of the application

if __name__ == "__main__":
    show_menu() # show the main menu when the script is run directly