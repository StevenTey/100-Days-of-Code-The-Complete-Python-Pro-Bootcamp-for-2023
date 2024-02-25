from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")

window = Tk()
window.title("Mile to KM Calculator")
window.config(padx=20, pady=20)

miles_input = Entry()
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_euqal_label = Label(text="is equal to")
is_euqal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)   

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(column=1, row=2)

# Label
# my_label = Label(text="is equal to", font=("Arial", 16, "bold"))
# my_label.grid(column=0, row=1)
# my_label.config(padx=50, pady=50)

# def calculated():
#     print("Calculated")
#     miles = input.get()
#     km = miles * 1.60934
#     return km

# button = Button(text="Click Me", command=calculated)
# button.pack()

# Entry

# input = Entry(width=10)
# input.pack()
# input.get()

window.mainloop()