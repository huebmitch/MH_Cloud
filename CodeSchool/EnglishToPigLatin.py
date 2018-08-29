'''
Created on Feb 26, 2016

@author: usreei
'''

print('Welcome to the Pig Latin Translator!')
original = input("Enter a word:")
if len(original) > 0 and original.isalpha():
    print("Thanks, now translating.")
    word = original.lower()
    first = word[0]
    pyg = "oy"
    new_word = word + first + pyg
    new_word = new_word[1:]
else:
    print("empty")

print(new_word)
