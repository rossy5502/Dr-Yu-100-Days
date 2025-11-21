import random,pandas,tkinter

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
flip_timer = None


#-------------------load the csv file using pandas as a list of dictionaries------------------------
def csv_to_dict():
    try:
        df = pandas.read_csv("../data/words_to_learn.csv")
    except FileNotFoundError:
        df = pandas.read_csv("../data/spanish_words.csv")
    records = df.to_dict(orient="records")
    return records


class FlashCardUI:

    def __init__(self,window_):
        self.countdown = None
        self.flip_timer = None
        self.window_=window_
        self.to_learn = csv_to_dict()
        #window config
        self.window_.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
        self.window_.title("Flash Card")
        self.canvas = tkinter.Canvas(width=800, height=526)
        self.card_front_img = tkinter.PhotoImage(file="../images/card_front.png")
        self.card_back_img = tkinter.PhotoImage(file="../images/card_back.png")
        self.canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.canvas_image = self.canvas.create_image(400, 263, image=self.card_front_img)
        self.canvas_title = self.canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
        self.canvas_word = self.canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
        self.canvas_timer = self.canvas.create_text(400, 400, text="", font=("Ariel", 35, "bold"))
        #Buttons
        self.red_img = tkinter.PhotoImage(file="../images/right.png")
        self.green_img = tkinter.PhotoImage(file="../images/wrong.png")
        self.green_button = tkinter.Button(image=self.green_img, highlightthickness=0, command=self.delete_card)
        self.green_button.grid(row=1, column=1)
        self.red_button = tkinter.Button(image=self.red_img, highlightthickness=0, command=self.next_card)
        self.red_button.grid(row=1, column=0)
        self.next_card()
#-------------------run this function to display the french word when you run the py file--------------

    def next_card(self):
        global current_card
        if self.flip_timer:
            self.window_.after_cancel(self.flip_timer)
        current_card = random.choice(self.to_learn)
        self.canvas.itemconfig(self.canvas_title, text="Spanish")
        self.canvas.itemconfig(self.canvas_word, text=current_card["Spanish"])
        self.canvas.itemconfig(self.canvas_image, image=self.card_front_img)
        self.countdown_values = iter(range(3, 0, -1))
        self.flip_timer_countdown()

    def delete_card(self):
        self.to_learn.remove(current_card)
        df = pandas.DataFrame(self.to_learn)
        df.to_csv("../data/words_to_learn.csv", index=False)
        self.next_card()

    def flip_timer_countdown(self):
        try:
            count = next(self.countdown_values)
            self.canvas.itemconfig(self.canvas_timer, text=str(count))
            self.flip_timer = self.window_.after(1000, self.flip_timer_countdown)
        except StopIteration:
            self.canvas.itemconfig(self.canvas_timer, text="")
            self.flip_card()

    def flip_card(self):
        global flip_timer
        flip_timer = None
        self.canvas.itemconfig(self.canvas_title, text="English")
        self.canvas.itemconfig(self.canvas_word, text=current_card["English"])
        self.canvas.itemconfig(self.canvas_image, image=self.card_back_img)

if __name__ == "__main__":
    window = tkinter.Tk()
    ui = FlashCardUI(window)
    window.mainloop()