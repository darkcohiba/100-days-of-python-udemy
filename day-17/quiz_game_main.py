from data import question_data as data
from question_model import Question

question_bank = []

for question in data:
    new_q = Question(question["text"], question["answer"])
    question_bank.append(new_q)

print(question_bank[0].text)