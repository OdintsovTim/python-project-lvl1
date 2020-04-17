import math
import random


MAX_NUMBER = 100
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for num in range(2, math.ceil(math.sqrt(number))):
        if number % num == 0:
            return False
    return True


def round():
    '''Returns question and correct answer for prime game.'''
    question = random.randint(2, MAX_NUMBER)
    correct_answer = 'yes' if is_prime(question) else 'no'

    return question, correct_answer
