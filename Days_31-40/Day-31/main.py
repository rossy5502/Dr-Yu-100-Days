import pandas
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"

# IMPORT DATAFRAME FROM CSV FILE
data=pandas.read_csv("data/french_words.csv")
to_learn=data.to_dict(orient='records')
current_card={}


def next_card():
    global current_card
    current_card=random.choice(to_learn) # this will pick a random dictionary    from the list
    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(canvas_word, text=current_card["French"], fill="black")
    canvas.itemconfig(bg=BACKGROUND_COLOR,image=card_front_img)


def flip_card():
    canvas.itemconfig(canvas_title, text="English", fill="black")
    canvas.itemconfig(canvas_word, text=current_card["English"], fill="black")
    canvas.itemconfig(bg=BACKGROUND_COLOR, image=card_back_img)


#create a window
window=Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
#setting a window for 3 seconds wait before flipping the card
window.after(3000, func=flip_card)
# NOW THE CANVAS
canvas=Canvas(width=800, height=526)
card_front_img=PhotoImage(file="images/card_front.png")
card_front=canvas.create_image(400, 263, image=card_front_img)
card_back_img=PhotoImage(file="images/card_back.png")
card_back=canvas.create_image(400, 263, image=card_back_img)

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
# NOW THE CANVAS TEXT
canvas_title=canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
canvas_word=canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
# NOW THE BUTTONS
right_img=PhotoImage(file="images/right.png")
right_button=Button(image=right_img, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)
wrong_img=PhotoImage(file="images/wrong.png")
wrong_button=Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)
next_card()


window.mainloop()

