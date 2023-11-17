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

    def test_find_sets_or_sequences_3_kings(self):
        print("find sets")
        deck = Deck()
        deck.cards.sort()
        hand = Deck(empty=True)

        # Draw 3 kings and a five of diamonds
        hand.add_card(deck.draw_at(51))
        hand.add_card(deck.draw_at(25))
        hand.add_card(deck.draw_at(12))
        hand.add_card(deck.draw_at(16))

        hand.print_deck(include_value=True)

        assert hand.in_sequence_or_set(hand.cards[0]) == False
        assert hand.in_sequence_or_set(hand.cards[1]) == True
        assert hand.in_sequence_or_set(hand.cards[2]) == True
        assert hand.in_sequence_or_set(hand.cards[3]) == True

    def test_find_sets_or_sequences_4_kings_3_queens(self):
        print("find sets")
        deck = Deck()
        deck.cards.sort()
        hand = Deck(empty=True)

        # Draw 4 kings and 3 queens
        hand.add_card(deck.draw_at(51))
        hand.add_card(deck.draw_at(50))
        hand.add_card(deck.draw_at(38))
        hand.add_card(deck.draw_at(25))
        hand.add_card(deck.draw_at(24))
        hand.add_card(deck.draw_at(12))
        hand.add_card(deck.draw_at(11))

        hand.print_deck(include_value=True)

        for c in hand.cards:
            assert hand.in_sequence_or_set(c) == True

    def test_find_sets_or_sequences_2_kings(self):
        print("find sets")
        deck = Deck()
        deck.cards.sort()
        hand = Deck(empty=True)

        # Draw 2 kings and a five of diamonds
        hand.add_card(deck.draw_at(25))
        hand.add_card(deck.draw_at(12))
        hand.add_card(deck.draw_at(16))

        hand.print_deck(include_value=True)

        assert hand.in_sequence_or_set(hand.cards[0]) == False
        assert hand.in_sequence_or_set(hand.cards[1]) == False
        assert hand.in_sequence_or_set(hand.cards[2]) == False

    def test_find_sets_or_sequences_king_queen_jack_different_suit(self):
        print("find sets")
        deck = Deck()
        deck.cards.sort()
        hand = Deck(empty=True)

        # Draw king jack queen different suits
        hand.add_card(deck.draw_at(51))
        hand.add_card(deck.draw_at(37))
        hand.add_card(deck.draw_at(23))

        hand.print_deck(include_value=True)

        assert hand.in_sequence_or_set(hand.cards[0]) == False
        assert hand.in_sequence_or_set(hand.cards[1]) == False
        assert hand.in_sequence_or_set(hand.cards[2]) == False

    def test_find_sequences_king_queen_jack_same_suit(self):
        print("find sets")
        deck = Deck()
        deck.cards.sort()
        hand = Deck(empty=True)

        # Draw king jack queen of hearts
        hand.add_card(deck.draw_at(51))
        hand.add_card(deck.draw_at(50))
        hand.add_card(deck.draw_at(49))

        hand.print_deck(include_value=True)

        assert hand.in_sequence_or_set(hand.cards[0]) == True
        assert hand.in_sequence_or_set(hand.cards[1]) == True
        assert hand.in_sequence_or_set(hand.cards[2]) == True

    def test_find_sequences_many_cards(self):
        print("find sets")
        deck = Deck()
        deck.cards.sort()
        hand = Deck(empty=True)

        # Draw lots of cards in sequence and not in sequence
        hand.add_card(deck.draw_at(51))
        hand.add_card(deck.draw_at(50))
        hand.add_card(deck.draw_at(49))
        hand.add_card(deck.draw_at(30))
        hand.add_card(deck.draw_at(29))
        hand.add_card(deck.draw_at(28))
        hand.add_card(deck.draw_at(27))
        hand.add_card(deck.draw_at(26))
        hand.add_card(deck.draw_at(25))
        hand.add_card(deck.draw_at(24))
        hand.add_card(deck.draw_at(1))
        hand.print_deck(include_value=True)

        assert hand.in_sequence_or_set(hand.cards[0]) == False
        assert hand.in_sequence_or_set(hand.cards[1]) == False
        assert hand.in_sequence_or_set(hand.cards[2]) == False
        assert hand.in_sequence_or_set(hand.cards[3]) == True
        assert hand.in_sequence_or_set(hand.cards[4]) == True
        assert hand.in_sequence_or_set(hand.cards[5]) == True
        assert hand.in_sequence_or_set(hand.cards[6]) == True
        assert hand.in_sequence_or_set(hand.cards[7]) == True
        assert hand.in_sequence_or_set(hand.cards[8]) == True
        assert hand.in_sequence_or_set(hand.cards[9]) == True
        assert hand.in_sequence_or_set(hand.cards[10]) == True