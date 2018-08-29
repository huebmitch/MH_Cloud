"""
A 'Set' is 3 cards in which each individual feature is either all the SAME on each card...
OR all DIFFERENT on each card.
That is to say, any feature in the 'Set' of three cards is either common to all three
cards or is different on each card.

https://www.reddit.com/r/dailyprogrammer/comments/3ke4l6/20150909_challenge_231_intermediate_set_game/
https://github.com/piratefsh/set-solver
"""

import random
import pprint
import itertools

Shapes = ['O', 'S', 'D']
Color = ['R', 'P', 'G']
Number = ['1', '2', '3']
#Fill = ['Solid', 'Striped', 'Outline']

ALL_CARDS = [(w, x, y) for w in Shapes
             for x in Color
             for y in Number]
             #for z in Fill]

IN_PLAY_CARDS = set()

while len(IN_PLAY_CARDS) < 12:
    ACTIVE_CARDS = {random.choice(ALL_CARDS)}
    for x in ACTIVE_CARDS:
        IN_PLAY_CARDS.add(x)

pprint.pprint(IN_PLAY_CARDS)
print("")

IN_PLAY_COMBOS = [','.join(map(str,comb)) for comb in itertools.combinations(IN_PLAY_CARDS, 3)]
pprint.pprint((IN_PLAY_COMBOS))

