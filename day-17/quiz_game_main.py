from data import question_data as data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in data:
    new_q = Question(question["text"], question["answer"])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()