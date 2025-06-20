#handling implemented in Python GUI

from tkinter import *
def on_click():
    print("Button clicked!")
    
root = Tk()
btn = Button(root, text="Click Me", command=on_click)
btn.pack()
root.mainloop()