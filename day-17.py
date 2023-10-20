from resources.day17.question import Question
from resources.day17.data import question_data
from resources.day17.brain import Brain

question_bank = [Question(q['text'], q['answer']) for q in question_data]

brain = Brain(question_bank)
brain.start_quiz()
