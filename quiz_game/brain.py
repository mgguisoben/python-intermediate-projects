class Brain:


    def __init__(self, q_input):
        self.question_number = 0
        self.question_list = q_input
        self.score = 0


    def start_quiz(self):
        while len(self.question_list) != self.question_number:
            self.next_question()
        else:
            print("You've completed the quiz.")
            print(f"Your final score is {self.score}/{len(self.question_list)}")

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_q.text} (True/False)? ").title()
        self.check_answer(user_answer, current_q.answer)


    def check_answer(self, answer, correct):
        if answer == correct:
            self.score += 1
            print("You got it right")
        else:
            print("That's wrong")

        print(f"The correct answer is: {correct}")
        print(f"Your final score is {self.score}/{len(self.question_list)}\n\n")
