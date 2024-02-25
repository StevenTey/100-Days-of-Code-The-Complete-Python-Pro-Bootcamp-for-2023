from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in range(len(question_data)):
    q_name = "Question_" + str(i)
    q_text = question_data[i]["text"]
    q_answer = question_data[i]["answer"]
    q_name = Question(q_text, q_answer)
    question_bank.append(q_name)
    # print(q_name.text)

quiz = QuizBrain(question_bank)

while quiz.still_have_questions
    quiz.next_question()

print("You've completed the quiz")