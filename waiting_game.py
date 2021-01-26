#!/usr/bin/python3
import time
import random

def waiting_game():
    target = random.randint(2, 4)
    print('\nYour target time is {} seconds'.format(target))

    input(' ---Press Enter to Begin---')
    start = time.perf_counter()

    input('\n ...Press Enter again after {} seconds...'.format(target))
    enlapsed = time.perf_counter() - start

    print('\nElapsed time: {0:.3f} seconds'.format(enlapsed))
    if enlapsed == target:
        print('(Unbeliveble! Perfect timing!)')
    elif enlapsed < target:
        print('{0:.3f} seconds too fast'.format(target - enlapsed))
    else:
        print('{0:.3f} seconds too slow'.format(enlapsed - target))

waiting_game()