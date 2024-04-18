from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    question_txt = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_txt, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print("You've Completed the Quiz")
print(f"Your final Score is {quiz.score}/{len(quiz.question_list)}")
