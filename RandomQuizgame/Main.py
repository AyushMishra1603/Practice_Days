from data import question_data
from Question_model import Question
from QuizBrain import QuizBrain
question_bank = []

for question in question_data:
    text = question["question"]
    answer = question["correct_answer"]
    new_quiz = Question(text, answer)
    question_bank.append(new_quiz)

quiz = QuizBrain(question_bank)

while quiz.still_questions_are_left():
    quiz.next_question()

print("You've completed all the quiz!")
print(f"Your final scoret is: {quiz.score}/{len(question_bank)}")
