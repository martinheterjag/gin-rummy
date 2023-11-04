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
            # Mark card as with * if in a set or a sequends
            used_card = self.hand.in_sequence_or_set(card)
            mark = "*" if used_card else ""
            cards += f"{card.to_string()}{mark}\t"

        print(indexes)
        print(cards)
