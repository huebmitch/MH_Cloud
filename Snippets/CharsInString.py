'''
Created on Mar 24, 2016

@author: usreei
'''

import pprint

message = "This string will have it's characters counted."
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
