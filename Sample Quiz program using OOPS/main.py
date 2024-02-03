from data import question_data
from question_model import Question
from quiz_brian import QuizBrian

question_list = []
for question in question_data:
  question_text = question["text"]
  question_answer = question["answer"]
  new_question = Question(question_text, question_answer)
  question_list.append(new_question)


quiz = QuizBrian(question_list)
while quiz.still_has_questions():
  quiz.next_question()

print("The Quiz was ended ")
print(f"Your Final Score is : {quiz.score}/{quiz.question_number}")  
