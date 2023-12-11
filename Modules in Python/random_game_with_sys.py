"""Module imports."""
import sys
import random

def run_guess(player_guess, rand_number):
    if player_guess < first or player_guess > last:
        print(f'Please guess a number between {first} and {last}!')
        return False

    if rand_number == player_guess:
        print(f'You are correct, the guess was {rand_number}')
        return True
    else:
        print('Tough luck, please guess again.')

first = 1 #int(sys.argv[1])
last = 10 #int(sys.argv[2])

rand_number = random.randint(first,last)

if __name__ == '__main__':

    correct_guess = False

    while not correct_guess:
        try:
            player_guess = int(input(f'Guess the number between {first} and {last}: '))
            if run_guess(player_guess, rand_number):
                break

        except ValueError:
            print('Please enter a numerical value.')
            continue
