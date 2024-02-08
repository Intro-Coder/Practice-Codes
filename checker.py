

class Checker:

    def __init__(self, answer_list):
        self.answer_list = answer_list
        self.answer_number = 0
        self.guesses = []
        self.score = 0

    def check_answer(self, user_input):

        if self.answer_number < len(self.answer_list):

            answer = self.answer_list[self.answer_number]

            if answer == user_input:
                print("correct!")
                self.score += 1

            else:
                print("wrong!")

            self.answer_number += 1
            self.guesses.append(user_input)


    def calculate_score(self):

        score = self.score/len(self.answer_list) * 100

        print("Answers:", self.answer_list)
        print("User guess:", self.guesses)
        print("your score is:", score, "%")





