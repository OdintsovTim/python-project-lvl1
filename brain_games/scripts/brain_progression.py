#!/usr/bin/env python3

from brain_games import cli, games_logic


def main():
    '''Scripts main func.'''
    name = cli.welcome_user(progression=True)
    games_logic.make_game(name, progression=True)


if __name__ == '__main__':
    main()
