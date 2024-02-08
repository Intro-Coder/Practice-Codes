from questions import Question
from data import data_list
from checker import Checker

question_list = []
answer_list = []
n = 0

for items in data_list:
    question_list.append(items["question"])
    answer_list.append(items["correct_answer"])

# -------------------------------------------------
question = Question(question_list)
user1 = Checker(answer_list)

while n < len(question_list):

    # display question
    question.display_question()

    # loop breaker
    n += 1

    # user input
    user_input = input("Answer:  ").title()

    # check answer
    user1.check_answer(user_input)

# calculate score
user1.calculate_score()