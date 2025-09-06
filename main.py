from gameScene import GameScene
from menuScene import MenuScene


def main() -> None: 
    GAME_RESOLUTION = (960, 540)

    bestSize = 0
    bestCause = "???"

    keepGoing = True   

    firstMenu = MenuScene(bestSize, bestCause)
    firstMenu.start()
    if firstMenu.nextAction != "Play":
        keepGoing = False

    while keepGoing:
        game = GameScene(GAME_RESOLUTION)
        game.start()

        if game.player.power > bestSize:
            bestSize = game.player.power
            bestCause = game.endCause

        menu = MenuScene(bestSize, bestCause)
        menu.start()

        if menu.nextAction != "Play":
            keepGoing = False


if __name__ == "__main__":
    main()