# Copyright (C) 2023 Martin Eriksson, licenced under MIT licence

import unittest

from src.game import *

class TestGame(unittest.TestCase):
    def test_create_game(self):
        game = Game()
        # Game should start with 1 open card in discardpile
        assert len(game.discard_pile.cards) == 1
        # 10 cards in each players hand
        assert len(game.player1_hand.cards) == 10
        assert len(game.player2_hand.cards) == 10
        # rest in draw pile
        assert len(game.draw_pile.cards) == 52 - 10 - 10 - 1
