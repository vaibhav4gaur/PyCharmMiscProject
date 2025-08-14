# import libraries
from tkinter import *

# gui interaction
window = Tk()

#adding inputs
window.title("Simple")
window.geometry("250x50")


label1 = Label(window, text = "mail")
label2 = Label(window, text = "password")

label1.grid(row = 0 , column = 1)
label2.grid(row = 1 , column = 1)

mainloop()

