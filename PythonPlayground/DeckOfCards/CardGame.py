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
# Need a Comment section at the top of the module to outline the creator and basic instructions on what the method calls are to create deck, shuffle deck and draw from deck.vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

from random import shuffle


suit = ["Hearts", "Spades", "Clubs", "Diamonds"]
names = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
values = list(range(1,14))
deck = []

for s in suit:
    for n in names:
        deck.append("{} of {}".format(n, s))

print(deck)


#hand = 0

#while hand < 5:
#    shuffle(suit)
#    shuffle(value)
#    print(value[0] + " of " + suit[0])
#    hand = hand + 1