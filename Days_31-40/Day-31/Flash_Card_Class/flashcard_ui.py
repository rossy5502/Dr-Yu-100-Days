import random
import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"


class FlashCardUI:
    def __init__(self, master, words):
        self.master = master
        self.words = words[:]  # copy
        self.to_learn = words[:]
        self.current_card = None
        self.flip_timer = None

        # Window config
        self.master.title("French Flash Cards")
        self.master.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

        # Canvas
        self.canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.card_front = tk.PhotoImage(file="../images/card_front.png")
        self.card_back = tk.PhotoImage(file="../images/card_back.png")
        self.card_image = self.canvas.create_image(400, 263, image=self.card_front)
        self.title_text = self.canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
        self.word_text = self.canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
        self.timer_text = self.canvas.create_text(400, 400, text="", font=("Arial", 40, "italic"))
        self.canvas.grid(row=0, column=0, columnspan=2)

        # Buttons
        self.cross_image = tk.PhotoImage(file="../images/wrong.png")
        self.check_image = tk.PhotoImage(file="../images/right.png")
        self.unknown_button = tk.Button(image=self.cross_image, highlightthickness=0, command=self.on_unknown)
        self.known_button = tk.Button(image=self.check_image, highlightthickness=0, command=self.on_known)
        self.unknown_button.grid(row=1, column=0)
        self.known_button.grid(row=1, column=1)

        # Start with a card
        self.next_card()

    def show_front(self, title, word):
        self.canvas.itemconfig(self.card_image, image=self.card_front)
        self.canvas.itemconfig(self.title_text, text=title)
        self.canvas.itemconfig(self.word_text, text=word)

    def show_back(self, title, word):
        self.canvas.itemconfig(self.card_image, image=self.card_back)
        self.canvas.itemconfig(self.title_text, text=title)
        self.canvas.itemconfig(self.word_text, text=word)

    def set_timer_text(self, text):
        self.canvas.itemconfig(self.timer_text, text=text)

    def schedule_flip(self, delay_ms=3000):
        if self.flip_timer is not None:
            self.master.after_cancel(self.flip_timer)
        self.countdown = 3
        self.update_countdown()

    def update_countdown(self):
        if self.countdown > 0:
            self.set_timer_text(str(self.countdown))
            self.countdown -= 1
            self.flip_timer = self.master.after(1000, self.update_countdown)
        else:
            self.set_timer_text("")
            self.flip()

    def flip(self):
        if not self.current_card:
            return
        self.show_back("English", self.current_card.get("English", ""))

    def next_card(self):
        if not self.to_learn:   #if to_learn is empty
            self.set_timer_text("All done!")    #no more words to learn
            return
        self.current_card = random.choice(self.to_learn) #randomly select a {french, english} dictionary
        self.show_front("French", self.current_card.get("French", ""))
        self.set_timer_text("")
        self.schedule_flip(3000)

    def on_known(self):
        if self.current_card in self.to_learn:
            self.to_learn.remove(self.current_card)
        self.next_card()

    def on_unknown(self):
        self.next_card()
