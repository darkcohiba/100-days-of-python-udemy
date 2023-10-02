from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manger")
window.config(padx=20, pady=20, bg="yellow")


canvas = Canvas(width=200, height=200, bg="yellow")
canvas.grid(row=0, column=1)

logo = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=logo)

website_label = Label(text="Website", bg="yellow", fg="black")
email_label = Label(text="Email/Username", bg="yellow", fg="black")
password_label = Label(text="password", bg="yellow", fg="black")
website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

website_entry = Entry(width=35)
email_entry = Entry(width=35)
password_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1)
password_entry.grid(row=3, column=1)




# keep the window open
window.mainloop()