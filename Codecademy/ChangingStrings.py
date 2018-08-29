'''
Created on Feb 26, 2016

@author: usreei
'''

stringtochange = "Hello"

##Reverse String Order
def reverse(text):
    TEXT = ''
    x = len(text)
    while(x > 0):
        TEXT = TEXT + text[x - 1]
        x = x - 1
    return TEXT

print(reverse(stringtochange))

##Remove Vowels from string
def anti_vowel(text):
    vowels = 'aeiouAEIOU'
    new_text = ''
    for i in text:
        if i.lower() not in vowels:
            new_text += i
    return new_text

print(anti_vowel(stringtochange))

##Score a Scrabble Word
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}


def scrabble_score(word):
    word = word.lower()
    total = 0
    for i in word:
        total = total + (score[i])
    return total

print(scrabble_score(stringtochange))
