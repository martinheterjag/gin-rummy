# Copyright (C) 2023 Martin Eriksson, licenced under MIT licence

from src.deck import *

class Game:
    def __init__(self):
        self.draw_pile = Deck()
        self.discard_pile = Deck(face_up=True, empty=True)
        self.player1_hand = Deck(empty=True)
        self.player2_hand = Deck(empty=True)

        for i in range(0, 10):
            self.player1_hand.add_card(self.draw_pile.draw())
            self.player2_hand.add_card(self.draw_pile.draw())

        self.discard_pile.add_card(self.draw_pile.draw())