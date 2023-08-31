# miles to kilometers converter
from tkinter import *
window = Tk()
# title
window.title("Miles to KM Converter!")
# sizing
# window.minsize(width=200, height=200)
window.config(padx=20, pady=20)


def calculate_km():
    km_value_label["text"] = round(int(miles_input.get()) * 1.609, 2)
    print("clicked")

miles_input = Entry(width=5)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_value_label= Label(text="0")
km_value_label.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate_km)
calculate_button.grid(column=1, row=2)


# keep the window open
window.mainloop()