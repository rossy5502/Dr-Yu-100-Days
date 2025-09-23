from data import question_data
from quiz_brain import QuizBrain, Question  # import QuizBrain class
Question_bank = []

for question in question_data:
    new_question = Question(question["text"], question["answer"])
    Question_bank.append(new_question)



quiz = QuizBrain(Question_bank)

while quiz.question_number < len(Question_bank):
    quiz.next_question()




