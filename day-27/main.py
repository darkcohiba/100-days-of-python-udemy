import tkinter

window = tkinter.Tk()
# title
window.title("GUI!")
# sizing
window.minsize(width=500, height=300)

# label
first_label = tkinter.Label(text="My First Label", font=("Arial", 24, "italic"))
# centers the label on the screen
first_label.pack()


# change text two different ways
# first_label["text"] = "updated"
# first_label.config(text="updated again!")

# create button along with button function
def button_click():
    print("clicked!")
    first_label["text"] = "button was clicked!"
button = tkinter.Button(text="Click Me!", command=button_click)
button.pack()

# entry component





# keep the window open
window.mainloop()