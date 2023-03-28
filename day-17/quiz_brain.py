class QuizBrain:

    def __init__(self):
        self.question_number = 0
        self.question_list = input("What are the questions: ")


sam = QuizBrain()

print(sam.question_list)