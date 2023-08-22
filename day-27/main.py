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


button = tkinter.Button(text="Click Me!", command=button_click)
# add component to page
button.pack()

# entry component
input = tkinter.Entry(width=20)
# add component to page
input.pack()

# text box
text = tkinter.Text()
#
# numbers = [10, 12, 13, 15, 20]
#
# [10, 12, 13, 15]
#
# results = [number for number in numbers if number < 11]
# print(results)
# keep the window open
window.mainloop()

