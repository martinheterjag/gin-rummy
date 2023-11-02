# Copyright (C) 2023 Martin Eriksson, licenced under MIT licence

from enum import Enum
import random

class Suit(Enum):
    CLUBS = '♣️'
    DIAMONDS = '♦️'
    SPADES = '♠️'
    HEARTS = '♥️'

class Ranking(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

class Card:
    def __init__(self, suit, ranking):
        self.suit = suit
        self.ranking = ranking
        if self.ranking < 10:
            self.value = self.ranking
        else:
            self.value = 10
    
    def ranking_short(self):
        short = str(self.ranking)
        if short == '1':
            short = 'A'
        elif short == '11':
            short = 'J'
        elif short == '12':
            short = 'Q'
        elif short == '13':
            short = 'K'

        return short

    def suit_to_num(self, suit):
        # returning in magnitude of 100 to give suits higher
        # value than ranking when sorting the deck or hand
        if Suit(suit) == Suit.CLUBS:
            return 100
        if Suit(suit) == Suit.DIAMONDS:
            return 200
        if Suit(suit) == Suit.SPADES:
            return 300
        if Suit(suit) == Suit.HEARTS:
            return 400

    def to_string(self, include_value=False):
        if include_value:
            return f'{self.ranking_short()}{self.suit} ({self.value})'
        return f'{self.ranking_short()}{self.suit}'
    
    # Implement comparison funcitons to be able to sort
    def __lt__(self, other):
        s = self.suit_to_num(self.suit) + self.ranking
        o = self.suit_to_num(other.suit) + other.ranking
        return s < o

    def __le__(self, other):
        s = self.suit_to_num(self.suit) + self.ranking
        o = self.suit_to_num(other.suit) + other.ranking
        return s <= o

    def __eq__(self, other):
        s = self.suit_to_num(self.suit) + self.ranking
        o = self.suit_to_num(other.suit) + other.ranking
        return s == o

    def __ne__(self, other):
        s = self.suit_to_num(self.suit) + self.ranking
        o = self.suit_to_num(other.suit) + other.ranking
        return s != o

    def __gt__(self, other):
        s = self.suit_to_num(self.suit) + self.ranking
        o = self.suit_to_num(other.suit) + other.ranking
        return s > o

    def __ge__(self, other):
        s = self.suit_to_num(self.suit) + self.ranking
        o = self.suit_to_num(other.suit) + other.ranking
        return s >= o
    

class Deck:
    def __init__(self, empty=False):
        if not empty:
            self.cards = self.make_deck()
            self.shuffle()
        else:
            self.cards = []
    
    # Creates and returns a new sorted deck with 52 cards (note that it doesnt put them in self.cards)
    def make_deck(this):
        cards = []
        for s in Suit:
            for r in Ranking:
                cards.append(Card(s.value, r.value))
        return cards
    
    def print_deck(self):
        for c in self.cards:
            print(c.to_string())

    def shuffle(self, quiet=True):
        if not quiet:
            print("shuffle deck")
        random.shuffle(self.cards)
    
    def draw(self):
        if len(self.cards) == 0:
            print("Warning, trying to draw from an empty deck")
            return -1
        return self.cards.pop(0)

    def draw_at(self, index):
        if len(self.cards) == 0:
            print("Warning, trying to draw from an empty deck")
            return -1
        return self.cards.pop(index)

    def add_card(self, card):
        self.cards.insert(0, card)
        return len(self.cards)

    def merge(self, deck):
        for c in range(len(deck.cards)):
            self.add_card(deck.draw())
