class Question:
    def __init__(self, text,answer):
        self.text = text
        self.answer = answer

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
        self.question_number += 1

    def check_answer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{len(self.question_list)}\n")
