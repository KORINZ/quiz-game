class QuizExecution:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        global current_question
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (O/X) ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("\n正解です！\n")
            self.score += 1
            print(f"説明：{current_question.explanation}\n")
            print(f"現在の正解率は {round(self.score / self.question_number * 100, 1)}% です。\n")
            print("-----------------------------")
        else:
            print("\n惜しいです！\n")
            print(f"説明：{current_question.explanation}\n")
            print(f"現在の正解率は {round(self.score / self.question_number * 100, 1)}% です。\n")
            print("-----------------------------\n")

