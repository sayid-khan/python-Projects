import random

def guess(x):
    random_number = random.randint(1,x)
    guess=0
    while guess != random_number:
        guess = int(input(f'guess a random number between 1 and {x}: '))
        if guess < random_number:
            print('sorry, the guess is too low.')
        elif guess > random_number:
            print('sorry, the guess is too high.')

    print(f'yaay congrats you have guessed the right number {random_number},correctly!')


guess(10)