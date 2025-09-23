# simple_quiz.py
question_data = [
    {"text": "Is Python a programming language?", "answer": "True"},
    {"text": "Is 2+2=5?", "answer": "False"},
    {"text": "Is the sky blue?", "answer": "True"}
]

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

class QuizBrain:
    def __init__(self, questions):
        self.questions = questions
        self.question_number = 0
        self.score = 0

    def next_question(self):
        current = self.questions[self.question_number]
        user_answer = input(f"Q{self.question_number + 1}: {current.text} (True/False): ")
        self.check_answer(user_answer, current.answer)
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer.strip().lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Wrong!")
        print(f"Score: {self.score}/{self.question_number + 1}\n")

question_bank = [Question(q["text"], q["answer"]) for q in question_data]
quiz = QuizBrain(question_bank)

while quiz.question_number < len(question_bank):
    quiz.next_question()

print(f"Final Score: {quiz.score}/{len(question_bank)}")
# A simple quiz application using classes to manage questions and quiz flow.