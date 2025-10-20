
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        """Get the next question text or a completion message if no more questions."""
        if self.still_has_questions():
            self.current_question = self.question_list[self.question_number]  # list of tuples
            self.question_number += 1  # Move to the next question for next time
            return self.current_question[0]  # Return question text
        
        return ""  # Return empty string when quiz is done

    def check_answer(self,is_correct: str) -> bool:
        if is_correct == self.current_question[1]:
            return True
        return False

