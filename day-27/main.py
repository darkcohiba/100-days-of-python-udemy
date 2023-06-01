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









# keep the window open
window.mainloop()