'''
Created on Feb 26, 2016

@author: usreei
'''

def censor(text, word):
    words = text.split(" ")
    w = []
    for i in words:
        if i == word:
            w.append(len(i) * "*")
        else:
            w.append(i)

    return " ".join(w)

print(censor("Hello my name is slim", "slim"))
