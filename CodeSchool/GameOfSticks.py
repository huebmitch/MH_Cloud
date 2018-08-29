'''
Created on Feb 22, 2016
Game of Sticks: Simple Game
@author: usreei
'''
## Number of Sticks to start
sticks = 21

## Instructions for user
print("There are 21 sticks, you can take 1-4 number of sticks at a time.")
print("Whoever will take the last stick will loose")

## This is the actual game code
while True:
    print("Sticks left: ", sticks)
    '''Tells you how many sticks are left.'''

    sticks_taken = int(input("Take sticks(1-4):"))
    ## Users choice

    if sticks == 1:
        print("You took the last stick, you loose")
        break
    ## User losses

    if sticks_taken >= 5 or sticks_taken <= 0:
        print("Wrong choice")
        continue
    print("Computer took: ", (5 - sticks_taken), "\n")
    sticks -= 5
