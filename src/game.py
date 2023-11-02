# Copyright (C) 2023 Martin Eriksson, licenced under MIT licence

from src.deck import *
from src.player import Player

class Game:
    def __init__(self):
        self.deal_cards()

        self.players = [
            Player(self.player1_hand),
            Player(self.player2_hand)
        ]

        # TODO: Make turn random
        self.turn = 0
        print("\n♣️♦♠️♥️ G I N ♣️♦️♠️♥️ R U M M Y ♣️♦♠️♥️\n")

    def deal_cards(self):
        self.draw_pile = Deck()
        self.discard_pile = Deck(empty=True)
        self.player1_hand = Deck(empty=True)
        self.player2_hand = Deck(empty=True)

        for i in range(0, 10):
            self.player1_hand.add_card(self.draw_pile.draw())
            self.player2_hand.add_card(self.draw_pile.draw())

        self.discard_pile.add_card(self.draw_pile.draw())

    def start_turn(self):
        # Show cards
        print(f"----- Player {self.turn + 1}'s turn -----")
        print(f"Draw Pile: {len(self.draw_pile.cards)}")
        print(f"Discard Pile: {self.discard_pile.cards[0].to_string()}")
        print("Hand:")
        self.players[self.turn].print_hand()
        print("\nDraw from (1)Draw pile or (2)Discard pile?")

    # First action each turn
    def pick_pile(self, pile) -> bool:
        if pile == 1:
            print("You picked the draw pile")
            self.players[self.turn].hand.add_card(self.draw_pile.draw())
        elif 2:
            print("You picked the discard pile")
            self.players[self.turn].hand.add_card(self.discard_pile.draw())
        else:
            print("Incorrect choice, try again")
            return False
        # Print hand again before picking card to play.
        print("Hand:")
        self.players[self.turn].print_hand()
        print("\npick a card from 1 to 11?")
        return True

    # Second action each turn
    def play_card(self, card_to_play):
        card_str = self.players[self.turn].hand.cards[card_to_play - 1].to_string()
        print(f"You picked ({card_to_play}) {card_str}")
        self.discard_pile.add_card(
            self.players[self.turn].hand.draw_at(card_to_play - 1))

        if self.turn == 0:
            self.turn = 1
        else:
            self.turn = 0
