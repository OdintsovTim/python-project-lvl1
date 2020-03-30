import prompt


def welcome_user(game):
    '''Greets and asks for a name of username and save it.'''
    print('Welcome to the Brain Games!')

    if game == 'even':
        print('Answer "yes" if number even otherwise answer "no".')
    elif game == 'calc':
        print('What is the result of the expression?')
    elif game == 'gcd':
        print('Find the greatest common divisor of given numbers.')
    elif game == 'progression':
        print('What number is missing in the progression?')
    elif game == 'prime':
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
    print()

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    return name
