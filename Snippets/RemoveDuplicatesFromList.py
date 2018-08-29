'''
Created on Feb 26, 2016

@author: usreei
'''

def remove_duplicates(x):
    b = []
    for a in x:
        if a not in b:
            b.append(a)
    return b

print(remove_duplicates([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]))
