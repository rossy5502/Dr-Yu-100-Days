from tkinter import *

window=Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)


def calculate():
    value=round(float(user_input.get()) * 1.60934)
    km_value_label.config(text=f"{value}")


user_input=Entry(width=10,font=("Arial",20,"bold"))
user_input.grid(column=1, row=0,pady=30,padx=10)
miles_label=Label(text="Miles",font=("Arial",20,"bold"))
miles_label.grid(column=2, row=0,pady=30,padx=10)
is_equal_to_label=Label(text="is equal to",font=("Arial",20,"bold"))
is_equal_to_label.grid(column=0, row=1,pady=30,padx=10)
km_value_label=Label(text="0",font=("Arial",20,"bold")) # here where the result will be displayed
km_value_label.grid(column=1, row=1,pady=30,padx=10)
km_label=Label(text="Km",font=("Arial",20,"bold"))
km_label.grid(column=2, row=1)
calculate_button=Button(text="Calculate",font=("Arial",20,"bold"), command=calculate)
calculate_button.grid(column=1, row=2)





window.mainloop()
