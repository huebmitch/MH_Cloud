'''
Created on Aug 28, 2017

@author: usreei
'''

import string
import random
import time

startingPossibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' .,!?;:'

target = input("Enter your target text: ")
attemptThis = ''.join(random.choice(startingPossibleCharacters) for i in range(len(target)))
attemptNext = ''

attempted = []

completed = False

generation = 0

while completed == False:
    print(attemptThis)
    attemptNext = ''
    completed = True
    for i in range(len(target)):
        if attemptThis[i] != target[i]:
            completed = False
            attemptNext += random.choice(startingPossibleCharacters)
        else:
            attemptNext += target[i]
    generation += 1
    attemptThis = attemptNext
    attempted.append(attemptThis)
    time.sleep(0.1)

print("Target matched! That took " + str(generation) + " generation(s)")
#print(attempted)