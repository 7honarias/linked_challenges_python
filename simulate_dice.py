#!/usr/bin/python3
"""simulate random dice probability"""
from random import randint
from collections import Counter

def roll_dice(*dice, num_tials=1_000_000):
    counts = Counter()
    for roll in range(num_tials):
        counts[sum((randint(1,sides) for sides in dice))] += 1

    print('\nOUTCOME\t PROBABILITY')
    for outcome in range(len(dice), sum(dice)+1):
        print('{}\t{:0.2f}%'.format(outcome, counts[outcome]*100/num_tials))


roll_dice(4,6,6)