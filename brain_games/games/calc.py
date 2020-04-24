import operator
import random


MAX_NUMBER = 100
MIN_NUMBER = -100
OPERATIONS = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
DESCRIPTION = 'What is the result of the expression?'


def round():
    '''Returns question and correct answer for calc game.'''
    first_random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    symbol, function = random.choice(OPERATIONS)

    correct_answer = str(function(first_random_number, second_random_number))
    question = '{0} {1} {2}'.format(first_random_number, symbol,
                                    second_random_number)

    return question, correct_answer
