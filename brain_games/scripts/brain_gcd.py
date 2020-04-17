#!/usr/bin/env python3

from brain_games import engine, games


def main():
    '''Scripts main func.'''
    engine.run(games.gcd)


if __name__ == '__main__':
    main()
