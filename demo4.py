from tkinter import *
import tkinter.messagebox

window = Tk()

tkinter.messagebox.showerror("Info" , "Running out time")
question = tkinter.messagebox.askyesno("Weather" , "Will it rain?")

if question == False:
    print("Take an Umbrella")

else:
    print("Okay")


mainloop()