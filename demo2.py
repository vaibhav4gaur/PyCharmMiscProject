from tkinter import  *
window = Tk()
window.title("Loggin Page")
window.geometry("300x300")
def log_entry():
    print("Logged in")

button = Button(window, text = "LOGIN", command = log_entry, width = 12, bg = "red",fg = "white", font = ("bold",12) )
button.pack()
mainloop()