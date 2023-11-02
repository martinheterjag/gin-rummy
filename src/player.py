# Copyright (C) 2023 Martin Eriksson, licenced under MIT licence

from src.deck import *

class Player:
    def __init__(self, hand: Deck):
        self.hand = hand
        self.score = 0

    def print_hand(self):
        self.hand.cards.sort()
        i = 0
        indexes = ""
        cards = ""
        for card in self.hand.cards:
            i += 1
            indexes += f"({i})\t"
            cards += f"{card.to_string()}\t"

        print(indexes)
        print(cards)