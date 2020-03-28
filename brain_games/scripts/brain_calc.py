#!/usr/bin/env python3

from brain_games import cli, games_logic


def main():
    '''Scripts main func.'''
    name = cli.welcome_user(calc=True)
    games_logic.make_game(name, calc=True)


if __name__ == '__main__':
    main()
