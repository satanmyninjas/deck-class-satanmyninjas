import random

class Deck:
    """
    This is used to represent a standard deck of cards.
    
    Use the .deal method to get a singular card as an output.
    """

    ranks = [str(r) for r in range(2, 11)] + list('JQKA')
    suits = list('cdhs')
    # [do_stuff(i,j) for i in list1 for j in list2] (ex. of nested for loop in listcomp for reference)
    def __init__(self):
        self._cards = [range(2, 11) for element_1 in ranks for element_2 in suits]

    def __repr__(self):
        return f' Deck({card})'

    def __len__(self):
        return len(self._cards)

    def deal(self):
        return self._cards[random.randint(0, len(self._cards))]

