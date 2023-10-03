from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manger")
window.config(padx=100, pady=100, bg="white")

# canvas with our image
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.grid(row=0, column=1)

logo = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=logo)

# labels
website_label = Label(text="Website", bg="white", fg="black")
email_label = Label(text="Email/Username", bg="white", fg="black")
password_label = Label(text="password", bg="white", fg="black")
website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

# input fields
website_entry = Entry(width=35, fg="black", bg="white", highlightthickness=0, highlightbackground="white")
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=35, fg="black", bg="white", highlightthickness=0, highlightbackground="white")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21, fg="black", bg="white", highlightthickness=0, highlightbackground="white")
password_entry.grid(row=3, column=1)

# buttons
generate_password_button = Button(text="Generate Password", highlightthickness=0, highlightbackground="white")
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, highlightthickness=0, highlightbackground="white")
add_button.grid(column=1, row=4, columnspan=2)

# keep the window open
window.mainloop()