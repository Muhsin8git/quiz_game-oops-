class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.score = 0
        self.question_list = questions

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer =input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        correct_answer = current_question.answer
        self.check_answer(user_answer,correct_answer)
    def check_answer(self,user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Hurray its correct")
        else:
            print("You got it wrong")
        print(f"You have have score of {self.score}/{self.question_number}")
