import random


MAX_NUMBER = 100
MIN_NUMBER = -100


def make_game(name, even=False, calc=False):
    '''Logic of games'''
    correct_answers_counter = 0

    while correct_answers_counter < 3:
        if even:
            question, correct_answer = make_results_even_game()
        elif calc:
            question, correct_answer = make_results_calc_game()

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


def make_results_even_game():
    '''Question and correct answer for even game.'''
    question = random.randint(MIN_NUMBER, MAX_NUMBER)

    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer



    print(f'Congratulations, {name}!')
