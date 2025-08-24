import pygame, simpleGE

class GameScene(simpleGE.Scene):
    def __init__(self, size=...):
        super().__init__(size)

        self.setCaption("Eat smaller fish to get bigger!")
        self.setImage("assets/backdrop.png")



def main():
    resolution = (960, 540)

    game = GameScene(resolution)
    game.start()

if __name__ == "__main__":
    main()