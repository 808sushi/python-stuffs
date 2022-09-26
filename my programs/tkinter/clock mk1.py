from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("clock mk1")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text = string)
    label.after(1000, time)

label = Label(root, font=("fr", 100), background="black", foreground="white")
label.pack()
time()
mainloop()