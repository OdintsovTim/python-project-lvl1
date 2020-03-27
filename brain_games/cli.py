import prompt


def welcome_user():
    '''Asks for a username and greets him.'''
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
