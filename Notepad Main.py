import tkinter as tk
from tkinter import filedialog
import time

def about():
    about_window = tk.Toplevel(root)
    about_window.title("About")
    about_window.geometry("400x25")
    about_label = tk.Label(about_window, text="This is a simple text editor, that I am making to learn more python. Enjoy! :)")
    about_label.pack()


def open_file(text_widget):
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text_widget.delete('1.0', 'end')
            text_widget.insert('1.0', file.read())

def save_file(text_widget):
    file_path = filedialog.asksaveasfilename()
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_widget.get('1.0', 'end'))

def time_date(text_widget):
    text_widget.insert('insert', time.strftime("%a %I:%M %p"))

root = tk.Tk()
root.geometry('800x600')  # Set the size of the window
root.title("Shitty Notepad")  # Set the title of the window

# Create a Text widget that fills the whole window
text_widget = tk.Text(root, font=("MonaSans-Medium.ttf", 16))  # Set default font to Helvetica size 16
text_widget.pack(fill='both', expand=True)

# Create a Menu bar
menu_bar = tk.Menu(root)

# Create a File menu and add it to the menu bar
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=lambda: open_file(text_widget))
file_menu.add_command(label="Save", command=lambda: save_file(text_widget))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Create an Edit menu and add it to the menu bar
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=lambda: text_widget.event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", command=lambda: text_widget.event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", command=lambda: text_widget.event_generate("<<Paste>>"))
edit_menu.add_separator()
edit_menu.add_command(label="Time/Date", command=lambda: time(text_widget))
edit_menu.add_command(label="Undo", command=lambda: text_widget.event_generate("<<Undo>>"))
edit_menu.add_command(label="Redo", command=lambda: text_widget.event_generate("<<Redo>>"))
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Create a Help menu and add it to the menu bar
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Configure the root window to use our new menu bar
root.config(menu=menu_bar)

root.mainloop()