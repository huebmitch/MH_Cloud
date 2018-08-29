'''
Created on Feb 16, 2016

@author: usreei
'''
# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20. \nYou have 6 tries')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Type your guess now:')
    guess = int(input())

    if guess < 1 or guess > 20:
        print('Your guess is not between 1 - 20')
    elif guess > secretNumber:
        print('Your guess is too high.')
    elif guess < secretNumber:
        print('Your guess is too low.')
    else:
        break
if guess == secretNumber:
    print('Good Job! You guessed my number in ' + str(guessesTaken) + ' guesses.')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
