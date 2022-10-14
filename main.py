from question_model import Question
from question_data import question_data
from quiz_execution import QuizExecution

question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    question_explanation = question['explanation']
    new_question = Question(question_text, question_answer, question_explanation)
    question_bank.append(new_question)

quiz = QuizExecution(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("最終問でした！お疲れ様でした！\n")
print(f"最終の正解率は {round(quiz.score / quiz.question_number * 100, 1)}% です!\n")
