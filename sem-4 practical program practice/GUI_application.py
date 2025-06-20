#create a basic GUI application with two input fields and a submit button

from tkinter import *
def submit():
    name = name_entry.get()
    age = age_entry.get()
    print(f"Name: {name}, Age: {age}")
    
root = Tk()
root.title("Basic GUI Form")

# Labels and Entry Fields
Label(root, text="Name:").pack()
name_entry = Entry(root)
name_entry.pack()

Label(root, text="Age:").pack()
age_entry = Entry(root)
age_entry.pack()

# Submit Button
submit_btn = Button(root, text="Submit", command=submit)
submit_btn.pack(pady=10)
root.mainloop()