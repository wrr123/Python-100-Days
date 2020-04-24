import random


def roll():
    x = random.randint(0, 6)
    y = random.randint(0, 6)
    print(f'({x}, {y})')
