from brain import Brain
from data import question_data
from question import Question

question_bank = [Question(q['text'], q['answer']) for q in question_data]

brain = Brain(question_bank)
brain.start_quiz()
