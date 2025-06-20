#GUI with different font styles and colors to display student data

from tkinter import *
from tkinter import font

root = Tk()
root.title("Student Information")
root.geometry("300x200")

# Custom Fonts
title_font = ("Helvetica", 16, "bold")
data_font = ("Arial", 12, "italic")

# Title Label
title_label = Label(root, text="Student Data", font=title_font, fg="blue")
title_label.pack(pady=10)

# Student Info Labels
Label(root, text="Name: parth", font=data_font, fg="green").pack()
Label(root, text="Age: 19", font=data_font, fg="purple").pack()
Label(root, text="Course: BCA", font=data_font, fg="darkred").pack()
root.mainloop()