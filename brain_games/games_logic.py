import math
import operator
import random


MAX_NUMBER = 100
MIN_NUMBER = -100
OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def make_game(name, game):
    '''Making a template for a games'''
    correct_answers_counter = 0

    while correct_answers_counter < 3:
        question, correct_answer = select_question_answer_by_game(game)

        print(f'Question: {question}')
        users_answer = input('Your answer: ').lower()

        if users_answer == correct_answer:
            print('Correct!')
            correct_answers_counter += 1
        else:
            print(
                '"{0}" is wrong answer ;(. Correct answer was "{1}".'.format(
                    users_answer, correct_answer
                )
            )
            print(f'Let\'s try again, {name}')
            break
    else:
        print(f'Congratulations, {name}!')


def select_question_answer_by_game(game):
    if game == 'even':
        question, correct_answer = make_results_even_game()
    elif game == 'calc':
        question, correct_answer = make_results_calc_game()
    elif game == 'gcd':
        question, correct_answer = make_results_gcd_game()
    elif game == 'progression':
        question, correct_answer = make_results_progression_game()
    elif game == 'prime':
        question, correct_answer = make_results_prime_game()

    return question, correct_answer


def make_results_even_game():
    '''Returns question and correct answer for even game.'''
    question = random.randint(MIN_NUMBER, MAX_NUMBER)

    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer


def make_results_calc_game():
    '''Returns question and correct answer for calc game.'''
    first_random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    operation = random.choice(list(OPERATIONS.keys()))

    correct_answer = str(OPERATIONS[operation](first_random_number, second_random_number))
    question = f'{first_random_number} {operation} {second_random_number}'

    return question, correct_answer


def make_results_gcd_game():
    '''Returns question and correct answer for gcd game.'''
    first_random_number = random.randint(1, MAX_NUMBER)
    second_random_number = random.randint(1, MAX_NUMBER)

    maximum = max(first_random_number, second_random_number)
    minimum = min(first_random_number, second_random_number)
    while maximum % minimum != 0:
        maximum, minimum = minimum, maximum % minimum

    correct_answer = str(minimum)
    question = f'{first_random_number} {second_random_number}'

    return question, correct_answer


def make_results_progression_game():
    '''Returns question and correct answer for progression game.'''
    step = random.randint(1, 10)
    first_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    progression = list(range(first_number, first_number + step * 10, step))

    correct_answer_index = random.randint(0, 9)
    correct_answer = str(progression[correct_answer_index])
    progression[correct_answer_index] = '..'
    question = ' '.join([str(num) for num in progression])

    return question, correct_answer


def make_results_prime_game():
    '''Returns question and correct answer for prime game.'''
    question = random.randint(2, MAX_NUMBER)

    for num in range(2, math.ceil(math.sqrt(question))):
        if question % num == 0:
            correct_answer = 'no'
            break
    else:
        correct_answer = 'yes'

    return question, correct_answer
