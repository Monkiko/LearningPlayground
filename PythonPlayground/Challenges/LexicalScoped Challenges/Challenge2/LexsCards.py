# Creator: LexicalScoped
# To create a deck call for deck object
#   example: deck = Deck()
# we will use deck as the deck object for the following examples.

# To shuffle the deck object
#   deck.Shuffle()
# this will add the discard/in-use cards back to the deck and randomize the order.

# To Draw from the deck object
#   deck.Draw()
# this will remove a card from the deck and place it in an "in-use/discard" container

import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        match value:
            case 1:
                self.name = "Ace"
            case 11:
                self.name = "Jack"
            case 12:
                self.name = "Queen"
            case 13:
                self.name = "King"
            case _:
               self.name = str(value)

class Deck:
    suits = [ "Spades", "Clubs", "Hearts", "Diamonds" ]
    cards = []
    used_cards = []

    def __init__(self):
        for suit in self.suits:
            for index in range(1, 14):
                self.cards.append(Card(suit, index))

    def shuffle(self):
        self.cards.extend(self.used_cards)
        self.used_cards = []
        random.shuffle(self.cards)

    def draw(self):
        card = self.cards.pop()
        self.used_cards.append(card)
        return card


# Used for Testing if needed
#def main():
    # test code here
#    return

#if __name__=="__main__":
#    main()

deck = Deck()

print(deck)