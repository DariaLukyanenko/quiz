import requests
from question_maker import Question
from question_manager import QuestionManager
from data import question_data


API_URL = 'https://opentdb.com/'
PARAMS = 'api.php?amount=10&category=11&type=boolean'

response = requests.get(API_URL + PARAMS)
BANK = response.json()['results']

print(BANK)
bank_questions=[]
for i in range(len(BANK)):
    ques=Question(BANK[i]['question'],BANK[i]['correct_answer'])
    bank_questions.append(ques)
    
quiz = QuestionManager(bank_questions)

while quiz.question_finished():
    quiz.next_question()
    

