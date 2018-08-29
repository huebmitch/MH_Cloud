from MHcarddeck import CardDeck

d1 = CardDeck("Thelma")
d2 = CardDeck("Louise")

print(d1.dealer)

d1.dealer = "Teddy"

print(d1.dealer)

d1.shuffle()
print(d1.cards)

for i in range(5):
    x = d1.deal()
    print("x:", x)