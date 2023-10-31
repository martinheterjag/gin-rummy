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

    def to_string(self, include_value=False):
        if include_value:
            return f'{self.ranking_short()} {self.suit}  ({self.value})'
        return f'{self.ranking_short()} {self.suit}'
    

class Deck:
    def __init__(self, face_up=False, empty=False):
        self.face_up = face_up
        if not empty:
            self.cards = self.make_deck()
            self.shuffle()
    
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
    
    def add_card(self, card):
        self.cards.append(card)
        return len(self.cards)

    def merge(self, deck):
        for c in range(len(deck.cards)):
            self.add_card(deck.draw())

deck = Deck()
deck.print_deck()
print('----------')
deck2 = Deck()
deck2.print_deck()

deck.merge(deck2)

print(f'deck1: {len(deck.cards)}, deck2: {len(deck2.cards)}')
    