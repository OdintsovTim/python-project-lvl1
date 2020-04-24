import random


MAX_NUMBER = 100
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(first_num, second_num):
    '''Returns gcd of two numbers.'''
    while first_num % second_num != 0:
        first_num, second_num = second_num, first_num % second_num

    return second_num


def round():
    '''Returns question and correct answer for gcd game.'''
    first_random_number = random.randint(1, MAX_NUMBER)
    second_random_number = random.randint(1, MAX_NUMBER)

    correct_answer = str(gcd(first_random_number, second_random_number))
    question = '{0} {1}'.format(first_random_number, second_random_number)

    return question, correct_answer
