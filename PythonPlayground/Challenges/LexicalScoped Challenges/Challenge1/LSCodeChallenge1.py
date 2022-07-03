# Part 1 Objectives

# Develop a module to handle Playing Cards

# Need to define cards to contain
    # name (String > value, except for 1 (Ace) 11 (Jack), 12 (Queen), 13 (King))
    # value (integer >  1 to 13)
    # suit (String > Spades, Clubs, Hearts, Diamonds)
# Need to define Deck:
    # Contain Cards in Deck
    # Contain Cards that have been drawn (in use/discard pile)
# Need build functions or methods to handle the following:
    # Shuffle (adding the in use/discards back into the deck and randomize)
    # Draw (pull card from top of Cards in Deck, put the card in the “in use/discard pile” and return the card object to where-ever the “draw” was called from)

# Requirements:
# Need to be able to work with the Deck, Shuffle and Draw functions outside of the module.
# Need a Comment section at the top of the module to outline the creator and basic instructions on what the method calls are to create deck, shuffle deck and draw from deck.

import random

class Cards:
    def __init__(self, suit, name):
        #self.value = value
        self.suit = suit
        self.name = name

    def show(self):
        print("{} of {}".format(self.name, self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for n in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]:
                self.cards.append(Cards(s, n))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range (len(self.cards)-1,0,-1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()


deck = Deck()
deck.shuffle()


bob = Player("Bob")
bob.draw(deck)
bob.showHand()