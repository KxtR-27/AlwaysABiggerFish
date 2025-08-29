from gameScene import GameScene

def main() -> None:
    resolution = (960, 540)

    game = GameScene(resolution)
    game.start()

if __name__ == "__main__":
    main()