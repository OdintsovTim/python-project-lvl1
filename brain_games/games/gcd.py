import random


MAX_NUMBER = 100
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def find_gcd(first_num, second_num):
    '''Returns gcd of two numbers.'''
    maximum = max(first_num, second_num)
    minimum = min(first_num, second_num)

    while maximum % minimum != 0:
        maximum, minimum = minimum, maximum % minimum

    return minimum


def round():
    '''Returns question and correct answer for gcd game.'''
    first_random_number = random.randint(1, MAX_NUMBER)
    second_random_number = random.randint(1, MAX_NUMBER)

    correct_answer = str(find_gcd(first_random_number, second_random_number))
    question = '{0} {1}'.format(first_random_number, second_random_number)

    return question, correct_answer
