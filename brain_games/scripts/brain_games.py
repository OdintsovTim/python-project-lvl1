#!/usr/bin/python3

from brain_games import cli


def main():
    '''Scripts main func'''
    name = cli.welcome_user()
    print(f'Bye, {name}')


if __name__ == '__main__':
    main()
