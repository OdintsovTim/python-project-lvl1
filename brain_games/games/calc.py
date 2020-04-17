import operator
import random


MAX_NUMBER = 100
MIN_NUMBER = -100
OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}
DESCRIPTION = 'What is the result of the expression?'


def round():
    '''Returns question and correct answer for calc game.'''
    first_random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    operation = random.choice(list(OPERATIONS.keys()))

    correct_answer = str(OPERATIONS[operation](first_random_number,
                                               second_random_number))
    question = '{0} {1} {2}'.format(first_random_number, operation,
                                    second_random_number)

    return question, correct_answer
