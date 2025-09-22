from question_model import Question  # import Question class
from data import question_data
from
Question_bank = []

for question in question_data:
    new_question = Question(question["text"], question["answer"])
    Question_bank.append(new_question)




