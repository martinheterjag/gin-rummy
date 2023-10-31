# Copyright (C) 2023 Martin Eriksson, licenced under MIT licence

import unittest

from src.deck import *

class TestCard(unittest.TestCase):
    def test_create_card(self):
        card = Card(Suit.SPADES.value, Ranking.ACE.value)
        assert card.ranking == 1
        assert card.suit == '♠️'

    def test_card_values(self):
        ace = Card(Suit.SPADES.value, Ranking.ACE.value)
        assert ace.value == 1
        five = Card(Suit.SPADES.value, Ranking.FIVE.value)
        assert five.value == 5
        eight = Card(Suit.SPADES.value, Ranking.EIGHT.value)
        assert eight.value == 8
        ten = Card(Suit.SPADES.value, Ranking.TEN.value)
        assert ten.value == 10
        jack = Card(Suit.SPADES.value, Ranking.JACK.value)
        assert jack.value == 10
        queen = Card(Suit.SPADES.value, Ranking.QUEEN.value)
        assert queen.value == 10
        king = Card(Suit.SPADES.value, Ranking.KING.value)
        assert king.value == 10

class TestDeck(unittest.TestCase):
    def test_deck_size(self):
        deck = Deck()
        assert len(deck.cards) == 52

    def test_empty_deck_size(self):
        deck = Deck(empty=True)
        assert len(deck.cards) == 0