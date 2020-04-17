import prompt


def greeting_user(description):
    '''Greeting user and returns his name.'''
    print('Welcome to the Brain Games!')
    print(description + '\n')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!\n'.format(name))

    return name


def run(module):
    '''Making a template for a games.'''
    name = greeting_user(module.DESCRIPTION)
    correct_answers_counter = 0

    while correct_answers_counter < 3:
        question, correct_answer = module.round()

        print('Question: {0}'.format(question))
        users_answer = prompt.string('Your answer: ').lower()

        if users_answer == correct_answer:
            print('Correct!')
            correct_answers_counter += 1
        else:
            print(
                '"{0}" is wrong answer ;(. Correct answer was "{1}".'.format(
                    users_answer, correct_answer
                )
            )
            print('Let\'s try again, {0}'.format(name))
            break
    else:
        print('Congratulations, {0}!'.format(name))
