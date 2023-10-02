from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manger")
window.config(padx=100, pady=50, bg="yellow")


canvas = Canvas(width=200, height=200, bg="yellow")
canvas.pack()

logo = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=logo)



# keep the window open
window.mainloop()