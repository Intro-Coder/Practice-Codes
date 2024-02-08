class Question:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0

    def display_question(self):

        if self.question_number < len(self.question_list):

            current_question = self.question_list[self.question_number]
            self.question_number += 1
            print(f"Q.{self.question_number}: {current_question} (True or False)")



