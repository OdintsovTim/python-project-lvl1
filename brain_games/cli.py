import prompt


def welcome_user():
    '''Greets and asks for a name of username and save it.'''
    print('Welcome to the Brain Games!')
    print()
    name = prompt.string('May I have your name? ')
    return name


def greet_user_by_name(name):
    '''Greets user by his name'''
    print(f'Hello, {name}!')
