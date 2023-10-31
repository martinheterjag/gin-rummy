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
    
    def test_draw_top_card(self):
        deck = Deck()
        suit = deck.cards[0].suit
        rank = deck.cards[0].ranking
        assert len(deck.cards) == 52
        card = deck.draw()
        assert card.ranking == rank
        assert card.suit == suit
        assert len(deck.cards) == 51

    def test_merging_decks(self):
        deck1 = Deck()
        deck2 = Deck()
        deck1.merge(deck2)
        assert len(deck1.cards) == 2 * 52
        assert len(deck2.cards) == 0

        # If two fresh decks are merged there should
        # be 8 ofeach rank and 26 of each suit
        kings = 0
        spades = 0
        for card in deck1.cards:
            if Suit(card.suit) == Suit.SPADES:
                spades += 1 
            if Ranking(card.ranking) == Ranking.KING:
                kings += 1

        assert kings == 8
        assert spades == 26