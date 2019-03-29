#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    outcomes = []
    plays = ['rock', 'paper', 'scissors']

    def find_all_outcomes(rounds_left, result):
        if rounds_left == 0:
            outcomes.append(result)
            return
        for play in plays:
            find_all_outcomes(rounds_left - 1, result + [play])

    find_all_outcomes(n, [])
    return outcomes


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
