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
    first_label["text"] = input.get()
    # print what is in the
    print(text.get("1.0", tkinter.END))


button = tkinter.Button(text="Click Me!", command=button_click)
# add component to page
button.pack()

# entry component
input = tkinter.Entry(width=20)
# add component to page
input.pack()

# text box
text = tkinter.Text(height=10, width=50)
text.insert(tkinter.END, "Example.")
# text.focus()
text.pack()

#
def radio_used():
    print(radio_state.get())
    first_label["text"] = radio_state.get()

#Variable to hold on to which radio button value is checked.
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#
# numbers = [10, 12, 13, 15, 20]
#
# [10, 12, 13, 15]
#
# results = [number for number in numbers if number < 11]
# print(results)
# keep the window open
window.mainloop()

