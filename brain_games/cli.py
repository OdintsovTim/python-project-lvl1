import prompt


def welcome_user(even=False, calc=False, gcd=False, progression=False):
    '''Greets and asks for a name of username and save it.'''
    print('Welcome to the Brain Games!')

    if even:
        print('Answer "yes" if number even otherwise answer "no".')
    elif calc:
        print('What is the result of the expression?')
    elif gcd:
        print('Find the greatest common divisor of given numbers.')
    elif progression:
        print('What number is missing in the progression?')
    print()

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    return name
