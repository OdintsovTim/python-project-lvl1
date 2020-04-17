import random


MAX_NUMBER = 100
MIN_NUMBER = -100
DESCRIPTION = 'What number is missing in the progression?'


def round():
    '''Returns question and correct answer for progression game.'''
    step = random.randint(1, 10)
    first_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    progression = list(range(first_number, first_number + step * 10, step))

    correct_answer_index = random.randint(0, 9)
    correct_answer = str(progression[correct_answer_index])
    progression[correct_answer_index] = '..'
    question = ' '.join([str(num) for num in progression])

    return question, correct_answer
