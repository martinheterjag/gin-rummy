# Copyright (C) 2023 Martin Eriksson, licenced under MIT licence

import os
import time
import sys
from src.game import Game

def read_input(max: int) -> int:
    while True:
        try:
            i = input()
            if i == 'q':
                print('You pressed q for quit! Good bye!')
                sys.exit()
            input_int = int(i)
        except ValueError:
            print('Invalid input')
        else:
            if input_int in range(1, max + 1):
                break
            else:
                print('option not in range')
    return input_int

def main() -> int:
    game = Game()
    game_finished = False
    while(game_finished == False):
        game.start_turn()
        pile = read_input(2)
        game.pick_pile(pile)
        card = read_input(11)
        game.play_card(card)
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    main()
    exit(0)