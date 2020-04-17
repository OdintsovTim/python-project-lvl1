import random


MAX_NUMBER = 100
MIN_NUMBER = -100
DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def round():
    '''Returns question and correct answer for even game.'''
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if question % 2 == 0 else 'no'

    return question, correct_answer
