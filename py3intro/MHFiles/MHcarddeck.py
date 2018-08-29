import random


class CardDeck():
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self, dealer):
        print("Dealer is:", dealer)
        self._cards = []
        for s in self.SUITS:
            for r in self.RANKS:
                card = '{}-{}'.format(r, s)
                self._cards.append(card)
        self._dealer = dealer

    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self):
        return self._cards.pop()

    @property
    def dealer(self):
        return self._dealer

    @property
    def cards(self):
        return self._cards

    @dealer.setter
    def dealer(self, value):
        if isinstance(value, str):
            self._dealer = value
        else:
            raise TypeError("Dealer must be a string")
