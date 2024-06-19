class Question:
    def __init__(self, question_id, question_stem, correct_answer):
        self.question_id = question_id
        self.question_stem = question_stem
        self.correct_answer = correct_answer.lower() # convert to lower

    def __str__(self):
        return (f'({self.question_id}) {self.question_stem}[{self.correct_answer}]')
    
    def is_correct(self, answer):
        if self.correct_answer.lower() == answer.lower():
            return True
        return False
    
class Student:
    def __init__(self, student_name):
        self.student_name = student_name
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def get_number_of_questions(self):
        return (len(self.questions))

    def calculate_score(self, student_answers):
        score = 0
        for i in range(len(self.questions)):
            question = self.questions[i]
            student_answer = student_answers[i]
            if question.is_correct(student_answer):
                score += 1
        return score
            
        
        
questions = [Question(1, 'What do bees make?', 'honey'), Question(2, 'What color are Smurfs?', 'Blue')]
s1 = Student('Bob Chan')
for q in questions:
    s1.add_question(q)
print(s1.calculate_score(['honey', 'honey']))
print(type(s1))
s2 = Student("Peter Pan")
print(s1.get_number_of_questions())
print(s2.get_number_of_questions())
    
