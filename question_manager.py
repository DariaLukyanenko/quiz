class QuestionManager():
    '''
    attributes: \n
    question_number \n
    question_list
    '''
    def __init__(self,list):
        self.number=0
        self.score=0
        self.list=list
        
    def next_question(self):
        '''asking question to user'''
        answer = input(f'{self.list[self.number].text} (True/False)')
        self.check_answer(answer)
        self.number += 1
        

    def question_finished(self):
        '''checking if there any more questions'''
        if self.number == len(self.list):
            return False
        return True

    
    def check_answer(self,answer):
        '''checking correctness of the answer'''
        print(self.list[self.number].answer, ' answer')
        print(answer, ' our answer')
        if self.list[self.number].answer==answer:
            self.score+=1
            print('good!')
        else:
            print('no good(')

        print(f'Your score is {self.score}')
   
            


