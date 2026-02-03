from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank =[]
for questions in question_data:
    new_question = Question(questions['text'], questions['answer'])
    question_bank.append(new_question)


quizz = QuizBrain(question_bank)

while quizz.still_has_questions():
    quizz.next_question()

print("You have completed the quizz")
print(f"Your final score is: {quizz.score}/{len(quizz.question_list)}")