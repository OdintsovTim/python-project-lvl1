import random


MAX_NUMBER = 100
MIN_NUMBER = -100


    correct_answers_counter = 0
    min_number = - 1000
    max_number = 1000

    while correct_answers_counter < 3:
        random_number = random.randint(min_number, max_number)

        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        print(f'Question: {random_number}')
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

    print(f'Congratulations, {name}!')
