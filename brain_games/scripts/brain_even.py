#!/usr/bin/python3

from brain_games import cli, games_logic


def main():
    '''scripts main func'''
    name = cli.welcome_user_to_even_game()
    cli.greet_user_by_name(name)
    print()
    games_logic.make_even_game(name)


if __name__ == '__main__':
    main()
