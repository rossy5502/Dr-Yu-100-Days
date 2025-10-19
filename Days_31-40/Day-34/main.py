from quizinterface import QuizInterface
from quiz_brain import QuizBrain
import requests
import html

def main():
    # Fetch questions from the API
    request = requests.get("https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=boolean")
    request.raise_for_status()
    data = request.json()
    question_data = data["results"]

    # Prepare question bank
    question_bank = []
    for question in question_data:
        question_text = html.unescape(question["question"])
        question_answer = html.unescape(question["correct_answer"])
        question_bank.append((question_text, question_answer))

    quiz = QuizBrain(question_bank)
    quiz_interface = QuizInterface(quiz)


if __name__ == "__main__":
    main()

    
