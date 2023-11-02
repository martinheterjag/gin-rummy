from src.game import Game

def main() -> int:
    game = Game()
    game.start_turn()
    game.pick_pile(1)
    game.play_card(1)
    game.start_turn()
    game.pick_pile(1)
    game.play_card(1)


if __name__ == "__main__":
    main()
    exit(0)