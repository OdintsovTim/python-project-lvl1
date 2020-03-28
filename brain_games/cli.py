import prompt


def welcome_user(even=False, calc=False):
    '''Greets and asks for a name of username and save it.'''
    print('Welcome to the Brain Games!')

    if even:
        print('Answer "yes" if number even otherwise answer "no".')
    elif calc:
        print('What is the result of the expression?')
    print()

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    return name
