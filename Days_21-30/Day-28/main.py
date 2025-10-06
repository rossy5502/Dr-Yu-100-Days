from tkinter import *
from time import sleep

from numpy.ma.core import left_shift

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 25
CHECKMARK = "✔"
checkmark=""
timer = None
reps=0
#---------------------- UI SETUP ----------------------
window = Tk()
window.title("Pomodoro Timer")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100, bg=YELLOW)


# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    """Resets the timer to 00:00 and cancels any running timer."""
    global timer,reps,checkmark
    if timer is not None:
        window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    reps=0
    checkmark=""
    checkmark_label.config(text=checkmark)
    title_label.config(text="Timer", fg=GREEN)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps,checkmark
    work_sec=WORK_MIN * 6
    short_break_sec=SHORT_BREAK_MIN * 6
    long_break_sec=LONG_BREAK_MIN * 6
    reps+=1
    if reps%8==0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
        checkmark=""
        checkmark_label.config(text=checkmark)
    elif reps%2==0:
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
        if reps%2==1:
            checkmark+=CHECKMARK
            checkmark_label.config(text=checkmark)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """Counts down from given number and updates the UI."""
    global timer,reps,checkmark
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()




# ---------------------------- UI SETUP ------------------------------- #

title_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
title_label.pack()

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()

# Create a frame for the buttons
button_frame = Frame(window, bg=YELLOW)
button_frame.pack(pady=20)

# Pack buttons inside the frame
start_button = Button(button_frame, text="Start", font=(FONT_NAME, 16, "bold"), command=start_timer)
start_button.pack(side="left", padx=25)

checkmark_label = Label(text=checkmark, font=(FONT_NAME, 16, "bold"), fg=GREEN, bg=YELLOW)
checkmark_label.pack()

reset_button = Button(button_frame, text="Reset", font=(FONT_NAME, 16, "bold"), command=reset_timer)
reset_button.pack(side="right", padx=25)


window.mainloop()
