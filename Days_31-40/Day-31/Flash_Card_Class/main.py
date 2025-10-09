import tkinter as tk

import pandas
from random import choice

from flashcard_ui import FlashCardUI


def load_words():
    df = pandas.read_csv("../data/french_words.csv")
    # Expect columns 'French' and 'English'
    records = df.to_dict(orient="records")
    return records




 
if __name__ == "__main__":
    words = load_words()
    window = tk.Tk()
    ui = FlashCardUI(window, words)
    window.mainloop()