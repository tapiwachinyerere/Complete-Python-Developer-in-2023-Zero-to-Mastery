"""Module imports."""
import sys
import random


first = int(sys.argv[1])
last = int(sys.argv[2])

rand_number = random.randint(first,last)

correct_guess = False

while not correct_guess:
    try:
        player_guess = int(input(f'Guess the number between {first} and {last}: '))

        if player_guess < first or player_guess > last:
            print(f'Please guess a number between {first} and {last}!')

        if rand_number == player_guess:
            print(f'You are correct, the guess was {rand_number}')
            correct_guess = True
        else:
            print('Tough luck, please guess again.')
            continue

    except ValueError:
        print('Please enter a numerical value.')
        continue
