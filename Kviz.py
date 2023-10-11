class Question:

    def __init__(self,question_text, question_answer):
        self.text = question_text
        self.answer = question_answer


q_1 = Question("python vznikol v 1991", "True")
q_2 = Question("linux zalozi Linus", "True")
print(q_1.text)
print(q_1.answer)
print(q_2.text)
print(q_2.answer)

question_list = []

for one_question in question_data:
    question_t = one_question["text"]
    question_a = one_question["answer"]
    new_question = Question(question_t, question_a)
    question_list.append(new_question)

quiz = QuizBrain(question_list)
quiz.next_question()

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_li = q_list

    def next_question(self):
        current_question = self.question_li[self.question_number]
        self.question_number += 1
        input(f"otazka c. {self.question_number}: {current_question.text}(True/False): ")
