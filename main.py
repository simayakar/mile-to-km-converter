from tkinter import *


def calculate_km():
    user_input = entry_box.get()
    calculated_km = round(float(user_input) * 1.6)
    l3.config(text=calculated_km)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=50)
window.config(padx=20, pady=20)

#Entry

entry_box = Entry(width=5)
entry_box.insert(END, string="0")
entry_box.grid(row=0, column=1)

#Label Miles
l1 = Label(text="Miles")
l1.config(padx=5)
l1.grid(row=0, column=2)


#Label is equal to
l2 = Label(text="is equal to")
l2.config(padx=5)
l2.grid(row=1, column=0)

#Label number
l3 = Label(text="0")
l3.config(padx=5)
l3.grid(row=1, column=1)

#Label Km
l4 = Label(text="Km")
l4.config(padx=5)
l4.grid(row=1, column=2)

#Button
button = Button(text="Calculate", command=calculate_km)
button.grid(row=2, column=1)


window.mainloop()