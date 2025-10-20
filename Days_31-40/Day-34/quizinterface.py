THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:#the quiz_brain is an object now of QuizBrain class
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        # Score label
        self.score_label = Label(text=f"Score: {self.quiz.score}", 
                               font=("Arial", 20), 
                               bg=THEME_COLOR, 
                               fg="white")
        self.score_label.grid(row=0, column=1)
        self.questions_count_label = Label(text=f"Question {self.quiz.question_number}/{self.quiz.question_number}",
                               font=("Arial", 20),
                               bg=THEME_COLOR,
                               fg="white")
        self.questions_count_label.grid(row=0, column=0)
        
        # Canvas for question display
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text="",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        
        # Buttons
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, 
                                highlightthickness=0, 
                                command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, 
                                 highlightthickness=0, 
                                 command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()
        

    def true_pressed(self):
        is_correct = self.quiz.check_answer("True")
        self.update_score(is_correct)
        self.get_next_question()

    def false_pressed(self):
        is_correct = self.quiz.check_answer("False")
        self.update_score(is_correct)
        self.get_next_question()
        
    def update_score(self, is_correct):
        """Update the score if the answer is correct."""
        if is_correct:
            self.quiz.score += 1
            self.score_label.config(text=f"Score: {self.quiz.score}")

    def get_next_question(self):
        self.questions_count_label.config(text=f"Question {self.quiz.question_number}/{len(self.quiz.question_list)}")
        question_text = self.quiz.next_question()
        if question_text:  # If there are more questions
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:  # No more questions
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz!\nFinal Score: "
                                                            f"{self.quiz.score}/{len(self.quiz.question_list)}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")





